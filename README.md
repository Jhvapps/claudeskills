# Jack's Claude Skills

Personal Claude Code skills repo. Each folder under `skills/` is a skill with a `SKILL.md` that tells Claude when and how to use it.

## 🤖 Instructions for Claude

**Before answering Jack's request, scan this index and decide whether any skill applies.**

1. Read the **Skill Index** below — match keywords, intent, and verbs in Jack's message to a skill's description.
2. If a skill matches, open `skills/<name>/SKILL.md` in this repo for the full contract and follow it.
3. Prefer invoking a skill over free-form reasoning when the domain fits (shipping code, QA, design, planning, security).
4. If multiple skills could apply, pick the most specific one. If none fit, proceed normally.
5. Skills named `plan-*` run **before** implementation; skills named after a verb (`ship`, `qa`, `review`) run **during or after**.

## 📚 Skill Index

### Planning & Strategy

- **[autoplan](skills/autoplan/SKILL.md)** — Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles.
- **[plan-ceo-review](skills/plan-ceo-review/SKILL.md)** — CEO/founder-mode plan review.
- **[plan-design-review](skills/plan-design-review/SKILL.md)** — Designer's eye plan review — interactive, like CEO and Eng review.
- **[plan-devex-review](skills/plan-devex-review/SKILL.md)** — Interactive developer experience plan review.
- **[plan-eng-review](skills/plan-eng-review/SKILL.md)** — Eng manager-mode plan review.
- **[plan-tune](skills/plan-tune/SKILL.md)** — Self-tuning question sensitivity + developer psychographic for gstack (v1: observational).
- **[office-hours](skills/office-hours/SKILL.md)** — YC Office Hours — two modes.

### Shipping & Deploy

- **[ship](skills/ship/SKILL.md)** — Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR.
- **[land-and-deploy](skills/land-and-deploy/SKILL.md)** — Land and deploy workflow.
- **[setup-deploy](skills/setup-deploy/SKILL.md)** — Configure deployment settings for /land-and-deploy.
- **[document-release](skills/document-release/SKILL.md)** — Post-ship documentation update.
- **[retro](skills/retro/SKILL.md)** — Weekly engineering retrospective.
- **[review](skills/review/SKILL.md)** — Pre-landing PR review.

### QA & Testing

- **[qa](skills/qa/SKILL.md)** — Systematically QA test a web application and fix bugs found.
- **[qa-only](skills/qa-only/SKILL.md)** — Report-only QA testing.
- **[browse](skills/browse/SKILL.md)** — Fast headless browser for QA testing and site dogfooding.
- **[benchmark](skills/benchmark/SKILL.md)** — Performance regression detection using the browse daemon.
- **[canary](skills/canary/SKILL.md)** — Post-deploy canary monitoring.
- **[health](skills/health/SKILL.md)** — Code quality dashboard.
- **[investigate](skills/investigate/SKILL.md)** — Systematic debugging with root cause investigation.

### Design & UI

- **[design-consultation](skills/design-consultation/SKILL.md)** — Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates font+color preview pages.
- **[design-html](skills/design-html/SKILL.md)** — Design finalization: generates production-quality Pretext-native HTML/CSS.
- **[design-review](skills/design-review/SKILL.md)** — Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them.
- **[design-shotgun](skills/design-shotgun/SKILL.md)** — Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate.
- **[design-system](skills/design-system/SKILL.md)** — Extract a brand's design from any reference the user provides (site URL, screenshot, or existing assets) and generate a full design system reference page AND a 1-page A4 brand book PDF.
- **[cinematic-hero-builder](skills/cinematic-hero-builder/SKILL.md)** — End-to-end premium website builder — from business URL to cinematic $15k-looking site.
- **[marp-slides](skills/marp-slides/SKILL.md)** — Create beautiful MARP presentation decks with SVG charts, interactive elements, dashboard components, animations, dark/light themes.
- **[devex-review](skills/devex-review/SKILL.md)** — Live developer experience audit.

### Context & Memory

- **[context-save](skills/context-save/SKILL.md)** — Save working context.
- **[context-restore](skills/context-restore/SKILL.md)** — Restore working context saved earlier by /context-save.
- **[learn](skills/learn/SKILL.md)** — Manage project learnings.

### Safety & Guardrails

- **[careful](skills/careful/SKILL.md)** — Safety guardrails for destructive commands.
- **[freeze](skills/freeze/SKILL.md)** — Restrict file edits to a specific directory for the session.
- **[guard](skills/guard/SKILL.md)** — Full safety mode: destructive command warnings + directory-scoped edits.
- **[unfreeze](skills/unfreeze/SKILL.md)** — Clear the freeze boundary set by /freeze, allowing edits to all directories again.
- **[cso](skills/cso/SKILL.md)** — Chief Security Officer mode.

### Browser & Integrations

- **[open-gstack-browser](skills/open-gstack-browser/SKILL.md)** — Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in.
- **[connect-chrome](skills/connect-chrome/SKILL.md)** — Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in.
- **[setup-browser-cookies](skills/setup-browser-cookies/SKILL.md)** — Import cookies from your real Chromium browser into the headless browse session.
- **[pair-agent](skills/pair-agent/SKILL.md)** — Pair a remote AI agent with your browser.
- **[codex](skills/codex/SKILL.md)** — OpenAI Codex CLI wrapper — three modes.

### Setup & Admin

- **[gstack-upgrade](skills/gstack-upgrade/SKILL.md)** — Upgrade gstack to the latest version.

## 📦 Structure

```
claudeskills/
├── README.md              ← this file (the index Claude reads first)
└── skills/
    ├── <skill-name>/
    │   └── SKILL.md       ← full skill contract
    └── ...
```

## ➕ Adding a new skill

1. `mkdir skills/<your-skill>`
2. Create `skills/<your-skill>/SKILL.md` with YAML frontmatter (`name:`, `description:`) + body.
3. Add a one-line entry under the right category in this README.
4. Commit and push.

---

**Total skills: 42** — maintained by Jack ([@Jhvapps](https://github.com/Jhvapps)).