# Managing the System & Replies

Cold email is not set-and-forget. It's a machine that needs maintenance.

## Pre-launch checklist

- Health-check every mailbox + sequence; test DNS + deliverability.
- Mailboxes on **slow ramp, max ~20/day** to start; domains ≥30 days; 100% health.
- Spintax + personalization in place; copy passed spam-word check + deliverability test.
- Tag mailboxes, add the tag to the campaign (auto-pulls them in).
- Advanced deliverability settings ON: skip hostile prospects, skip/last unlikely-to-reply, block risky emails (leave "allow risky" unchecked).
- **App installed + positive-reply notifications ON** (or a custom automation).

## Speed to lead (the #1 job)

- **Reply within 5–10 min.** Replying within 30 min = ~60% higher chance of converting to a call.
- **Speed > personalization.** A fast canned response beats a slow perfect one.
- **Reply from the unibox** — never mailbox-forward. A reply from a different mailbox reads as a new cold email and gets rejected.
- Once they reply, it's a **warm** conversation — send links/images/videos freely.

## The unibox workflow

- **Others tab** catches replies from deleted leads or different addresses — check it, there's gold there (use "attach lead" to merge).
- Read every tag, including "**not interested**" — the AI mis-tags, and some are actually open.
- Use **macros/snippets** (`#` key) for fast canned replies; the tool learns which macro you use and starts suggesting.
- Set **reminders**: "if no reply in 1 week, follow up." Often takes 2–4 touches to hit them at the right time.

## Soft-no replies (money left on the table)

Someone who replied politely "not interested right now" took the time to engage — send one more: acknowledge, drop a case-study link, wish them well. They won't mark you spam after a courteous exchange, and you leave a door open. Build a **soft-no macro**.

## Fastest ways to blow a lead

- Replying too slow (they forgot they answered).
- Canned reply that ignores their specific question — answer the question first.
- **Info-dumping** — goal is to get them on a CALL, not to answer everything. Leave a curiosity gap.
- No clear next step — every reply needs a specific CTA + booking link.
- Not following up after no action.

## Hostile leads

Turn on "skip hostile prospects." When you get a "f off," hit **delete lead + add to block list**. Brush it off — it's easier than cold calling. Prep your team so a new hire isn't rattled.

## Cold → warm handoff (CRM)

- **Do NOT dump every interested reply into your main CRM.** They haven't proven intent.
- Keep the conversation in the unibox until they take an **action** (book a call, opt in on a form).
- On that action → automation adds them to your main CRM (GoHighLevel etc.) → nurture/reminder sequence.
- Add every won/booked lead + existing customers + competitors to a **block-list Google Sheet** the tool reads, so you never cold-email them.

## Block list

Two layers: the tool's built-in block list (from unibox actions/API) + a **public Google Sheet** of emails you manage (customers, vendors, competitors). Add AI block-list triggers (unsubscribe words, "f off" words) to auto-block.

## Adding/removing leads (cost control)

Sending tools charge per lead stored. When a campaign is 100% complete:
1. Filter to fully-contacted leads (not "not yet contacted").
2. **Download them + their statuses** into a master Google Sheet (keep for recycling).
3. **Delete** from the tool to free quota.
4. **Clone** the campaign for fresh A/B data + load new leads.
The unibox still catches replies from deleted leads (in the Others tab).

## Recycling lists (small TAM)

People forget you in 3 months. Re-email the same list every 3–6 months, **repositioned** (new pain points, new case studies) — they didn't reply the first time due to fit, trust, or timing; change the angle. Skip prior **interested** (handle as warm) and prior **not-interested**; target completed/no-reply.

## Team SOP at scale

- One person: lead flow — scrape/clean/load, run A/B tests, keep lists full.
- One person: the unibox — reply fast, convert to calls, manage the CRM pipeline. (Diffusion of responsibility kills shared uniboxes — assign ONE owner.)
- You: offers, new copy, picking winners.

## Code-red signals

- Reply rate plummets overnight → check last-7-days analytics.
- Big inbox-placement drop → pause campaigns, warm, change copy first, then wait.
- Reply buildup / lists running out → stop scaling until the team catches up.
