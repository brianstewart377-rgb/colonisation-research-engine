"""Runtime query examples.

A small, read-only query layer demonstrating the questions the runtime must be
able to answer. No optimisation, no caching, no business logic - just clear
projections over the generated schema. The runtime is opened read-only so it can
never be mutated through this interface.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from .config import DEFAULT_OUTPUT_DB


def _row_to_dict(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


class Runtime:
    """Read-only accessor over a generated CRE runtime database."""

    def __init__(self, db_path: Path | str = DEFAULT_OUTPUT_DB):
        self._conn = sqlite3.connect(f"file:{Path(db_path)}?mode=ro", uri=True)
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
