4 files


# Q2 Supplemental Template Positions
## Extracted from Remaining Templates (2021–2025)
 
This file supplements `q2-standard-positions.md` with positions from the remaining templates:
- Amendment Template v. 2023
- Partner Marketplace Developer Agreement (2021)
- Partner Marketplace SDK License Agreement (2021)
- Terms of Use of SDK or APIs (2024)
- Standalone Hosting & Security Addendum (2024)
- Standalone Security Addendum Exhibit C (standard + CCPA variant, 2024)
- Bank Services Agreement Template (Helix)
- Channel Partner Program Addendum (Centrix variant) v. 2024
- Partner Accelerator Program Addendum (Annual w True-Up) v. 2024
- Partner Accelerator Program Addendum (Variable) v. 2024
- Partner Integration Agreement (Ciphertext Example)
- Q2 Certified Delivery Partner Agreement (Dec 2025)
- Referral Program Addendum (Lead Referral) v. 2023
- Referral Program Addendum (Standard) v. 2023
---
 
## 1. Amendment Template
 
**Q2 Standard Structure:**
- Short form — identifies the base agreement being amended, the Amendment Effective Date (date of last signature), and contains inline T&C edits
- Except as modified, all other agreement terms ratified and confirmed
- Uses same signature block as MPA (SCM DocuSign fields)
**Flag if counterparty proposes:**
- 🟡 Amendment purporting to override MPA terms without explicit statement of precedence
- 🟡 Missing ratification clause (could be read as replacing entire agreement)
- 🟡 Amendment Effective Date retroactive without agreement
---
 
## 2. Referral Program Addendums (Standard and Lead Referral)
 
**Key positions:**
 
**Referral Fee:** 5% of Net License Revenues on Initial Order (one-time payment)
 
**Net License Revenues:** Software license revenues from Initial Order only — excludes: renewal revenues, third-party product revenues, installation/maintenance/support fees, discounts, taxes, shipping/handling, procurement fees
 
**Payment terms:** Q2 pays Partner within 45 days of receiving Partner's invoice; Q2 provides Quarterly Reports within 4 weeks after each quarter end
 
**Referral Fee survival post-termination:** 3 months (except termination for cause by Q2)
 
**Lead Referral variant — lead acceptance:**
- Q2 has 5 business days to accept/reject a lead
- Accepted lead auto-revokes if: (a) meeting not scheduled within 30 days or (b) meeting not held within 60 days of acceptance
- Q2's rejection decisions are final — no liability to Partner
**No assignment:** Referral addendums are personal to Partner — no assignment without Q2's prior written consent (stricter than MPA)
 
**Liability cap carve-outs:** Same MPA five carve-outs (confidentiality, IP/indemnification, gross negligence/willful misconduct, payment obligations) — consistent with Q2 standard
 
**Flag if counterparty proposes:**
- 🟡 Referral fees on renewals or services revenues (Q2 standard is initial order license fees only)
- 🟡 Payment within less than 45 days after Quarterly Report
- 🟡 Survival of referral fee obligations beyond 3 months post-termination
- 🟡 Assignment rights in a referral agreement (expressly prohibited in Q2 standard)
---
 
## 3. Partner Accelerator Addendums (Annual w True-Up and Variable)
 
**These addendums govern Partners who have built applications on Q2's SDK.**
 
**Fee structure:**
- Annual: 30% × Annual Revenue; minimum $9,600/year per Client; true-up quarterly
- Variable: 30% × monthly Revenue; minimum $800/month per Client; paid monthly within 30 days
**Auto-renewal notice:** Only **30 days** (shorter than MPA standard of 180 days for Channel/Reseller)
 
**Initial term:** 12 months (short — flag if counterparty pushes for longer without justification)
 
**Liability carve-outs:** Same MPA five carve-outs — NOT the broader Reseller Addendum language
 
**Insurance:** E&O/Cyber at **$5M per claim** (lower than MPA's $10M — specific to Accelerator context)
 
**Flag if counterparty proposes:**
- 🟡 Fee percentages below 30% of revenue
- 🟡 Minimum fees waived or below $800/month
- 🟡 Auto-renewal notice longer than 90 days (Q2 standard for Accelerator is 30 days, very favorable to Q2)
---
 
## 4. Partner Marketplace Developer Agreement & SDK License Agreement (2021)
 
**These are older Marketplace-era agreements — use as reference for SDK/API licensing context.**
 
**Key SDK/API positions:**
- Q2 owns all rights in SDK/APIs; Developer owns all rights in Applications built on them
- License is: personal, non-exclusive, non-transferable, revocable
- Developer may not: sublicense, reverse engineer, decompile, disassemble, use to gain unauthorized access
- No viral open-source integration (no GPL/LGPL)
- Feedback: Developer assigns all IP in feedback/suggestions to Q2 (perpetual, worldwide, royalty-free)
**SDK License Agreement — Residuals clause (note):**
This older SDK License contains a **residuals clause** allowing use of CI retained in unaided memory. This is NOT in Q2's standard NDA templates or MPA. When reviewing counterparty paper:
- 🔴 If a counterparty's NDA or agreement includes a residuals clause, flag it — Q2's standard agreements (NDA, MPA) do not include this
- The Certified Delivery Partner Agreement (2025) also includes a residuals clause — this is the newer pattern for developer/delivery agreements specifically
**Marketplace Developer Agreement — Liability cap:**
- Indemnification claims: capped at greater of $3M or fees received by that party
- Other claims: capped at 12 months of fees paid/received
- This is a more complex dual-tier cap specific to Marketplace context
**Security breach notification:** 24 hours after discovery (consistent with Reseller standard)
 
---
 
## 5. Terms of Use of SDK or APIs (2024)
 
**Short-form click-through terms incorporated by reference into Partner Program Addendums.**
 
Key restrictions on Partner:
- No sublicense, rental, reverse engineering, or disassembly of SDK/APIs
- No third-party software provider access to Applications without Q2's prior written consent
- No use for unauthorized access to any service, data, or network
- No Viral Open-Source Software integration
- Export controls apply (no embargoed nations)
**Order of precedence:** SDK Terms control over conflicting Agreement terms unless Agreement expressly states otherwise.
 
**Flag if counterparty tries to:**
- 🔴 Exclude SDK Terms from their agreement scope
- 🔴 Allow sublicensing or third-party access to Applications without Q2 consent
- 🟡 Alter the order of precedence so their agreement terms prevail over SDK Terms
---
 
## 6. Standalone Security Addendums (2024) — Standard and CCPA Variant
 
**These are the definitive Q2 security requirements for Partners handling Client/End User Data.**
 
**Key requirements on Partner (buy-side):**
- Comprehensive written information security program
- AES encryption in transit and at rest (largest key space practical)
- Industry-standard firewalls, up-to-date anti-virus
- Vulnerability scanning: **weekly minimum** on all network assets
- SOC 1 Type II and SOC 2 Type II reports annually, at Partner's expense
- Penetration testing: annual external pen test by independent third party
- MFA required on all internet-accessible applications
- IP filtering against known malicious IPs and OFAC-restricted countries
- Security Breach notification: **within 24 hours** of discovery/suspicion
- Background checks on all personnel with access to Client Data (7-year criminal history, OFAC, SSN trace, credit checks)
- Business continuity and disaster recovery plans — tested annually
- Data retention: records maintained minimum 5 years (or per litigation hold)
- No transfer of Q2 CI outside United States without prior written consent
- Annual Q2 audit right (60 days notice; more frequent if material breach or regulatory requirement)
- Subcontractors: Partner remains primarily liable; must flow down all Security Addendum obligations
**CCPA Variant — additional obligations:**
- Company (Partner) may not sell or share Personal Information
- Personal Information used only for Business Purposes specified in agreement
- Must assist Q2 with consumer deletion requests
- Cannot combine Q2 customer Personal Information with data from other sources
- Must notify Q2 if it can no longer meet CCPA obligations
**Standalone Hosting & Security Addendum (for Channel Partner / Centrix):**
This variant covers Q2's *own* security obligations when Q2 is the service provider:
- Q2 maintains comprehensive written ISSP
- Q2 security breach notification to Partner: **within 48 hours**
- Q2 provides SOC 1 and SOC 2 Type II reports annually
- Q2 maintains BCTA (business continuity/technology availability plan), tested annually
- Document destruction with certificate on request
- Background checks on Q2 personnel with access to Client Data
- Partner audit rights: once per 12 months (30 days notice); more frequent for regulatory or material breach
**Flag if counterparty proposes weaker standards than Q2's Security Addendum:**
- 🔴 Breach notification window longer than 48 hours
- 🔴 No SOC 2 Type II obligation
- 🔴 No Q2 audit right
- 🔴 Vulnerability scanning less frequent than weekly
- 🔴 No background check obligations for personnel with access to Client Data
- 🔴 Transfer of Q2 CI outside US without consent
- 🟡 Annual testing not required for BCTA/DR plans
---
 
## 7. Bank Services Agreement (Helix Template)
 
**Used for Q2's Bank of Record relationships in the Helix BaaS program — specialized.**
 
**Key distinctive positions (different from standard partner agreements):**
 
**Governing law / venue:** Asymmetric — Q2 brings claims in Travis County, Texas; Bank brings claims in a county TBD (left blank in template). Flag if Bank insists on a non-Texas venue for Q2.
 
**Liability cap:** Mutual 12-month cap; no consequential damages (same carve-outs as MPA)
 
**IP:** Q2 owns Helix exclusively; Bank gets limited revocable license for Banking Services only. Suggestions/feedback from Bank: Bank grants Q2 worldwide, non-restricted, perpetual royalty-free license.
 
**Right of First Refusal:** Q2 has ROFR on substantially similar services Bank might seek from third parties — Bank must offer to Q2 first on stated terms, Q2 has 30 days to accept/reject.
 
**Term:** 60-month initial term; auto-renews for 36-month Renewal Terms; 180-day non-renewal notice.
 
**Termination cure period:** 90 days (longer than MPA's 30 days — specific to banking relationship complexity)
 
**Security breach notification:** Within 48 hours
 
**Non-solicitation:** Bank cannot solicit Helix Client customers, vendors, or licensors for 1 year post-termination.
 
**Flag if counterparty (Bank) proposes:**
- 🔴 Removal of Q2's Right of First Refusal on Substantially Similar Services
- 🔴 Venue outside Texas for Bank's claims against Q2
- 🟡 Initial term shorter than 60 months (Bank relationship requires significant investment)
- 🟡 No non-solicitation post-termination
---
 
## 8. Channel Partner Addendum — Centrix Variant (for COCC, Apiture)
 
**Substantively similar to standard Channel Partner Addendum with two important additions:**
 
**Existing Partner Clients protection:**
- Q2 cannot directly solicit Partner's known Existing Partner Clients during the Term
- If Q2 directly contracts an Existing Partner Client, Q2 owes Partner a **20% referral fee** of Q2's monthly revenue from that client during the initial term, escalating by 5% per additional breach (up to 40% maximum)
- Symmetric protection: Partner cannot solicit Q2's Existing Q2 Clients; if it does, Partner owes Q2 the equivalent escalating referral fee
**Auto-renewal notice:** **120 days** (versus 180 days in standard Channel Partner Addendum)
 
**Enhanced Liability Cap:**
This variant replaces the MPA General Liability Cap for certain claims with an **Enhanced Cap**:
- Carve-out claims (confidentiality breach, IP breach, indemnification, gross negligence/willful misconduct): capped at the **greater of (i) 36 months of fees paid or (ii) highest monthly fee × 36**
- This is Q2's enhanced/escalated cap for Centrix-type partnerships — not the standard MPA cap
- **Note:** This Enhanced Cap is broader than the MPA five carve-outs but still capped — it is NOT unlimited exposure. This is acceptable as a negotiated Centrix-specific position.
**Flag:**
- 🔴 Counterparty trying to remove the existing client protection provisions (§ 2.9)
- 🟡 Enhanced Cap applied to standard (non-Centrix) Channel Partner relationships
- 🟡 Auto-renewal notice shorter than 120 days in Centrix-type deals
---
 
## 9. Partner Integration Agreement (Ciphertext Example)
 
**Used for bilateral integration deals where Q2 integrates with a Partner's product for mutual clients.**
 
**Key distinctive positions:**
 
**Integration ownership:** Q2 owns the Integration (except Partner Materials integrated therein); Partner owns Company Services and Company Materials.
 
**Feedback/suggestions:** Each party assigns IP in suggestions to the receiving party (mutual assignment — different from MPA where only Partner assigns to Q2).
 
**Termination for convenience:** Q2 can terminate on **30 days' notice** (unlike MPA which has no T4C right). This is Q2-favorable.
 
**Co-Program Fees:** 30% of amounts Partner collects from Active Program Clients for Partner Services.
 
**Governing law:** Texas (Travis County) — consistent with Q2 standard.
 
**Change of Control:** Assignment permitted in M&A (unlike standard NDA which has no M&A exception); surviving entity assumes obligations.
 
**Liability cap:** 12-month fees paid by Partner to Q2; carve-outs for indemnification, confidentiality breach, and proprietary rights breach — consistent with MPA five carve-outs (not broader).
 
---
 
## 10. Q2 Certified Delivery Partner Agreement (Dec 2025) — Most Recent Template
 
**Used for third-party implementation/delivery partners certified to deploy Q2 Products.**
 
**Key distinctive positions:**
 
**Fee structure:** Partner pays Q2 **10% of total fees** Partner charges Customers for delivery services (reverse flow — Partner pays Q2 for certification/access, not Q2 paying Partner).
 
**Certification:** Per-product, per-individual. Valid 2 years; refresh required within 60 days of material product changes; renewal within 30 days of expiration.
 
**Termination of certification:** Q2 can terminate individual certifications on 15 days' notice for non-compliance with certification requirements.
 
**Termination for convenience:** No T4C in this agreement (unlike Partner Integration Agreement) — only termination for cause.
 
**Non-compete restriction on Company:** Company may not develop, commercialize, or distribute enhancements that replace or replicate core Q2 Product functionality, compete with Q2's subscription model, or undermine Q2's business model.
 
**Residuals clause:** This 2025 agreement includes a residuals clause (same pattern as the 2021 SDK License). This is intentional for developer/delivery agreements — NOT a position to offer in commercial or NDA contexts.
 
**Governing law:** Texas (Travis County, non-exclusive) — consistent with Q2 standard.
 
**Dispute resolution:** Good faith executive negotiation for 30 days before formal proceedings — consistent with MPA.
 
**Security:** Full Security Addendum (Exhibit A) incorporated — same obligations as standalone Security Addendum.
 
**Insurance:** E&O/Cyber at **$1M per claim** (lower than MPA $10M — this is a delivery partner, not a technology vendor; flag if a technology vendor tries to use this lower limit).
 
**Flag if counterparty proposes:**
- 🔴 Certified Delivery Partner insurance limits ($1M E&O) applied to a technology/SaaS vendor relationship (should be $10M or $5M)
- 🔴 Removal of non-compete restriction on competing with Q2's core product functionality
- 🟡 Certification renewal periods extended beyond Q2's standard
---
 
## Template Coverage Summary
 
| Template | Status | Key Flag Topics |
|---|---|---|
| Master Partner Agreement v. 2024 | ✅ Full coverage in q2-standard-positions.md | Governs all addenda |
| Amendment Template v. 2023 | ✅ Covered above | Precedence, retroactivity |
| Reseller Program Addendum v. 2024 | ✅ Full coverage in q2-standard-positions.md | Unlimited exposure (reject) |
| Channel Partner Addendum v. 2024 | ✅ Full coverage in q2-standard-positions.md | 3-year term, 180-day notice |
| Channel Partner Addendum (Centrix) v. 2024 | ✅ Covered above | Existing client protection, Enhanced Cap |
| Partner Accelerator Agreement (Click-thru) v. 2024 | ✅ Full coverage in q2-standard-positions.md | Fee structure, IP ownership |
| Partner Accelerator Addendum (Annual) v. 2024 | ✅ Covered above | 30-day renewal notice |
| Partner Accelerator Addendum (Variable) v. 2024 | ✅ Covered above | Monthly fees, 30-day notice |
| Integration Agreement Template (2022) | ✅ Full coverage in q2-standard-positions.md | NY law (legacy) |
| Referral and Integration Agreement | ✅ Full coverage in q2-standard-positions.md | Fee structure |
| Referral Program Addendum (Standard) v. 2023 | ✅ Covered above | 5% fee, no assignment |
| Referral Program Addendum (Lead Referral) v. 2023 | ✅ Covered above | Lead registration policy |
| Partner Marketplace Developer Agreement (2021) | ✅ Covered above | SDK/API licensing, feedback |
| Partner Marketplace SDK License Agreement (2021) | ✅ Covered above | Residuals clause (developer only) |
| Terms of Use of SDK or APIs (2024) | ✅ Covered above | SDK restrictions, precedence |
| Standalone Hosting & Security Addendum (2024) | ✅ Covered above | Q2's own security obligations |
| Standalone Security Addendum Exhibit C (2024) | ✅ Covered above | Partner security obligations |
| Standalone Security Addendum (w CCPA) (2024) | ✅ Covered above | CCPA addendum obligations |
| Bank Services Agreement (Helix) | ✅ Covered above | ROFR, 60-month term, asymmetric venue |
| Partner Integration Agreement (Ciphertext) | ✅ Covered above | T4C for Q2, Co-Program Fees |
| Q2 Certified Delivery Partner Agreement (2025) | ✅ Covered above | 10% fee, non-compete, $1M insurance |
| All 6 NDA Templates | ✅ Full coverage in q2-nda-positions.md | See NDA reference file |
| CONNECT 25 Speaker Agreement | ⬜ Out of scope for commercial contract review | Events/speaking only |
