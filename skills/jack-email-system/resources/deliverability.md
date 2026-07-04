# Deliverability & Recovery

Highest-value sub-skill in cold email — few people are good at it, businesses pay to fix spam problems. If lead gen isn't working, **always diagnose deliverability first**.

## Factors that affect deliverability

- Domain: DNS config, **age** (30-day minimum, older = safer, huge for Microsoft), reputation.
- Mailbox + IP reputation (the ESP/server).
- Blacklists (domain + IP — separate from reputation).
- **Copy** — spam words/phrases, links, images, code.
- **Spam complaints** — #1 killer. Nothing tanks you faster than being marked spam. Warm-up dilutes your complaint rate — that's its whole job.
- **Bounces** — hurt as fast as spam. Not just invalid emails: blocked content / bad reputation also bounce. Hard bounce (bad address/no domain) hurts; soft bounce (full mailbox/server down) doesn't.

## Are you in spam? (you can't see open rates)

Use **reply rate as a proxy** + **inbox placement tests**.
- **Health score = unreliable** (it's just warm-up emails, all green means nothing).
- **Inbox placement tests = gold standard** — real live sends to seed inboxes. Turn this ON in your sending tool; automate it daily.
- Watch for the "**this message seems dangerous**" flag — deliverability tests won't catch it. Log into a sending mailbox and send the real copy to yourself at several business/personal inboxes to check for the flag.

## Diagnosing a broken campaign (top → bottom)

1. **Check DNS config** — easydmarc.com / MX Toolbox domain scan. Missing SPF/DKIM/DMARC is the most common, easiest fix. If broken, pause all campaigns first.
2. **Blacklist check** — MX Toolbox blacklist tool on the domain. Spamhaus/SORBS/Spamcop are the ones that really hurt. IP blacklists rarely matter if you're on Google. On a blacklist → stop campaigns, warm only ~30 days, come off, don't restart until clear. (You land on blacklists mostly by hitting **spam traps** — landmine mailboxes — so audit your data source.)
3. **Domain age** — no tool tells you this. If <30 days, wait / use older domains.
4. **Copy** — the likely culprit if DNS + blacklists are clean. Do a real GlockApps test with the actual campaign copy.
5. **Reputation** — only fix is good warm-up + time. Monitor via **Google Postmaster** (the only place that shows if people mark you spam — add all sending domains via a TXT/CNAME record).

## GlockApps (the deep test)

Free plan = 2 spam tests/month; highest-quality inbox placement test.
1. Start a manual test (pick region, e.g. North America) → get an ID + seed mailbox list.
2. Send your real campaign copy from a real campaign mailbox to those seeds with the ID string in the subject.
3. Read the report:
   - **IP analytics** — Google IPs on a blocklist? Not your problem (Google rotates them).
   - **Domain blacklists** — these matter a lot.
   - **DKIM/DMARC** check.
   - **Spam filter reason** — e.g. "Google detected spam in keywords" tells you it's COPY. Fix copy → re-test.
   - **SpamAssassin score** — element-level check, not a placement verdict.
   - **Dig into destination:** 20% spam to Zoho/Proton = ignore. 20% spam that IS Google Workspace = emergency.

## The Recovery Protocol (works for almost any cause except copy)

1. **Remove ALL mailboxes on the affected domain from campaigns** for 2–4 weeks (4 for a blacklist).
2. **Warm-up only** — no cold sends. Tag them (e.g. `warming + date`) to track.
3. Watch health + inbox placement tests. Still bad after 60 days + copy changes + still blacklisted → leave warming but replace them.
4. Typical full recovery: **4–8 weeks.**

If it IS copy: just change the copy — problem solved, no cooldown needed.

## Automate it

In your sending tool, attach automations to inbox placement tests:
- Placement <50% (or your threshold, ~70–80%) → **pause sending 14–30 days**, warm up.
- On any blacklist → pause 30 days.
- Placement recovers >70% → **slow-ramp back** into the campaign.

This turns deliverability management into set-and-forget.

## Career note

Email deliverability is a blue-ocean, high-ticket offer on its own (deliverability agency/consultancy) — lots of demand, few experts.
