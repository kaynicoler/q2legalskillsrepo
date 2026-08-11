Q2 Legal · Skill Keeper export

Skill   : capture
Author  : —
LLM     : Claude
Model   : —
Version : v3
Exported: 8/11/2026, 5:09:40 PM

── Claude Import ─────────────────────────────────────────────────────────
To install as a Claude Cowork skill:
  1. Rename this .zip file to .skill
  2. Open Claude Cowork → Settings → Capabilities → Skills
  3. Click "Install skill" and select the .skill file

── Contents ──────────────────────────────────────────────────────────────
  SKILL.md         — agent instructions with YAML frontmatter
                     (references embedded inline for Claude runtime use)
  references/      — 3 reference file(s)
    · complexity_matching.md
    · voice_preservation.md
    · workspace_detection.md
  scripts/         — 3 script file(s)
    · complexity_estimator.py
    · dump_classifier.py
    · workspace_inventory.py
  manifest.json    — full structured export for re-import into Skill Keeper
