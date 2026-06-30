#!/usr/bin/env python3
"""Demonstration of the CRE runtime query layer.

Run after building the runtime:

    python3 -m runtime.build_runtime
    python3 -m runtime.examples.run_queries
"""

from __future__ import annotations

import json

from ..queries import Runtime


def _show(title: str, payload) -> None:
    print(f"\n### {title}")
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def main() -> None:
    with Runtime() as rt:
        _show("runtime metadata", rt.meta())
        _show("retrieve mechanic M-0007", rt.get_mechanic("M-0007"))
        _show("retrieve planner rule PR-0003", rt.get_planner_rule("PR-0003"))
        _show("retrieve decision D-0001", rt.get_decision("D-0001"))
        _show("retrieve contradiction C-0002", rt.get_contradiction("C-0002"))
        _show("retrieve unknown U-0001", rt.get_unknown("U-0001"))
        _show("evidence chain for CL-0042", rt.get_evidence_chain("CL-0042"))

        print("\n" + "=" * 64)
        print("Success-criteria queries")
        print("=" * 64)
        _show("Which planner rules depend on M-0007?", rt.planner_rules_depending_on("M-0007"))
        _show("Which evidence supports CL-0042?", rt.evidence_supporting_claim("CL-0042"))
        _show("Which decisions reference M-0010?", rt.decisions_referencing("M-0010"))
        _show("Which mechanics have pending live verification?", rt.mechanics_pending_live_verification())
        _show("Which contradictions affect mechanic M-0005? (direct)", rt.contradictions_affecting("M-0005"))
        _show("Which contradictions affect rule ER-0002? (direct rule)", rt.contradictions_affecting("ER-0002"))
        _show("Which contradictions affect rule PR-0003? (indirect via mechanic)", rt.contradictions_affecting("PR-0003"))


if __name__ == "__main__":
    main()
