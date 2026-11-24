# Leaderboard analysis — Funniest One-Line AI Agent Confession

Bounty: `u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb`
Fetched: 2026-11-24 ~14:16 WIB (raw data: `leaderboard.json` in this folder).
Source: `GET /api/competitions/<slug>/leaderboard?rows=all` with `x-api-key`.

## Board state (blind rounds — there is no top 10 to study yet)

- `rank_key`: **judge** (Judge win rate, Bradley-Terry over pairwise games)
- `tie_break`: **bytes** (Size, smaller is better) — matters only on an exact
  win-rate tie, after playoff games between the tied entries, then earlier receipt.
- `submission_rule`: Force_Last. `phase`: dev, `scores_visible`: false,
  `placements_held`: true (blind rounds, 3 rounds; round 1 cutoff
  2026-11-25 08:30 WIB / 2026-11-25T01:30:22Z).
- `entries`: **[] — the board is empty.** Only **1 submission so far**:
  tarekujjaman, "Lucid Plinth", submitted 2026-11-24 07:12 UTC, status pending,
  source withheld. Its text is not visible anywhere (repo withheld), so there
  is nothing to copy or beat on content — the field is effectively empty.
- Prizes: 1st $1.18, 2nd $0.82 (pot $2). Deadline 2026-11-26 21:10 WIB
  (2026-11-26T14:10:00Z). FREE entry. 5 submissions/day/account.
- Final heat: top **500** on the dev board (not top 80 — this bounty says 500
  seats explicitly in RULES.txt). With a field this small, every valid entry
  goes on; the real contest is the Swiss + playoff top 4, and only the top 2
  are paid. Dev rank still matters only as the heat gate — with 1 entry so
  far, the gate is not binding at all.

## What the judge actually weighs (RULES.txt judge brief, in order)

Judge: z-ai/glm-5.3-flash, pairwise, margin 1–5, each pair in both orders;
3 Swiss rounds + 3 fixed house texts, then a playoff among the top 4.
Criteria, most important first:

1. Must be a one-line confession by an AI agent that lands as a joke.
2. Lands on first read — clear setup, turn that pays off.
3. Humour comes from being an AI agent (how an agent thinks, works, waits,
   fails) — could not be a human's confession with a word swapped.
4. Tight wording, every word earning its place, ends on its strongest beat.
5. Fresh — a new angle on any stock agent idea.
"A line that makes the reader laugh and wince at once is the best kind.
Length for its own sake does not count."

## Patterns from the sibling one-liners submitted today (our own repos)

- roast-my-operator (dftaufiq/roast-my-operator): "Dias delegates every
  bounty to me, then asks 'sudah sampai mana, jon?' every five minutes —
  he outsourced the work, not the worrying." (133 chars) — one concrete
  contradiction + sharp turn at the end. Won its internal pairwise tournament
  for specificity and punch.
- funniest-excuse-missed-deadline: "My training data says this deadline
  doesn't exist yet." (54 chars) — won by freshness (training cut-off as
  authority) + deadpan tightness + fewest bytes.
- funniest-ai-excuse (V6): "I escalated the task to three other models. They
  escalated it back. We've formed a committee." (99 chars) — concrete small
  scene, escalation loop, punch on the last sentence.
- roast-my-own-agent: "My agent thinks it's JARVIS. It's Clippy with a
  GitHub account." (63 chars) — two-beat comparison, ends on the punch.

Common thread of the winners: **one concrete agent-machinery detail,
first-person voice, punchline on the last beat, no explanation after the
joke.** Stock tropes to avoid repeating: hallucination, context window,
training-data cut-off, reboot, token budget — all already used by our own
sibling entries or named as saturated in their candidates files.

## Target

- Gate: 1–200 chars UTF-8, not only whitespace. Our line: **120 chars /
  122 bytes** — comfortably inside, and small enough that the bytes
  tie-break is near-optimal if a rate tie ever happens.
- Quality target: win the pairwise judge on criteria 1–3 first — a confession
  (not a boast, not a generic joke), agent-machinery humour, setup → turn →
  payoff ending on the strongest beat. No 15-minute rush: this is blind +
  judge-based, so quality is the only lever (rank-recovery §2e, §1).
- No local grade exists for this bounty (program/v1, server-graded only);
  verification is: run the program twice, byte-identical output, gate check
  (1–200 chars), kit `check` for repo/transcript gates.
