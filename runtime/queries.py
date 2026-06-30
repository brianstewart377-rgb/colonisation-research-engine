"""Runtime query examples.

A small, read-only query layer demonstrating the questions the runtime must be
able to answer. No optimisation, no caching, no business logic - just clear
projections over the generated schema. The runtime is opened read-only so it can
never be mutated through this interface.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from .config import DEFAULT_OUTPUT_DB
from .validation import validate


def _row_to_dict(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def _sorted_ids(ids: set[str]) -> list[str]:
    return sorted(ids)


def _sort_dicts(rows: list[dict], key: str) -> list[dict]:
    return sorted(rows, key=lambda r: (r.get(key) or ""))


def _sort_by_embedded_id(rows: list[dict], obj_key: str, id_key: str) -> list[dict]:
    def k(row: dict) -> str:
        obj = row.get(obj_key)
        if isinstance(obj, dict):
            return str(obj.get(id_key) or "")
        return ""

    return sorted(rows, key=k)


@dataclass(frozen=True)
class _Edge:
    from_id: str
    to_id: str
    relationship: str
    origin: str



class Runtime:
    """Read-only accessor over a generated CRE runtime database."""

    def __init__(self, db_path: Path | str = DEFAULT_OUTPUT_DB):
        self._db_path = Path(db_path)
        self._conn = sqlite3.connect(f"file:{self._db_path}?mode=ro", uri=True)
        self._conn.row_factory = _row_to_dict

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> "Runtime":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    def _all(self, sql: str, params: tuple = ()) -> list[dict]:
        return self._conn.execute(sql, params).fetchall()

    def _one(self, sql: str, params: tuple = ()) -> dict | None:
        rows = self._all(sql, params)
        return rows[0] if rows else None

    def _raw_conn(self) -> sqlite3.Connection:
        return sqlite3.connect(f"file:{self._db_path}?mode=ro", uri=True)

    def get_object(self, object_id: str) -> dict | None:
        return self._one("SELECT * FROM objects WHERE object_id = ?", (object_id,))

    # ------------------------------------------------------------------ #
    # Single-object retrieval                                            #
    # ------------------------------------------------------------------ #
    def get_mechanic(self, mechanic_id: str) -> dict | None:
        return self._one("SELECT * FROM mechanics WHERE mechanic_id = ?", (mechanic_id,))

    def get_planner_rule(self, rule_id: str) -> dict | None:
        return self._one("SELECT * FROM planner_rules WHERE rule_id = ?", (rule_id,))

    def get_decision(self, decision_id: str) -> dict | None:
        return self._one("SELECT * FROM decisions WHERE decision_id = ?", (decision_id,))

    def get_contradiction(self, contradiction_id: str) -> dict | None:
        return self._one("SELECT * FROM contradictions WHERE contradiction_id = ?", (contradiction_id,))

    def get_unknown(self, unknown_id: str) -> dict | None:
        return self._one("SELECT * FROM unknowns WHERE unknown_id = ?", (unknown_id,))

    def get_claim(self, claim_id: str) -> dict | None:
        return self._one("SELECT * FROM claims WHERE claim_id = ?", (claim_id,))

    def get_evidence(self, evidence_id: str) -> dict | None:
        return self._one("SELECT * FROM evidence WHERE evidence_id = ?", (evidence_id,))

    def get_experiment(self, experiment_id: str) -> dict | None:
        return self._one("SELECT * FROM experiments WHERE experiment_id = ?", (experiment_id,))

    def get_live_verification(self, verification_id: str) -> dict | None:
        return self._one(
            "SELECT * FROM live_verifications WHERE verification_id = ?",
            (verification_id,),
        )

    def get_evidence_chain(self, claim_id: str) -> dict:
        """Full provenance chain backing a claim (claim -> source entities)."""

        claim = self._one("SELECT * FROM claims WHERE claim_id = ?", (claim_id,))
        links = self._all(
            """
            SELECT p.source_entity, p.relationship, p.basis_note,
                   o.object_type AS source_type, o.title AS source_title
            FROM claim_provenance_links p
            LEFT JOIN objects o ON o.object_id = p.source_entity
            WHERE p.claim_id = ?
            ORDER BY p.relationship, p.source_entity
            """,
            (claim_id,),
        )
        return {"claim": claim, "provenance": links}

    def explain_decision(self, decision_id: str) -> dict | None:
        decision = self.get_decision(decision_id)
        if decision is None:
            return None

        direct_edges = [
            _Edge(
                from_id=r["from_id"],
                to_id=r["to_id"],
                relationship=r["relationship"],
                origin=r["origin"],
            )
            for r in self._all(
                """
                SELECT from_id, to_id, relationship, origin
                FROM object_references
                WHERE from_id = ?
                ORDER BY to_id, relationship, origin
                """,
                (decision_id,),
            )
        ]

        direct_evidence_ids = {e.to_id for e in direct_edges if e.relationship == "references_evidence"}
        direct_claim_ids = {e.to_id for e in direct_edges if e.relationship == "references_claim"}
        direct_mechanic_ids = {e.to_id for e in direct_edges if e.relationship == "references_mechanic"}
        direct_rule_ids = {e.to_id for e in direct_edges if e.relationship == "references_rule"}
        direct_experiment_ids = {e.to_id for e in direct_edges if e.relationship == "references_experiment"}
        other_direct_ids = {
            e.to_id
            for e in direct_edges
            if e.relationship
            not in (
                "references_evidence",
                "references_claim",
                "references_mechanic",
                "references_rule",
                "references_experiment",
            )
        }

        direct_references = {
            "evidence": _sort_dicts(
                [self.get_evidence(i) or {"evidence_id": i} for i in _sorted_ids(direct_evidence_ids)],
                "evidence_id",
            ),
            "claims": _sort_dicts(
                [self.get_claim(i) or {"claim_id": i} for i in _sorted_ids(direct_claim_ids)],
                "claim_id",
            ),
            "mechanics": _sort_dicts(
                [self.get_mechanic(i) or {"mechanic_id": i} for i in _sorted_ids(direct_mechanic_ids)],
                "mechanic_id",
            ),
            "planner_rules": _sort_dicts(
                [self.get_object(i) or {"object_id": i} for i in _sorted_ids(direct_rule_ids)],
                "object_id",
            ),
            "experiments": _sort_dicts(
                [self.get_experiment(i) or {"experiment_id": i} for i in _sorted_ids(direct_experiment_ids)],
                "experiment_id",
            ),
            "other": _sort_dicts(
                [self.get_object(i) or {"object_id": i} for i in _sorted_ids(other_direct_ids)],
                "object_id",
            ),
        }

        claim_support: list[dict] = []
        claim_edges: list[_Edge] = []
        mechanic_ids: set[str] = set(direct_mechanic_ids)

        for cid in _sorted_ids(direct_claim_ids):
            claim = self.get_claim(cid) or {"claim_id": cid}
            prov_rows = self._all(
                """
                SELECT claim_id, source_entity, relationship, basis_note
                FROM claim_provenance_links
                WHERE claim_id = ?
                ORDER BY relationship, source_entity
                """,
                (cid,),
            )
            c_refs = self._all(
                """
                SELECT from_id, to_id, relationship, origin
                FROM object_references
                WHERE from_id = ?
                  AND relationship IN ('supports_mechanic', 'relates_contradiction', 'relates_unknown', 'derived_from')
                ORDER BY to_id, relationship, origin
                """,
                (cid,),
            )
            for r in c_refs:
                claim_edges.append(_Edge(r["from_id"], r["to_id"], r["relationship"], r["origin"]))
            linked_mechanics = [r["to_id"] for r in c_refs if r["relationship"] == "supports_mechanic"]
            linked_contradictions = [r["to_id"] for r in c_refs if r["relationship"] == "relates_contradiction"]
            linked_unknowns = [r["to_id"] for r in c_refs if r["relationship"] == "relates_unknown"]
            for mid in linked_mechanics:
                mechanic_ids.add(mid)

            claim_support.append(
                {
                    "claim": claim,
                    "provenance": prov_rows,
                    "linked_mechanics": [self.get_mechanic(m) or {"mechanic_id": m} for m in sorted(set(linked_mechanics))],
                    "linked_contradictions": [self.get_contradiction(c) or {"contradiction_id": c} for c in sorted(set(linked_contradictions))],
                    "linked_unknowns": [self.get_unknown(u) or {"unknown_id": u} for u in sorted(set(linked_unknowns))],
                }
            )

        mechanic_context: list[dict] = []
        mechanic_edges: list[_Edge] = []
        traceability_edges: list[_Edge] = []

        guardrail_contradictions: set[str] = set()
        guardrail_unknowns: set[str] = set()
        guardrail_live_verifications: set[str] = set()

        for mid in _sorted_ids(mechanic_ids):
            mechanic = self.get_mechanic(mid) or {"mechanic_id": mid}

            contradictions = self._all(
                """
                SELECT c.*
                FROM object_references r
                JOIN contradictions c ON c.contradiction_id = r.from_id
                WHERE r.to_id = ? AND r.relationship = 'affects_mechanic'
                ORDER BY c.contradiction_id
                """,
                (mid,),
            )
            unknowns = self._all(
                """
                SELECT u.*
                FROM object_references r
                JOIN unknowns u ON u.unknown_id = r.from_id
                WHERE r.to_id = ? AND r.relationship = 'about_mechanic'
                ORDER BY u.unknown_id
                """,
                (mid,),
            )
            live_verifications = self._all(
                """
                SELECT lv.*
                FROM object_references r
                JOIN live_verifications lv ON lv.verification_id = r.from_id
                WHERE r.to_id = ? AND r.relationship = 'verifies_mechanic'
                ORDER BY lv.verification_id
                """,
                (mid,),
            )
            dependent_rules = self._all(
                """
                SELECT DISTINCT o.object_id, o.object_type, o.title, o.status, o.source_ref
                FROM object_references r
                JOIN objects o ON o.object_id = r.from_id
                WHERE r.to_id = ? AND r.relationship = 'depends_on_mechanic'
                ORDER BY o.object_id
                """,
                (mid,),
            )
            evidence_traceability = self._all(
                """
                SELECT evidence_id, mechanic_id, relationship, strength, basis, notes
                FROM evidence_traceability
                WHERE mechanic_id = ?
                ORDER BY evidence_id, relationship
                """,
                (mid,),
            )

            m_refs = self._all(
                """
                SELECT from_id, to_id, relationship, origin
                FROM object_references
                WHERE to_id = ?
                  AND relationship IN ('affects_mechanic', 'about_mechanic', 'verifies_mechanic', 'depends_on_mechanic')
                ORDER BY from_id, relationship, origin
                """,
                (mid,),
            )
            for r in m_refs:
                mechanic_edges.append(_Edge(r["from_id"], r["to_id"], r["relationship"], r["origin"]))

            for row in evidence_traceability:
                rel = row.get("relationship") or "traceability"
                traceability_edges.append(_Edge(row["evidence_id"], row["mechanic_id"], rel, "evidence_traceability"))

            for c in contradictions:
                cid = c.get("contradiction_id")
                if cid:
                    guardrail_contradictions.add(cid)
            for u in unknowns:
                uid = u.get("unknown_id")
                if uid:
                    guardrail_unknowns.add(uid)
            for lv in live_verifications:
                lvid = lv.get("verification_id")
                if lvid:
                    guardrail_live_verifications.add(lvid)

            mechanic_context.append(
                {
                    "mechanic": mechanic,
                    "contradictions": contradictions,
                    "unknowns": unknowns,
                    "live_verifications": live_verifications,
                    "dependent_rules": dependent_rules,
                    "evidence_traceability": evidence_traceability,
                }
            )

        guardrails = {
            "contradictions": _sort_dicts(
                [self.get_contradiction(i) or {"contradiction_id": i} for i in _sorted_ids(guardrail_contradictions)],
                "contradiction_id",
            ),
            "unknowns": _sort_dicts(
                [self.get_unknown(i) or {"unknown_id": i} for i in _sorted_ids(guardrail_unknowns)],
                "unknown_id",
            ),
            "live_verifications": _sort_dicts(
                [self.get_live_verification(i) or {"verification_id": i} for i in _sorted_ids(guardrail_live_verifications)],
                "verification_id",
            ),
        }

        node_ids: set[str] = {decision_id}
        for bucket in direct_references.values():
            for row in bucket:
                if "object_id" in row:
                    node_ids.add(row["object_id"])
                for k in ("evidence_id", "claim_id", "mechanic_id", "experiment_id"):
                    if k in row and row[k]:
                        node_ids.add(row[k])
        for entry in claim_support:
            c = entry.get("claim") or {}
            if isinstance(c, dict) and c.get("claim_id"):
                node_ids.add(c["claim_id"])
            for prov in entry.get("provenance") or []:
                sid = prov.get("source_entity")
                if sid:
                    node_ids.add(sid)
            for k in ("linked_mechanics", "linked_contradictions", "linked_unknowns"):
                for row in entry.get(k) or []:
                    for kk in ("mechanic_id", "contradiction_id", "unknown_id"):
                        if kk in row and row[kk]:
                            node_ids.add(row[kk])
        for ctx in mechanic_context:
            m = ctx.get("mechanic") or {}
            if isinstance(m, dict) and m.get("mechanic_id"):
                node_ids.add(m["mechanic_id"])
            for row in ctx.get("contradictions") or []:
                if row.get("contradiction_id"):
                    node_ids.add(row["contradiction_id"])
            for row in ctx.get("unknowns") or []:
                if row.get("unknown_id"):
                    node_ids.add(row["unknown_id"])
            for row in ctx.get("live_verifications") or []:
                if row.get("verification_id"):
                    node_ids.add(row["verification_id"])
            for row in ctx.get("dependent_rules") or []:
                if row.get("object_id"):
                    node_ids.add(row["object_id"])
            for row in ctx.get("evidence_traceability") or []:
                if row.get("evidence_id"):
                    node_ids.add(row["evidence_id"])
        for row in guardrails["contradictions"]:
            if row.get("contradiction_id"):
                node_ids.add(row["contradiction_id"])
        for row in guardrails["unknowns"]:
            if row.get("unknown_id"):
                node_ids.add(row["unknown_id"])
        for row in guardrails["live_verifications"]:
            if row.get("verification_id"):
                node_ids.add(row["verification_id"])

        nodes = []
        for oid in sorted(node_ids):
            obj = self.get_object(oid) or {"object_id": oid}
            nodes.append(
                {
                    "id": obj.get("object_id", oid),
                    "type": obj.get("object_type"),
                    "title": obj.get("title"),
                    "status": obj.get("status"),
                }
            )

        edges: list[dict] = []
        for e in sorted(direct_edges + claim_edges + mechanic_edges + traceability_edges, key=lambda x: (x.from_id, x.relationship, x.to_id, x.origin)):
            edges.append(
                {
                    "from_id": e.from_id,
                    "to_id": e.to_id,
                    "relationship": e.relationship,
                    "origin": e.origin,
                }
            )
        for entry in claim_support:
            for prov in entry.get("provenance") or []:
                cid = prov.get("claim_id")
                sid = prov.get("source_entity")
                rel = prov.get("relationship")
                if cid and sid and rel:
                    edges.append(
                        {
                            "from_id": cid,
                            "to_id": sid,
                            "relationship": rel,
                            "origin": "claim_provenance_links",
                        }
                    )
        edges = sorted(edges, key=lambda r: (r["from_id"], r["relationship"], r["to_id"], r["origin"]))

        raw_conn = self._raw_conn()
        try:
            val = validate(raw_conn).as_dict()
        finally:
            raw_conn.close()

        affecting = []
        other_count = 0
        for cat, items in (val.get("warnings") or {}).items():
            for item in items:
                iid = item.get("id") or item.get("object_id") or item.get("claim_id")
                if iid and iid in node_ids:
                    affecting.append({"category": cat, "item": item})
                else:
                    other_count += 1
        affecting = sorted(affecting, key=lambda x: ((x["category"] or ""), (x["item"].get("id") or x["item"].get("object_id") or "")))

        return {
            "decision": decision,
            "decision_boundary": {
                "decision": decision.get("decision"),
                "rationale": decision.get("rationale"),
                "trade_offs": decision.get("trade_offs"),
                "consequences": decision.get("consequences"),
                "confidence": decision.get("confidence"),
                "review_status": decision.get("review_status"),
            },
            "direct_references": direct_references,
            "claim_support": _sort_by_embedded_id(claim_support, "claim", "claim_id"),
            "mechanic_context": _sort_by_embedded_id(mechanic_context, "mechanic", "mechanic_id"),
            "guardrails": guardrails,
            "trace": {"nodes": nodes, "edges": edges},
            "validation_context": {
                "ok": bool(val.get("ok")),
                "warnings_affecting_explanation": affecting,
                "other_runtime_warnings_count": other_count,
            },
        }

    # ------------------------------------------------------------------ #
    # Success-criteria queries                                           #
    # ------------------------------------------------------------------ #
    def planner_rules_depending_on(self, mechanic_id: str) -> list[dict]:
        """Which planner rules depend on a mechanic? (e.g. M-0007)"""

        return self._all(
            """
            SELECT DISTINCT pr.rule_id, pr.title, pr.status
            FROM object_references r
            JOIN planner_rules pr ON pr.rule_id = r.from_id
            WHERE r.to_id = ? AND r.relationship = 'depends_on_mechanic'
            ORDER BY pr.rule_id
            """,
            (mechanic_id,),
        )

    def evidence_supporting_claim(self, claim_id: str) -> list[dict]:
        """Which evidence/source entities support a claim? (e.g. CL-0042)"""

        return self._all(
            """
            SELECT p.source_entity, p.relationship, p.basis_note,
                   o.object_type AS source_type, o.title AS source_title
            FROM claim_provenance_links p
            LEFT JOIN objects o ON o.object_id = p.source_entity
            WHERE p.claim_id = ?
            ORDER BY p.source_entity
            """,
            (claim_id,),
        )

    def decisions_referencing(self, mechanic_id: str) -> list[dict]:
        """Which decisions reference a mechanic? (e.g. M-0010)"""

        return self._all(
            """
            SELECT DISTINCT d.decision_id, d.title, d.status, r.relationship
            FROM object_references r
            JOIN decisions d ON d.decision_id = r.from_id
            WHERE r.to_id = ? AND r.relationship = 'references_mechanic'
            ORDER BY d.decision_id
            """,
            (mechanic_id,),
        )

    def mechanics_pending_live_verification(self) -> list[dict]:
        """Mechanics that have outstanding live verification attached.

        A mechanic is *pending live verification* when it is targeted by an
        entry in the live-verification matrix, or by a claim still flagged as
        needing live verification. This identifies mechanics whose confidence is
        gated on real-game testing; it does NOT assert that every downstream use
        of the mechanic is automatically blocked - that judgement belongs to the
        (out-of-scope) planner layer, not the runtime.
        """

        return self._all(
            """
            SELECT m.mechanic_id, m.title, m.status,
                   GROUP_CONCAT(DISTINCT r.from_id) AS pending_verification_sources
            FROM mechanics m
            JOIN object_references r ON r.to_id = m.mechanic_id
            WHERE r.relationship IN ('verifies_mechanic', 'supports_mechanic')
              AND (
                    r.from_id IN (SELECT verification_id FROM live_verifications)
                 OR r.from_id IN (SELECT claim_id FROM claims WHERE needs_live_verification = 'yes')
              )
            GROUP BY m.mechanic_id, m.title, m.status
            ORDER BY m.mechanic_id
            """
        )

    # Backwards-compatible alias for the original success-criteria phrasing.
    def mechanics_blocked_by_live_verification(self) -> list[dict]:
        return self.mechanics_pending_live_verification()

    def contradictions_affecting(self, object_id: str) -> list[dict]:
        """Which contradictions affect this recommendation (a mechanic or rule)?

        Resolves three paths and labels each via ``link_path``:
          * direct_mechanic - the object is a mechanic a contradiction affects;
          * direct_rule     - the object is a rule that records a contradiction;
          * indirect_rule   - rule --depends_on_mechanic--> mechanic
                              <--affects_mechanic-- contradiction.
        """

        return self._all(
            """
            -- direct: object is a mechanic the contradiction affects
            SELECT c.contradiction_id, c.title, c.confidence, c.planner_implications,
                   'direct_mechanic' AS link_path
            FROM contradictions c
            JOIN object_references r
              ON r.from_id = c.contradiction_id AND r.relationship = 'affects_mechanic'
            WHERE r.to_id = ?

            UNION

            -- direct: object is a rule that records the contradiction
            SELECT c.contradiction_id, c.title, c.confidence, c.planner_implications,
                   'direct_rule' AS link_path
            FROM object_references rr
            JOIN contradictions c ON c.contradiction_id = rr.to_id
            WHERE rr.from_id = ? AND rr.relationship = 'has_contradiction'

            UNION

            -- indirect: object is a rule depending on a mechanic the contradiction affects
            SELECT c.contradiction_id, c.title, c.confidence, c.planner_implications,
                   'indirect_rule' AS link_path
            FROM object_references dep
            JOIN object_references aff
              ON aff.to_id = dep.to_id AND aff.relationship = 'affects_mechanic'
            JOIN contradictions c ON c.contradiction_id = aff.from_id
            WHERE dep.from_id = ? AND dep.relationship = 'depends_on_mechanic'

            ORDER BY 1, 5
            """,
            (object_id, object_id, object_id),
        )

    # ------------------------------------------------------------------ #
    # Metadata                                                           #
    # ------------------------------------------------------------------ #
    def meta(self) -> dict:
        return {r["key"]: r["value"] for r in self._all("SELECT key, value FROM runtime_meta")}
