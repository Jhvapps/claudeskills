# Verdict note template

File: `/Users/mac/Documents/Obsidian Vault/30 Decisions/YYYY-MM-DD <short-slug>.md`

Fill every bracket. Keep the whole note under 700 words. Tables for scores, bullets everywhere else. No em-dashes.

```markdown
---
type: decision
date: YYYY-MM-DD
business: [[<Business>/_overview|<Business>]]
verdict: SIGN OFF | SIGN OFF WITH CONDITIONS | DO NOT SIGN OFF | NOT ENOUGH INFO
mode: quick | full
tags: [decision, council, <business-slug>]
---

# <Decision in one line>

**Verdict: <VERDICT>**

## The decision
- Options: A <...> / B <...> / C <keep doing what I do now>
- Numbers used: revenue <...>, cash <...>, team <...>
- Limits: deadline <...>, Jack's hours <...>, budget <...>
- Success: <what, by when>
- Jack's lean going in: <option> because <why>
- Door: one-way | two-way

## Scores

| Seat (weight) | A | B | C | Kill risk |
|---|---|---|---|---|
| Strategy (x<w>) | <n> | <n> | <n> | <none / option + reason> |
| Offer & Money (x<w>) | | | | |
| Attention (x<w>) | | | | |
| Capital (x<w>) | | | | |
| Operations (x<w>) | | | | |
| People & Time (x<w>) | | | | |
| Product & Demand (x<w>) | | | | |
| Operator (x<w>) | | | | |
| **Weighted** | **<n>** | **<n>** | **<n>** | |

## The argument
- Biggest disagreement: <seat> vs <seat> on <what>. Resolution: <one line>.
- Second disagreement: <...>
- The losing seat was right about: <one line>

## Conditions (if any)
1. <checkable action> · owner <name> · by <date>
2. <...>
3. <...>

## What would change this verdict
- <one line>

## Next action (48 hours)
- <one line, one owner>

## Questions Jack still owes the council
- <seat>: <question>

*Seats are simulations of each advisor's public frameworks, not the people. No quotes are attributed.*
```

Then append to today's daily note under `## ✅ Decisions made today`:

```markdown
- **<Decision in one line>**: <VERDICT>. [[YYYY-MM-DD <short-slug>]]
```
