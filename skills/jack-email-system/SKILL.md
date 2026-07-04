---
name: "Jack Email System"
description: "Plan, write, and troubleshoot B2B cold email outreach the LeadGen Jay way. Use whenever building a cold email campaign, writing outreach copy or sequences, buying/setting up domains and mailboxes, building or cleaning lead lists, fixing spam/deliverability problems, scaling send volume, or reviewing why replies are low. Enforces the 3 Pillars (infrastructure, list, copy), the Triple Tap copy framework, and current deliverability rules."
---

# Jack Email System

Distilled operating manual for B2B cold email outreach. Use it before writing a single line of copy or buying a single domain. It stops the most common ways campaigns die.

## The Iron Rule

**Cold email works for ~4 of 10 offers on the first try. Every business can make it work within 60 days IF the 3 Pillars are solid. If a campaign is broken, diagnose bottom-up: Infrastructure → List → Copy. Never fix copy first.**

Fundamentals beat fancy AI every time. Do not reach for AI personalization, signals, or Clay until a plain control campaign is already working.

---

## The 3 Pillars (diagnose in this order)

A cold email castle stands on 3 pillars. One weak pillar collapses the whole thing.

1. **Technical Infrastructure** — do emails hit the inbox, not spam? (Easiest to get right: just follow the recipe. See `resources/infrastructure.md`.)
2. **List** — are you emailing the right, valid person? (Wrong person = spam complaints = dead domain. See `resources/list-building.md`.)
3. **Offer + Copy** — will they open, read, and reply? (Hardest. No universal template. See `resources/copywriting.md`.)

If nothing is landing: test infrastructure first, then list validity, THEN copy. Doing it backwards wastes days.

---

## Non-Negotiable Rules (2025+)

These are the settings/behaviours that keep you out of spam. Apply every time:

- **Never send cold email from your primary domain.** Buy separate lookalike .com domains. Primary is sacred.
- **Domains must age ≥30 days** (ideally 60–90) before sending. Warm mailboxes from day one.
- **Use Google (Google Workspace) mailboxes** via a reseller at ~$3/mo, not $8.40 retail. Google has highest inbox placement (~87%). Diversify providers only at scale.
- **5 mailboxes per domain, ~20–25 sends/day per mailbox** (≤100/day per domain). Lower is safer.
- **Warm-up always ON**, ramping +1/day to your daily limit. Warm-up counteracts spam complaints.
- **No links, no images, no tracking in email #1.** Text only. Open tracking OFF, click tracking OFF (they kill deliverability and are useless without links).
- **Mandatory spintax** on all copy to avoid repeat-phrase spam flags.
- **No unsubscribe links / opt-out language in email #1.** In extended sequences use soft language ("if I'm barking up the wrong tree, just say and I'll leave you be").
- **Never use mailbox auto-forwarding.** Reply from inside the sending tool's unibox — a reply from a different mailbox reads as a fresh cold email and gets rejected.
- **Only email "good"/valid addresses.** Verify every list. Bounces destroy reputation as fast as spam complaints. Verify catch-alls/riskies before sending.
- **Set up SPF + DKIM + DMARC** on every sending domain before the first send.

---

## Workflow: Launching a Campaign

1. **Pick the offer + audience.** Map the ICP. If unsure who converts, split-test 5–10 segments — cold email is the fastest audience-discovery tool. See `resources/offer.md`.
2. **Build + clean the list.** Apollo → scrape/verify → qualify. Verified emails only. See `resources/list-building.md`.
3. **Confirm infrastructure is healthy.** Domains aged, DNS records valid, mailboxes warmed to 100% health, "test domain setup" green. See `resources/infrastructure.md`.
4. **Write the sequence** using the Triple Tap. 3 emails max. Run copy through a spam-word checker + spintax. See `resources/copywriting.md`.
5. **Set up split tests** — one variable at a time (subject → body → CTA). Judge on **positive reply rate**, not raw reply rate. See `resources/copywriting.md`.
6. **Launch with slow ramp** + inbox placement tests + auto-pause automations.
7. **Reply fast (<10 min), from the unibox.** Speed to lead beats personalization. Move hot leads to your real CRM only once they take an action (book/opt-in). See `resources/managing-replies.md`.

---

## What "Good" Looks Like

Generic Apollo-data campaign, done right:
- Reply rate **1–2% = good, scalable.** Need matching positive-reply/opportunity rate (~1%).
- **>5% reply = high performer** — flag it, ask "what worked, how do I do more?"
- **<1% reply, <0.5% opportunity = low performer** — go back to the 3 Pillars.
- 10–20% reply rates ("instantly porn") are almost always tiny hyper-targeted signal lists — not what to expect at scale.

**Adjust expectations by target:** the more money a lead has (and the more cold email they get — agencies, doctors, funded startups), the lower the reply rate. Blue oceans = people with money who get few cold emails.

---

## Scaling (only after a control campaign works)

- Scale **horizontally** (more mailboxes), not by cranking sends/mailbox past 50/day.
- Equation: `emails to book 1 call (J) × calls wanted/day` → total daily sends → ÷25 per mailbox → mailboxes → ÷5 per domain → domains. Find your J number before scaling.
- Mature large-TAM system = 500–1,000 mailboxes ($1,500–3,000/mo). Cheap vs paid ads.
- Diversify providers as you scale (Google + Microsoft + managed SMTP) to hedge one going down.
- Staff: 1 person on lead flow (scrape/clean/load + testing), 1 person on the unibox (replies → calls).
- Recycle lists every 3–6 months, repositioned (new pain points/case studies), skipping prior interested + not-interested.

---

## Reference Files

- `resources/infrastructure.md` — domains, DNS (SPF/DKIM/DMARC), mailboxes, Google vs Microsoft vs SMTP, warm-up settings.
- `resources/list-building.md` — Apollo filters, the trusted-leads scrape hack, who responds, verification, signals.
- `resources/offer.md` — making a boring offer irresistible: loss leader, Trojan horse, lead magnets, reverse lead magnets.
- `resources/copywriting.md` — Triple Tap framework, subject/preview text, body, CTA, sequences, spintax, split testing.
- `resources/deliverability.md` — how to know if you're in spam, GlockApps testing, the recovery protocol, blacklists.
- `resources/managing-replies.md` — unibox workflow, speed to lead, soft-no replies, CRM handoff, hostile leads.
- `resources/tool-stack.md` — the full recommended tool stack + costs (<$100/mo to start).
- `resources/advanced.md` — Clay, AI personalization at scale, signal workflows, reply automation, omnichannel.

**Source:** LeadGen Jay (Jay Feldman) Cold Email Masterclass 2025.
