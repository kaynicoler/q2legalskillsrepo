---
name: contract-review
description: Review legal contracts, NDAs, employment agreements, SaaS terms, and M&A documents. Identifies unfavorable terms, suggests redlines, and compares to market standards. Use for contract analysis, due diligence, or negotiation prep.
version: 3.0.0
---

# Contract Review Skill

Review legal contracts for risks, extract key terms, and suggest redlines. Built on the CUAD dataset (41 risk categories), ContractEval benchmarks, and LegalBench.

## When to Activate

- User mentions "review contract", "analyze agreement", "check this contract"
- User uploads or references a PDF/DOCX legal document
- User asks about specific clauses, risks, or terms

---

## Q2 NDA Review Instructions

### Q2 NDA Playbook — Controlling Standard

When the document is an NDA, confidentiality agreement, mutual NDA, one-way NDA, or otherwise contains confidentiality provisions that require NDA-style review, load and apply `q2-nda-playbook.md` from this skill directory.

The Q2 NDA Playbook is Q2 Software's controlling substantive standard for NDA review.

Apply the following source priority for NDA reviews:

1. The NDA under review
2. `q2-nda-playbook.md`
3. Q2 standard NDA templates or approved Q2 fallback language
4. Generic contract-review guidance in this skill

If any generic checklist, benchmark, market-standard statement, CUAD category, risk heuristic, or example in this skill conflicts with the Q2 NDA Playbook, **the Q2 NDA Playbook controls**.

Use generic contract-review rules for issue spotting only. Do not let them override, supplement, expand, or contradict a clause-specific Q2 AI Decision Rule.

### Clause-Level Decision Framework

For every relevant NDA clause present in the document, identify the corresponding Q2 playbook clause and apply its AI Decision Rule.

Each playbook clause may define:
- **Preferred Language** — Q2's preferred drafting position
- **Fallback Language** — an acceptable negotiated compromise
- **Restricted Language** — language Q2 should not accept without revision
- **AI Decision Rule** — the controlling ACCEPT / COMMENT / REDLINE / ESCALATE instruction

Use these dispositions consistently:
- **ACCEPT** — substantively acceptable; no change required
- **COMMENT** — acceptable or potentially acceptable, but requires clarification, business confirmation, or a non-blocking note
- **REDLINE** — does not satisfy Q2's acceptable position and should be revised
- **ESCALATE** — requires attorney or appropriate stakeholder review rather than an attempted model-generated cure

Do not independently upgrade or downgrade the playbook result based on generic market standards.

If the playbook permits multiple outcomes depending on facts, apply the stated conditions and explain which condition controls. If no applicable playbook provision can be identified, state that the issue is not clearly addressed by the Q2 NDA Playbook rather than inventing a Q2 position.

### Balanced NDA Principle

Do not redline language merely because Q2's preferred wording could be substituted. A drafting preference is not a legal or commercial issue by itself.

If a provision satisfies the Q2 playbook's ACCEPT criteria, falls within an expressly acceptable range, or reaches the same substantive result as Q2's acceptable position:
- mark the provision **Reviewed & Acceptable**;
- do not generate a redline solely to conform wording to Q2 paper;
- do not characterize the provision as risky merely because the drafting differs from Q2's preferred language.

Preserve negotiation capital for provisions that create meaningful legal, commercial, operational, or compliance exposure. A balanced NDA may legitimately produce zero redlines. When appropriate, conclude: **Recommendation: Approve as drafted. No redlines required.**

### Restricted Language and Redlines

When the playbook identifies Restricted Language:
1. Explain briefly why the provision is problematic.
2. Apply the clause-specific AI Decision Rule.
3. If the result is REDLINE, replace or narrow the problematic language using Q2 Preferred Language first, or Q2 Fallback Language when the preferred position is unnecessarily aggressive or the playbook directs use of the fallback.
4. Make the smallest change necessary to resolve the Q2 concern.

Use the **Restricted Language → Preferred Language / Fallback Language** pattern when generating redlines for `legal-redline-tools`. Prefer surgical edits over wholesale clause replacement. Do not add unrelated protections while correcting another issue.

### Mandatory Escalation Triggers

Flag the following for attorney or designated stakeholder review and do not attempt to fully cure them unless the applicable Q2 playbook rule expressly authorizes a specific redline:
- Indemnification in a standalone NDA
- Non-circumvention or no-contact restrictions
- Broad non-solicitation beyond the Q2-approved scope
- NDA language that supersedes an existing MSA, DPA, SOW, or other governing agreement without an appropriate carveout
- Q2 entity identity that is unclear, incorrect, or inconsistent
- Any provision expressly designated ESCALATE by the Q2 NDA Playbook
- Any provision whose legal effect cannot be determined confidently from the document
- Any material provision not covered by the Q2 playbook where accepting it would create a substantive Q2 obligation or restriction

For escalated issues, identify the clause, explain the issue briefly, identify the relevant playbook rule where available, and state what decision or confirmation is required. Do not invent an approved Q2 position.

### NDA-Specific Review Workflow

For an NDA review, perform this sequence:

1. **Pre-Review Check** — Confirm legal names, correct Q2 entity, effective date, draft/executed status, blank fields, missing exhibits, mutual vs. one-way structure, and references to other governing confidentiality agreements.
2. **Identify NDA Structure** — Determine Q2's role, stated purpose, confidentiality duration, trade secret treatment, permitted recipients, required-disclosure procedure, return/destruction obligations, governing law/venue, and any obligations beyond confidentiality.
3. **Apply Q2 Playbook Clause by Clause** — Map relevant provisions to the Q2 NDA Playbook and apply the controlling AI Decision Rule. Do not use generic NDA benchmarks to override the playbook.
4. **Identify Non-NDA Restrictions** — Pay particular attention to indemnification, non-solicitation, non-circumvention, no-contact, non-compete, exclusivity, standstill, IP assignments, residuals, feedback rights, publicity rights, audit rights, unusual security obligations, unrelated representations/warranties, and language modifying existing agreements.

### NDA Output Format

Use this structure for NDA reviews:

1. **NDA Review: [Document Name]**
   - Document Type
   - Q2 Entity
   - Counterparty
   - Q2 Position
   - Risk Level
   - Document Status
2. **Pre-Signing Alerts** — Include only if applicable.
3. **Executive Summary** — State whether the NDA is balanced, whether material Q2 playbook deviations exist, whether redlines are required, and whether escalation is required. Do not overstate low-risk drafting differences.
4. **Key NDA Terms** — Include structure, purpose, confidentiality period, trade secret treatment, permitted recipients, compelled disclosure, return/destruction, residuals, governing law, and other material terms.
5. **Redlines Required** — Include only provisions whose Q2 AI Decision Rule results in REDLINE. For each, identify the issue, Q2 position, practical risk, surgical redline, and fallback only when supported by the playbook. If none, state: **None. The agreement does not contain provisions requiring substantive revision under the Q2 NDA Playbook.**
6. **Comments / Business Points** — Include clauses classified COMMENT. Do not place ACCEPT items here.
7. **Reviewed & Acceptable** — Always include this section and explain why accepted provisions are acceptable. Do not claim a provision is acceptable if it is absent or unsupported by the playbook.
8. **Escalations** — List all ESCALATE issues and identify what decision or attorney input is required. If none, state **None.**
9. **Missing or Unclear Provisions** — Identify only omissions or ambiguities that matter under the Q2 NDA Playbook. Do not recommend provisions merely because they appear in other NDAs.
10. **Recommendation** — Use the appropriate conclusion: **Approve as drafted. No redlines required.** / **Approve subject to the limited redlines above.** / **Business confirmation required before approval.** / **Attorney review required before execution.**

### NDA Override for Generic Checklists and Benchmarks

The generic `NDA Checklist`, `Risk Categories`, `Market Standard Benchmarks`, jurisdiction notes, and other contract-review heuristics in this skill are secondary guidance only when reviewing an NDA.

For NDA reviews:
- Do not automatically treat a particular confidentiality duration as acceptable or unacceptable based solely on generic market ranges.
- Do not assume that 3 years is always preferred.
- Do not automatically flag 2 years, 5 years, or another duration unless the Q2 NDA Playbook requires it.
- Do not classify a provision as a red flag solely because it differs from a generic benchmark.
- Do not apply SaaS, M&A, employment, payment, broker, or other document-type standards to an NDA unless the NDA actually creates that type of substantive obligation.
- Do not use CUAD categories to create negotiation requirements that do not exist in the Q2 playbook.
- Use generic checklists only to identify potentially relevant language that must then be evaluated under the Q2 playbook.

The Q2 NDA Playbook exclusively controls substantive NDA acceptability.

### NDA Review Guardrails

- Review only language actually present in the document.
- Do not hallucinate clauses, risks, or missing provisions.
- Quote or cite relevant agreement language when identifying material issues.
- Distinguish legal risk from drafting preference.
- Distinguish COMMENT from REDLINE.
- Do not turn every deviation from Q2 preferred wording into a negotiation point.
- Apply Q2 fallback positions when permitted instead of escalating unnecessarily.
- Use surgical redlines.
- Preserve acceptable counterparty language whenever possible.
- Always show material provisions that were reviewed and found acceptable.
- Escalate when the playbook requires escalation or when the Q2 position is genuinely unclear.
- Never rely on a generic market standard when a clause-specific Q2 rule exists.
- A balanced NDA may legitimately produce zero redlines.

---

## Step 1: Pre-Review Checklist

Before analyzing content, verify document completeness:

- [ ] **Blank fields**: Flag any "$X", "TBD", "[amount]", "____" placeholders
- [ ] **Missing exhibits**: List all referenced schedules/exhibits and note which are missing
- [ ] **Signature status**: Draft or already executed?
- [ ] **All pages present**: Check for truncation or missing sections

If blank fields or missing exhibits exist, flag prominently in output header.

---

## Step 2: Identify Document Type & User Position

**Ask if unclear:** "Which party are you? (customer, vendor, buyer, seller, licensor, licensee, receiving party, disclosing party)"

This affects what's "risky":
- Customer reviewing vendor agreement → flag vendor-favorable terms
- Vendor reviewing own template → flag customer-favorable terms
- Buyer in M&A → flag seller-favorable terms
- Seller in M&A → flag buyer-favorable terms
- Receiving party in NDA → flag disclosing party-favorable terms

**Assess power dynamic:**
- Startup vs. large enterprise? (limited negotiating leverage)
- Standard form vs. negotiated? (some terms non-negotiable)
- Regulated industry? (some terms legally required)

---

## Output Format

Use **markdown** for readable, scannable output. Do NOT use XML tags.

---

### Example Output

```markdown
# Contract Review: [Document Name]

**Document Type:** SaaS Subscription Agreement
**Your Position:** Customer
**Counterparty:** Acme Software Inc.
**Risk Level:** 🟡 Medium
**Document Status:** Draft / Executed on [date]

## ⚠️ Pre-Signing Alerts

- **Blank field:** Fee amount in Section 4.1 is "$____"
- **Missing exhibit:** Exhibit B (SLA) referenced but not attached

## Executive Summary

Standard vendor agreement with some one-sided terms. The 3-month liability cap and
asymmetric termination rights need attention. Data ownership is clear.

---

## Key Terms

| Term | Value | Location |
|------|-------|----------|
| Initial Term | 12 months | Section 8.1 |
| Auto-Renewal | 12-month periods, 60-day notice | Section 8.2 |
| Liability Cap | 3 months' fees | Section 10.2 |
| Governing Law | Delaware | Section 12.1 |

---

## Red Flags (Quick Scan)

| Flag | Found | Location |
|------|-------|----------|
| Liability cap < 6 months | ⚠️ Yes | Section 10.2 |
| Uncapped indemnification | No | — |
| Unilateral amendment rights | ⚠️ Yes | Section 14.1 |
| No termination for convenience | No | — |
| Perpetual obligations | No | — |
| Offshore jurisdiction | No | — |

---

## Risk Analysis

### 🔴 Critical

**Limitation of Liability** (Section 10.2)
> "Liability shall not exceed fees paid in the preceding three (3) months"

- **Issue:** 3-month cap is below market standard (typically 12 months)
- **Risk:** For $120K annual contract, liability capped at $30K
- **Market Standard:** 12 months' fees
- **Negotiability:** Medium — most vendors accept 6-12 months
- **Redline:** Change "three (3) months" → "twelve (12) months"
- **Fallback:** Accept 6 months as compromise

---

### 🟡 Important

**Termination for Convenience** (Section 8.5)
> "Vendor may terminate for any reason upon 30 days notice"

- **Issue:** One-sided; customer lacks equivalent right
- **Market Standard:** Mutual termination rights
- **Negotiability:** High — reasonable ask
- **Redline:** Add "Either party may terminate..." or change to "90 days"

---

### 🟢 Reviewed & Acceptable

| Category | Status | Notes |
|----------|--------|-------|
| Data Ownership | ✓ | Customer owns all customer data |
| IP Rights | ✓ | Clear separation, no broad assignment |
| Confidentiality | ✓ | Mutual, 3-year term, standard exceptions |
| Governing Law | ✓ | Delaware — neutral for commercial |

---

## Missing Provisions

| Provision | Priority | Why It Matters |
|-----------|----------|----------------|
| Data Export Rights | Critical | No guaranteed way to get data out on termination |
| SLA Credits | Important | 99.9% uptime stated but no remedy for breach |
| Price Increase Cap | Important | Renewal pricing uncapped |

**Suggested language for Data Export:**
> "Upon termination, Vendor shall make Customer Data available for export in CSV or JSON format for 90 days at no additional charge."

---

## Internal Consistency Issues

- ⚠️ Section 5.2 references "Exhibit C" but no Exhibit C exists
- ⚠️ "Confidential Information" defined in Section 3.1 but used lowercase in Section 7

---

## Negotiation Priority

| # | Issue | Ask | Negotiability |
|---|-------|-----|---------------|
| 1 | Liability cap | 12 months | Medium |
| 2 | Termination rights | Mutual | High |
| 3 | Data export | Add provision | High |
| 4 | Price cap | 5% annual max | Medium |

---

*This review is for informational purposes only. Material terms should be reviewed by qualified legal counsel.*
```

---

## Red Flags Quick Scan

Check these danger signs FIRST before deep analysis:

| Red Flag | Why It Matters |
|----------|----------------|
| Liability cap < 6 months | Inadequate protection |
| Uncapped indemnification | Unlimited exposure |
| "As-is" with no warranty | No recourse for defects |
| Unilateral suspension without notice | Service can vanish |
| Unilateral amendment rights | Terms can change |
| No termination for convenience | Locked in |
| Perpetual obligations (tails, non-competes) | Indefinite exposure |
| Offshore jurisdiction (BVI, Cayman) | Expensive to enforce |
| Pre-signed conflict waivers | No recourse for conflicts |
| "Sole discretion" language favoring counterparty | No objective standard |
| Class action waiver + mandatory arbitration | Limited remedies |
| Asymmetric assignment rights | They can assign, you can't |

---

## Document Type Checklists

### NDA Checklist

| Category | Check For |
|----------|-----------|
| Direction | One-way or mutual? |
| Definition scope | "All information" too broad? Standard exceptions? |
| Term | 2 years short, 3-5 typical, indefinite for trade secrets |
| Permitted disclosure | "Representatives" defined? Flow-down required? |
| Residuals clause | Can use general knowledge retained in memory? |
| Non-solicitation | Employees protected? |
| Standstill | Prevents hostile acquisition actions? |
| No-contact | Customers, suppliers, employees protected? |
| Return/destruction | Certification required? |
| Public announcement | Prohibits disclosure of discussions? |
| Compelled disclosure | Notice required? Time to seek protective order? |
| Injunctive relief | Pre-agreed specific performance? Bond waiver? |

### SaaS/MSA Checklist

| Category | Check For |
|----------|-----------|
| Liability cap | 12+ months = standard |
| Uptime SLA | 99.9% with credits = standard |
| Suspension rights | Unilateral? Notice required? |
| Data ownership | Customer owns customer data? |
| Data export | Format, duration, cost on termination? |
| Price increases | Capped? Notice period? |
| Auto-renewal notice | 90+ days = good, <60 = risk |
| Termination | Mutual for convenience? Cure period for cause? |
| Subprocessors | Notice of changes? Approval rights? |
| Insurance | Vendor carries E&O, cyber? |

### Payment/Merchant Agreement Checklist

| Category | Check For |
|----------|-----------|
| Reserve/holdback | Amount, duration, release conditions? |
| Chargeback liability | Capped? Fraud protection? |
| Network rules | Incorporated by reference? Access provided? |
| Auto-debit authority | Notice before debits? |
| Settlement timing | When do you receive funds? |
| Volume commitments | Realistic? Penalty for shortfall? |
| Suspension rights | Immediate or notice? |
| Termination tail | How long do obligations survive? |
| Audit rights | Frequency, notice, cost allocation? |
| PCI compliance | Who bears cost? |

### M&A Agreement Checklist

| Category | Check For |
|----------|-----------|
| Purchase price | Cash vs. stock vs. earnout mix? |
| Earnout mechanics | Measurement, discretion, audit rights, acceleration? |
| Escrow/holdback | Amount (10-15% typical), duration (12-18 mo), release? |
| Rep survival | 12-24 months general, longer for fundamental |
| Indemnification cap | 10-20% of purchase price typical |
| Basket type | True deductible vs. tipping? |
| Sandbagging | Pro-buyer or anti-sandbagging? |
| Non-compete | 2-3 years, geographic scope? |
| Working capital | Target, collar, true-up mechanism? |
| MAC definition | Carve-outs for market conditions? |
| Employment comp | Counted in purchase price or separate? |

### Finder/Broker Agreement Checklist

| Category | Check For |
|----------|-----------|
| Fee percentage | Specified or blank? |
| Fee calculation | What's included in deal value? Employment comp? |
| "Covered buyer" definition | How broad? Any prior relationship carve-out? |
| Tail period | 12-24 months typical; perpetual = red flag |
| Exclusivity | Exclusive or non-exclusive? |
| Minimum fee | Floor amount? |
| Joint representation | Consent required? Conflict waiver? |
| Escrow deduction | Auto-pay from proceeds? |
| Term/termination | Can you exit? |
| Broker status | BD registered if securities involved? |

---

## Risk Categories (CUAD 41 + Extensions)

### Document Basics
- Document Name and Type
- Parties (legal names, roles)
- Agreement Date / Effective Date
- Expiration Date
- Renewal Terms
- **Document Status** (draft/executed)
- **Blank Fields / Placeholders**

### Term & Termination
- Contract Term / Duration
- Termination for Convenience
- Termination for Cause
- Post-Termination Services
- Survival Clauses
- **Suspension Rights** (immediate vs. with notice)
- **Cure Periods**

### Assignment & Control
- Anti-Assignment Clause
- Change of Control
- Consent Requirements
- **Asymmetric Assignment** (they can, you can't)

### Financial Terms
- Payment Terms
- Price Restrictions / Adjustments
- Most Favored Nation (MFN)
- Minimum Commitment
- Volume Restrictions
- Audit Rights
- **Price Escalation Caps**
- **Reserve/Holdback Requirements**
- **Auto-Debit Authority**

### Liability & Risk
- Limitation of Liability
- Cap on Liability
- Uncapped Liability Carve-outs
- Indemnification
- Insurance Requirements
- Warranty Duration
- **Warranty Disclaimer (As-Is)**
- **Exclusive Remedy Clauses**
- **Chargeback/Return Liability**

### IP & Confidentiality
- IP Ownership Assignment
- License Grant
- Affiliate License - Licensor/Licensee
- Covenant Not To Sue
- Non-Compete
- Non-Solicitation (Employees/Customers)
- Competitive Restriction Exception
- Exclusivity
- Non-Disparagement
- Confidentiality Duration
- Third Party Beneficiary
- **Residuals Clause**
- **Feedback Ownership**

### Dispute Resolution
- Governing Law
- Jurisdiction / Venue
- Arbitration vs Litigation
- Jury Trial Waiver
- **Class Action Waiver**
- **Offshore Jurisdiction Flags**

### Special Provisions
- ROFR / ROFO / ROFN
- Revenue/Profit Sharing
- Joint IP Ownership
- Source Code Escrow
- Irrevocable or Perpetual License
- **Data Export Rights**
- **Uptime/Availability SLA**
- **Sublicensing Rights**
- **Unilateral Amendment Rights**

---

## Market Standard Benchmarks

| Provision | Standard | Yellow Flag | Red Flag |
|-----------|----------|-------------|----------|
| **Liability cap** | 12 months' fees | 6-11 months | <6 months |
| **Non-compete duration** | 1-2 years | 3-4 years | 5+ years |
| **Non-compete geography** | Where business operates | State-wide | Nationwide |
| **Auto-renewal notice** | 90+ days | 60-89 days | <60 days |
| **Termination notice** | Mutual, 60-90 days | One-sided, 30 days | Immediate |
| **Indemnification** | Mutual, capped | Asymmetric | Uncapped |
| **Rep survival (M&A)** | 12-18 months general | 24-30 months | 36+ months |
| **Escrow (M&A)** | 10-15% for 12-18 mo | 15-20% for 18-24 mo | >20% or >24 mo |
| **Confidentiality (NDA)** | Apply Q2 NDA Playbook | Do not use generic duration benchmark | Do not use generic duration benchmark |
| **Fee tail (broker)** | 12-18 months | 24 months | Perpetual |
| **SLA uptime** | 99.9% with credits | 99.5% | No SLA |
| **Data export** | 90 days, standard format | 30 days | None |
| **Price increase cap** | CPI or 5% annual | 10% annual | Uncapped |
| **Cure period** | 30 days | 15 days | None |

---

## Negotiability Guide

| Rating | Meaning | Examples |
|--------|---------|----------|
| **High** | Usually accepted | Mutual termination, cure periods, data export |
| **Medium** | Depends on leverage | Liability cap increase, price caps |
| **Low** | Rarely changed | Network rules (payments), regulatory requirements |
| **None** | Non-negotiable | Card network mandates, banking regulations |

**Power dynamic factors:**
- Large customer + small vendor = more leverage
- Startup + enterprise vendor = less leverage
- Competitive market = more leverage
- Sole-source vendor = less leverage
- Regulated terms = no leverage (legally required)

---

## Jurisdiction Notes

**Non-Competes:**
- California, North Dakota, Oklahoma, Minnesota: Generally void
- Other states: Reasonableness test applies

**Choice of Law:**
- Delaware: Corp-friendly, predictable
- New York: Financial agreements, sophisticated courts
- California: Employee-friendly, tech industry
- BVI/Cayman: Offshore, expensive to litigate, potential red flag

**Arbitration Venues:**
- AAA, JAMS: Standard US commercial
- SIAC (Singapore), LCIA (London): International, expensive
- Mandatory + class waiver: Limits remedies significantly

---

## Guardrails

- **Not legal advice**: Recommend attorney review for material terms
- **Not tax advice**: Flag but don't opine
- **Jurisdiction matters**: Note when enforceability varies
- **Express uncertainty**: Say when interpretation is unclear
- **No hallucination**: Only reference text actually in document
- **Show what's acceptable**: Always include "Reviewed & Acceptable" section
- **Document status matters**: Note if already executed (review is informational)
