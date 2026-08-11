---
name: general-counsel-advisor
description: "General Counsel advisory for startups: contract review (MSA, SaaS, NDA, DPA, employment), IP strategy, term sheet decoding, and regulatory landscape mapping. Use when reviewing any contract or term sheet, deciding when to engage outside counsel, defining IP strategy, evaluating regulatory exposure (HIPAA, GDPR, FDA, fintech), or when user mentions general counsel, GC, legal review, contract risk, term sheet, IP assignment, or regulatory exposure. NOT a substitute for licensed counsel — surfaces questions to bring to qualified attorneys."
llm: Claude
version: v2
updated: 2026-08-11T21:57:55.915Z
created: 2026-07-07T16:40:20.912Z
---
# General Counsel Advisor

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#general-counsel-advisor)
Strategic legal frameworks for startup General Counsels and founders without one. Contract risk, IP strategy, term sheet decoding, regulatory landscape.

This is not legal advice. It surfaces the right questions to bring to qualified outside counsel and catches the obvious traps before they reach a signature. Treat every output as a starting point for a conversation with a licensed attorney, not as a substitute for one.

## Keywords

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#keywords)
general counsel, GC, legal review, contract review, MSA, SaaS agreement, NDA, DPA, employment agreement, contractor agreement, IP assignment, invention assignment, open source license, OSS compliance, term sheet, liquidation preference, anti-dilution, option pool, vesting, acceleration, drag-along, pro-rata, board composition, regulatory, HIPAA, GDPR, CCPA, FDA, MDR, fintech, BSA/AML, money transmitter, AI Act, indemnity, liability cap, force majeure, auto-renewal, choice of law, venue, non-compete, non-solicit

## Quick Start

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#quick-start)

```
# Scan a contract for risky clauses (uses bundled sample if no path given)
python scripts/contract_risk_scanner.py
python scripts/contract_risk_scanner.py path/to/contract.txt

# Analyze a term sheet for founder-friendliness
python scripts/term_sheet_analyzer.py
python scripts/term_sheet_analyzer.py path/to/term_sheet.json
```

## Key Questions (ask these first)

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#key-questions-ask-these-first)

- Who owns the IP being created or shared? (Founders forget that contractors don't auto-assign IP without a written clause.)
- What's the liability cap, and what's carved out? (Standard: 12 months of fees, with carve-outs for IP infringement, data breach, willful misconduct.)
- Is there a DPA in place if any personal data flows? (GDPR, CCPA, state laws — non-negotiable if EU/CA data is touched.)
- What's the termination right, notice period, and auto-renewal trap? (5-year auto-renew with 60-day notice is a common founder mistake.)
- Does this contract or product launch trigger a new regulatory regime? (Healthcare → HIPAA. Fintech → BSA/AML. Medical device → FDA/MDR.)
- For term sheets: liquidation preference, pre-money option pool, anti-dilution flavor? (Three places where 5% of founder economics can quietly disappear.)

## Core Responsibilities

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#core-responsibilities)

### 1. Contract Review

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#1-contract-review)
Standard contracts a startup signs in its first 5 years:

- Vendor MSA — Master Service Agreement (cloud, tooling, services)
- Customer SaaS Agreement — your standard customer paper + customer redlines
- NDA — mutual + one-way, with carve-outs for residuals + independent development
- DPA — Data Processing Agreement (required when personal data flows)
- Employment Agreement — offer letter, IP assignment, non-compete (where enforceable), arbitration
- Contractor / 1099 Agreement — IP assignment is critical; misclassification risk
- Equity Agreements — option grants, RSU agreements, advisor grants (FAST template, YC SAFE for advisors)

Run `contract_risk_scanner.py` on the text. It flags the 12 most common founder-killer clauses.

### 2. IP Strategy

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#2-ip-strategy)

- Invention assignment — every employee and contractor signs one. No exceptions.
- Open source license compliance — track every OSS dependency's license; AGPL and GPL trigger copyleft obligations.
- Trade secrets — define what's protected and how (clean room dev, access controls, NDAs).
- Patents — file provisional within 12 months of disclosure; PCT for international.
- Trademarks — register the word mark first, design mark second; clear before launch.
- Copyright — automatic on creation, but register for statutory damages eligibility.

See `references/ip_and_regulatory.md`.

### 3. Term Sheet Decoding

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#3-term-sheet-decoding)
When a term sheet arrives, the difference between a founder-friendly and founder-hostile sheet often hides in three clauses:

- Liquidation preference — 1x non-participating is standard; 1x participating or 2x is hostile
- Pre-money vs post-money option pool — pre-money pool dilutes founders; post-money dilutes everyone proportionally
- Anti-dilution — broad-based weighted average is standard; full ratchet is hostile

Run `term_sheet_analyzer.py` to get a 0-100 founder-friendliness score with flags.

### 4. Regulatory Landscape

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#4-regulatory-landscape)
When to engage outside counsel before committing:

| Trigger | Regime | First Step |
| --- | --- | --- |
| Healthcare data | HIPAA, HITECH, state breach laws | Specialist health-tech counsel |
| Cardholder data | PCI DSS (industry standard, not law, but contractually required) | QSA + counsel |
| Money movement | BSA/AML, state money-transmitter (50-state patchwork) | Fintech specialist |
| Medical device claims | FDA 510(k) / De Novo / PMA, MDR (EU), ISO 13485 | Medical-device specialist |
| EU residents' personal data | GDPR + EU AI Act if AI is deployed | EU privacy counsel |
| California residents | CCPA / CPRA | Privacy generalist |
| Securities (tokens, equity crowdfunding) | SEC rules (Reg D, Reg A+, Reg CF) | Securities counsel |
| Defense / aerospace customers | ITAR, EAR, DFARS, CMMC | Export-control counsel |
| AI in EU | EU AI Act (risk-tiered) | EU privacy + product counsel |
| AI for hiring (NYC, CO, IL) | Local bias-audit laws | Employment counsel |

See `references/ip_and_regulatory.md` for sequencing.

## Workflows

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#workflows)

### Workflow 1: Contract Review

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#workflow-1-contract-review)

1. Save the contract as plain text
2. Run `contract_risk_scanner.py path/to/contract.txt`
3. For each HIGH risk finding, draft a counter-proposal
4. Bring the redline + counter-proposals to outside counsel
5. Log the decision via `/cs:decide`

### Workflow 2: Term Sheet Response

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#workflow-2-term-sheet-response)

1. Save the term sheet as a JSON file matching the schema in `term_sheet_analyzer.py --help`
2. Run `python scripts/term_sheet_analyzer.py path/to/term_sheet.json`
3. Review the founder-friendliness score and per-clause flags
4. Negotiate the worst 3 clauses (don't try to win all 20)
5. Always have a securities/venture attorney review before signing
6. Log via `/cs:decide` with `/cs:freeze 30` to prevent regret-driven re-opening

### Workflow 3: IP Hygiene Audit

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#workflow-3-ip-hygiene-audit)

1. Confirm every employee and contractor (past 12 months) signed invention assignment
2. Run an OSS license inventory (`pip-licenses`, `license-checker` for npm)
3. Map AGPL/GPL dependencies and confirm compliance (or remove)
4. File provisional patents on novel inventions (12-month deadline from disclosure)
5. Register word-mark trademarks for the product name

### Workflow 4: Regulatory Trigger Assessment

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#workflow-4-regulatory-trigger-assessment)

1. List planned product features for the next 12 months
2. Map each feature to the trigger table in this document
3. For any HIPAA / FDA / fintech trigger, engage a specialist counsel before building
4. Document the regulatory roadmap and budget alongside the product roadmap
5. Pair with `cs-ciso-advisor` for ISO 27001 / SOC 2 sequencing

## Output Standard (when invoked via `/cs:gc-review`)

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#output-standard-when-invoked-via-csgc-review)

```
**Bottom Line:** [sign / negotiate / do not sign]
**The Risks:** [3 highest-severity issues]
**Counter-Proposals:** [specific language]
**Outside Counsel Action Items:** [what to bring to the attorney]
**Your Decision:** [the call only the founder can make]

```

## Adjacent Skills

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#adjacent-skills)

- `c-level-advisor/skills/ciso-advisor/` — Compliance overlap (SOC 2, ISO 27001, HIPAA technical safeguards)
- `c-level-advisor/skills/cfo-advisor/` — Term sheet → dilution math
- `c-level-advisor/skills/ma-playbook/` — Acquisition agreements, integration playbooks
- `ra-qm-team/` — ISO 13485, MDR, FDA 510(k), GDPR execution
- `c-level-advisor/c-level-agents/skills/gc-review/SKILL.md` — `/cs:gc-review` slash command

## References

[](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md#references)

- [contracts_playbook.md](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/references/contracts_playbook.md) — Standard contracts, clause checklist, common founder traps
- [ip_and_regulatory.md](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/references/ip_and_regulatory.md) — IP protection + regulatory landscape mapping
- [term_sheet_decoder.md](https://github.com/alirezarezvani/claude-skills/blob/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/references/term_sheet_decoder.md) — Term sheet glossary + founder-friendly defaults + pushback strategies


---

## Reference: contracts_playbook

#!/usr/bin/env python3
"""contract_risk_scanner.py — Scan a contract for founder-killer clauses.

Stdlib-only. Outputs human-readable or JSON. Detects 12 common risk patterns:
  1. Unilateral termination favoring the counterparty
  2. Auto-renewal with long notice (60+ days)
  3. Uncapped liability or exclusion of standard caps
  4. Broad indemnification flowing one direction
  5. Non-mutual confidentiality
  6. Missing or vague IP ownership clauses
  7. Aggressive non-compete / non-solicit
  8. Choice of law/venue in counterparty's home jurisdiction (one-sided)
  9. Force majeure favoring only the counterparty
 10. Missing DPA reference when personal data flows
 11. Most-favored-nation pricing clauses
 12. Audit rights without reciprocity

NOT legal advice. Use this to triage; bring findings to qualified counsel.

Usage:
    python contract_risk_scanner.py                       # uses embedded sample
    python contract_risk_scanner.py path/to/contract.txt
    python contract_risk_scanner.py contract.txt --output json
    python contract_risk_scanner.py --help
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from typing import List


SAMPLE_CONTRACT = """\
MASTER SERVICES AGREEMENT

This Agreement shall automatically renew for successive one (1) year terms
unless either party provides ninety (90) days written notice of non-renewal.

LIMITATION OF LIABILITY. In no event shall Provider's aggregate liability
arising out of this Agreement exceed the fees paid by Customer in the
twelve (12) months preceding the claim. Notwithstanding the foregoing,
Customer's indemnification obligations under Section 8 shall be uncapped.

INDEMNIFICATION. Customer shall defend, indemnify and hold harmless
Provider, its affiliates, officers, directors and employees from and against
any and all claims, damages, losses and expenses arising out of or relating
to Customer's use of the Services.

INTELLECTUAL PROPERTY. The parties agree that intellectual property created
during the engagement shall belong to the party who develops it.

NON-COMPETE. For a period of three (3) years following termination, Customer
shall not engage with any competitor of Provider in any capacity, in any
geography.

GOVERNING LAW. This Agreement shall be governed by the laws of Delaware,
and any disputes shall be resolved exclusively in the state and federal
courts located in Wilmington, Delaware.

FORCE MAJEURE. Provider shall not be liable for any failure to perform due
to causes beyond its reasonable control.
"""


@dataclass
class Finding:
    rule_id: str
    severity: str           # CRITICAL | HIGH | MEDIUM | LOW
    title: str
    excerpt: str
    why_it_matters: str
    suggested_redline: str


RULES = [
    {
        "id": "AUTO_RENEW_LONG_NOTICE",
        "severity": "HIGH",
        "title": "Auto-renewal with long notice period",
        "pattern": re.compile(
            r"automatically renew.{0,200}?(\d+|sixty|ninety|one hundred|180)\s*(\(\d+\))?\s*day",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "Auto-renewal with >30 day notice is a classic vendor trap: founders forget the "
            "deadline and get locked into another full term. Especially painful on multi-year contracts."
        ),
        "redline": (
            "Counter: '...unless either party provides thirty (30) days written notice of non-renewal' "
            "OR remove auto-renewal entirely and require affirmative re-signature."
        ),
    },
    {
        "id": "UNCAPPED_CUSTOMER_INDEMNITY",
        "severity": "CRITICAL",
        "title": "Customer indemnity carved out from liability cap (uncapped)",
        "pattern": re.compile(
            r"(customer'?s|your)\s+indemnification.{0,200}?(uncapped|shall be uncapped|excluded from)",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "Uncapped customer indemnity means a single bad claim can exceed all fees ever paid. "
            "Standard practice: mutual indemnity, both sides capped at fees, with narrow carve-outs "
            "(IP infringement, data breach, gross negligence)."
        ),
        "redline": (
            "Counter: cap customer indemnity at 12 months of fees, mutual indemnity, carve-outs only "
            "for willful misconduct and breach of confidentiality."
        ),
    },
    {
        "id": "ONE_SIDED_INDEMNITY",
        "severity": "HIGH",
        "title": "Indemnification flows in one direction only",
        "pattern": re.compile(
            r"(customer|client)\s+shall\s+(defend|indemnify).{0,500}?(provider|company|vendor)",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "One-sided indemnity means you take on risk for the counterparty's actions without reciprocity. "
            "A balanced contract has mutual indemnification with mirrored carve-outs."
        ),
        "redline": (
            "Counter: 'Each party shall defend, indemnify and hold harmless the other party...' with "
            "mirrored scope and equal caps."
        ),
    },
    {
        "id": "VAGUE_IP",
        "severity": "CRITICAL",
        "title": "Vague IP ownership clause",
        "pattern": re.compile(
            r"intellectual property.{0,200}?(belong to the party who develops it|jointly owned|to be determined|as agreed)",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "Vague IP language is the #1 source of post-engagement disputes. Joint ownership often means "
            "neither party can license freely without the other's consent. 'As agreed' is unenforceable."
        ),
        "redline": (
            "Counter: 'All work product, deliverables, and derivative works created under this Agreement "
            "shall be the sole and exclusive property of Customer. Provider hereby assigns all right, title "
            "and interest...' Or explicitly carve out Provider's pre-existing IP and tools with a license back."
        ),
    },
    {
        "id": "AGGRESSIVE_NONCOMPETE",
        "severity": "HIGH",
        "title": "Aggressive non-compete (long duration or broad geography)",
        "pattern": re.compile(
            r"non.compete.{0,300}?(two|three|four|five|2|3|4|5)\s*\(?\d*\)?\s*year",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "Non-competes >12 months or with unbounded geography are often unenforceable (especially in "
            "California, and increasingly federally) but create chilling effects. They also signal the "
            "counterparty's overall negotiation posture."
        ),
        "redline": (
            "Counter: maximum 12 months, specific competitor list (not 'any competitor'), specific "
            "geography. For California-resident counterparties, remove entirely (California labor code "
            "voids most non-competes)."
        ),
    },
    {
        "id": "ONE_SIDED_VENUE",
        "severity": "MEDIUM",
        "title": "Choice of law/venue exclusively in counterparty jurisdiction",
        "pattern": re.compile(
            r"(exclusively in|exclusive jurisdiction).{0,300}?(courts? located in|state and federal courts of)",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "Exclusive venue in counterparty's jurisdiction means you bear travel cost and out-of-state "
            "counsel cost for any dispute. For startups this can effectively prevent enforcement."
        ),
        "redline": (
            "Counter: neutral venue (Delaware is common), or 'venue in the jurisdiction of the defendant' "
            "(forces plaintiff to travel), or arbitration in a neutral location with AAA/JAMS rules."
        ),
    },
    {
        "id": "ONE_SIDED_FORCE_MAJEURE",
        "severity": "MEDIUM",
        "title": "Force majeure clause favors one party",
        "pattern": re.compile(
            r"(provider|company|vendor)\s+shall not be liable.{0,200}?(force majeure|causes beyond)",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "If only the vendor gets force-majeure protection, you pay full price during a pandemic / "
            "outage / supply chain disruption but receive nothing. Mutual force majeure is standard."
        ),
        "redline": (
            "Counter: 'Neither party shall be liable...' with explicit list of qualifying events "
            "(pandemic, war, natural disaster, government action) and a termination right after 30 days."
        ),
    },
    {
        "id": "MISSING_DPA",
        "severity": "HIGH",
        "title": "Personal data appears to flow but no DPA referenced",
        "pattern": re.compile(
            r"(personal data|personally identifiable|user data|customer data|PII)(?!.{0,500}(DPA|data processing agreement|GDPR))",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "If personal data of EU residents (or California residents) flows, a DPA is legally required. "
            "Missing DPA = GDPR Article 28 violation, potential 4%-of-revenue fine, contract unenforceable "
            "with EU customers."
        ),
        "redline": (
            "Counter: 'The parties shall execute a Data Processing Agreement substantially in the form "
            "of Exhibit X prior to any processing of Personal Data.' Use IAPP or Vendor-friendly DPA template."
        ),
    },
    {
        "id": "MOST_FAVORED_NATION",
        "severity": "MEDIUM",
        "title": "Most-favored-nation (MFN) pricing clause",
        "pattern": re.compile(
            r"(most.favored.nation|MFN|best price|lowest price).{0,200}?(offered to|charged to)",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "MFN clauses prevent you from offering volume discounts or strategic pricing to anyone else. "
            "If you sign with one customer, every future customer can demand the same price."
        ),
        "redline": (
            "Counter: remove the MFN entirely. If kept, narrow to 'similarly situated customers, same "
            "tier and volume, excluding strategic / launch / migration discounts.'"
        ),
    },
    {
        "id": "ONE_SIDED_AUDIT",
        "severity": "MEDIUM",
        "title": "Audit rights without reciprocity",
        "pattern": re.compile(
            r"(customer|client).{0,100}?right to audit",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "One-sided audit rights mean the counterparty can demand records on demand, often at your "
            "expense. Reciprocity is standard for B2B agreements."
        ),
        "redline": (
            "Counter: mutual audit rights, max once per year, at requesting party's expense, with "
            "30-day notice, during business hours, narrowed to specific compliance categories."
        ),
    },
    {
        "id": "BROAD_NON_SOLICIT",
        "severity": "MEDIUM",
        "title": "Broad non-solicit (employees AND customers, long duration)",
        "pattern": re.compile(
            r"non.solicit.{0,300}?(employees? and customers?|customers? and employees?)",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "Combined employee + customer non-solicits, especially with long duration, can severely "
            "limit hiring and business development. Many states limit enforceability."
        ),
        "redline": (
            "Counter: split into employee-only (12 months max) and customer-only (12 months max) clauses, "
            "with carve-outs for general advertising / open job postings and for customers who initiate "
            "contact independently."
        ),
    },
    {
        "id": "PERPETUAL_LICENSE_BACK",
        "severity": "HIGH",
        "title": "Perpetual license-back to counterparty of your data or work",
        "pattern": re.compile(
            r"perpetual.{0,100}?(license|right).{0,300}?(customer data|user data|work product|deliverables)",
            re.IGNORECASE | re.DOTALL,
        ),
        "why_it_matters": (
            "A perpetual license-back lets the counterparty use your data or deliverables forever, even "
            "after termination. This is acceptable for usage analytics, NOT for customer data or core IP."
        ),
        "redline": (
            "Counter: time-limited license (for the term of the agreement only), specific purpose "
            "(service delivery only, not training AI models, not sharing with third parties), and "
            "post-termination return-or-destroy obligation."
        ),
    },
]


def scan(text: str) -> List[Finding]:
    findings: List[Finding] = []
    for rule in RULES:
        for match in rule["pattern"].finditer(text):
            excerpt = match.group(0).strip()
            # truncate long excerpts
            if len(excerpt) > 300:
                excerpt = excerpt[:297] + "..."
            findings.append(Finding(
                rule_id=rule["id"],
                severity=rule["severity"],
                title=rule["title"],
                excerpt=excerpt,
                why_it_matters=rule["why_it_matters"],
                suggested_redline=rule["redline"],
            ))
    # rank by severity then rule order
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    findings.sort(key=lambda f: (severity_order.get(f.severity, 9), f.rule_id))
    return findings


def render_text(findings: List[Finding], source: str) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("CONTRACT RISK SCAN")
    lines.append(f"Source: {source}")
    lines.append(f"Findings: {len(findings)}")
    lines.append("=" * 72)
    lines.append("")
    if not findings:
        lines.append("No risk patterns matched. (Absence of findings does not mean the contract is safe;")
        lines.append("it means the 12 common patterns this scanner checks did not trigger.)")
        lines.append("")
        lines.append("Always engage qualified counsel before signing.")
        return "\n".join(lines)

    severity_counts = {}
    for f in findings:
        severity_counts[f.severity] = severity_counts.get(f.severity, 0) + 1
    severity_summary = "  ".join(
        f"{sev}: {severity_counts.get(sev, 0)}"
        for sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW")
        if severity_counts.get(sev, 0) > 0
    )
    lines.append(f"Severity: {severity_summary}")
    lines.append("")

    for i, f in enumerate(findings, 1):
        lines.append(f"[{i}] {f.severity} — {f.title}")
        lines.append(f"    Rule: {f.rule_id}")
        lines.append(f"    Excerpt: \"{f.excerpt}\"")
        lines.append("")
        lines.append(f"    Why it matters:")
        for line in _wrap(f.why_it_matters, 4):
            lines.append(line)
        lines.append("")
        lines.append(f"    Suggested redline:")
        for line in _wrap(f.suggested_redline, 4):
            lines.append(line)
        lines.append("")
        lines.append("-" * 72)

    lines.append("")
    lines.append("REMINDER: This scanner triages obvious traps. Always bring redlines to qualified counsel.")
    return "\n".join(lines)


def _wrap(text: str, indent: int, width: int = 68) -> List[str]:
    import textwrap
    return textwrap.wrap(text, width=width, initial_indent=" " * indent, subsequent_indent=" " * indent) or [" " * indent + text]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a contract for the 12 most common founder-killer clauses.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("path", nargs="?", help="Path to contract text file (uses embedded sample if omitted)")
    parser.add_argument("--output", choices=("text", "json"), default="text", help="Output format")
    args = parser.parse_args()

    if args.path:
        try:
            with open(args.path, "r", encoding="utf-8") as f:
                text = f.read()
            source = args.path
        except (IOError, OSError) as e:
            print(f"error: could not read {args.path}: {e}", file=sys.stderr)
            return 1
    else:
        text = SAMPLE_CONTRACT
        source = "<embedded sample MSA>"

    findings = scan(text)

    if args.output == "json":
        payload = {
            "source": source,
            "findings_count": len(findings),
            "findings": [asdict(f) for f in findings],
        }
        print(json.dumps(payload, indent=2))
    else:
        print(render_text(findings, source))

    return 0


if __name__ == "__main__":
    sys.exit(main())

## Reference: ip_and_regulatory

# IP Strategy & Regulatory Landscape

The two areas where startups most often discover legal exposure after it's too late to fix cheaply: IP ownership and regulatory triggers. **Not legal advice.**

## Part 1: IP Strategy

### IP Inventory — The Four Categories

| Type | What it protects | How you get it | How you lose it |
|---|---|---|---|
| **Patents** | Inventions (novel, non-obvious, useful) | File application | Public disclosure > 12 months before filing |
| **Copyright** | Original works of authorship (code, content, designs) | Automatic on fixation | Almost never; can be assigned away |
| **Trademark** | Brand identifiers (names, logos, slogans) | Use in commerce + registration | Not policing infringement; becoming generic |
| **Trade secret** | Confidential business information | Reasonable measures to keep secret | Public disclosure; failure to maintain confidentiality |

### Invention Assignment — The Single Most Important IP Practice

**Rule:** Every person who touches the company's product or systems must sign an invention assignment agreement **before** they start work.

This includes:
- Co-founders (often forgotten — usually fixed via founder restricted-stock purchase agreements)
- Employees (in employment agreement)
- Contractors (in contractor agreement; NOT automatic in US law)
- Interns (often forgotten — use a short standalone IP agreement)
- Advisors (in advisor agreement, scope limited to inventions related to company)

**Why it matters:** Without written assignment, the creator retains ownership. A contractor who built a critical service for 6 months and never signed an assignment can come back years later and demand a license — or assert that competitors can also use what they built.

**The "previously created inventions" exhibit:** Every IP assignment should include an exhibit where the signer lists pre-existing inventions they want to exclude. This protects everyone — the signer's prior work isn't accidentally assigned, and the company has documentation of what came in.

### Open Source License Compliance

**Permissive licenses** (MIT, Apache 2.0, BSD 2/3): Use freely, attribute, no copyleft.

**Weak copyleft** (LGPL, MPL): Can use in proprietary product; modifications to the OSS itself must be released. Distribution model matters.

**Strong copyleft** (GPL v2, GPL v3, AGPL): Distribution / SaaS use of a strong-copyleft component can require releasing your derivative work under the same license. **AGPL is the most aggressive** — it applies even when you only run the software on a server (SaaS / network use).

**Practice:**

1. Maintain an OSS inventory: `pip-licenses`, `license-checker` (npm), `cargo-license`, `go-licenses`.
2. Identify any GPL / AGPL / SSPL dependencies.
3. For each: either (a) comply with the license, (b) replace with a permissively-licensed alternative, or (c) document the carve-out (some companies build internally with GPL but only ship the binary externally — verify with counsel).
4. Run the inventory before any due diligence (acquisition, financing).

### Patents — When to File

**File when:**

- You have a genuinely novel technical invention (algorithm, hardware design, materials, biotech process).
- You face well-funded competitors who could copy without consequence.
- You're in a patent-dense industry (semiconductors, pharma, networking, medical devices).
- Filing strengthens fundraising / acquisition optics (limited weight for software-only startups).

**Don't bother when:**

- Your "invention" is a UX flow or business method (these are extremely hard to patent post-Alice Corp).
- You're in early stage with limited capital and no competitors close enough to copy.
- Defensive only and joining a patent pool (LOT Network, OIN) might be cheaper.

**Process:**

1. **Provisional patent** ($300-500 USPTO fee + $3K-5K attorney). 12 months to file non-provisional.
2. **Non-provisional / utility patent** ($1K USPTO fee + $10K-15K attorney + prosecution costs).
3. **PCT application** for international filings ($5K-10K).
4. **National phase entries** in each country you care about ($5K-15K per country).

Budget $25K-50K total for one well-prosecuted patent family with international coverage.

### Trade Secrets

**Reasonable measures required for legal protection:**

- NDA / confidentiality clauses with everyone who has access.
- Access controls (need-to-know basis, not company-wide).
- Marking documents "Confidential."
- Departure procedures (return of materials, exit interview, deactivation).
- Training employees on what's a trade secret.

**Without these measures, the information may not qualify for trade secret protection if disclosed — even by a thief.**

**Common trade secrets:**

- Customer lists with usage / pricing data
- Algorithms not disclosed in published patents
- Manufacturing processes
- Sales playbooks and pricing models
- Internal financial projections
- Source code (unless OSS)

### Trademark Strategy

**Search before launch:**

- USPTO TESS search (free, but limited; doesn't catch common-law marks).
- Professional search via attorney ($500-2K) catches common-law marks and similar-mark conflicts.
- International searches via WIPO Global Brand Database.

**Register early:**

- US: Intent-to-use application (1B) lets you reserve a mark before launch.
- International: Madrid Protocol filing extends to 100+ countries.
- Word marks first (the brand name itself), design marks second (logos).

**Policing:**

- Set up Google Alerts and USPTO TMNG for your mark.
- Send cease-and-desist letters promptly; failure to police can weaken the mark.

---

## Part 2: Regulatory Landscape — When to Engage Counsel

The startups that survive their first regulatory encounter engage specialist counsel **before** building, not after. The ones that don't usually pivot, retreat, or pay heavy fines.

### Trigger Matrix

| Trigger | Regulatory Regime | Specialist Needed | Earliest Action |
|---|---|---|---|
| Healthcare data (patient records, claims, PHI) | HIPAA, HITECH, state breach laws | Health-tech attorney | Business Associate Agreement, OCR-aligned risk assessment |
| Cardholder data | PCI DSS (industry standard; contractually required) | QSA + counsel | Scope reduction, tokenization, certified processor |
| Money movement (transmitting funds, custody, crypto) | BSA/AML, state money-transmitter (50-state patchwork) | Fintech attorney | Stripe Treasury / Banking as a Service to avoid MT registration |
| Lending | Truth in Lending Act, state usury laws, ECOA | Fintech / consumer-finance attorney | Bank partnership, state licensing analysis |
| Medical device claims | FDA 510(k), De Novo, PMA; EU MDR; ISO 13485 | Medical-device regulatory specialist | Pre-submission meeting with FDA |
| EU residents' personal data | GDPR + ePrivacy + EU AI Act if AI | EU privacy attorney | DPA, SCCs for international transfer, DPIA |
| California residents | CCPA / CPRA | Privacy generalist | Privacy notice, opt-out mechanisms, vendor management |
| Children's data (under 13 US, under 16 in some EU states) | COPPA, GDPR-K | Privacy attorney | Parental consent, no-track defaults |
| Securities (tokens, equity crowdfunding, advisory boards) | SEC rules (Reg D, Reg A+, Reg CF, Howey test) | Securities attorney | Token sale legal opinion, Form D filing |
| Defense / aerospace customers | ITAR, EAR, DFARS, CMMC | Export-control attorney | Export classification, registered with State Dept |
| AI in EU | EU AI Act (risk-tiered: prohibited / high-risk / limited / minimal) | EU privacy + product attorney | Risk assessment, conformity assessment for high-risk |
| AI for hiring | NYC Local Law 144, CO SB 21-169, IL HB 53 | Employment attorney | Bias audit, candidate notice |
| Telehealth / online prescribing | State medical board rules, DEA registration for controlled substances | Telehealth specialist | State-by-state physician licensing strategy |
| Insurance (sale, underwriting, brokerage) | State insurance commissioners | Insurance attorney | State licensing, agency agreement |

### Sequencing: SOC 2 → ISO 27001 → Industry-Specific

For most B2B SaaS, the security/compliance sequence is:

1. **SOC 2 Type 1** (point-in-time audit) — ~$15K-25K, 3-6 months prep
2. **SOC 2 Type 2** (continuous, ~6-12 month audit window) — ~$25K-50K
3. **ISO 27001** if expanding internationally — ~$30K-60K, builds on SOC 2 controls
4. **ISO 42001** if AI is core to product — first AI management system standard
5. **Industry overlays:** HIPAA technical safeguards, FedRAMP (federal customers), PCI DSS (cardholder data)

**Sequencing logic:** SOC 2 unlocks the majority of enterprise sales. ISO 27001 unlocks European and Asia-Pacific. Industry overlays are required for specific verticals.

### When to Get a General Counsel Hire

| Stage | GC need |
|---|---|
| Pre-seed / seed | None. Use outside counsel ad-hoc + Clerky/Stripe Atlas templates |
| Series A | Fractional GC (~$10-20K/month) OR senior associate at firm |
| Series B | Full-time GC if regulated industry, customer contracts are heavy, or fundraising is constant |
| Series C+ | Full-time GC + Deputy/Associate GC if international |

**Signs you need a GC hire:**

- You're spending > $200K/year on outside counsel
- You're signing > 1 enterprise contract per week with customer redlines
- You're in a regulated industry (healthcare, fintech, defense)
- You're preparing for IPO or going-public transaction
- You're acquiring companies

### Cross-Border Considerations

**Hiring international employees:**

- Use Deel / Remote / Velocity Global for first 1-5 contractors per country.
- Establish an entity (subsidiary or EOR-to-entity transition) at 5-10+ employees.
- Tax residency, permanent establishment risk, and equity grants vary significantly.

**International data flows:**

- EU → US: SCCs + Transfer Impact Assessment (TIA); DPF if certified.
- China → outbound: PIPL approval + standard contract + security assessment.
- UK → outside: UK SCCs (similar to EU).
- Schrems / DPF status changes regularly — monitor with privacy counsel.

**International IP:**

- Patent: PCT application within 12 months of first national filing.
- Trademark: Madrid Protocol for multi-country filings.
- Copyright: Berne Convention covers most countries automatically.

---

## Closing: The General Counsel's Three Rules

1. **Get it in writing.** Verbal agreements and "we'll figure it out later" produce 80% of post-engagement disputes.
2. **Identify the regulatory trigger before you build.** It's 10x cheaper to design around a regulation than to retrofit.
3. **Always have outside counsel review anything binding.** This document is triage; real legal review is mandatory.

## Reference: term_sheet_decoder

# Term Sheet Decoder

Glossary + founder-friendly defaults + pushback strategies for every clause in a standard venture term sheet. **Not legal advice.** Always engage venture / securities counsel before responding.

## The Three Clauses That Matter Most

In any term sheet review, focus disproportionately on these three. They drive ~80% of the founder economics impact.

### 1. Liquidation Preference

**What it is:** Investors get their investment back (the "preference") before founders see anything in an exit.

**The dimensions:**

- **Multiple:** 1x (standard) means $1 back per $1 invested. 2x means $2 back. Higher = more hostile.
- **Participating vs Non-participating:**
  - **Non-participating (founder-friendly):** Investor chooses preference OR convert to common at exit. Most exits hit the conversion threshold, so preference is effectively just downside protection.
  - **Participating ("double-dip"):** Investor gets preference back AND a pro-rata share of remaining proceeds as if converted. Significantly increases investor take in mid-range exits.
- **Cap:** Caps the total return at, say, 2x or 3x of investment for participating preferences. Limits the double-dip.

**Standard (Series A/B):** 1x non-participating.

**Hostile flavors:**
- 1x participating uncapped (significant founder dilution at exit)
- 2x preference (only acceptable in distressed rounds)
- Multi-stack preferences (Series A + Series B both get their preferences before any common)

**Pushback:** "Our standard is 1x non-participating. Participating preferences create misalignment with management at exit."

### 2. Option Pool — Pre-Money vs Post-Money

**The "option pool shuffle":** Investors typically require an unallocated option pool (10-20% of post-money) to be created **before** the new investment. If this comes out of pre-money, founders are diluted; if post-money, all shareholders dilute proportionally.

**Example math (Series A):**

| Scenario | Pre-Money | Pool Size | Effective Pre-Money for Founders |
|---|---|---|---|
| $30M pre, 10% pool pre-money | $30M | 10% of post | ~$26M (10% comes from founders) |
| $30M pre, 10% pool post-money | $30M | 10% of post | $30M (pool spread across all) |

**Standard:** 10-15% pool, often pre-money at Series A. Founder-friendly: smaller pool or post-money.

**Pushback:** "We've modeled our hiring plan and 8% supports the next 18 months. Let's right-size to actual need, not standard percentage." Or: "Pool top-up should come out of post-money so the new investor shares the dilution."

### 3. Anti-Dilution

**What it is:** Protection for investors against future down rounds. If a later round prices below the current, the current investor's price is adjusted retroactively.

**Flavors (least to most hostile):**

- **None:** Rare; only in seed SAFEs sometimes.
- **Broad-based weighted average (standard):** Adjusts using all shares (common, options, warrants). Modest founder dilution in a down round.
- **Narrow-based weighted average:** Uses only preferred. More dilutive than broad-based.
- **Full ratchet (hostile):** Investor's price resets entirely to the new round's price. Massively dilutive to founders.

**Standard:** Broad-based weighted average.

**Pushback:** "Full ratchet is non-starter at this stage. Narrow-based is unusual. We need broad-based weighted average — this is the NVCA standard."

---

## The Full Glossary

### Board Composition

**Standard at Series A:** 2 founders / 1 investor / 1 independent (or 1 founder / 1 investor / 1 independent for solo founders).

**At Series B:** Often 2 / 2 / 1 (balanced with independent tie-breaker).

**At Series C+:** Often investors get majority (signals control transition).

**Founder protection:** Always insist on the independent seat. Independent directors prevent deadlock and provide a neutral voice.

**Pushback on investor-majority boards at A:** "Investor control of the board at Series A is premature. Let's keep founder control with an independent tie-breaker until Series B."

### Vesting (for founders)

**Founder vesting in a financing:** Investors often require founder shares to be subject to vesting (re-vesting if you already exercised). Standard: 4 years, 1-year cliff. Often the cliff is waived if you've been at the company > 1 year.

**Acceleration:**

- **Single trigger:** All unvested shares vest immediately upon change of control. Founder-friendly but rare; investors resist.
- **Double trigger (standard):** Acceleration requires (a) change of control AND (b) involuntary termination of the founder within X months. Industry standard at Series A+.

**Pushback:** "Double-trigger acceleration is industry standard. Without it, founders are exposed to acquirer post-acquisition staffing decisions."

### Pro-Rata Rights

**What it is:** The right (but not obligation) to participate in future rounds proportionally to maintain ownership.

**Standard:** Lead investor + major investors (typically those above some ownership threshold) get pro-rata. Smaller checks often don't.

**Founder impact:** Granting pro-rata is generally fine — it shows investor conviction and aligns long-term. The cost is small dilution in future rounds.

**Pushback:** Only push back if there's a long tail of small investors each demanding pro-rata; cap to "major investors" defined by ownership %.

### Drag-Along

**What it is:** If a majority approves a sale, all shareholders must agree (including minority holders, including founders who later become minority).

**Founder-friendly version:** Drag-along requires founder consent OR a minimum sale price threshold (e.g., > 3x liquidation preference).

**Hostile version:** Drag-along with no founder consent and no price floor. Investors can force a sale at any price over founder objection.

**Pushback:** "Drag-along is standard, but we need founder consent OR a price floor."

### Protective Provisions

**What it is:** Investor consent rights for certain corporate decisions.

**Standard (NVCA model):**

- Issuing new senior or pari-passu preferred stock
- Authorizing new shares above existing pool
- Liquidating, merging, or selling the company
- Amending the charter or bylaws
- Increasing the board size
- Paying dividends
- Major debt

**Aggressive (push back):**

- Approving the annual budget
- Hiring or firing executives
- Setting compensation above thresholds
- Approving individual contracts above thresholds
- Capital expenditures above thresholds

**Pushback:** "We're aligned on the NVCA standard list. Operating decisions like budget and hiring are management's responsibility — protective provisions are for fundamental corporate changes."

### Information Rights

**Standard:** Quarterly unaudited financials, annual audited financials, annual budget.

**Aggressive (push back):** Monthly financials, board observer rights, weekly KPI dashboards, inspection rights at will.

**Pushback:** "Standard quarterly + annual is enough. Monthly creates significant CFO overhead at our stage. We'll commit to ad-hoc updates on material events."

### Dividends

**Standard:** None (default).

**Acceptable:** Non-cumulative dividends "when and if declared by the board" — almost never paid in practice.

**Hostile:** Cumulative dividends accrue every year regardless of declaration and must be paid in cash at exit. This is a creeping liquidation preference.

**Pushback:** "Cumulative dividends create a hidden liquidation preference that accrues over time. Non-cumulative when-declared, or none, is standard."

### Right of First Refusal (ROFR) / Co-Sale

**What it is:** If founders try to sell shares to a third party, investors have the right to buy first (ROFR) or to sell alongside (co-sale).

**Founder-friendly:** Standard ROFR + co-sale for all preferred; founders can still do secondary up to small thresholds without triggering.

**Hostile:** No secondary at all without unanimous investor consent.

**Pushback:** "We need to allow modest founder secondary (e.g., up to $1M aggregate) without investor consent — this is needed for founder financial planning."

### Founder Liquidity

**What it is:** Built-in secondary at later rounds (Series B/C) where founders sell some shares.

**Standard:** Becoming more common; 10-20% of round size as founder secondary.

**Pushback:** Raise this in Series B+ discussions; not typically negotiated at Series A.

### Most Favored Nation (MFN)

**What it is:** If you give a later investor better terms, the MFN-holder gets the same terms retroactively.

**Common in:** Seed SAFEs and convertible notes; rare in priced rounds.

**Founder trap:** MFN provisions can prevent you from offering competitive terms to new lead investors later. Be specific about what's covered (just SAFE terms? all terms?).

### No-Shop / Exclusivity

**What it is:** During due diligence, you can't shop the round to other investors.

**Standard:** 30-45 days. Founder-friendly. Investor-aligned because it shows commitment.

**Pushback only if:** > 60 days, or if it extends post-execution of definitive docs.

---

## Founder-Friendly Defaults (Cheat Sheet)

| Clause | Founder-Friendly Default |
|---|---|
| Liquidation preference | 1x non-participating |
| Anti-dilution | Broad-based weighted average |
| Option pool | 8-12%, post-money |
| Board (Series A) | 2F / 1I / 1Indep |
| Vesting (founder re-vest) | 4yr / 1yr cliff, often with credit for time served |
| Acceleration | Double-trigger |
| Pro-rata | For lead + major investors |
| Drag-along | Requires founder consent or price floor |
| Protective provisions | NVCA standard list only |
| Information rights | Quarterly + annual + budget |
| Dividends | None or non-cumulative when-declared |
| ROFR / co-sale | Standard, with carve-out for modest founder secondary |
| MFN (in notes/SAFEs) | Avoid if possible; if not, narrow scope |
| No-shop | 30-45 days |

---

## Negotiation Strategy

**Pick your battles:** A term sheet has 25-40 clauses. Winning every one is impossible and signals you don't understand priorities.

**Focus on the top 3 mistakes (in order):**

1. Liquidation preference flavor (participating vs non-participating)
2. Option pool pre-money vs post-money + size
3. Board control and protective provisions

These are the clauses where you can save 5-10% of founder economics or retain operating control. Everything else is secondary.

**The "founder-friendly NVCA" framing:** Many investors signal their posture by deviating from the NVCA model (the industry standard documents published by the National Venture Capital Association). Pushing back to "let's use the NVCA standard" is rarely rejected and resolves most issues.

**Walking away:** If a lead insists on:
- 1x participating uncapped preference
- Full ratchet anti-dilution
- Investor-majority board at Series A
- Cumulative dividends

These are not standard. A founder-friendly lead doesn't insist on these. Either walk or get specific written justification (sometimes a distressed cap-table situation justifies one of them, but never all).

---

## After Signing

Once the term sheet is signed:

1. **No-shop is active.** Don't talk to other investors except to officially decline.
2. **Definitive documents (SPA, IRA, Voting Agreement, ROFR Agreement) take 4-6 weeks.** Don't lose energy here; main fight was the term sheet.
3. **Closing conditions:** legal opinion, secretary's certificate, charter filing, capitalization confirmation.
4. **Wire timing:** Investors often wire 1-3 days after charter filing. Plan accordingly.

Run `scripts/term_sheet_analyzer.py` on the structured JSON of the term sheet for an automated scoring + flag analysis.

---

**Final reminder:** This document is a decoder, not a negotiation manual. Real term sheet response always involves your venture / securities counsel + your lead investor's diligence + your board (if any). Use this as a primer before those conversations.

