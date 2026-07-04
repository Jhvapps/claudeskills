# Jack's Claude Skills

Personal Claude Code skills repo. Each folder under `skills/` contains a `SKILL.md` that tells Claude when and how to use it.

## 🤖 Instructions for Claude

**Before answering Jack's request, scan this index and decide whether any skill applies.**

1. Read the **Skill Index** below — match Jack's intent to a skill's description.
2. **Marketing tasks** → always start with `/product-marketing-context` if the project doesn't already have `.claude/product-marketing-context.md`. All marketing skills read it first.
3. If a skill matches, open its `SKILL.md` and follow it.
4. If multiple skills apply, pick the most specific OR chain them (e.g. `/customer-research` → `/copywriting` → `/page-cro` → `/ab-test-setup`).
5. Skills named `plan-*` run **before** implementation; verb-named (`ship`, `qa`) run **during/after**.

## 🗺️ Marketing Tree

```
                  ┌─────────────────────────────────────┐
                  │  product-marketing-context (ROOT)   │
                  │  (read by all marketing skills)     │
                  └──────────────┬──────────────────────┘
                                 │
     ┌────────┬─────────┬────────┼────────┬─────────┬─────────┐
     │        │         │        │        │         │         │
  Strategy  SEO &    Content   Paid &   Growth &   Sales &    CRO
            Content  & Copy    Measure  Retention  GTM
```

Cross-references to keep in mind:
- `copywriting` ↔ `page-cro` ↔ `ab-test-setup` (copy + landing + test it)
- `revops` ↔ `sales-enablement` ↔ `cold-email` (the outbound stack)
- `seo-audit` ↔ `schema-markup` ↔ `ai-seo` (the SEO stack)
- `customer-research` → `copywriting`, `page-cro`, `competitor-alternatives`

## 📚 Skill Index

### 🎯 Marketing (tree-organised in `skills/marketing/`)

**Foundation:** 
- **[product-marketing-context](skills/marketing/product-marketing-context/SKILL.md)** — When the user wants to create or update their product marketing context document.

**Strategy**

- **[marketing-ideas](skills/marketing/strategy/marketing-ideas/SKILL.md)** — When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product.
- **[marketing-psychology](skills/marketing/strategy/marketing-psychology/SKILL.md)** — When the user wants to apply psychological principles, mental models, or behavioral science to marketing.
- **[customer-research](skills/marketing/strategy/customer-research/SKILL.md)** — When the user wants to conduct, analyze, or synthesize customer research.

**SEO & Content**

- **[seo-audit](skills/marketing/seo-content/seo-audit/SKILL.md)** — When the user wants to audit, review, or diagnose SEO issues on their site.
- **[ai-seo](skills/marketing/seo-content/ai-seo/SKILL.md)** — When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers.
- **[site-architecture](skills/marketing/seo-content/site-architecture/SKILL.md)** — When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking.
- **[programmatic-seo](skills/marketing/seo-content/programmatic-seo/SKILL.md)** — When the user wants to create SEO-driven pages at scale using templates and data.
- **[schema-markup](skills/marketing/seo-content/schema-markup/SKILL.md)** — When the user wants to add, fix, or optimize schema markup and structured data on their site.
- **[content-strategy](skills/marketing/seo-content/content-strategy/SKILL.md)** — When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover.
- **[aso-audit](skills/marketing/seo-content/aso-audit/SKILL.md)** — When the user wants to audit or optimize an App Store or Google Play listing.

**CRO (Conversion)**

- **[page-cro](skills/marketing/cro/page-cro/SKILL.md)** — When the user wants to optimize, improve, or increase conversions on any marketing page — including homepage, landing pages, pricing pages, feature pages, or blog posts.
- **[signup-flow-cro](skills/marketing/cro/signup-flow-cro/SKILL.md)** — When the user wants to optimize signup, registration, account creation, or trial activation flows.
- **[onboarding-cro](skills/marketing/cro/onboarding-cro/SKILL.md)** — When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value.
- **[form-cro](skills/marketing/cro/form-cro/SKILL.md)** — When the user wants to optimize any form that is NOT signup/registration — including lead capture forms, contact forms, demo request forms, application forms, survey forms, or c...
- **[popup-cro](skills/marketing/cro/popup-cro/SKILL.md)** — When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes.
- **[paywall-upgrade-cro](skills/marketing/cro/paywall-upgrade-cro/SKILL.md)** — When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates.

**Content & Copy**

- **[copywriting](skills/marketing/content-copy/copywriting/SKILL.md)** — When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages.
- **[copy-editing](skills/marketing/content-copy/copy-editing/SKILL.md)** — When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content.
- **[cold-email](skills/marketing/content-copy/cold-email/SKILL.md)** — Write B2B cold emails and follow-up sequences that get replies.
- **[jack-email-system](skills/jack-email-system/SKILL.md)** — Full cold-email outreach operating system (LeadGen Jay method): the 3 Pillars (infrastructure, list, copy), Triple Tap framework, deliverability recovery, tool stack, signals & automation. Use for the whole outreach machine — domains/mailboxes, list building, deliverability/spam fixes, scaling. Pairs with `cold-email` (which is just the copywriting).
- **[email-sequence](skills/marketing/content-copy/email-sequence/SKILL.md)** — When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program.
- **[social-content](skills/marketing/content-copy/social-content/SKILL.md)** — When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or other platforms.

**Paid & Measurement**

- **[paid-ads](skills/marketing/paid-measurement/paid-ads/SKILL.md)** — When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms.
- **[ad-creative](skills/marketing/paid-measurement/ad-creative/SKILL.md)** — When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertising platform.
- **[ab-test-setup](skills/marketing/paid-measurement/ab-test-setup/SKILL.md)** — When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program.
- **[analytics-tracking](skills/marketing/paid-measurement/analytics-tracking/SKILL.md)** — When the user wants to set up, improve, or audit analytics tracking and measurement.

**Growth & Retention**

- **[referral-program](skills/marketing/growth-retention/referral-program/SKILL.md)** — When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy.
- **[free-tool-strategy](skills/marketing/growth-retention/free-tool-strategy/SKILL.md)** — When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness.
- **[churn-prevention](skills/marketing/growth-retention/churn-prevention/SKILL.md)** — When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies.
- **[community-marketing](skills/marketing/growth-retention/community-marketing/SKILL.md)** — Build and leverage online communities to drive product growth and brand loyalty.
- **[lead-magnets](skills/marketing/growth-retention/lead-magnets/SKILL.md)** — When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation.

**Sales & GTM**

- **[revops](skills/marketing/sales-gtm/revops/SKILL.md)** — When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes.
- **[sales-enablement](skills/marketing/sales-gtm/sales-enablement/SKILL.md)** — When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts.
- **[launch-strategy](skills/marketing/sales-gtm/launch-strategy/SKILL.md)** — When the user wants to plan a product launch, feature announcement, or release strategy.
- **[pricing-strategy](skills/marketing/sales-gtm/pricing-strategy/SKILL.md)** — When the user wants help with pricing decisions, packaging, or monetization strategy.
- **[competitor-alternatives](skills/marketing/sales-gtm/competitor-alternatives/SKILL.md)** — When the user wants to create competitor comparison or alternative pages for SEO and sales enablement.
- **[competitor-profiling](skills/marketing/sales-gtm/competitor-profiling/SKILL.md)** — When the user wants to research, profile, or analyze competitors from their URLs.
- **[directory-submissions](skills/marketing/sales-gtm/directory-submissions/SKILL.md)** — When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks, domain rating, and discovery.

### Planning & Strategy

- **[autoplan](skills/autoplan/SKILL.md)** — Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles.
- **[plan-ceo-review](skills/plan-ceo-review/SKILL.md)** — CEO/founder-mode plan review.
- **[plan-design-review](skills/plan-design-review/SKILL.md)** — Designer's eye plan review — interactive, like CEO and Eng review.
- **[plan-devex-review](skills/plan-devex-review/SKILL.md)** — Interactive developer experience plan review.
- **[plan-eng-review](skills/plan-eng-review/SKILL.md)** — Eng manager-mode plan review.
- **[plan-tune](skills/plan-tune/SKILL.md)** — Self-tuning question sensitivity + developer psychographic for gstack (v1: observational).
- **[office-hours](skills/office-hours/SKILL.md)** — YC Office Hours — two modes.
- **[sparc-methodology](skills/sparc-methodology/SKILL.md)** — SPARC development workflow: Specification, Pseudocode, Architecture, Refinement, Completion.
- **[agent-goal-planner](skills/agent-goal-planner/SKILL.md)** — Agent skill for goal-planner - invoke with $agent-goal-planner

### Multi-Agent & Swarms

- **[hive-mind](skills/hive-mind/SKILL.md)** — Byzantine fault-tolerant consensus and distributed coordination.
- **[hive-mind-advanced](skills/hive-mind-advanced/SKILL.md)** — Advanced Hive Mind collective intelligence system for queen-led multi-agent coordination with consensus mechanisms and persistent memory
- **[swarm-orchestration](skills/swarm-orchestration/SKILL.md)** — Multi-agent swarm coordination for complex tasks.
- **[agent-coordination](skills/agent-coordination/SKILL.md)** — Agent spawning, lifecycle management, and coordination patterns.
- **[agent-queen-coordinator](skills/agent-queen-coordinator/SKILL.md)** — Agent skill for queen-coordinator - invoke with $agent-queen-coordinator
- **[agent-orchestrator-task](skills/agent-orchestrator-task/SKILL.md)** — Agent skill for orchestrator-task - invoke with $agent-orchestrator-task

### Automation & Workflows

- **[workflow-automation](skills/workflow-automation/SKILL.md)** — Workflow creation, execution, and template management.
- **[hooks-automation](skills/hooks-automation/SKILL.md)** — Automated coordination, formatting, and learning from Claude Code operations using intelligent hooks with MCP integration.
- **[skill-builder](skills/skill-builder/SKILL.md)** — Create new Claude Code Skills with proper YAML frontmatter, progressive disclosure structure, and complete directory organization.
- **[memory-management](skills/memory-management/SKILL.md)** — AgentDB memory system with HNSW vector search.

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

- **[design-consultation](skills/design-consultation/SKILL.md)** — Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates...
- **[design-html](skills/design-html/SKILL.md)** — Design finalization: generates production-quality Pretext-native HTML/CSS.
- **[design-review](skills/design-review/SKILL.md)** — Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them.
- **[design-shotgun](skills/design-shotgun/SKILL.md)** — Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate.
- **[design-system](skills/design-system/SKILL.md)** — Extract a brand's design from any reference the user provides (site URL, screenshot, or existing assets) and generate a full design system reference page AND a 1-page A4 brand b...
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
├── README.md
└── skills/
    ├── <gstack/ruflo/design skill>/     # flat — tech/planning/design
    │   └── SKILL.md
    └── marketing/                       # tree — mirrors the diagram
        ├── product-marketing-context/   # foundation (read first)
        ├── strategy/
        ├── seo-content/
        ├── cro/
        ├── content-copy/
        ├── paid-measurement/
        ├── growth-retention/
        └── sales-gtm/
```

Claude Code still discovers skills flat via symlinks at `~/.claude/skills/<name>` → the nested path in this repo. So `/cold-email`, `/page-cro`, etc. work the same as any other slash command.

## ➕ Adding a new skill

1. `mkdir skills/<category>/<your-skill>` (or `skills/<your-skill>` for non-marketing)
2. Create the `SKILL.md` with YAML frontmatter + body.
3. `ln -s /Users/mac/repos/claudeskills/skills/<path>/<your-skill> ~/.claude/skills/<your-skill>`
4. Add a line to this README under the right category.
5. Commit and push.

## 📦 Sources

- **gstack** — [garrytan/gstack](https://github.com/garrytan/gstack) — planning, shipping, QA, design tooling (MIT)
- **ruflo** — [ruvnet/ruflo](https://github.com/ruvnet/ruflo) — multi-agent/swarm skills
- **marketingskills** — [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) — full marketing suite
- **personal** — original skills authored here

---

**Total skills: 92** — maintained by Jack ([@Jhvapps](https://github.com/Jhvapps)).