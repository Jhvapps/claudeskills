---
name: decision-council
description: "Run a business decision past a simulated council of advisor lenses (Bezos strategy, Hormozi offers and money, Gary Vee attention, Buffett capital, Wickman operations, Martell founder time, Paul Graham product, plus a hospitality floor operator) that score the options, argue the disagreements, and return a SIGN OFF / SIGN OFF WITH CONDITIONS / DO NOT SIGN OFF verdict written to the Obsidian vault. Use when Jack says 'council', 'sign off', 'sign this off', 'check this decision', 'should I', 'go or no-go', 'run it past the board', 'roast this', 'red team this', 'am I making a mistake', or describes a choice between options for any of his businesses. Quick mode for reversible calls, full council with parallel seat agents for one-way doors."
metadata:
  version: 1.0.0
---

# Decision Council

A board that argues, then signs off. Eight advisor lenses built from each person's public frameworks (not the people, never invented quotes) score Jack's options, fight over the disagreements, and the Chair (you) hands down a verdict. Every verdict is written to the vault so Jack can see later what he decided and why.

Read `references/seats.md` for the seat briefs and `references/verdict-template.md` for the output format before running.

## 1. Intake (one round of questions, max)

Pull context first, then ask only for what is still missing:

1. Read today's and yesterday's daily note (`/Users/mac/Documents/Obsidian Vault/01 Daily/`) and the business `_overview.md` under `10 Businesses/` if the decision names a business. Check memory for anything already decided.
2. The decision pack you need:
   - **Decision** in one line.
   - **Options**: two or three. "Keep doing what I do now" is always one of them.
   - **Numbers**: revenue, cash, team size for the business affected. Real numbers or "unknown", never guesses.
   - **Limits**: deadline, Jack's hours per week, budget.
   - **Success** looks like what, by when.
   - **Jack's lean** and why. The council tests the lean, it does not rubber-stamp it.
3. If more than two items are missing, ask for them in one message. If Jack says "just run it", run it and mark the gaps as NOT ENOUGH INFO in the verdict.

## 2. Classify the door

Ask the Bezos question first: is this a one-way door (hard to reverse: signing a lease, hiring, taking investment, launching a brand, raising prices for existing customers) or a two-way door (cheap to undo)?

- **Two-way door, or Jack says `--quick`:** quick council. Four seats (Strategy, Offer & Money, Capital, Operations), one round, no sub-agents. You play every seat inline.
- **One-way door, or Jack says `--full`:** full council. All eight seats as parallel sub-agents, two rounds.
- `--seats bezos,hormozi` seats only those named.

Auto-seat the **Operator** whenever the decision touches a venue, rota, menu, pricing on the floor, or a Coal & Co entity.

## 3. Run the council

**Full mode:** launch one Agent per seat in a single parallel fan-out. Give each the seat brief from `references/seats.md` verbatim plus the full decision pack. Each seat returns, in under 250 words:
- a score 1 to 10 for every option, one line of reasoning each
- `KILL RISK: yes/no` with the reason (could this option sink cash, the licence, the brand, or Jack's health?)
- its single strongest argument for its top option and against Jack's lean
- one question Jack must answer before signing

**Round 2 (full only):** find the two biggest disagreements between seats. Send each dissenting seat the other's argument and ask for a reply in under 120 words. If every seat agreed in round 1, appoint the Capital seat as devil's advocate for the leading option. Consensus that fast is a signal something was missed.

**Quick mode:** write the four seat takes yourself, same format, shorter.

## 4. Verdict

1. Weight each seat 1 to 3 by how much its pillar matters to this decision. Show the weights.
2. Weighted average per option. Highest wins on paper.
3. **Ruin-risk cap:** if any seat flagged KILL RISK on the winning option, the verdict cannot be SIGN OFF. It becomes SIGN OFF WITH CONDITIONS where condition one removes that risk, or DO NOT SIGN OFF.
4. Choose one: **SIGN OFF**, **SIGN OFF WITH CONDITIONS** (max three, each a checkable action with an owner and a date), **DO NOT SIGN OFF** (say what would change it), or **NOT ENOUGH INFO** (list the exact numbers needed).
5. Name the dissent. If a seat lost, say what it was right about.
6. Next action within 48 hours, one line.

## 5. Write it down

1. Write the note to `/Users/mac/Documents/Obsidian Vault/30 Decisions/YYYY-MM-DD <short-slug>.md` using `references/verdict-template.md`. Wikilink the business (`[[Need/_overview|Need]]` style). No em-dashes anywhere.
2. Append one line to today's daily note under `## ✅ Decisions made today`: `- **<decision>**: <VERDICT>. [[YYYY-MM-DD <short-slug>]]`.
3. Reply in chat in Jack's format: verdict in one line, the three numbered conditions or next steps, then the dissent in one bullet. Nothing else. The long version lives in the vault.

## Rules

- Lenses are simulations of public frameworks. Say so once in the note. Never quote a seat as if the real person said it.
- Jack's numbers go into the maths visibly so he can check them.
- Full council is eight to twelve agent runs. Do not run it for two-way doors; push back if Jack asks for `--full` on a reversible call.
- Hand off after the verdict when it fits: offer or pricing work to `/hormozi-offer` or `/grand-slam-offer`, a marketing argument to `/marketing-council`, a raise to `/crowdfunding`, an idea that is not yet a decision to `/office-hours`.
