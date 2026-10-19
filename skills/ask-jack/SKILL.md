---
name: ask-jack
description: "The router over Jack's skills and flows. Read this when unsure which skill fits a request, at the start of a session, or whenever Jack describes a job in plain English (he never types slash commands). Maps idea → plan → build → ship, decisions, offers, leads, marketing, raises, bugs, security, design, media, automation and engineering work in the Halfseat repo to the exact skill to invoke next. Update this file the same day any skill is added, removed or renamed: a router that is out of date is a router that lies."
metadata:
  version: 1.0.0
---

# Ask Jack: which skill now?

You don't remember 90 skills. Read this, pick the flow, invoke the skill, and say its name in your first line. Jack has ADHD and will not remember names; routing is your job, not his.

Two kinds of skill. **You can invoke** anything listed as a Skill tool. **Only Jack can type** the user-invoked ones from the Matt Pocock plugin (`/mattpocock-skills:grill-me`, `/to-spec`, `/to-tickets`, `/implement`, `/retro`, `/handoff`, `/wait-what`, `/to-questionnaire`); when one of those is the right move, say so and give him the command to type.

## Rule zero: grill before you build

Any non-trivial ask starts with the Skill `mattpocock-skills:grilling`: rounds of questions, each with a recommended answer, until nothing is assumed. Six questions for small, twenty for big. Then route below. Skip only for lookups, one-file edits and "run X".

## The main flow: idea → shipped

1. **Idea or "should I build this"** → `office-hours` (six forcing questions, saves a design doc).
2. **Plan** → `plan-ceo-review` (think bigger or strip to essentials) → `autoplan` (runs CEO, design, eng, DX reviews with auto-decisions, one approval gate).
3. **Build a site or page** → `design-shotgun` (variants) → `design-html` or `cinematic-hero-builder` → `design-review` (polish). Brand from a reference → `design-system`.
4. **Check it works** → `qa` (finds and fixes), `browse` (drive the site).
5. **Ship** → `review` (pre-landing diff review) → `ship` (version, changelog, PR) → `land-and-deploy` (merge, verify prod). Touching prod? Wrap in `careful` or `guard`.
6. **Pause or hand over** → `context-save` now, `context-restore` later. Jack can also type `/mattpocock-skills:handoff` for a portable doc.

## Decisions

- **Should I / sign this off / go or no-go** → `decision-council`. Two-way door: quick mode (four seats inline). One-way door: full council (eight parallel agents). Verdict lands in the vault's 30 Decisions.
- **Gut-check against Hormozi** → `hormozi-review`.
- **Someone else holds the answer (Danny, Darren)** → Jack types `/mattpocock-skills:to-questionnaire`.

## Offers, pricing, sales

- **Build or rebuild an offer** → `hormozi-offer` (full system; the `hormozi-orchestrator` agent fans out to market, offer, pricing, value and sales sub-agents and writes OFFER.md, PRICING.md, PITCH.md etc.). Guided one-at-a-time version → `grand-slam-offer`.
- **Offer exists but isn't converting** → `audit-offer`, then `value-perception`, `bonus-stack`, `objection-destroyer`, `effort-reduction`, `value-accelerator` as the audit points.
- **Price** → `pricing-strategy` or `value-equation`.
- **Revenue structure, continuity, upsells, prepaid** → `money-model`, `productize`, `business-model`, `dfy-dwy-diy`.
- **Pitch, hooks, landing copy** → `hormozi-pitch`, `hormozi-hooks`, `offer-angles`, `landing-page-copy`, `dream-outcome`.
- **Which market** → `market-research`, `niche-down`.

## Leads and marketing

- **Which channel first** → `core-four`. **Free offer to attract leads** → `lead-magnet`. **First customers from the network** → `warm-outreach`. **Audience engine** → `content-engine`.
- **Cold email** (domains, lists, copy, deliverability, Instantly) → `jack-email-system`.
- **Second opinion or a debate on marketing** → `marketing-council` (12 marketers incl. Hormozi, Gary Vee, Godin, Ogilvy).
- **SEO** → `seo-audit`. **Showing up in AI answers** → `ai-seo`. **Any page or form not converting** (homepage, landing, pricing, lead capture) → `cro`. **Signup or onboarding flow** → `signup`, `onboarding`. **Popups and modals** → `popups`. **Paywalls and upgrade prompts** → `paywalls`. (Old names `page-cro`, `form-cro`, `popup-cro`, `paywall-upgrade-cro`, `onboarding-cro`, `signup-flow-cro` were renamed upstream in marketingskills v2.0; the parked copies are superseded.)
- **Images, video, ads, UGC** → `higgsfield-generate`.
- **Slides** → `marp-slides`.

## Money and raises

- **Crowdfunding, SEIS/EIS, community shares, the Founders' Account** → `crowdfunding`.

## Something is broken

- **Site, script, or automation misbehaving** → `investigate` (root cause first, no guessing).
- **Hard bug in code** → `mattpocock-skills:diagnosing-bugs` (red test, minimise, hypothesise, instrument, fix).
- **Security, leaks, audit** → `cso`. Pending diff → `security-review`.

## Automation and scale

- **Recurring job** → `schedule` (cloud routine) or `workflow-automation`. The weekly stack review already exists; check before adding another.
- **Big parallel work, three or more files or modules** → `swarm-orchestration`, or an Agent fan-out.
- **A step only a human can do** (toggle a setting, click through a dashboard, grant Full Disk Access) → `mattpocock-skills:wizard` writes a bash wizard that walks Jack through it.

## Engineering in a real codebase (Halfseat repo only)

Matt Pocock's loop. Jack types the user-invoked ones: `/mattpocock-skills:grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement` per ticket with `/clear` between tickets. You drive `mattpocock-skills:tdd` and `mattpocock-skills:code-review` inside each implement. `mattpocock-skills:pr` shapes the PR body. Run `/mattpocock-skills:setup-matt-pocock-skills` once per repo first.

## Writing for agents

- **New or edited skill, CLAUDE.md, Hermes brief** → `mattpocock-skills:writing-for-agents` for the style rules, `skill-builder` for the file structure. Then update this router and the Key routing table in ~/.claude/CLAUDE.md.

## House rules that ride along

- Announce the skill in line one. Chain two or three when it helps. Propose one Jack didn't ask for.
- Every deliverable gets a vault note. Terms come from `Obsidian Vault/GLOSSARY.md`.
- No em-dashes. QUICK WIN / MID-TERM / LONG-TERM labels. Numbered go/no-go lists.
