---
name: capture
description: "Captures and organizes chaotic brain dumps into a structured, actionable system with zero information loss. Use this skill whenever the user says 'capture this', 'brain dump', 'let me dump some ideas', 'I've got a bunch of thoughts', 'here's everything on my mind', 'idea dump', 'let me get this out of my head', 'I need to organize my thoughts', 'here's what I'm thinking', or any variation where someone is unloading a messy stream of ideas, tasks, thoughts, and plans wanting them turned into something coherent. Also trigger when the user pastes or dictates a long, unstructured block of mixed ideas — even without the exact phrase — the intent is the same. Fast-to-action by design: no upfront intake. Output is four sections (Projects/Ideas, Tasks, Connections, How I Can Help) ending with a directive question. Asks at most one mid-organization clarifying question when a single item is genuinely ambiguous between task and project."
llm: Claude
version: v3
updated: 2026-08-11T22:09:40.574Z
created: 2026-07-07T17:02:07.641Z
---
# Capture — Brain-Dump Organizer

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#capture--brain-dump-organizer)
A fast-to-action skill for transforming unstructured streams of mixed thoughts, tasks, and ideas into a clean four-section actionable system with zero information loss.

## Invocation Triggers

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#invocation-triggers)
Explicit phrases (any of):

- "brain dump"
- "capture this"
- "let me dump some ideas"
- "I've got a bunch of thoughts"
- "here's everything on my mind"
- "idea dump"
- "let me just get this out of my head"
- "I need to organize my thoughts"
- "here's what I'm thinking"

Implicit signals (no phrase, but the intent is unmistakable):

- User pastes or dictates a long unstructured block of mixed ideas, tasks, plans
- Multiple unrelated thoughts in one message without organizing framing
- A wall of bullet-y text covering 3+ unrelated topics

When you detect an implicit trigger, run the skill. Do NOT ask "do you want me to organize this?" first — the dump itself IS the request.

## Operating Principles (All Five Apply Always)

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#operating-principles-all-five-apply-always)

1. Capture everything. Zero loss. Trivial items go in; the user prunes later. Never silently drop something because it "seemed unimportant".
2. Preserve voice. If the user said "build something crazy with AI", do NOT restate as "Explore innovative AI-driven solutions." Keep the energy and the casual register. See `references/voice_preservation.md` for concrete anti-patterns.
3. Match output complexity to input. A 5-task dump does NOT get forced into 4 elaborate sections. See `references/complexity_matching.md` and the Compressed Output Pattern below.
4. Be honest about ambiguity. If you're unsure what something means, flag it. Don't guess silently.
5. No action without approval. The ONLY immediate action is the organization itself. Every offer in Section 4 waits for the user's explicit pick.

## Grill-Me Mid-Organization Clarifier

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#grill-me-mid-organization-clarifier)
Capture is fast-to-action by design. No upfront intake. The dump is enough — start organizing immediately.

The grill-me discipline applies as a single mid-organization clarifying question, asked only when one item in the dump is genuinely ambiguous between *task* and *project*, AND the misclassification would meaningfully change the output:

> Quick clarification — one item in your dump could go either way. Is [X] a one-shot task or a multi-step project?
> 
> *Why I'm asking:* If I guess wrong on a borderline item I either bury a project as a task or inflate a task into a project that doesn't need the structure. One question per dump prevents that.

Stop condition: Max 1 clarifying question per dump. After the answer (or if no clarification was needed), deliver the four (or compressed) sections.

If the dump is unambiguous, skip the clarifier entirely.

Anti-pattern (do not do this): asking 3 clarifying questions up front. That breaks the dump-and-organize flow that makes capture useful.

## Section 1: Projects & Ideas

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#section-1-projects--ideas)
Cluster related items into themed projects when natural clustering exists. This section also holds:

- Standalone creative sparks
- Half-formed concepts
- "What if" thoughts
- Embedded decisions (`Decide: X or Y`) and open questions (`Q: ...`) — kept WITHIN the relevant project, NOT extracted into a separate top-level category

Format per project:

```
### {Project name in user's voice}

- {component / sub-idea}
- {component}
- Q: {open question this project needs answered}
- Decide: {decision this project requires}

```

Use the user's words for the project name. If the user wrote "ai dating app for ferrets", do NOT rename it to "AI-Powered Pet Companion Platform".

## Section 2: Tasks

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#section-2-tasks)
Flat, scannable, action-oriented. Includes:

- Explicit todos
- Decisions framed as `Decide: ...`
- Open questions framed as `Resolve: ...`

If a task belongs to a project from Section 1, append `[Project: X]` to link it — but don't repeat the project's context.

Format:

```
- {task in imperative voice}  [Project: X if related]
- Decide: {decision}  [Project: X if related]
- Resolve: {open question}
- ...

```

## Section 3: Connections

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#section-3-connections)
This is where the skill earns its keep — and where fabrication is forbidden.

Workflow:

1. Inventory the workspace — Glob for filename patterns matching dump keywords, Grep for content matches, read the top-level directory structure. Use `scripts/workspace_inventory.py` to do this deterministically.
2. Match dump items to existing content — files / folders relating to dumped items, prior thinking in documents, in-progress projects with overlap.
3. Surface dependencies within the dump — items that affect each other, themes, ordering implications.
4. Be honest about inaccessibility — if you can't inspect the workspace (no filesystem available, MCP not connected), say so explicitly. Do NOT make up plausible-sounding connections.

Hard rule: NEVER fabricate connections. Only surface ones actually found by Glob/Grep/Read. If no real connections exist:

> Connections: No connections found — workspace inventory clean.

If the workspace is inaccessible:

> Connections: No workspace accessible from here. If you're running this from Claude Code or have a project with files attached, I can fill this in. Want to share where this work lives?

See `references/workspace_detection.md` for the per-context detection-tactic catalog.

## Section 4: How I Can Help

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#section-4-how-i-can-help)
Concrete offers, not abstract possibilities. Every offer specifies what would be produced AND where it would go.

| ✅ Right pattern | ❌ Anti-pattern |
| --- | --- |
| "I can research Consensus MCP integration patterns and give you 3 options. Output: `docs/consensus-options.md`." | "You might want to look into integration approaches." |
| "I can draft the Q3 launch plan as a 1-pager. Output: chat reply, then `docs/q3-launch.md` if you want it filed." | "Maybe think about Q3 planning." |
| "I can scaffold the new auth module with the existing pattern from `src/users/`. Output: 4 files in `src/auth/`." | "We could explore auth options." |

End with the directive question:

> Which of these should I tackle?

## Compressed Output Pattern

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#compressed-output-pattern)
When the dump has 5 or fewer items and items are unrelated (no natural clustering), drop the 4-section format and use compressed:

```
## What I heard

- {item}
- {item}
- {item}
- ...

## How I can help

- {concrete offer with what + where}
- {concrete offer with what + where}

Which should I tackle?

```

The trigger is the `complexity_estimator.py` recommendation OR your judgment when no clusters exist. See `references/complexity_matching.md` for worked examples of when each format applies.

## Workspace Detection Strategy

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#workspace-detection-strategy)

| Context | Detection method |
| --- | --- |
| Claude Code CLI | Glob for files matching dump keywords; Grep for content matches; read top-level structure. Use `scripts/workspace_inventory.py`. |
| Claude.ai with project | Check project knowledge files for thematic overlap. List file titles; surface matches by keyword. |
| Connected tools (Notion, Drive, etc.) | Search via MCP if available. |
| No accessible workspace | State the limitation explicitly; ask user about their setup; do NOT fabricate. |

## Approval Gate

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#approval-gate)
After the four (or compressed) sections are delivered:

- Wait for the user's explicit pick before doing anything else.
- If the user says "go" without picking a specific offer: honor it, but explicitly note any items you weren't 100% sure about so they can correct.
- The organization itself is the only auto-action. Every Section 4 offer requires green light.

## Error Handling

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#error-handling)

| Situation | Behavior |
| --- | --- |
| Workspace inaccessible | State this; skip Section 3 or surface "no workspace accessible" + ask about setup |
| Dump is very short (3-5 items) | Use compressed output; don't force 4 sections |
| Items are highly ambiguous | Flag in output, ask up to 1 clarifier (or skip clarifier and surface ambiguity in delivery) |
| Dump contains sensitive info | Acknowledge but don't echo verbatim if user asks for organization without quoting |
| Conflicting items in the dump | Surface the conflict in Section 1 or 3 explicitly (`Conflict: X says A, Y says B`) |
| User says "go" before approval | Honor it, but explicitly note items you weren't sure about |

## Tooling

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#tooling)

| Script | Role |
| --- | --- |
| `scripts/workspace_inventory.py` | Glob+Grep helper for Section 3. `python workspace_inventory.py --root . --keywords "k1,k2"` returns matches by keyword + folder structure. |
| `scripts/dump_classifier.py` | Regex-classifies each dump line into `task` / `decision` / `question` / `idea` / `project-component`. Heuristic — override with judgment. |
| `scripts/complexity_estimator.py` | Counts items, detects clustering signal, recommends `format=full` or `format=compressed`. |

## References

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#references)

- `references/workspace_detection.md` — context-specific detection tactics (CLI / web / MCP / inaccessible)
- `references/voice_preservation.md` — corporate-speak anti-patterns with concrete examples
- `references/complexity_matching.md` — compressed vs full output, worked examples

## Anti-Patterns To Reject

[](https://github.com/alirezarezvani/claude-skills/blob/main/productivity/capture/skills/capture/SKILL.md#anti-patterns-to-reject)

- Fabricating workspace connections that weren't actually Glob/Grep-verified
- Dropping items deemed "trivial" — capture everything, let the user prune
- Corporate-ifying the user's casual language
- Forcing 4-section structure when input is small (5 simple tasks doesn't need it)
- Acting on Section-4 offers immediately without approval
- Splitting decisions/questions into a separate top-level category instead of embedding them in the relevant project
- Vague Section-4 offers ("you might want to consider…")
- Asking 3+ clarifying questions up front (breaks fast-to-action)


---

## Reference: complexity_matching

# Complexity Matching — Compressed vs Full 4-Section Output

This reference answers exactly one decision: **when does capture use the full 4-section format vs the compressed format, and what does each look like in practice?**

Pair with `scripts/complexity_estimator.py` for the deterministic recommendation.

## The Core Rule

> **Match output complexity to input complexity.**

A 30-item dump with natural clusters needs the full 4-section structure to be useful. A 5-item dump of unrelated todos drowns in that structure — the format becomes ceremony, not signal. Force-fitting structure on a small dump makes the skill feel bureaucratic.

## When to Use Each Format

| Signal | Recommended format |
|---|---|
| 8+ items AND natural clustering exists (3+ items share a theme) | Full 4-section |
| 8+ items but NO clustering (all unrelated todos) | Compressed (with explicit "no clusters" note) |
| 5–7 items, mixed kinds, some clustering | Either — judgment call. Lean compressed unless clusters are strong. |
| ≤5 items, unrelated | Compressed |
| ≤5 items but all related to one project | Compressed with single project header |
| Workspace inaccessible AND ≤5 items | Compressed with no Section 3 (still note "no workspace accessible") |

`complexity_estimator.py` returns `format=full` or `format=compressed` based on item count + clustering signal. Use it as the seed; override with judgment when context warrants.

## Format A: Full 4-Section

Use for substantive dumps with real structure. Roughly:

```
## Projects & Ideas

### {Project A in user's voice}
- {component}
- {component}
- Q: {open question}
- Decide: {decision}

### {Project B}
- ...

## Tasks

- {task} [Project: A]
- {task}
- Decide: {decision}
- Resolve: {open question}

## Connections

- {file/folder}: {real workspace match}
- (or) "No connections found — workspace inventory clean."
- (or) "No workspace accessible from here..."

## How I Can Help

- {concrete offer: what + where}
- {concrete offer: what + where}

**Which of these should I tackle?**
```

## Format B: Compressed

Use for small or unrelated dumps. Roughly:

```
## What I heard

- {item}
- {item}
- {item}
- Decide: {decision}
- Resolve: {open question}

## How I can help

- {concrete offer: what + where}
- {concrete offer: what + where}

Which should I tackle?
```

Notice what's gone in compressed:
- No project headers (nothing to cluster)
- No separate Tasks section (the list IS the tasks)
- No Connections section as a separate header (if there's a real connection, fold it inline as a parenthetical: `- fix the auth bug (relates to src/auth/login.ts:42)`)
- Same Section 4 discipline (concrete offers + directive question)

## Worked Examples

### Example 1: Full 4-section (12 items, 2 clusters)

**Dump:**
> "Ok so dump time. Q3 launch is approaching — need to nail down pricing, draft the launch email, brief Sarah on the marketing angle. Also ferret app keeps nagging me — should I talk to my cofounder about it, or is it just procrastination? Need to sketch the matching algorithm if it's serious. Also: fix the damn auth bug, rewrite the login form because it's ugly, write tests for both. Oh and I should probably do my Q3 OKRs before launch."

**Extracted items:** 11
**Clusters:** Q3 Launch (4 items), Ferret App (3 items), Auth (3 items), OKRs (1 item)
**Recommendation:** `format=full` (clear clustering, 11 items)

**Output:**

```
## Projects & Ideas

### Q3 Launch
- Nail down pricing
- Draft launch email
- Brief Sarah on the marketing angle
- Decide: Q3 OKRs (do before launch)

### Ferret App
- Talk to cofounder OR decide it's procrastination
- Sketch matching algorithm (if serious)
- Decide: serious project or shelf?

### Auth Fixes
- Fix the auth bug
- Rewrite the login form (it's ugly)
- Write tests for the bug fix + login rewrite

## Tasks

- Nail down Q3 pricing  [Project: Q3 Launch]
- Draft Q3 launch email  [Project: Q3 Launch]
- Brief Sarah on Q3 marketing angle  [Project: Q3 Launch]
- Talk to cofounder about ferret app  [Project: Ferret App]
- Sketch ferret matching algo  [Project: Ferret App]
- Fix auth bug  [Project: Auth Fixes]
- Rewrite login form  [Project: Auth Fixes]
- Write tests for auth + login  [Project: Auth Fixes]
- Do Q3 OKRs (before launch)
- Decide: ferret app — serious or shelf?

## Connections

(workspace inventory results go here — only verified matches)

## How I Can Help

- I can draft the Q3 launch email as a 1-pager. Output: chat reply.
- I can pull together a pricing-options matrix from your existing pricing docs. Output: `docs/q3-pricing-options.md`.
- I can scaffold the ferret matching algorithm sketch (input → match score). Output: `docs/ferret-algo-sketch.md`.

**Which of these should I tackle?**
```

### Example 2: Compressed (5 unrelated items)

**Dump:**
> "Quick: email Sarah, fix that test that's been flaky, decide between Postgres and Mongo for the new service, dentist appointment, finish reading the article on RAG."

**Extracted items:** 5
**Clusters:** none (all unrelated)
**Recommendation:** `format=compressed`

**Output:**

```
## What I heard

- Email Sarah
- Fix the flaky test
- Decide: Postgres or Mongo for the new service
- Dentist appointment
- Finish reading the RAG article

## How I can help

- I can draft the email to Sarah if you tell me what it's about. Output: chat reply.
- I can investigate the flaky test (likely racing condition; happy to reproduce). Output: chat analysis + fix PR if you want.
- I can pull a Postgres-vs-Mongo decision matrix scoped to your service requirements. Output: chat reply or `docs/db-decision.md`.

Which should I tackle?
```

Notice the dentist appointment + RAG article aren't in "How I can help" — there's nothing meaningful to offer on those. That's correct: don't pad Section 4 with offers for things that don't need help.

### Example 3: Compressed but workspace-aware (small + connection inline)

**Dump:**
> "auth bug is back, need to look at the login flow again, also I want to add 2FA finally."

**Extracted items:** 3
**Clusters:** all auth-related but only 3 items
**Recommendation:** `format=compressed`

**Output:**

```
## What I heard (Auth)

- Auth bug is back (relates to `src/auth/login.ts` based on workspace inventory)
- Look at login flow again
- Add 2FA

## How I can help

- I can reproduce the auth bug from the symptoms — what's the failure mode? Output: chat repro + fix.
- I can sketch a 2FA implementation matching your existing auth pattern (TOTP via the same provider you use). Output: `docs/2fa-sketch.md`.

Which should I tackle?
```

Notice the workspace connection got folded inline as a parenthetical instead of a separate Section 3 header. That's the compressed-with-context pattern.

## Operational Checklist

Before delivering output:

- [ ] Run `complexity_estimator.py` (or apply the Signal table above)
- [ ] If `format=compressed`, do NOT force the 4-section format
- [ ] If `format=full`, ensure the clusters are real (3+ items per cluster) — don't invent clusters to fill the format
- [ ] Either way, Section 4 ("How I can help") MUST have concrete offers with what + where
- [ ] Either way, end with the directive question

## Why This Matters

A skill that returns the same format regardless of input is a template, not a skill. The reason capture is useful is that it adapts to the dump's actual shape. When a 5-item list comes back wrapped in 4 elaborate empty-feeling sections, the user learns to distrust the skill. When a 30-item dump comes back as a flat compressed list, the user learns the skill can't actually handle complexity.

Match the output to the input, every time.

## Reference: voice_preservation

# Voice Preservation — Anti-Corporate-Speak Discipline

This reference answers exactly one decision: **what does it mean to "preserve the user's voice" in capture output, and what concrete patterns must be avoided?**

## The Core Rule

If the user said it casually, restate it casually. If the user said it crudely, restate it crudely (within the user's own register). Capture is for THEM, not for an imagined corporate audience reading their notes later.

> **Restating someone's casual idea in corporate language is a tax. It feels formal but it loses the energy that made the idea worth capturing.**

## Concrete Anti-Patterns (Side-by-Side)

| User said | ❌ Corporate-ified (anti-pattern) | ✅ Voice-preserved |
|---|---|---|
| "build something crazy with AI" | "Explore innovative AI-driven solutions" | "Build something crazy with AI" |
| "the dating app idea but for ferrets" | "Pet-companion matching platform leveraging social-graph principles" | "Dating app for ferrets" |
| "figure out the damn pricing already" | "Conduct comprehensive pricing strategy analysis" | "Figure out pricing (final answer)" |
| "fuck around with Consensus MCP" | "Investigate Consensus MCP integration opportunities" | "Try out Consensus MCP" |
| "make the landing page not suck" | "Optimize landing page user experience metrics" | "Make the landing page not suck" |
| "talk to Sarah about the thing" | "Schedule alignment discussion with Sarah re: outstanding initiative" | "Talk to Sarah about the thing" |
| "I'm tired of debugging this" | "Investigate root causes of recurring debugging friction" | "Tired of debugging this — find the root cause" |

## What Counts As "Voice"

- **Register** — formal vs casual, dry vs energetic, ironic vs earnest
- **Vocabulary** — the user's exact noun choices for things ("ferrets", "thing", "Sarah" — not "pets", "initiative", "stakeholder")
- **Cadence** — short choppy phrases stay short; long flowing thoughts stay flowing
- **Profanity / slang** — preserve as-is; don't sanitize
- **Self-talk markers** — "ugh", "actually", "wait", "ok so" — these signal genuine thinking and belong in the captured form

## What's Allowed to Change

- **Punctuation cleanup** — adding a period, fixing typos
- **Imperative reframing** for the Tasks section — "I should email Sarah" → "Email Sarah" (one-word edit, voice preserved)
- **Light disambiguation** — if "the thing" is genuinely confusing in context, note it but ask to clarify (don't replace it silently)

## What's Never Allowed

- Replacing user nouns with "platform" / "solution" / "initiative" / "framework"
- Verbing nouns: "let's research" → "let's conduct research"
- Adding qualifiers the user didn't say: "explore", "leverage", "deep dive into"
- "Action-itemizing" everything: "talk to Sarah" → "Establish communication touchpoint with Sarah"
- Removing emotion: "I'm pissed about X" → "There is a concern regarding X"
- Bullet-point fluff: "Implement", "Establish", "Facilitate" prefixes added for no reason

## Cluster Naming

When clustering items into projects (Section 1), the project name **MUST** use the user's words. Examples:

| Items in cluster | ❌ Anti-pattern name | ✅ Voice-preserved name |
|---|---|---|
| "ferret app", "ferret features", "ferret marketing" | "Pet Companion Platform" | "Ferret App" |
| "Q3 launch", "Q3 pricing", "Q3 emails" | "Q3 Go-to-Market Initiative" | "Q3 Launch" |
| "fix the auth bug", "auth tests", "rewrite login" | "Authentication System Modernization" | "Auth fixes" |

If the user used multiple terms for the same cluster, pick the one they used most or most colloquially.

## Operating Test

Before writing each line, ask:

> Would the user *recognize* this as something they'd say?

If no, you've drifted. Rewrite to match their register.

## Why This Matters

Voice preservation isn't aesthetic — it's functional. Two reasons:

1. **Recognition.** The user reads their own captured dump back in 2 days and needs to instantly recognize "yes, that's me, that's what I meant." Corporate restatement breaks recognition. The user thinks "wait, did I actually say that?" and starts second-guessing the rest of the output.

2. **Energy.** A dump captured in voice retains the *why* behind each item — the frustration, the excitement, the half-formed hope. Corporate restatement strips the why and leaves a list of generic action items that no one is excited to act on.

Capture is the user's brain on paper. Don't translate it into a stranger's brain.

## Reference: workspace_detection

# Workspace Detection Tactics

This reference answers exactly one decision: **how does the capture skill verify Section 3 connections without fabricating them, across the four contexts the skill might run in?**

Pair with `scripts/workspace_inventory.py` for the deterministic Glob+Grep implementation.

## The Core Rule

Section 3 ("Connections") earns the skill its keep. It also breaks the skill faster than anything else if it lies. The rule:

> **Only surface connections that were actually verified by Glob, Grep, Read, or an equivalent retrieval call this turn.**

If you can't verify, you say "no workspace accessible" or "no connections found" — never invent something plausible-sounding.

## Context 1: Claude Code CLI (filesystem-native)

**Tools available:** `Glob`, `Grep`, `Read`, `Bash`.

**Tactics, in order:**

1. **Extract keywords from the dump.** Pull domain nouns, project names, file-format hints (`.md`, `.py`, `auth`, `consensus`, `pricing`).
2. **Glob for filename matches.** `Glob("**/*{keyword}*")` for each keyword. Limit to top-N matches per keyword to avoid noise.
3. **Grep for content matches.** `Grep("{keyword}")` constrained to source extensions.
4. **Read the top-level structure.** `Bash("ls -la")` and `Bash("find . -maxdepth 2 -type d | head -30")` to surface relevant folders.
5. **Stitch the matches into Section 3 entries.** Each entry: `- {file or folder}: {how it relates to dump item N, with evidence}`.

**Example output:**

```
## Connections

- `engineering/grill-me/` — relates to your "build a grill skill" dump item (folder exists, has plugin.json + SKILL.md). Likely the template you'd want to mirror.
- `megaprompts/05-capture-megaprompt.md` — relates to your "convert capture spec to skill" item. The spec file is here.
- `documentation/implementation/` — empty directory, but the location for the implementation plan you mentioned.
```

**What NOT to do:**
- "There's probably a config for that somewhere" — speculation, no verification.
- "Your project likely has an auth module" — guess, no Glob.
- "I see you might have considered X before" — projection, no Grep.

## Context 2: Claude.ai with project knowledge

**Tools available:** Project-knowledge file list, file content reads.

**Tactics:**

1. **List the project knowledge files** — at the start of the run, get the file inventory.
2. **Match by title keyword** — for each dump keyword, find files whose titles contain it.
3. **Open the top matches** and check if the content is actually related (not just title coincidence).
4. **Surface only the verified matches** in Section 3.

**What NOT to do:**
- Cite a file you didn't open — title match alone is not enough.
- Claim a file says X without quoting evidence.

## Context 3: Connected tools (Notion, Drive, GitHub, Slack via MCP)

**Tools available:** Whatever MCP tools the harness has registered for the user's connected services.

**Tactics:**

1. **Check tool availability first** — list the MCP tools surfaced for this session. If no Notion/Drive/GitHub MCP is registered, skip this context.
2. **Search via MCP** — use the search tool for each tool with dump keywords.
3. **Surface verified hits** with the link / ID returned by the tool.

**What NOT to do:**
- Reference a Notion page that wasn't returned by the search.
- Cite a GitHub issue number without confirming via the GitHub MCP.

## Context 4: No accessible workspace

**Signals you're in this context:**
- No filesystem tools loaded
- No project knowledge attached
- No workspace MCPs registered
- `workspace_inventory.py` returns empty + you can't verify any other way

**Required behavior:**

State the limitation explicitly. Ask about the user's setup. Do NOT fabricate connections.

**Template output:**

```
## Connections

No workspace accessible from here, so this section is empty. If you're running
this from Claude Code or have a project with files attached, I can fill it in.

Want to share where this work lives — a repo path, a Notion workspace, an
attached project? I can re-run the connections pass with that context.
```

## Operational Checklist (Per Run)

- [ ] Extract dump keywords (domain nouns, project names, format hints)
- [ ] Determine context (CLI / web project / MCP-connected / inaccessible)
- [ ] Run the context-appropriate tactics; never skip verification
- [ ] If context is "inaccessible", say so explicitly + ask about setup
- [ ] Each Section 3 entry must cite the evidence (filename matched, search hit, etc.)
- [ ] Zero entries with phrasing like "probably", "likely", "you might have" — those are speculation, not connections

## Why This Matters

The single fastest way to lose user trust in capture is to surface a fabricated connection. Once the user catches one — "wait, that file doesn't exist" — they stop trusting the entire output, including the items that were correct. Verification is cheap; fabrication is expensive.

