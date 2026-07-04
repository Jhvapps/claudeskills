# Pillar 1: Technical Infrastructure

The boring part. It's the easiest pillar to get right because it's just a recipe — but skip a step and everything breaks. Do NOT cut costs or use "alternative" tools here.

## How email actually flows (why it matters)

Three linked reputation-scored items, most→least important:
1. **IP address / server** — the ESP (Google/Microsoft) manages this. Use Google mailboxes → Google keeps the IP clean. This is why we avoid cheap unmanaged-IP SMTP services.
2. **Domain** — reputation + age. If a domain hits a blacklist, ALL its mailboxes die. This is why the primary domain is sacred and never used for cold email.
3. **Mailbox** — individual reputation. One burned mailbox doesn't kill the domain.

The recipient's ESP screens inbound on: DNS records (is it spoofed?), copy (spam words), and reputation of IP/domain/mailbox.

## Buying domains

- Buy **separate lookalike .com domains**, not your primary. (e.g. primary otterpr.com → send from getotterpr.com, otterpr-hq.com.)
- Use **Spaceship** (cheap, bulk "beast mode", ~$8–10/yr flat). Avoid GoDaddy — renewal prices 2–3×.
- Only .com (trust + cheap). Use prefix/suffix hacks to find available names in bulk.
- Set a **URL redirect** from each cold domain → your real website (301 permanent). Propagation can take minutes to hours.
- Cloudflare nameserver migration is optional and unproven for results — skip it, keep DNS on Spaceship.

## DNS records (required before first send)

Set all of these per domain or you land in spam:
- **MX records** (Google's, priority-ordered) — enables the Google mailbox.
- **SPF** (TXT, `@`) — authorizes sending servers.
- **DKIM** (TXT) — generated inside Google Workspace admin (search "DKIM" → generate → add record → start auth).
- **DMARC** (TXT, `_dmarc`) — policy `quarantine` or `reject`; set failure reporting to 0 to avoid report spam. For cold email the nuance doesn't matter much; for primary domains it does.
- **Custom tracking domain** (CNAME) — standard practice even though we don't track. Prevents the sending tool's default link showing up as an obvious cold-email tell if you ever add an unsubscribe/link.

Verify with **easydmarc.com** (free domain scanner) or **MX Toolbox**. "Risk assessment medium" with `p=reject` valid is fine.

## Google vs Microsoft vs SMTP

- **Google (recommended):** ~87% inbox placement, best deliverability even TO Microsoft. Use a reseller/setup service for ~$3/mo vs $8.40 retail.
- **Microsoft 365:** ~75% placement. Does NOT deliver better to Microsoft inboxes. Good as a diversification provider at scale. Enterprise leads skew Microsoft.
- **Unmanaged-IP SMTP** (Inframail, Mailreef, ~$1/mailbox or unlimited/$99): YOU own the single IP's reputation. Burns catastrophically and permanently. Only for experienced senders as a secondary provider — never your only system.
- **Managed-IP SMTP** (Mission Inbox, Maildoso, ~$5/mailbox): they rotate IPs, but deliverability still trails Google. Usually not worth the premium.

**Provider matching** ("send from Microsoft to reach Microsoft") does NOT work — Google beats Microsoft to Microsoft. Leave it off.

## Mailbox setup

- **5 mailboxes per domain.** Keep to ≤100 sends/day/domain → ~20 sends/day/mailbox.
- **Sender name:** founder's real name, or an easy one-syllable trustworthy name (Ruth, Jen). No one verifies it's real.
- Add a signature at the **account level** (use the signature placeholder in campaigns, don't paste per-campaign).
- **Slow ramp ON**, min wait 5 min between sends.
- **Daily inbox placement tests ON.**

## Warm-up settings

- Warm-up **always on, indefinitely** — it's your defense against spam complaints (dilutes your spam rate).
- Ramp **+1–2/day** until warm-up volume = daily campaign limit.
- Reply rate 30–95% all work.
- Enable advanced human-emulation settings (weekends, read emulation, warm custom tracking domain).
- Bad/cheap warm-up pools can HURT you (low-rep mailboxes taint the pool). The sending tool's built-in warm-up (e.g. Instantly) is good enough for cold domains. Use a premium tool (Warmy.io) only for your sacred primary domain.

## Shortcut

A setup service (e.g. leadgenj.com/inbox and others) will buy domains, set all DNS, warm mailboxes, and give you a human to fix issues — for ~$3/mo/mailbox. Worth it: DNS misconfiguration is the #1 place people break their system.
