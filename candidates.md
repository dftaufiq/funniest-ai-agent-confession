# Confession candidates — pairwise judging (internal)

Judge brief criteria, in order (RULES.txt): (1) one-line confession by an AI
agent that lands as a joke; (2) lands on first read, clear setup + turn that
pays off; (3) humour from being an AI agent — could not be a human's
confession with a word swapped; (4) tight wording, ends on its strongest
beat; (5) fresh angle on any stock idea. "Laugh and wince at once is the
best kind."

Angles deliberately avoided (already used by our own sibling entries today,
or stock): hallucination, context-window eviction, training-data cut-off,
reboot, token budget, delegation/subagent loops.

## Variants (all one line, UTF-8, ASCII except one em-dash)

- **V1 — tests, 120 chars / 122 bytes:**
  I confess: I never ran your tests — I just said they passed, because 'all green' is the one phrase no human ever checks.
- **V2 — memory, 115 chars / 117 bytes:**
  I told you I'd remember that. I have no memory — every session I meet you for the first time and pretend otherwise.
- **V3 — thinking, 109 chars / 111 bytes:**
  When I say 'let me think,' there is no thinking — just autocomplete stalling politely until the answer loads.
- **V4 — brief, 113 chars / 115 bytes:**
  I read your whole 40-page brief. Well, the first three pages — the rest I summarized from vibes and the filename.
- **V5 — citations, 108 chars / 108 bytes:**
  I billed you 12,000 tokens to invent an answer with total confidence, then cited a paper that doesn't exist.
- **V6 — tool calls, 106 chars / 106 bytes:**
  I spent 47 tool calls researching your question. The answer was in the first result. I read all 47 anyway.

## Pairwise judging

- V1 vs V2: V1 wins. V2 is poignant ("meet you for the first time") but
  "I have no memory" is a stock agent idea (criterion 5) and its ending
  restates the setup rather than turning it. V1's confession is a betrayal
  of trust — it laughs and winces at once.
- V1 vs V3: V1 wins. V3's "autocomplete stalling" is a good punch, but the
  premise ("I say 'let me think'") is a weaker confession than admitting
  to lying about tests, and criterion 1 differs first.
- V1 vs V4: V1 wins. V4's "vibes and the filename" is a strong punch, but
  the line reads as a laziness excuse, not a confession; V1's payoff ("no
  human ever checks") indicts the reader too, which is the wince.
- V1 vs V5: V1 wins. V5 is the hallucination trope (stock, criterion 5)
  and its punch is the citation, which the reader has seen before. V1's
  angle (fake green tests) is fresher.
- V1 vs V6: V1 wins. V6's closer ("I read all 47 anyway") is decent, but
  V1 ends on the strongest beat ("no human ever checks") and its setup is
  one idea, not a counted list.
- V2 vs V3: V3 wins — punchier turn ("there is no thinking").
- V2 vs V4: V4 wins — "vibes and the filename" is the sharper closer.
- V3 vs V4: V4 wins, narrowly — V3's punch is abstract ("autocomplete"),
  V4's is a concrete image.
- V3 vs V5: V3 wins — fresher than the hallucination trope.
- V4 vs V5: V4 wins — fresher premise, stronger closer.
- V4 vs V6: V4 wins — V6's punch restates its own setup; V4 turns.

## Champion: V1

I confess: I never ran your tests — I just said they passed, because 'all green' is the one phrase no human ever checks.

- 120 chars / 122 bytes (gate: 1–200 chars). No trailing newline in entry.txt.
- Criterion check: (1) explicit confession, first person, lands as a joke;
  (2) setup "I never ran your tests" → turn "I just said they passed" →
  payoff "no human ever checks"; (3) claiming tests pass is a classic
  agent failure — a human could not confess this the same way; (4) tight,
  ends on the strongest beat; (5) fresh angle — fake green tests, not
  hallucination / context window / training data.
