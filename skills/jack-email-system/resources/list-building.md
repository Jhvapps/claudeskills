# Pillar 2: List Building

The most underrated, most-screwed-up pillar. Everyone thinks they've got it dialed. Wrong person = spam complaint = dead domain. Relevance is everything.

## Core truth

Your leads don't know you, don't trust you, aren't looking for you. You're taking a **targeted guess** they have the pain now. You'll usually be wrong — that's fine. Build the list so the guess is as good as possible.

## Who to reach out to

- **Have a business already?** Export your customer list from CRM, enrich (company, industry, job title), feed to AI to define the ICP, then target lookalikes.
- **No business/data?** Write a detailed offer description (who you help, how, the mechanism). Feed to ChatGPT/Claude → get target-segment recommendations → test 5–10 segments.

## Who actually responds

- **Blue oceans** — people who get FEW cold emails. Easy-to-find "money" targets (agencies, doctors, lawyers, funded startups) get slammed → lower reply. Ignored industries (manufacturing, farming) reply more.
- **Decision makers** (owner/founder/CEO/C-suite) reply far more than mid-level (HR, developers). Mid-levels resist change and won't push it up. Always go C-suite.
- **Younger companies** — no entrenched vendors/tools.
- **Newly-hired execs** (e.g. new CMO) — brought in to drive change, will adopt new solutions.
- **Inverse rule:** more money the lead has → lower reply rate. Adjust expectations, don't guarantee reply rates blind.

## Where to find them

Ask first: **is my ICP on LinkedIn?** (Do they have a company profile + job title there?)
- **Yes (most B2B):** use a B2B database.
- **No** (restaurants, trades, local mom-and-pops): scrape **Google Maps** (Leadswift, or IGLeads for all-in-one).
- **Influencers/creators:** scrape social (IGLeads).
- **Unusual criteria** (e.g. "companies that support veterans"): lookalike scraping (Ocean.io).
- **Doctors, real estate, mobile numbers:** BookYourData.

## The Apollo scrape hack (cheapest bulk data)

Zoom Info = most accurate but $15k–25k/yr and no bulk export. **Apollo = best balance** and it's scrapable.
1. Sign up for a **free Apollo account.**
2. Build filters (below), copy the resulting **URL**.
3. Paste URL into **trustedleads.io** → they scrape + verify **10,000 leads for ~$50.**
4. Since you can't save exclusion lists this way, control a rotating parameter (scrape one state at a time) to avoid duplicates.

For automation: build your own Apollo scraper (Apify) + Million Verifier pipeline (see `advanced.md`).

## Apollo filters — always use

- **Email status = Verified** (unless a tiny TAM).
- **Job title** — stack decision-maker titles (founder, co-founder, CEO, CMO, COO, president). Apollo matches similar titles.
- **Location** — account HQ (usually United States).
- **Employees** — custom range (e.g. 3–100) to skip brand-new + enterprise.
- **Company keywords** (not just industry) — uses company description; industry alone gives garbage overlap. Shrinking the list is GOOD.

## Apollo filters — situational (good)

- **Technologies** — what software they run (source: BuiltWith, slightly delayed). Download Apollo's tech list, feed to AI ("find expensive B2B tools that signal they invest in X").
- **Job postings** — hiring for a role = they have that unsolved problem + budget. Delayed in Apollo; scrape LinkedIn jobs for fresher.

## Apollo filters — avoid (don't work)

- **Signal filters** (funding, growth, M&A, intent) — data too stale/inaccurate. Funding is also an abused signal. Use dedicated sources (Crunchbase for funding, Audience Lab for intent) if you must — see `advanced.md`.
- **Revenue** — private companies don't disclose; Apollo guesses. Use employee count as a proxy.

## Always double-check the list

After filtering, actually read the pulled companies. Wrong keyword pulls the wrong industry. Exclude keywords (e.g. `B2B`) and stack industries to refine until ~9/10 look like a real fit.

## Verification (never skip)

Even "verified" Apollo exports come out ~70–80% valid. Bounces kill reputation.
1. **Clean with Million Verifier** first (cheapest in bulk; buy bulk credits). Outputs: good / risky (catch-all + unknown) / bad.
2. **Email ONLY "good."**
3. **Risky ≈ 50% deliverable** and high-value — verify catch-alls/unknowns with **Findymail** (or Clay pipeline) before sending, especially with a small TAM. Don't just email risky raw.
4. Re-verify old lists — people change jobs; a 3-month-old "good" list rots. Keep a CRM clean with EverClean (Million Verifier's autopilot) or GHL's validate-on-entry.

**Never buy cheap lead lists** (LeadRocks etc.). Old/wrong data = mass bounces + spam reports = dead campaign. Wrong company name is the fastest way to get marked spam.

## Signals (advanced — see advanced.md)

A signal = recent, relevant event proving they have the pain NOW (job posting, funding, social engagement, award). Signal campaigns are what produce 5–20% reply rates. Requires accurate + timely data source + automation to push into the campaign. Do NOT start here — validate a control campaign first.
