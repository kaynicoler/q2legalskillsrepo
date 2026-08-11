---
name: inbox-setup
description: "One-time setup skill that builds a personalized inbox triage knowledge base via interactive interview. Interviews the user about their email patterns, business context, reply style, and priorities using grill-me discipline (one question at a time, forcing format where possible, dependency-ordered, each question explains why I'm asking), then generates the knowledge base files that power the companion 'inbox-triage' skill. Run this once before using inbox-triage for the first time. Re-run when business, pricing, or priorities change significantly. Triggers: 'set up my inbox', 'configure inbox triage', 'set up my email system', 'configure email triage', 'build my email knowledge base', 'initialize email management', 'set up inbox triage', 'onboard email triage', or any variation where someone wants to get the email triage system running for the first time."
llm: Claude
version: v2
updated: 2026-08-11T22:12:43.616Z
created: 2026-07-07T17:07:35.546Z
---
---
name: inbox-setup
description: "One-time setup skill that builds a personalized inbox triage knowledge base via interactive interview. Interviews the user about their email patterns, business context, reply style, and priorities using grill-me discipline (one question at a time, forcing format where possible, dependency-ordered, each question explains why I'm asking), then generates the knowledge base files that power the companion 'inbox-triage' skill. Run this once before using inbox-triage for the first time. Re-run when business, pricing, or priorities change significantly. Triggers: 'set up my inbox', 'configure inbox triage', 'set up my email system', 'configure email triage', 'build my email knowledge base', 'initialize email management', 'set up inbox triage', 'onboard email triage', or any variation where someone wants to get the email triage system running for the first time."
license: MIT
metadata:
  source_spec: "megaprompts/06-inbox-setup-megaprompt.md"
  build_pattern: "Path B (direct conversion)"
  paired_with: "inbox-triage (shared 7-file KB contract)"
  version: 1.0.0
---
  
# Inbox-Setup — Email Triage Onboarding
  
> **Paired with `inbox-triage`.** This skill writes the 7-file knowledge base at `${WORKSPACE}/Email/` that `inbox-triage` reads on every run. The file contracts (names, sections, fields) MUST match between the two skills exactly. See [`references/kb_file_contract.md`](references/kb_file_contract.md).
  
Run once (or re-run when business/priorities change). Interview the user about their email patterns, business context, reply style, and priorities. Generate the structured knowledge base in `${WORKSPACE}/Email/` that captures everything `inbox-triage` needs to process the inbox effectively.
  
## Invocation Triggers
  
- "set up my inbox"
- "configure inbox triage"
- "set up my email system"
- "configure email triage"
- "build my email knowledge base"
- "initialize email management"
- "set up inbox triage"
- "onboard email triage"
  
## Conduct Discipline
  
**Do NOT generate all files at once.** Walk through the 8 sections one at a time. Each section commits its file(s) before moving on. Partial completion (e.g., user drops off mid-interview) still produces a usable partial KB.
  
Grill-me discipline applies throughout:
  
- **One question per turn.** Never bundle. Even across section boundaries.
- **"Why I'm asking" on every question** — so users can answer well.
- **Forcing format where possible.** Multi-choice > open-ended.
- **Dependency-ordered.** Q2 depends on Q1; downstream sections depend on upstream.
  
See [`references/grill_me_section_walk.md`](references/grill_me_section_walk.md) for the 8-section discipline detail.
  
## Knowledge Base Contract — Files To Produce
  
Exactly these files at `${WORKSPACE}/Email/`:
  
| File | Purpose | Required? |
|---|---|---|
| `email-taxonomy.md` | Classification system + report preferences | **Yes** |
| `email-patterns.md` | Reply voice, tone, templates, hard rules | **Yes** |
| `evaluation-framework.md` | Decision tree for opportunity emails | Only if user receives pitches/opportunities |
| `rate-card.md` | Pricing, terms, negotiation posture | Only if user has pricing |
| `blocklist.md` | Auto-skip senders + learned decline patterns | **Yes** (seeded, grows over time) |
| `tracker.md` | Active follow-ups, overdue items, deadlines | **Yes** (starts mostly empty) |
| `triage-log/` | Directory for per-run logs | **Yes** (created empty) |
  
The contract is identical to what `inbox-triage` expects — see [`references/kb_file_contract.md`](references/kb_file_contract.md) for the full spec.
  
## Stop Condition (Full Interview)
  
~25–31 questions total across the 8 sections (depending on skip-logic). Hard ceiling: 35 questions including all sub-clarifications. Section 4 (Evaluation Framework) is skipped entirely when Section 1 surfaced no opportunity-email category, dropping the total by 6 questions and the rate-card file. After Section 8's confirmation + handoff message, intake is closed — **never re-open it**. To change preferences later, the user re-runs the skill (which detects existing files and asks per-file: replace / merge / skip). The grill-me one-at-a-time rule applies across section boundaries: do NOT batch questions even when moving from S{n} to S{n+1}.
  
## Section 1: The Big Picture
  
Six grill-me questions, one at a time:
  
- **S1.Q1:** "What do you do? Give me your role and business in 1–2 sentences. *Why I'm asking:* Context shapes what email patterns to expect — a solo creator's inbox looks nothing like an enterprise PM's."
- **S1.Q2:** "What dominates your inbox? Pick the top 1–2: sales pitches / client work / internal team / newsletters / customer support / financial / other. *Why I'm asking:* Dominant categories drive the taxonomy."
- **S1.Q3:** "Rough volume split — e.g., '60% business inquiries, 20% ops, 20% noise'. *Why I'm asking:* The split tells me where to focus triage effort."
- **S1.Q4:** "Which email address(es) should triage cover? *Why I'm asking:* If multiple, I'll set up per-address taxonomies."
- **S1.Q5:** "Run frequency: once daily / 2x daily / 3x daily / on-demand only? *Why I'm asking:* Drives the default search window in triage (9h overlap for 2x/day)."
- **S1.Q6:** "Anyone helping manage email — assistant, VA, team — or solo? *Why I'm asking:* Persona handling differs for delegated inboxes."
  
**Action:** Build mental model. Do NOT write files yet. Note whether opportunity emails are a category (drives S4 skip-logic).
  
## Section 2: Email Categories
  
Propose 5–7 categories based on Section 1 — pre-recommend a subset, not the whole template menu:
  
- New Opportunities
- Active Conversations
- Action Required
- Financial
- Important/Personal
- Informational
- Ignore/Low Priority
  
Then three forcing questions, one at a time:
  
- **S2.Q1:** "Here's my proposed taxonomy: [list]. Does this match your inbox reality — yes / mostly / no? *Why I'm asking:* If 'no', I need to redo the taxonomy before any other section makes sense."
- **S2.Q2:** "Missing categories? List them. (Skip if none.) *Why I'm asking:* Missing categories produce uncategorized emails downstream, which hurts triage quality."
- **S2.Q3:** "Which category takes the MOST time per email? *Why I'm asking:* That's where draft-reply effort needs to focus most."
  
**Action:** Generate `email-taxonomy.md` with categories, signals (for each: trigger phrases / sender patterns / subject markers), and default actions per category.
  
## Section 3: Reply Style & Voice
  
Six grill-me questions plus the critical sample request:
  
- **S3.Q1:** "Register: formal / casual / in-between? *Why I'm asking:* Calibrates default voice; we'll refine from samples next."
- **S3.Q2:** "Three communication pet peeves — phrases you hate, openings you avoid. *Why I'm asking:* I treat these as forbidden tokens in drafts."
- **S3.Q3:** "Phrases or sign-offs you always use — list as many as come to mind. *Why I'm asking:* These are your voice fingerprints."
- **S3.Q4:** "Different persona for different contexts — e.g., assistant replies as you? *Why I'm asking:* Persona context changes pronoun + signature handling."
- **S3.Q5:** "Typical reply length — one-liner / short paragraph / longer? *Why I'm asking:* Length is the easiest voice signal to get wrong."
- **S3.Q6:** "Hard rules — never X / always Y? (E.g., never emojis, always reply within 24h, never take calls without context.) *Why I'm asking:* Hard rules are enforced as non-negotiable in every draft."
  
### S3.SAMPLES (the critical highest-quality input)
  
> **Paste 3–5 real sent emails from your inbox.**
>
> *Why I'm asking:* Self-description of voice is unreliable. Real samples are the best signal — I'll analyze them for voice patterns that supplement everything above. Use `scripts/voice_sample_analyzer.py` to extract patterns deterministically.
  
If user runs a business: also ask about media kits, rate sheets, standard pitches, repeated replies.
  
**Action:** Generate `email-patterns.md` with tone description (with do/don't examples), persona rules, templates, signatures, hard rules. See [`references/voice_calibration.md`](references/voice_calibration.md) for the sample-extraction discipline.
  
## Section 4: Evaluation Framework (Conditional)
  
**Skip-logic:** only run this section if Section 1 surfaced opportunity emails as a meaningful inbox category. Otherwise jump straight to Section 5.
  
Six grill-me questions, one at a time:
  
- **S4.Q1:** "First thing you check when pitched something — give me your gut filter. *Why I'm asking:* That's the top of the decision tree."
- **S4.Q2:** "Three instant deal-breakers — things that make you decline immediately. *Why I'm asking:* These become PASS-auto signals."
- **S4.Q3:** "Three things that make you immediately interested. *Why I'm asking:* These become TAKE-IT signals."
- **S4.Q4:** "Standard pricing / terms — or 'no fixed pricing' if you negotiate every time. *Why I'm asking:* If you have a rate card, I'll generate one; if not, I'll skip."
- **S4.Q5:** "Negotiation posture: firm / flexible / depends on context? *Why I'm asking:* Drives draft tone on counter-offers."
- **S4.Q6:** "VIP senders or organizations that always get engagement — list names or domains. *Why I'm asking:* VIP list bypasses normal PASS filters."
  
**Action:** Generate `evaluation-framework.md` (decision tree + recommendation categories + VIP list) AND `rate-card.md` if pricing exists.
  
## Section 5: Blocklist & Patterns
  
Three grill-me questions, one at a time:
  
- **S5.Q1:** "Senders or domains to always skip — list them. (Skip if none.) *Why I'm asking:* Auto-blocklist saves the most time per run."
- **S5.Q2:** "Patterns in emails you always delete — e.g., 'unsubscribe' links from specific marketers, recruiter cold outreach, newsletters? *Why I'm asking:* Patterns let triage auto-skip variants without exact-match maintenance."
- **S5.Q3:** "Specific companies / recruiters / newsletters wasting time — list any. *Why I'm asking:* These seed the blocklist; triage will add more as you override decisions."
  
**Action:** Generate `blocklist.md` (auto-maintained by triage thereafter).
  
## Section 6: Current State
  
Three grill-me questions, one at a time:
  
- **S6.Q1:** "Active threads you're tracking — list with one-line context each. (Skip if none.) *Why I'm asking:* These become tracker entries so triage knows existing context."
- **S6.Q2:** "Overdue replies — anything you should have responded to but haven't? *Why I'm asking:* Triage flags these as priority every run until resolved."
- **S6.Q3:** "Time-sensitive items with deadlines — list with dates. *Why I'm asking:* Tracker enforces deadlines and surfaces them as overdue at the right time."
  
**Action:** Generate `tracker.md` with active follow-ups table, overdue section, resolved section (empty), update log (empty). Also create empty `triage-log/` directory.
  
## Section 7: Report Preferences
  
Three grill-me questions, one at a time:
  
- **S7.Q1:** "Delivery format — pick one: email draft to self / file in workspace / chat summary only. *Why I'm asking:* The triage report goes here every run."
- **S7.Q2:** "Detail level — pick one: 30-second scan / detailed breakdown / both (scan first, expand on request). *Why I'm asking:* Affects report length."
- **S7.Q3:** "Anything always shown first — e.g., overdue payments, VIP messages? *Why I'm asking:* Custom 'top-of-report' rules surface what you care about above standard sections."
  
**Action:** Save these preferences into `email-taxonomy.md` under a "Report Preferences" section.
  
## Section 8: Confirmation & Handoff
  
List every file created with one-sentence summary. Then:
  
> Your triage system is ready. Run the **inbox-triage** skill to process your inbox. First runs need oversight — system learns from your edits and overrides.
  
Remind: re-run this setup anytime business/pricing/priorities change.
  
Run `scripts/kb_validator.py --workspace ${WORKSPACE}` to confirm the 7-file contract is satisfied before final handoff.
  
## Privacy Boundary
  
**Never persist passwords, full account numbers, SSNs, or other sensitive credentials in knowledge base files.** If the user volunteers such info during the interview, acknowledge it but don't store it; the relevant KB file gets `[stored separately by user]` in its place.
  
## Re-Run Behavior
  
Re-running on an existing setup:
  
1. Detect `${WORKSPACE}/Email/`
2. For each existing file, ask per-file: **replace / merge / skip**
3. Walk only the sections whose files the user chose to update
4. Skip sections whose files the user kept
  
## Error Handling
  
| Situation | Behavior |
|---|---|
| Workspace inaccessible | Stop. Tell user where files would go and ask for permission/path |
| User refuses to share samples | Use self-description; flag in patterns file that calibration may need iteration |
| User says "skip this" mid-interview | Honor it; flag the gap in the file as `[needs follow-up]` |
| Sensitive info volunteered | Acknowledge but don't persist; note in file as `[stored separately by user]` |
| Re-run on existing setup | Detect existing files; ask user per-file: replace, merge, skip |
| User has no pricing / opportunities | Skip Section 4 entirely; don't create empty files |
  
## Portability
  
- **Claude Code CLI:** Native — writes markdown files directly to filesystem.
- **Claude.ai web:** Works with project files / artifacts. Document the alternate path: generate files as artifacts, instruct user to save to their workspace, or use connected file system if available.
  
## Tooling
  
| Script | Role |
|---|---|
| `scripts/kb_validator.py` | Validates the 7-file KB output (required files present, conditional files only if their sections ran, headers + structure correct). |
| `scripts/section_progress_tracker.py` | JSON-backed walk state at `~/.inbox_setup_sessions/<session>.json`. Tracks active section, answered questions, committed files. |
| `scripts/voice_sample_analyzer.py` | Extracts voice patterns from pasted sent-email samples — opening phrases, sign-offs, length distribution, register markers. |
  
## References
  
- [`references/kb_file_contract.md`](references/kb_file_contract.md) — the canonical 7-file contract (write perspective; mirror lives in `inbox-triage/references/`)
- [`references/grill_me_section_walk.md`](references/grill_me_section_walk.md) — 8-section discipline, skip-logic, commit-per-section
- [`references/voice_calibration.md`](references/voice_calibration.md) — sample-based voice extraction theory + anti-patterns
  
## Anti-Patterns To Reject
  
- Generating all files at once instead of walking through sections
- Asking all questions in one batch
- Hardcoded provider references (Gmail-only thinking)
- Persisting sensitive credentials in knowledge base
- Skipping the "why this question matters" explanation
- Skipping the sample-emails ask for voice (it's the highest-quality input)
- Overwriting existing files without consent on re-run
- Forcing creation of `rate-card.md` or `evaluation-framework.md` when they don't apply
  
---
  
**Version:** 1.0.0
**Source spec:** [`megaprompts/06-inbox-setup-megaprompt.md`](../../../../megaprompts/06-inbox-setup-megaprompt.md)
**Build pattern:** Path B (direct conversion). Paired with `inbox-triage`.


---

## Reference: grill_me_section_walk

# Grill-Me Section Walk Discipline

This reference answers exactly one decision: **how does inbox-setup walk 8 sections of ~25-31 questions without violating grill-me discipline, and what makes the discipline survive heavy intake?**

## The Core Tension

Capture's grill-me is **max-1 question** per dump (light intake). Inbox-setup is **25-31 questions across 8 sections** (heavy intake). At that scale, the one-question-at-a-time rule is easy to break — the interviewer is tempted to batch, the user is tempted to dump everything at once.

The discipline survives because:

1. **Section boundaries** create natural commit points
2. **Skip-logic** removes ~6 questions when irrelevant (Section 4)
3. **Per-section file writes** make partial completion still useful
4. **Forcing format** keeps questions answerable in seconds

## The Four Rules

### Rule 1: One Question Per Turn — Across Section Boundaries

The rule does NOT relax when moving between sections. After S2.Q3 commits `email-taxonomy.md`, ask S3.Q1 alone — not "S3.Q1 and S3.Q2 since you already know your voice."

**Why:** the user is fatigued by question 18; bundling 3 at once produces shallower answers. Better to be slow than to lose answer quality on the high-leverage voice + framework questions.

### Rule 2: "Why I'm Asking" On Every Single Question

Without the rationale, users either:
- Skip past the question thinking it's optional
- Answer minimally because they don't know what's at stake
- Misunderstand the depth needed

The rationale is short (1-2 sentences) and concrete ("This becomes a forbidden token in drafts" beats "this helps me understand your style").

### Rule 3: Forcing Format > Open-Ended

| ✅ Forcing | ❌ Open-ended |
|---|---|
| "Run frequency: once daily / 2x daily / 3x daily / on-demand only?" | "How often should I run?" |
| "Does this taxonomy match: yes / mostly / no?" | "What do you think of this taxonomy?" |
| "Register: formal / casual / in-between?" | "Describe your tone." |

Open-ended works for: pet peeves (S3.Q2), sign-offs (S3.Q3), hard rules (S3.Q6), VIP list (S4.Q6), tracker entries (S6.Q1) — where the answer space is genuinely unbounded and forcing format would harm signal.

### Rule 4: Commit Per Section, Not End-Of-Interview

After Section 2's 3 questions: write `email-taxonomy.md`. Do NOT wait until Section 8 to write all files at once.

**Why:** if the user drops off after Section 4 (~16 questions in), the user has a useful partial KB (taxonomy + patterns + framework + rate card). If files were batched at the end, drop-off leaves nothing.

## The 8 Sections at a Glance

| Section | Questions | Skip-Logic | Files Written at End |
|---|---:|---|---|
| 1. The Big Picture | 6 | always run | (none — build mental model) |
| 2. Email Categories | 3 | always run | `email-taxonomy.md` |
| 3. Reply Style & Voice | 6 + samples | always run | `email-patterns.md` |
| 4. Evaluation Framework | 6 | skipped if no opportunity category in S1 | `evaluation-framework.md` + `rate-card.md` (cond) |
| 5. Blocklist & Patterns | 3 | always run | `blocklist.md` |
| 6. Current State | 3 | always run | `tracker.md` + `triage-log/` dir |
| 7. Report Preferences | 3 | always run | appended to `email-taxonomy.md` |
| 8. Confirmation & Handoff | 0 (summary) | always run | (no file write; handoff message) |

**Total: 24 + 6 conditional = 30 max** (or 24 if S4 skipped). Hard ceiling 35 includes sub-clarifications.

## Skip-Logic Detail

### Section 4 Skip

After S1.Q2 ("what dominates your inbox?"), if the answer does NOT include:
- "sales pitches" / "opportunities" / "client work proposals"

Then mark S4 as skipped. State to user:

> Skipping Section 4 (Evaluation Framework) since your inbox doesn't include pitches/opportunities. Moving to Section 5.

The user CAN override: "Actually I do get opportunity emails — run that section." Honor the override.

### Per-Question Conditional Skips

Some individual questions have "(Skip if none)" suffix:

- S2.Q2 (missing categories?) — skip if user says all listed
- S5.Q1 (skip-senders?) — skip if user has none yet
- S6.Q1 (active threads?) — skip if user has none
- S6.Q2 (overdue?) — skip if user has none
- S6.Q3 (deadlines?) — skip if user has none

These skips ALSO commit to the file (with empty section) so triage knows the section was considered, not forgotten.

## Per-Section File Commit Pattern

```
1. Ask all questions in Section N (one at a time)
2. Synthesize answers into structured file content
3. Write file(s) at ${WORKSPACE}/Email/{filename}
4. Confirm to user: "✓ Section N complete. {file(s)} committed."
5. Record in session tracker:
     python scripts/section_progress_tracker.py \
       --action record_section_done --session NAME \
       --section N --files "{filename}"
6. Move to Section N+1's first question.
```

## Re-Run Mode

Detect re-run when `${WORKSPACE}/Email/email-taxonomy.md` exists.

Walk the user through per-file consent:

```
Found email-taxonomy.md from 2026-03-04 (45 days ago).
Replace / merge / skip?
- replace: rewrite from new interview answers
- merge: keep existing categories, add new ones from this run
- skip: leave file as-is; move to next file
```

Walk only the sections whose files the user chose to replace or merge. If user chose skip for a file, do NOT re-ask that section's questions.

## Sample-Collection Discipline (S3.SAMPLES)

The sample-emails ask is **the highest-quality voice signal** the skill has. It is NOT optional from a quality standpoint, but it IS skippable by user choice.

**Discipline:**

1. Ask for 3-5 real sent emails. Frame it as "the best signal I have."
2. If user pastes them: run `scripts/voice_sample_analyzer.py` and incorporate the output into `email-patterns.md` under "Voice Patterns (Extracted from Samples)."
3. If user refuses: use S3.Q1-Q6 self-description only. Flag in `email-patterns.md`:
   > `[calibration may need iteration — voice samples not collected during setup. First few triage runs will likely produce drafts that need editing; the system learns from your edits.]`
4. Never proceed past Section 3 without either samples OR explicit user-skip + flag.

## Anti-Patterns To Reject

- Asking S1.Q1-Q3 in one message ("tell me your role, what dominates your inbox, and rough volume split")
- Asking S2.Q1 without "Why I'm asking"
- Writing all 7 files at end of S8 (no per-section commit)
- Asking S4 questions when no opportunities surfaced in S1
- Asking S5.Q1 again when user already said "I have no blocklist yet" in S1
- Forcing closed-format on genuinely open questions (e.g., "Pet peeves: a) clichés b) emojis c) other" — kills signal)
- Skipping the rationale ("Why I'm asking") to "save time"
- Skipping the sample ask in S3
- Re-running and overwriting existing files without per-file consent

## Citations

The grill-me discipline this reference enforces is canonical in this repo. See:

- [`engineering/grill-me/`](../../../../engineering/grill-me/) — the source skill that formalized the discipline
- Matt Pocock's original grill-me skill (MIT)
- This repo's PR #657 cross-skill consistency audit, which verified the discipline transfers consistently across all intake-having skills (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

## Reference: kb_file_contract

# Knowledge Base File Contract (Write Perspective)

This reference answers exactly one decision: **what 7 files must `inbox-setup` produce, in what structure, so that `inbox-triage` can read them without ambiguity?**

This is the integration boundary between the paired skills. Any drift breaks the pair. PR #657's cross-skill consistency audit verified that the 7 KB filenames align verbatim between the two megaprompts; this reference is the canonical write-side spec. A mirror lives at `inbox-triage/references/kb_file_contract.md` (read perspective).

## The 7 Files at `${WORKSPACE}/Email/`

| File | Required? | Triggered by | Triage uses for |
|---|---|---|---|
| `email-taxonomy.md` | yes | Section 2 + Section 7 | classification + report preferences |
| `email-patterns.md` | yes | Section 3 | reply voice + templates + hard rules |
| `evaluation-framework.md` | conditional | Section 4 (only if S1 surfaced opportunities) | TAKE-IT / WORTH / PASS / FLAG decisions |
| `rate-card.md` | conditional | Section 4 (only if user has pricing) | negotiation posture + counter-offers |
| `blocklist.md` | yes (seeded) | Section 5 | auto-skip senders + decline patterns |
| `tracker.md` | yes (seeded) | Section 6 | active follow-ups + deadlines |
| `triage-log/` | yes (empty dir) | Section 6 | per-run logs (populated by triage) |

## File Specs (Write Side)

### email-taxonomy.md (required)

```markdown
# Email Taxonomy

## Categories

### {Category Name}
- Signals: {trigger phrases, sender patterns, subject markers}
- Default action: {classify / draft-reply / skip / flag-for-review}
- Typical volume: {N% of inbox}

### {Category 2}
...

## Report Preferences

- Delivery format: {email-draft-to-self | file-in-workspace | chat-summary-only}
- Detail level: {30-second-scan | detailed-breakdown | both}
- Always-shown-first: {overdue payments | VIP messages | custom rules}
```

**Generated at:** end of Section 2 (categories) + appended at end of Section 7 (Report Preferences).

### email-patterns.md (required)

```markdown
# Email Patterns

## Voice Register
{formal | casual | in-between}

## Pet Peeves (Forbidden Tokens)
- {phrase 1}
- {phrase 2}
- {phrase 3}

## Sign-Offs (Voice Fingerprints)
- {sign-off 1}
- {sign-off 2}
- ...

## Persona Context
{single-user | delegated (assistant replies as user) | multi-persona}

## Typical Reply Length
{one-liner | short-paragraph | longer}

## Hard Rules (Non-Negotiable in Every Draft)
- Never: {X}
- Always: {Y}

## Voice Patterns (Extracted from Samples)
- Opening phrases observed: {list}
- Sentence length distribution: {short / medium / long mix}
- Casual / formal markers: {list}

## Templates (Repeated Replies)
- {template 1 name}: {body}
- {template 2 name}: {body}
```

**Generated at:** end of Section 3. The "Voice Patterns" subsection comes from `scripts/voice_sample_analyzer.py` if samples were provided; otherwise marked `[calibration may need iteration]`.

### evaluation-framework.md (conditional)

```markdown
# Evaluation Framework (Opportunity Emails)

## Gut Filter (First Check)
{user's gut filter from S4.Q1}

## TAKE-IT Signals
- {signal 1}
- {signal 2}
- {signal 3}

## PASS Signals (Instant Deal-Breakers)
- {deal-breaker 1}
- {deal-breaker 2}
- {deal-breaker 3}

## Decision Tree

1. If sender in VIP list → TAKE IT (skip filter)
2. If any PASS signal matches → PASS (auto-decline draft)
3. If all TAKE-IT signals match → TAKE IT (auto-engage draft)
4. If partial TAKE-IT match → WORTH CONSIDERING
5. If unusual / ambiguous → FLAG FOR REVIEW

## VIP List (Bypass PASS Filters)
- {sender / domain 1}
- {sender / domain 2}
- ...

## Negotiation Posture
{firm | flexible | depends-on-context}
```

**Generated at:** end of Section 4. Skipped entirely if S1 surfaced no opportunity-email category.

### rate-card.md (conditional)

```markdown
# Rate Card

## Standard Pricing
- {service / offering 1}: {price}
- {service / offering 2}: {price}

## Terms
- Payment: {net X days | upfront | milestone}
- Revisions included: {N}
- Rush fee: {Y%}

## Negotiation Posture
{firm | flexible | depends-on-context}

## Counter-Offer Patterns
- If they offer < {floor}: {how to counter}
- If timeline is tight: {how to counter}
```

**Generated at:** end of Section 4. Skipped if user has no fixed pricing (S4.Q4 = "no fixed pricing").

### blocklist.md (required, seeded)

```markdown
# Blocklist

## Sender / Domain Auto-Skip
- {sender 1}: {reason} — added {date}
- {domain 1}: {reason} — added {date}

## Decline Patterns (Pattern-Match Auto-Skip)
- "{pattern phrase 1}": {reason}
- "{pattern phrase 2}": {reason}

## Recently Removed (User Overrode)
- {sender}: removed on {date} — user override
```

**Generated at:** end of Section 5 (initial seed). `inbox-triage` appends new declines + observed patterns on every run.

### tracker.md (required, seeded)

```markdown
# Tracker

## Active Follow-Ups

| Item | Context | Deadline | Status |
|---|---|---|---|
| {thread} | {one-line context} | {date} | pending |
| ... | ... | ... | ... |

## Overdue
- {thread}: missed deadline {date} — {context}

## Resolved (Recent)

## Update Log
- {date}: {what changed} — by {triage run | user}
```

**Generated at:** end of Section 6 (initial seed from S6.Q1-Q3). `inbox-triage` updates on every run.

### triage-log/ (required, empty directory)

Empty directory created at end of Section 6. `inbox-triage` writes per-run logs to `triage-log/<YYYY-MM-DD>-<run-label>.md`.

## Validation

Run `scripts/kb_validator.py --workspace ${WORKSPACE}` after Section 8 confirmation. It checks:

- All required files exist
- Conditional files exist iff their triggering section ran
- Each file has the expected H1 + section structure
- `triage-log/` is a directory (not a file)

## Why This Contract Matters

`inbox-triage` halts with a clear error if any required core file is missing. The contract is the integration boundary — both skills can be developed and tested independently, but they must agree on the file shape.

When updating either skill: update both sides of the contract simultaneously, or use `/cs:grill-with-docs` to detect drift between the two megaprompts before drift reaches code.

## Reference: voice_calibration

# Voice Calibration — Extracting Style from Sent-Email Samples

This reference answers exactly one decision: **why are real sent-email samples the highest-quality voice signal for inbox-triage's draft generation, and how does the skill extract usable patterns from them deterministically?**

Pair with `scripts/voice_sample_analyzer.py` for the deterministic extraction.

## The Core Claim

Users describe their own voice unreliably. They say "professional but warm" and their actual emails alternate between three sentences of formal hedging and "lol no" replies to colleagues. They say "I'm pretty casual" and their actual emails open with "I hope this email finds you well."

> **What users say about their voice ≠ what their voice actually is.**

Real sent emails resolve this gap. They show:

- Real opening phrases (not "I hope this email finds you well" if the user doesn't actually say that)
- Real sentence length (not "short" if the actual average is 3 paragraphs)
- Real sign-offs (not "thanks!" if the actual ratio is 80% "—Alex" and 20% no sign-off)
- Real register (the variation across recipient type that self-description misses)

## What S3.SAMPLES Asks For

> "Paste 3–5 real sent emails from your inbox."

3-5 is the operational sweet spot:

- **<3:** too few to detect patterns vs anomalies
- **3-5:** enough variance to detect baseline + adaptations
- **>5:** marginal signal, diminishing returns; takes longer to extract

The samples should span the user's typical email mix — at least one to a peer, one external, one transactional. If the user pastes 5 identical newsletters, ask for more variety.

## What `voice_sample_analyzer.py` Extracts

Deterministic stdlib analysis (no LLM):

1. **Opening phrases** — first 5-10 tokens of each sample's body. Pattern frequency.
2. **Sign-offs** — last 5-10 tokens of each sample. Pattern frequency.
3. **Sentence length distribution** — short (<10 words) / medium (10-25) / long (>25) ratio.
4. **Register markers** — counts of casual indicators ("lol", "yeah", "tbh", "btw") vs formal indicators ("I would like to", "please find", "kindly").
5. **Hedging frequency** — counts of softeners ("maybe", "I think", "perhaps", "just"). High hedging is a voice fingerprint.
6. **Personal pronouns** — "I" vs "we" frequency. Tells whether user writes as solo or representing a team.
7. **Punctuation patterns** — em-dash usage, exclamation marks, ellipses.

Output is a structured patterns block that goes into `email-patterns.md` under "Voice Patterns (Extracted from Samples)."

## How Self-Description (S3.Q1-Q6) Combines With Samples

Self-description and samples are **complementary**, not competing:

- **Self-description wins for:** hard rules (S3.Q6 — "never emojis"), forbidden tokens (S3.Q2 — "phrases I hate"), explicit sign-offs (S3.Q3 — what the user remembers using).
- **Samples win for:** baseline register, actual sentence length, opening phrases, register adaptation across recipient types.

In `email-patterns.md`, the two are combined: self-described preferences are stated as hard rules; sample-extracted patterns supplement as baseline behavior.

## When Samples Aren't Available

If the user refuses to paste samples (privacy, time, or just "I'd rather not"):

1. Honor the choice. Don't push back twice.
2. Use S3.Q1-Q6 self-description only.
3. Flag in `email-patterns.md`:

```markdown
## Voice Calibration Status

[calibration may need iteration — voice samples not collected during setup.
First few triage runs will likely produce drafts that need editing; the
system learns from your edits and overrides. Re-run inbox-setup with
samples when you're ready, OR triage will refine voice from your edit
patterns over 5+ runs.]
```

4. Inbox-triage will produce drafts in a more conservative default register (medium-formal, short-paragraph length). Drafts will need more editing on early runs.

## Common Anti-Patterns

### "I described my voice, that's enough"

Self-description has known blind spots (per the "Core Claim" above). Even high-self-awareness users overestimate their formality or underestimate their hedging frequency. Skip the samples and the first 10 triage runs produce drafts that "sound off" in a way users struggle to articulate.

### "I'll paste 5 emails that are similar"

5 emails to peers about the same project don't show register adaptation. The skill needs variance: one to a peer, one to a client/external, one transactional. If user pastes 5 similar emails, ask for one more from a different context.

### "I'll paste from my drafts folder"

Drafts may not represent voice the user actually sends — they may include rejected attempts. Ask for sent emails specifically.

### "I'll write 5 example emails for you"

Written-for-the-skill emails are self-description in disguise. Reject:

> "Examples written for me don't capture your actual voice — they capture how you describe your voice (which has known blind spots). Paste real sent emails, even short/boring ones. The mundane ones often signal voice better than carefully-crafted ones."

### "Forbidden tokens" extracted from samples instead of S3.Q2

Don't pull "forbidden tokens" from sample analysis — if a phrase appeared in a sent email, the user used it at some point. Forbidden tokens ONLY come from S3.Q2 (explicit "phrases I hate"). Voice extraction surfaces what the user DOES say, not what they DON'T.

## Operational Checklist (Per Setup Run)

- [ ] S3.Q1-Q6 asked one at a time with "why I'm asking"
- [ ] S3.SAMPLES asked AFTER Q1-Q6 (self-description first, samples second — samples calibrate the description, not replace it)
- [ ] 3-5 samples collected (or explicit user-skip + flag in patterns file)
- [ ] If collected: `scripts/voice_sample_analyzer.py` run; output incorporated into "Voice Patterns" subsection of patterns file
- [ ] Self-described hard rules + forbidden tokens preserved as authoritative
- [ ] Sample-extracted baseline preserved as descriptive (not authoritative)
- [ ] Calibration-status block included in patterns file (states whether samples were collected)

## Why This Reference Exists

The S3.SAMPLES step is the SINGLE most important question in the entire 25-31 question interview. Skipping it or doing it poorly compromises every subsequent triage run. This reference exists to make the discipline of "samples first, self-description second" explicit and operationally enforceable.

## Citations

Voice analysis canon:

1. **Brian Kernighan & Rob Pike, *The Practice of Programming* (Addison-Wesley, 1999)** — Chapter 1 on Style. The point that "names describe roles, not types" generalizes: a user's voice describes their habits, not their aspirations. Sample-based extraction captures habits.

2. **Steven Pinker, *The Sense of Style* (Viking, 2014)** — Chapter on register and the "Classic Style" trap. Self-described voice often defaults to Classic Style ideals that the user's actual voice doesn't match.

3. **Bryan Garner, *Garner's Modern English Usage* (5th ed., Oxford, 2022)** — Sections on register variation and register-adaptation across contexts. The justification for requiring sample variance (peer / external / transactional).

4. **Geoffrey Pullum, *The Cambridge Grammar of the English Language* (Cambridge, 2002), Chapter 12** — Register theory. Establishes that register is detectable from text features (sentence length, pronoun choice, hedging frequency) more reliably than from speaker self-report.

5. **Stylometric authorship attribution literature** — work by Patrick Juola, José Nilo G. Binongo, and the broader stylometry community. Establishes that text features (function-word frequency, punctuation patterns, sentence-length distribution) are robust voice signals. The features `voice_sample_analyzer.py` extracts are a subset of this canonical set.

6. **John Searle, *Speech Acts* (Cambridge, 1969)** — Performative theory. Useful framing for the "hard rules" (S3.Q6) discipline: hard rules are performatives the user commits to; voice is descriptive.

7. **Email-writing style guides at scale: *The Yahoo! Style Guide* (St. Martin's, 2010), *The Microsoft Manual of Style* (4th ed.).** Real-world style guides establish that register depends heavily on recipient + context, not on a single "professional voice." Justifies asking for sample variance.

