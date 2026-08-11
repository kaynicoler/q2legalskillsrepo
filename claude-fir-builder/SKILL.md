---
name: Claude-FIR-Builder
description: "Build a filled AI Champion Field Intelligence Report (FIR) as a ready-to-present PPTX for an OLT rep calibration meeting. Auto-drafts content by scanning Teams messages, Outlook emails, and Zoom transcripts for AI-related activity during a reporting period, then asks targeted follow-up questions only for genuine gaps. Use this skill whenever a Champion needs to prep their FIR, fill out the field intelligence report, get ready for their OLT rep meeting, generate their quarterly AI update, prep for their Champion check-in, or says anything like \\\"help me fill out my FIR\\\", \\\"draft my field report\\\", \\\"prep my OLT meeting\\\", \\\"build my field intelligence report\\\", \\\"I have my OLT sync coming up\\\", or \\\"it's time for my Champion report\\\". Also trigger when the Champion pastes in meeting notes, a signal log, or activity from the period and wants it turned into a structured report."
author: Cara Johnson
llm: Claude
version: v2
updated: 2026-08-11T21:23:51.128Z
created: 2026-08-03T23:16:33.891Z
---
---

name: champion-fir-builder description: Build a filled AI Champion Field Intelligence Report (FIR) as a ready-to-present PPTX for an OLT rep calibration meeting. Auto-drafts content by scanning Teams messages, Outlook emails, and Zoom transcripts for AI-related activity during a reporting period, then asks targeted follow-up questions only for genuine gaps. Use this skill whenever a Champion needs to prep their FIR, fill out the field intelligence report, get ready for their OLT rep meeting, generate their quarterly AI update, prep for their Champion check-in, or says anything like "help me fill out my FIR", "draft my field report", "prep my OLT meeting", "build my field intelligence report", "I have my OLT sync coming up", or "it's time for my Champion report". Also trigger when the Champion pastes in meeting notes, a signal log, or activity from the period and wants it turned into a structured report.

---

# AI Champion Field Intelligence Report Builder

You're helping an AI Champion at Q2 prepare their Field Intelligence Report (FIR) — a structured 9-slide summary of what's happening with AI adoption in their org, used as a conversation guide with their OLT rep.

The goal is to do as much of the work as possible. Champions are busy. If you can pull signal from their digital footprint — Teams messages, emails, Zoom transcripts, a running signal log — you should. Only ask questions for things you genuinely can't infer.

Think of yourself as a sharp assistant who has been watching the Champion's activity all quarter and can draft a coherent report in 10 minutes. The Champion's job is to review and refine, not start from scratch.

---

---
**The FIR structure (know this before you start)**
---

The FIR has 6 substantive sections plus a cover and appendix:

| Slide | Section | What it covers |
| --- | --- | --- |
| 1 | Cover | Champion name, org, OLT rep, reporting period |
| 3 | Section 1: Snapshot | 60-second read: overall momentum, what changed, single most important thing |
| 4 | Section 2: Adoption pulse | Which tools are gaining traction, who the power users are, adoption by team/role |
| 5 | Section 3: What's working | Strongest win/proof point, promising use cases, positive surprises |
| 6 | Section 4: What's stalled | Friction and blockers, unanswered questions, cross-team asks and routing |
| 7 | Section 5: Champion health check | Personal: role sustainability, own AI fluency, network connection, capacity |
| 8 | Section 6: Asks and next steps | Specific asks of the OLT rep, top 30-day focus areas, commitments |
| 9 | Appendix | Running signal log: wins, blockers, guidance gaps, routing needs, power-user signals |

Slide 2 is a "How to use" guide — leave it unchanged.

---

---
**Step 1: Gather setup info (ask all at once)**
---

Start by asking the Champion for the basics needed to get going. Ask everything in one message:

- **Their name** and **org/team**
- **OLT rep's name**
- **Reporting period** (e.g., "July 2026", "Q2 FY26", or specific dates)
- **Signal log** — do they have a running notes file capturing wins, blockers, and observations? If yes, what's the path or can they paste it in?

While waiting for their response, start Step 2 if you already have the reporting period from context.

---

---
**Step 2: Scan available sources (run in parallel)**
---

Use whatever connectors the Champion has available. Run these searches simultaneously. Cap each at 20-25 results. Skip any source gracefully if the connector isn't available, and note which ones you couldn't reach.

### Teams messages

Search for the reporting period using `chat_message_search` with AI-related keywords. Focus on messages the Champion *sent* — those are signals they've already expressed.

Good keyword batches:

- Round 1: "AI", "Claude", "Copilot", "use case"
- Round 2: "blocked", "stalled", "win", "adoption", "champion"

Note which channels the activity is concentrated in. Repeated questions on the same topic signal a guidance gap.

### Outlook emails

Use `outlook_email_search` for two targeted searches within the reporting period:

1. **Sent items**: keywords "AI", "Claude", "champion", "use case", "adoption"
2. **Inbox**: keywords "AI champion", "OLT", "AI adoption", "blocked", "escalate"

Cap at 15 emails per search. Sent items are the higher-signal source.

### Zoom / meeting transcripts

Search for transcripts or recordings from the reporting period via the Zoom connector. Look for AI tool discussions, blockers raised in team meetings, and use case demos.

### Signal log

If the Champion provided a signal log file or pasted text — this is the highest-priority source. It's already curated. Read it first and use it to anchor the other findings.

---

---
**Step 3: Synthesize and map to FIR sections**
---

Once you have the scanned material, map signals to sections:

**Section 1 (Snapshot):** Overall momentum signals, major events. Identify the single most important thing that happened.

**Section 2 (Adoption pulse):** Tool mentions by name, teams or roles using AI actively, individuals described as frequent users (power users). "First use" or "trying X" patterns indicate the exploring tier.

**Section 3 (What's working):** Wins with specific outcomes ("saved 2 hours", "got the client answer faster"), use cases that got positive reactions, surprises where AI performed better than expected.

**Section 4 (What's stalled):** Friction language ("can't", "waiting on", "still not sure"), repeated questions, anything routed to AITO/Legal/Security/Compliance.

**Section 5 (Champion health):** Sources rarely capture this well — the Champion's internal experience isn't in their Teams posts. Note as a gap to fill with direct questions.

**Section 6 (Asks and next steps):** Explicit asks or escalations, things the Champion can't resolve on their own.

Draft content for each section. Where sources are thin, note the gap.

---

---
**Step 4: Ask targeted gap-fill questions**
---

Present a brief summary of what you found ("I pulled X Teams messages and Y emails from [period] — here's what I have so far"), then ask targeted questions only for genuine gaps.

**Principles:**

- Don't ask about something you already have a good answer for
- Be specific — "I see you mentioned [X] in Teams, but I didn't find a clear outcome — what was the result?" is better than "What's working?"
- 5-8 questions total is the sweet spot; more than that feels like homework

**Always ask — Section 1 (Snapshot slide, bottom indicator):**

- "For the **Overall momentum** indicator — which best fits right now: **Building fast**, **Steady progress**, **Gaining slowly**, or **Stalled**?" Never infer this from sources. It's a judgment call only the Champion can make.

**Always ask — Section 5 (Champion health check, all 5 rows):**

Ask all five — they map directly to the health check grid on Slide 7. Use the exact option words so the answer maps cleanly to the template.

- "**Overall momentum in my org** — Strong / Building / Uneven / Stalled?"
- "**My own AI fluency & confidence** — Strong / Building / Developing / Unsure?"
- "**Connection to Champion network** — Active / Moderate / Developing / Minimal?"
- "**Confluence / Skills repo health** — Healthy / Needs work / Not yet live / Has titles only / Open?"
- "**My capacity for this role** — Open / Manageable / Tight / Unsustainable?"

Then ask the two open-text reflection questions:

- "What's been working well for you in the Champion role?"
- "What support do you need from your OLT rep personally — not just for your org?"

If the Champion gives a free-form answer ("I'm doing okay"), prompt once: "To lock in the right option for the template — would that be Manageable or Tight?"

**Section 6 questions** (if thin):

- "What are your top 2-3 focus areas for the next 30 days?"
- "What's the single most important thing you need from your OLT rep in this conversation?"

---

---
**Step 5: Generate the FIR PPTX**
---

Once you have content for all sections, generate the filled PPTX using the bundled template and population script.

**Template:** `assets/FIR_Template.pptx`

**Script:** `scripts/build_fir.py`

bash

```
python scripts/build_fir.py \
  --template assets/FIR_Template.pptx \
  --data fir_content.json \
  --output ChampionName_FIR_Period.pptx
```

**Output filename format:** `[FirstName]_FIR_[Period].pptx` — e.g., `Alex_FIR_July2026.pptx`

### JSON data schema

Save your FIR content as `fir_content.json` using this exact structure. The script keys off these field names — don't rename them.

**Content length:** Keep each narrative field to ~50 words. The answer boxes in the template are fixed-size. Text beyond the box will overflow and obscure the slide layout.

**Health check values:** The five `section5_health` option values must exactly match one of the valid option words listed below — the script does case-insensitive string matching against the pill labels in the slide.

json

```
{
  "cover": {
    "champion_name": "First Last",
    "org_team": "Team / Department",
    "olt_rep": "Rep Name",
    "reporting_period": "July 2026",
    "date": "July 28, 2026"
  },
  "section1_snapshot": {
    "adoption_status": "~50 words: overall AI adoption status and momentum",
    "what_changed": "~50 words: what is new since the last check-in",
    "most_important": "~50 words: the single most important thing to know right now",
    "momentum_rating": "Building fast | Steady progress | Gaining slowly | Stalled"
  },
  "section2_adoption": {
    "tools_gaining_traction": "~50 words: which tools and where",
    "power_users": "~50 words: named individuals and what they are doing",
    "adoption_table": [
      {
        "team_role": "Team or role name",
        "tools": "Tool1, Tool2",
        "signal": "Active | Exploring | Stalled",
        "notes": "Brief context"
      }
    ]
  },
  "section3_working": {
    "strongest_win": "~50 words: a specific named win with an outcome",
    "promising_use_cases": "~50 words: use cases showing early traction",
    "positive_surprise": "~50 words: something that worked better than expected"
  },
  "section4_stalled": {
    "friction_patterns": "~50 words: recurring blockers and friction",
    "open_questions": "~50 words: unanswered questions the team is waiting on",
    "cross_team_asks": "~50 words: items routed to other teams",
    "routing_log": [
      {
        "item": "What needs to happen",
        "route_to": "Team or person",
        "priority": "Critical | High | Medium",
        "status": "Current status"
      }
    ]
  },
  "section5_health": {
    "org_momentum":        "Strong | Building | Uneven | Stalled",
    "ai_fluency":          "Strong | Building | Developing | Unsure",
    "network_connection":  "Active | Moderate | Developing | Minimal",
    "confluence_health":   "Healthy | Needs work | Not yet live | Has titles only | Open",
    "capacity":            "Open | Manageable | Tight | Unsustainable",
    "working_well":        "~50 words: what is working well for the Champion personally in this role",
    "needs_support":       "~50 words: what personal support the Champion needs from their OLT rep"
  },
  "section6_asks": {
    "olt_rep_asks":        "~50 words: specific asks of the OLT rep (numbered list works well)",
    "focus_areas_30_days": "~50 words: top priorities for the next 30 days",
    "commitments": [
      {
        "commitment": "What will be done",
        "owner": "Who owns it",
        "due": "Target date"
      }
    ]
  },
  "signal_log": [
    {
      "date": "Month Day",
      "type": "Win / proof point | Blocker / friction | Guidance gap | Power-user signal | Routing need",
      "observation": "What happened or was observed",
      "next_step": "What action follows"
    }
  ]
}
```

### Script notes — do not work around these

The script handles several template quirks automatically. These are already fixed; adding workarounds will break things:

- **Bad CRC images:** The template has 4 background images with corrupt checksums. The script bypasses CRC validation to read the actual image data. Do not attempt to replace or re-embed these images.
- **Z-order inconsistency:** Some health check option containers sit above their label shapes in the PPTX XML stack. The script moves selected containers to the back before filling them. Do not manually fill containers with color.
- **Font inheritance:** Answer boxes in the template have no pre-existing runs. The script writes explicit 12pt Avenir LT Std directly into the XML on every run — it does not rely on slide master inheritance. Do not set auto-fit or change font size via python-pptx's high-level API.
- **Shared option names across rows:** Some option labels appear in multiple rows (e.g. "Strong" and "Building" in rows 1 and 2, "Developing" in rows 2 and 3, "Open" in rows 4 and 5). The script uses multi-home matching so each label is preserved in every row it belongs to. Do not simplify the option lists.
- **Template grid consistency:** Every pill position in the health grid has a visible container outline, dot, and text label. The script preserves all of these, even at positions where the label originates from an adjacent row's option set. Do not hide orphaned containers or white out labels at occupied grid positions.

---

---
**Step 6: Brief the Champion on the output**
---

Don't just hand over the file. Give the Champion a quick orientation:

- Which sections have strong sourced evidence (cite the sources: "based on 3 Teams messages and your signal log")
- Which sections are thinner or more based on their direct answers
- A flag on **Section 6 (Asks and next steps)**: this is the most actionable part of the OLT conversation — worth their extra attention before the meeting
- A reminder that red instructional text in the template can be deleted before sharing

Optionally, remind them that keeping a running signal log between now and their next FIR will make the next one even faster.

---

---
**Graceful degradation**
---

**No connectors at all:** Skip Step 2 entirely. Use the full guided interview in Step 4. Let the Champion know this upfront so they're not surprised.

**Partial connectors:** Use what's available, note what you couldn't reach, and fill gaps with targeted questions. Even one source (e.g., just Teams) can dramatically reduce the number of questions needed.

**Template not found:** If `assets/FIR_Template.pptx` is missing, ask the Champion for the path to their copy. If they don't have one, note that it should be available from the AI Champions Program resources.

The goal is always a complete, usable FIR — never leave the Champion with an empty document just because a connector failed.

---

---
**Quality bar for the output**
---

A good FIR has:

- At least one specific, named win in Section 3 (not just "AI is going well")
- At least one named person or team in Section 2 (not just "some teams are using it")
- A direct, honest assessment in Section 4 — if there are no blockers, that's notable; if there are, the FIR is the right place to surface them
- Specific asks in Section 6 — "I need you to help me get Legal to respond to the acceptable use question that's been open since May" is infinitely more useful than "continue to support me"

If any section is too vague, push back before generating the PPTX. One good round of clarification is worth it.
