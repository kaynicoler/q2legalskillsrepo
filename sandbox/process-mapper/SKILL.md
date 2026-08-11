---
name: process-mapper
description: Use when a BizOps lead, COO, or process-improvement owner needs to document an end-to-end business process (procurement, employee onboarding, incident handoff, customer-onboarding, claims adjudication) in BPMN-style notation, measure cycle times by stage, surface where work spends most of its time waiting vs. being worked, and quantify the gap between processing time and total elapsed time. Pairs Lean / Six Sigma / Theory-of-Constraints canon with deterministic stdlib-only Python tools to produce a process map, a ranked bottleneck list (with severity + root-cause hypothesis), and a cycle-time analysis (P50, P90, value-add ratio, Little's-Law throughput). Distinct from sales-pipeline, system-reliability (SLO), and strategic-OKR work — this is tactical process documentation for internal operations.
llm: Claude
version: v3
updated: 2026-08-11T21:54:04.437Z
created: 2026-07-07T16:24:06.409Z
---
# process-mapper

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#process-mapper)
BPMN-style business process documentation, bottleneck detection, and cycle-time analysis for internal-operations leaders.

## Purpose

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#purpose)
Internal-operations work suffers from three recurring failure modes:

1. Implicit process — the steps exist only in tribal knowledge, so handoffs drop and onboarding takes weeks.
2. Invisible waiting — most of the elapsed time on any business process is queue / wait / approval time, not actual work; teams optimize the wrong stage.
3. Local optimization — Goldratt's Theory of Constraints is ignored; resources are added to non-constraint stages, gaining nothing.

This skill produces a documented process map, identifies where work waits, and points the constraint out by name with deterministic logic — not LLM intuition.

## When to use

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#when-to-use)

- Documenting a new business process (procurement intake, vendor onboarding, employee onboarding, incident handoff, expense reimbursement, customer onboarding, claims adjudication).
- An existing process is "too slow" but nobody can name the bottleneck.
- Cycle time is being measured but value-add ratio is not — so the team can't tell whether the process is healthy or waste-heavy.
- Cross-functional handoffs are dropping work and root cause is unclear.

## Workflow

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#workflow)
Five-step deterministic flow:

1. Intake. Capture the process as a JSON file with one entry per stage: `name`, `owner`, `type` (`value-add` | `wait` | `rework`), `duration_minutes_p50`, `duration_minutes_p90`. Use `assets/process_template.md` and its JSON skeleton.
2. Map stages. Run `process_documenter.py` to produce an ASCII swim-lane diagram + a normalized JSON artifact. The swim-lane separates lanes by owner so cross-functional handoffs become visible.
3. Measure cycle time. Run `cycle_time_analyzer.py` to compute total P50, total P90, value-add ratio (VA%), and a Little's-Law throughput estimate. Verdict: VA% > 25% = HEALTHY, 10–25% = TYPICAL, < 10% = WASTE-HEAVY.
4. Detect bottlenecks. Run `bottleneck_detector.py` with the appropriate `--profile` (saas / services / manufacturing / healthcare). Output is a ranked list with severity (CRITICAL / HIGH / MEDIUM), root-cause hypothesis, and one recommended action per finding.
5. Recommend. Pair the bottleneck list with the cycle-time verdict; recommend a single constraint-focused intervention per Goldratt's "subordinate everything to the constraint" rule. Don't recommend optimization of a non-constraint stage.

## Scripts

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#scripts)
`scripts/process_documenter.py` — Reads a process JSON, validates it, and emits a text-based BPMN-style swim-lane diagram in Markdown (lanes by owner, stages annotated with type + duration). Also outputs a normalized JSON artifact for downstream tools. Stdlib only. `--sample` prints a 6-stage procurement-intake example.

`scripts/bottleneck_detector.py` — Applies three deterministic detection rules: (a) stage P50 > 2× mean of value-add stages, (b) wait-state % > 40% of total cycle, (c) rework % > 15%. Thresholds adjust by `--profile` because SaaS, services, manufacturing, and healthcare have different "normal" wait ratios. Output is a ranked list with severity, hypothesis, action.

`scripts/cycle_time_analyzer.py` — Computes total P50 and P90 cycle time, value-add ratio (VA%), wait %, rework %, and a Little's-Law throughput estimate (WIP / cycle time). Per Lean canon: VA% > 25% = HEALTHY, 10–25% = TYPICAL (most non-manufacturing processes land here), < 10% = WASTE-HEAVY.

## Quick example

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#quick-example)

```
# Renders a BPMN-style swim-lane diagram + normalized JSON for the built-in 6-stage procurement-intake example
cd business-operations/skills/process-mapper && python3 scripts/process_documenter.py --sample
```

## References

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#references)

- `references/lean_six_sigma_canon.md` — TIMWOOD wastes, value-stream mapping, Theory of Constraints, Kanban WIP, Little's Law. Cites Womack & Jones, Rother & Shook, Goldratt, Ohno, Liker, Pyzdek, Anderson.
- `references/bpmn_essentials.md` — Pools, lanes, gateways, events, message flows, common notation mistakes. Cites the OMG BPMN 2.0 spec, Silver, Allweyer, Freund/Rücker, OASIS, ISO/IEC 19510:2013.
- `references/bottleneck_anti_patterns.md` — Seven specific anti-patterns drawn from Goldratt, Kim et al., Spear, DORA, Deming, and process-mining research.

## Assumptions

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#assumptions)

1. The user can provide stage-level cycle-time data (even rough P50 / P90 estimates). If they cannot, the first step is to instrument the process — not to map it.
2. "Process" here means a repeatable business workflow with discrete stages, not a one-off project.
3. The user has authority to act on bottlenecks (or can route findings to someone who does). Without that, the output is academic.
4. Stage `type` is honest: a "value-add" stage labeled as such by the user really does change the work product from the customer's perspective. Mis-labelling waiting as value-add is the most common data-quality failure.

## Anti-patterns

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#anti-patterns)

- Mapping every process at once. Pick one. Goldratt: the constraint is a single point.
- Optimizing the non-constraint. If stage 4 is the bottleneck, speeding up stage 2 just builds inventory in front of stage 4. Subordinate everything to the constraint.
- Mistaking total cycle time for processing time. They are almost never the same; VA% reveals the gap.
- Adding people to a wait-bound process. Wait time is not solved by more headcount; it's solved by removing the handoff or batch.
- Treating rework as a separate problem. Rework loops belong in the process map. Hiding them understates true cycle time.

## Distinct from

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#distinct-from)

- business-growth skills — external sales motion, lead-funnel conversion, customer-success retention. Process-mapper is *internal* operations.
- engineering/slo-architect — system-reliability SLOs / error budgets / burn-rate alerts. Process-mapper is *business-process* cycle time, not system uptime.
- c-level-advisor (COO / CEO) — strategic prioritization of which processes to fix. Process-mapper is the tactical instrument used after that prioritization decision.
- project-management skills — Jira / Confluence ticket workflow tooling. Process-mapper is process *design*, not ticket *tracking*.

## Forcing-question library (Matt Pocock grill discipline)

[](https://github.com/alirezarezvani/claude-skills/blob/main/business-operations/skills/process-mapper/SKILL.md#forcing-question-library-matt-pocock-grill-discipline)
Before invoking the tools, the orchestrator (or `/cs:grill-bizops`) walks the user through these questions one at a time, with a recommended answer + canon citation. Never bundled.

1. "Do you have measured cycle times for the top-3 longest stages, or only estimates?" Recommended: insist on measured data. Canon: Goldratt 1984 (*The Goal*) — optimizing estimated bottlenecks reliably attacks the wrong constraint.
2. "Are you mapping the *current* process (as-is) or the *intended* process (to-be)?" Recommended: map as-is first. To-be after bottleneck is identified. Canon: Rother & Shook 1999 (*Learning to See*) — value-stream mapping starts with the current state, always.
3. "Where do handoffs occur between teams, and how long does each handoff wait?" Recommended: log every handoff with median wait time. Canon: Reinertsen 2009 (*Principles of Product Development Flow*) — wait time at handoffs is the largest invisible cost.
4. "What's your batch size at each stage?" Recommended: drive batch size toward 1 wherever possible. Canon: Anderson 2010 (*Kanban*) — batch size correlates 1:1 with cycle time variance.
5. "What's the rework rate per stage?" Recommended: surface it explicitly; rework loops belong in the map. Canon: Pyzdek (*Six Sigma Handbook*) — hidden rework drives 30-50% of total cycle time in service processes.

Walk depth-first. Don't open question 4 before 1-3 are answered. After all 5 are locked, invoke `process_documenter.py` → `bottleneck_detector.py` → `cycle_time_analyzer.py` in sequence.


---

## Reference: bottleneck_anti_patterns

# Bottleneck Anti-Patterns

Seven plus specific anti-patterns that recur in business-process improvement
work. Each is sourced to primary literature, and each has a corresponding
detection or recommendation in the skill's tools.

## Sources

1. **Goldratt, E. M. (1984). _The Goal._** North River Press. — Theory of Constraints.
2. **Kim, G., Behr, K. & Spafford, G. (2013). _The Phoenix Project: A Novel About IT, DevOps, and Helping Your Business Win._** IT Revolution Press. — TOC applied to IT operations.
3. **Spear, S. J. (2009). _The High-Velocity Edge._** McGraw-Hill. — Toyota-derived discipline for complex operations; explicit treatment of why local optimization fails.
4. **Forsgren, N., Humble, J. & Kim, G. (2018). _Accelerate: The Science of Lean Software and DevOps._** IT Revolution. — DORA research; empirical link between flow metrics and outcomes.
5. **Deming, W. E. (1986). _Out of the Crisis._** MIT Press. — System-of-profound-knowledge framework; root-cause discipline.
6. **van der Aalst, W. M. P. (2016). _Process Mining: Data Science in Action,_ 2nd ed.** Springer. — Empirical methodology for discovering actual process behavior vs. documented behavior.
7. **Reinertsen, D. G. (2009). _The Principles of Product Development Flow._** Celeritas Publishing. — Queueing theory and cost of delay.
8. **Forrester Research. (Multiple years.) _Process Mining: Vendor and Market Analyses._** — Industry research on process-mining adoption and the gap between modeled and actual process.

---

## AP-1. Optimizing the non-constraint

**Source:** Goldratt (1984), Kim et al. (2013).

A team identifies that stage 2 of a process is "slow" (relative to other
non-constraint stages) and optimizes it. The actual constraint is stage 4.
Result: throughput is unchanged; inventory grows in front of stage 4.

**Detection:** Compare every stage's P50 to the value-add mean (Rule R1) but
weight the recommendation by impact on total cycle. The skill's
`bottleneck_detector.py` ranks by impact_minutes_p50 specifically to direct
attention to the binding constraint.

**Counter-pattern:** Always solve the longest wait or longest stage first;
ignore "quick wins" elsewhere until the constraint moves.

---

## AP-2. Adding resources before identifying the constraint

**Source:** Goldratt (1984), Reinertsen (2009).

Symptom: "We need to hire more procurement analysts." Reality: the analysts
are not the constraint; manager approval queues are. Adding analysts increases
WIP, lengthens cycle time (per Little's Law), and makes the queue worse.

**Detection:** Rule R2 (wait-share > 40%) catches the case where the wait —
not capacity — dominates.

**Counter-pattern:** First check whether wait time exceeds value-add time. If
it does, no amount of new staffing will help. Remove the handoff, parallelize
the approval, or apply WIP limits.

---

## AP-3. Mistaking wait time for processing time

**Source:** Rother & Shook (1999), Deming (1986).

A team reports that "manager approval takes two days." On inspection, the
manager spends 10 minutes reviewing each request; the rest is queue time.
Process time is 10 minutes; lead time is two days. Treating them as the same
hides the real problem.

**Detection:** The skill's stage `type` field separates `value-add` from
`wait`. The value-add ratio (VA%) in `cycle_time_analyzer.py` quantifies the
gap.

**Counter-pattern:** Force stages to declare their type honestly. Any stage
where the worker is not actively engaged is a wait stage, regardless of who
"owns" it.

---

## AP-4. Inspection-as-quality

**Source:** Pyzdek (Six Sigma Handbook), Deming (1986), Spear (2009).

Defects keep escaping, so the team adds a final QA review. The defects don't
go down (the upstream stages haven't changed) — but cycle time goes up because
of the new stage. Worse, the QA reviewer is now blamed for misses.

**Detection:** Rule R3 (rework share > 15%) with the hypothesis "defects
escape upstream stages."

**Counter-pattern:** Find the earliest stage that could detect the defect; add
the check there (poka-yoke). Stop the line on detection; don't queue defects
for downstream rework.

---

## AP-5. Optimizing the documented process, not the actual one

**Source:** van der Aalst (2016), Forrester process-mining reports.

The team documents the "official" process and optimizes it. Process-mining
tools then reveal that 60% of cases skip stages, loop back, or take undocumented
routes. The optimization had no effect because it targeted a fiction.

**Detection:** The skill cannot detect this from the input JSON alone — it
relies on the user to report actual stage durations from real cases, not
target durations. The "Assumptions" section in SKILL.md surfaces this
explicitly.

**Counter-pattern:** Use ticket-system data, time-stamps, or event logs to
ground stage durations in actual cases. If the data isn't available, the
first step is instrumentation, not mapping.

---

## AP-6. Batched approvals as the default

**Source:** Reinertsen (2009), Anderson (Kanban, 2010).

Approvers batch requests: "I'll review everyone's POs on Friday afternoon."
This adds half the batch interval (typically 3–4 days) to the average wait
time of every request, with no quality benefit.

**Detection:** Wait stages with P50 durations measured in days (hundreds of
minutes) are almost always batched. The skill flags them via R1 and R2.

**Counter-pattern:** Move to continuous-flow approval. If continuous is
infeasible (e.g., a committee that meets weekly), at least shrink the batch
interval or move approval to a lower level where it can run continuously.

---

## AP-7. Local efficiency metrics

**Source:** Goldratt (1984), Deming (1986), Spear (2009).

Each stage is measured on its own efficiency (e.g., "manager handles 95% of
requests within SLA"). The system as a whole is not measured. Each role
optimizes locally, pushing work as fast as possible to the next queue —
which is exactly where it stalls.

**Detection:** The skill's verdict is always at the **process** level (VA%,
total cycle time), never at the stage level. The `bottleneck_detector.py`
recommendation text explicitly invokes Goldratt's "subordinate everything to
the constraint."

**Counter-pattern:** Measure throughput and total cycle time at the process
level. Stage-level metrics are diagnostic, not goal-setting.

---

## AP-8. Skipping the value-stream map and going straight to automation

**Source:** Kim et al. (2013), Forrester process-mining research.

A team buys an RPA / workflow automation tool, then automates the existing
broken process. Result: the bad process now runs faster, with the same wait
queues and same rework rate. Goldratt's term for this is "automating the
mess."

**Detection:** Outside the skill's automated detection; surfaced in
SKILL.md's "Anti-patterns" list.

**Counter-pattern:** Map the value stream first. Eliminate wait and rework
stages. Then — and only then — consider automating what remains.

---

## AP-9. Treating cycle time as fixed

**Source:** Forsgren, Humble & Kim (2018, _Accelerate_).

A team reports cycle time as a single number ("it takes 5 days"). Real cycle
times are distributions, often log-normal, with heavy P90 / P99 tails. A 5-day
P50 with a 30-day P90 is a wildly different process than a 5-day P50 with a
6-day P90; the first is unpredictable, the second is reliable.

**Detection:** The skill captures both P50 and P90 per stage and reports
both totals. A large P90 / P50 ratio in `cycle_time_analyzer.py` is a flag
for high variability even when total cycle time looks acceptable.

**Counter-pattern:** Always quote P50 and P90 (or P50 and P95). DORA's
_Accelerate_ research finds that lead-time **variability** correlates with
business outcomes as strongly as median lead time.

## Reference: bpmn_essentials

# BPMN Essentials for Business-Process Documentation

A practical reference on BPMN (Business Process Model and Notation) for
process-mapper users. The skill emits text-based swim-lane diagrams that
approximate the BPMN structure without requiring users to install Visio,
Lucidchart, or Camunda. This file explains the canon those diagrams reflect.

## Sources

1. **Object Management Group. (2011). _Business Process Model and Notation (BPMN), Version 2.0._** OMG Document Number formal/2011-01-03. — The normative specification.
2. **Silver, B. (2011). _BPMN Method and Style,_ 2nd ed.** Cody-Cassidy Press. — The canonical practitioner book; defines the "method and style" rules now widely treated as informal BPMN convention.
3. **Allweyer, T. (2010). _BPMN 2.0: Introduction to the Standard for Business Process Modeling._** Books on Demand. — Approachable academic introduction.
4. **Freund, J. & Rücker, B. (2019). _Real-Life BPMN,_ 4th ed.** CreateSpace. — Practical patterns from the Camunda team.
5. **OASIS. (2010). _Web Services Business Process Execution Language (WS-BPEL), Version 2.0._** — Related execution standard; clarifies the interplay between BPMN modeling and BPEL execution.
6. **ISO/IEC 19510:2013. _Information technology — Object Management Group Business Process Model and Notation._** — The international-standard version of OMG BPMN 2.0.
7. **Recker, J. (2010). "Opportunities and constraints: the current struggle with BPMN." _Business Process Management Journal,_ 16(1), 181–201.** — Peer-reviewed analysis of BPMN adoption pain points; sources the "common notation mistakes" list below.
8. **Dumas, M., La Rosa, M., Mendling, J. & Reijers, H. A. (2018). _Fundamentals of Business Process Management,_ 2nd ed.** Springer. — Textbook covering BPMN within the broader BPM lifecycle.

---

## Core BPMN elements

BPMN has hundreds of symbols. In practice, ~80% of useful diagrams use only
~10 of them. The skill's swim-lane output uses precisely these.

### Flow objects

- **Activity (task)** — a unit of work done by one role. Rectangle with rounded
  corners. In the skill's swim-lane: this is a `value-add` or `rework` stage.
- **Event** — something that happens (start, intermediate, end). Circles. The
  skill represents start/end implicitly as the first and last stage.
- **Gateway** — branching / merging point. Diamond. Common types:
  - **Exclusive (XOR)** — one path taken.
  - **Parallel (AND)** — all paths taken.
  - **Inclusive (OR)** — one or more paths taken based on data.

### Connecting objects

- **Sequence flow** — solid arrow inside one pool. The skill renders these as
  `->` between stages in the lane.
- **Message flow** — dashed arrow across pool boundaries. The skill's
  cross-lane handoffs (e.g., Requestor -> Manager) are message-flow-equivalents.
- **Association** — dotted line linking a data object to an activity.

### Swim lanes

- **Pool** — represents a participant (a company, a department, or a system).
  Each pool is independent; communication between pools uses message flow only.
- **Lane** — a sub-partition within a pool, usually a role or sub-team.

The skill maps one stage's `owner` field to one lane. The full diagram is a
single pool with multiple lanes — appropriate for an internal business process
where one organization controls the whole flow.

---

## Method and Style rules (Silver)

Silver's "Method and Style" is a set of practitioner conventions that make
BPMN diagrams readable. The most load-bearing rules:

1. **One start, one end** per pool. Multiple end events are allowed only if
   they represent different end-states (e.g., approved vs. rejected).
2. **Label every flow out of a gateway** with the condition (e.g., "amount >
   $10K"). An unlabeled gateway is unreadable.
3. **Sequence flow stays inside a pool.** Use message flow between pools.
4. **One verb-noun task name.** "Approve PO" beats "Approval step."
5. **Black-box pools** for participants you don't model in detail (e.g., the
   customer). Show only the message exchanges with them.

The skill enforces rule #4 implicitly by encouraging "Stage" names like
"Manager approves request" rather than "Approval."

---

## Common notation mistakes (Recker 2010; Freund/Rücker)

The following errors appear in over half of real-world BPMN diagrams:

| Mistake | Why it's wrong | What to do |
|---------|----------------|------------|
| Using sequence flow across pools | Pools are independent; only messages cross | Use dashed message flow |
| Missing gateway labels | The reader can't tell which path is taken when | Label every outbound flow |
| Multiple unrelated end events | Reader can't tell why a process ends in each spot | Consolidate or label by end-state |
| Conflating role with system | "JIRA" is a system, not a role; "Engineering Manager" is a role | Lanes = roles, not tools |
| Implicit gateways | Diverging sequence flows without a gateway diamond | Add an explicit XOR or parallel gateway |
| Modeling exceptions inline | Cluttered happy path | Use boundary events or a separate exception sub-process |
| No data objects | Reader doesn't know what artifacts move through | Add data-object boxes where they help |

The skill's stage-level `type` field (`value-add` | `wait` | `rework`) captures
the rework case explicitly so it doesn't get hidden inline. Users who want
full BPMN fidelity should export the normalized JSON and ingest it into a
BPMN-aware tool (Camunda Modeler, bpmn.io, Signavio).

---

## When to use BPMN vs. simpler notations

BPMN is appropriate when:

- The process has cross-functional handoffs (multiple lanes).
- The process has branching logic (gateways).
- The diagram will be reviewed by people who don't sit through a walkthrough.

For purely linear processes with no branching, a numbered list or a value
stream map is faster to produce and easier to read. The skill's swim-lane
output deliberately occupies the middle ground: more structured than a list,
less ceremony than full BPMN.

---

## BPMN 2.0 execution semantics

ISO/IEC 19510:2013 specifies executable semantics so that a BPMN diagram can
be loaded into a workflow engine (Camunda, jBPM, Activiti) and run directly.
The skill does not target executable BPMN — its output is for human reading
and constraint analysis. If a user wants to move from documentation to
automation, the normalized JSON is a starting point; mapping to the BPMN 2.0
XML schema is a separate exercise.

## Reference: lean_six_sigma_canon

# Lean / Six Sigma / Theory-of-Constraints Canon

A working reference for the process-mapper skill. The concepts below are the
intellectual foundation for every detection rule and verdict band the skill
emits. Citations are deliberately to the primary sources, not blog posts.

## Sources

1. **Womack, J. P. & Jones, D. T. (1996). _Lean Thinking: Banish Waste and Create Wealth in Your Corporation._** Free Press. — The five-step Lean discipline: specify value, identify the value stream, make value flow, let the customer pull, pursue perfection.
2. **Rother, M. & Shook, J. (1999). _Learning to See: Value Stream Mapping to Add Value and Eliminate Muda._** Lean Enterprise Institute. — The canonical text on Value Stream Mapping (VSM); origin of current-state / future-state map distinction.
3. **Goldratt, E. M. (1984). _The Goal: A Process of Ongoing Improvement._** North River Press. — The Theory of Constraints: identify, exploit, subordinate, elevate, repeat. Every process has exactly one binding constraint at a time.
4. **Ohno, T. (1988). _Toyota Production System: Beyond Large-Scale Production._** Productivity Press. — Origin of the seven wastes (muda), pull system, jidoka, and andon discipline.
5. **Liker, J. K. (2004). _The Toyota Way: 14 Management Principles from the World's Greatest Manufacturer._** McGraw-Hill. — Modern systemic treatment of TPS principles for non-manufacturing operations.
6. **Pyzdek, T. & Keller, P. (2018). _The Six Sigma Handbook,_ 5th ed.** McGraw-Hill. — DMAIC discipline, SIPOC, process-capability indices, defect-rate measurement.
7. **Anderson, D. J. (2010). _Kanban: Successful Evolutionary Change for Your Technology Business._** Blue Hole Press. — WIP limits, pull system applied to knowledge work, cumulative flow diagrams.
8. **Reinertsen, D. G. (2009). _The Principles of Product Development Flow._** Celeritas Publishing. — Queueing theory for knowledge-work product development; cost of delay.

---

## The Seven Wastes (TIMWOOD)

Ohno's original taxonomy, with the eighth ("non-utilized talent") added later:

| Code | Waste | What it looks like in business processes |
|------|-------|--------------------------------------------|
| **T** | Transport | Moving work between systems / inboxes / queues for no reason |
| **I** | Inventory | Backlogs of pending tickets, unprocessed invoices, open POs |
| **M** | Motion | People hunting for information, switching tools, reading email threads to reconstruct context |
| **W** | Waiting | Work sitting in someone's queue (the largest waste in office work) |
| **O** | Over-production | Producing forecasts, reports, or work nobody requested |
| **O** | Over-processing | Approval chains that add no scrutiny, gold-plating |
| **D** | Defects | Errors that force rework downstream |
| **(N)** | Non-utilized talent | Skilled people doing low-skill work |

The process-mapper skill identifies these via stage `type`: `wait` captures
**W** (and often **I**); `rework` captures **D**. Mis-labelling a wait stage as
`value-add` is the most common data-quality failure and will mask the true
constraint.

---

## Value Stream Mapping (Rother & Shook)

VSM separates **process time** (PT) from **lead time** (LT). For each stage:

- **PT** = the time work actually spends being touched.
- **LT** = the elapsed wall-clock time from when work arrives at the stage to
  when it leaves.

In the process-mapper schema, a `value-add` stage's `duration_minutes_p50` is
PT-like; a `wait` stage's duration is the LT component between PT-stages.

The **process cycle efficiency** (PCE) is:

    PCE = Total value-add time / Total lead time

This is exactly what `cycle_time_analyzer.py` computes as the "value-add ratio."
Rother & Shook's published benchmarks: office processes typically score
PCE < 10%; well-run service operations land 10–25%; world-class manufacturing
can clear 25–40%.

---

## Theory of Constraints (Goldratt)

Goldratt's Five Focusing Steps:

1. **Identify** the constraint.
2. **Exploit** it (squeeze every minute of capacity from the constraint).
3. **Subordinate** everything else to the constraint.
4. **Elevate** the constraint (only after step 2 is exhausted, add capacity).
5. **Repeat** — once the constraint moves, return to step 1.

Two implications used in the skill:

- **Optimizing a non-constraint stage produces no system improvement.** It
  builds inventory in front of the constraint. The `bottleneck_detector.py`
  output is ranked by impact specifically so users target the constraint
  first.
- **The constraint is almost always a wait stage in office work.** This is
  why Rule R2 (wait-share > 40%) is heavily weighted.

---

## Kanban WIP Limits (Anderson)

Little's Law:

    L = lambda * W

Where L = items in the system (WIP), lambda = throughput (items per unit time),
and W = average cycle time. Rearranged:

    lambda = L / W

Two practical consequences:

- **Cycle time scales linearly with WIP.** Cutting WIP in half cuts cycle time
  in half (other things equal). This is why the skill computes throughput from
  WIP / cycle time and surfaces a WIP-limit recommendation when wait-share is
  high.
- **Adding people to a wait-bound process makes it worse.** New workers add
  WIP without expanding the constraint, lengthening cycle time. The
  `bottleneck_detector` action text says this explicitly.

---

## Six Sigma DMAIC and Rework

Pyzdek's DMAIC (Define, Measure, Analyze, Improve, Control) treats rework as
a downstream symptom of an upstream defect. The Six-Sigma rule the skill
encodes: **rework is always solved upstream, never downstream.** Adding a
quality-control inspector at the end of the line catches defects but doesn't
prevent them, and inspection-as-quality is itself a TIMWOOD waste
(over-processing).

The poka-yoke (error-proofing) recommendation in Rule R3 follows directly:
add the check at the earliest stage that can detect the defect.

---

## Reinertsen's Queueing Insights

Reinertsen's _Principles of Product Development Flow_ adapts manufacturing
queueing theory to knowledge work. Key results used in the skill:

- **High utilization explodes queue length.** A worker at 90% utilization has
  ~10x the queue of a worker at 50% utilization. Office workflows that pin
  approvers at 100% utilization see wait stages grow without bound.
- **Small batches cut queue time.** Batched approvals (e.g., weekly review
  cycles) inflate P50 wait times by half the batch interval on average.

When the skill recommends "remove the handoff or batch," this is the canon
behind it.

## Reference: process_template

# Process Template

Use this template to document a business process before running it through
the process-mapper tools. Fill in the stage table first, then translate it
into the JSON skeleton at the bottom of this file. Feed that JSON into the
three CLI tools:

```
python3 scripts/process_documenter.py    --input my-process.json
python3 scripts/bottleneck_detector.py   --input my-process.json --profile saas
python3 scripts/cycle_time_analyzer.py   --input my-process.json --profile saas
```

---

## Process metadata

- **Process name:** _(e.g., Procurement Intake, Employee Onboarding, Incident Handoff)_
- **Owner role:** _(who is accountable for the end-to-end process)_
- **Frequency:** _(how often this process runs — daily, weekly, on-demand)_
- **Trigger event:** _(what starts the process)_
- **End state:** _(what marks the process complete)_
- **WIP at any time:** _(how many items are typically in process at once; needed for Little's-Law throughput)_

---

## Stage table

Six rows to start. Add or remove as needed. **Honesty about stage `type` is
the single most important data-quality choice.** If a stage is queue / wait,
mark it `wait`. If it changes the work product from the customer's
perspective, mark it `value-add`. If it exists to fix an upstream defect,
mark it `rework`.

| # | Stage name | Owner (role) | Type | P50 (min) | P90 (min) | Notes |
|---|------------|--------------|------|-----------|-----------|-------|
| 1 | _e.g., Submit request_ | Requestor | value-add | 15 | 30 | |
| 2 | _e.g., Wait for manager approval queue_ | Manager | wait | 480 | 1440 | Typically batched |
| 3 | _e.g., Manager approves_ | Manager | value-add | 10 | 25 | |
| 4 | _e.g., Wait for finance review_ | Finance | wait | 720 | 2880 | |
| 5 | _e.g., Finance validates budget code_ | Finance | value-add | 20 | 60 | |
| 6 | _e.g., Rework — missing vendor W-9_ | Requestor | rework | 120 | 360 | Frequent escape |

**Type definitions (Lean canon):**

- `value-add` — the stage changes the work product in a way the end customer
  would willingly pay for. Most stages are NOT value-add.
- `wait` — work is queued, idle, or waiting for someone. Wait stages are the
  largest source of cycle-time bloat in most office processes.
- `rework` — the stage exists to fix a defect introduced upstream. Six-Sigma
  canon: rework is always an upstream-quality problem.

---

## JSON skeleton

Copy this into `my-process.json`, edit the values to match your stage table,
and pass it to the CLI tools.

```json
{
  "process_name": "Replace with your process name",
  "wip": 12,
  "stages": [
    {
      "name": "Stage 1 name",
      "owner": "Owning role",
      "type": "value-add",
      "duration_minutes_p50": 15,
      "duration_minutes_p90": 30
    },
    {
      "name": "Stage 2 name",
      "owner": "Owning role",
      "type": "wait",
      "duration_minutes_p50": 480,
      "duration_minutes_p90": 1440
    },
    {
      "name": "Stage 3 name",
      "owner": "Owning role",
      "type": "value-add",
      "duration_minutes_p50": 10,
      "duration_minutes_p90": 25
    },
    {
      "name": "Stage 4 name",
      "owner": "Owning role",
      "type": "wait",
      "duration_minutes_p50": 720,
      "duration_minutes_p90": 2880
    },
    {
      "name": "Stage 5 name",
      "owner": "Owning role",
      "type": "value-add",
      "duration_minutes_p50": 20,
      "duration_minutes_p90": 60
    },
    {
      "name": "Stage 6 name",
      "owner": "Owning role",
      "type": "rework",
      "duration_minutes_p50": 120,
      "duration_minutes_p90": 360
    }
  ]
}
```

---

## Tips

- **Use real data when you can.** Pull stage durations from your ticket system
  (Jira, ServiceNow, Zendesk). Estimated durations are fine for a first pass
  but should be replaced before any change decision is made.
- **One process at a time.** Goldratt: every system has exactly one binding
  constraint. Mapping ten processes simultaneously dilutes attention away
  from the one that's actually limiting throughput.
- **Profile choice matters.** Pass `--profile manufacturing` for physical-goods
  flows, `--profile services` for human-delivered services with longer
  acceptable wait times, `--profile healthcare` for clinical or regulated
  human-in-the-loop flows, `--profile saas` for everything else.

