Q2 Legal · Skill Keeper export

Skill   : inbox-setup
Author  : —
LLM     : Claude
Model   : —
Version : v2
Exported: 8/11/2026, 5:12:43 PM

── Claude Import ─────────────────────────────────────────────────────────
To install as a Claude Cowork skill:
  1. Rename this .zip file to .skill
  2. Open Claude Cowork → Settings → Capabilities → Skills
  3. Click "Install skill" and select the .skill file

── Contents ──────────────────────────────────────────────────────────────
  SKILL.md         — agent instructions with YAML frontmatter
                     (references embedded inline for Claude runtime use)
  references/      — 3 reference file(s)
    · grill_me_section_walk.md
    · kb_file_contract.md
    · voice_calibration.md
  scripts/         — 3 script file(s)
    · kb_validator.py
    · section_progress_tracker.py
    · voice_sample_analyzer.py
  manifest.json    — full structured export for re-import into Skill Keeper
