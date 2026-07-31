---
name: Social Post Experiment Designer
description: Designs a structured A/B test for a content variable (hook, format, timing) with a clear hypothesis and success criteria.
version: 0.1.0
author: replynodes
license: MIT
category: analytics
platforms: [agnostic]
agent_compatibility: [agent-agnostic]
tags: [experimentation, ab-testing, analytics]
---

# Social Post Experiment Designer

## Purpose

Turns a vague instinct ("I wonder if shorter hooks do better") into a
structured experiment: one variable isolated, a clear hypothesis, and
defined success criteria — so results are interpretable instead of
anecdotal.

## When to use

- Testing a specific content variable (hook style, post length, format, posting time)
- After [Performance Insight Analyzer](performance-insight-analyzer.md) surfaces a pattern worth confirming deliberately

## Inputs

| Input | Required | Description |
|---|---|---|
| `variable_to_test` | Yes | The single thing being varied |
| `content_context` | Yes | The content/campaign this test runs within |
| `available_volume` | No | How many posts can realistically be dedicated to this test |

## Instructions

1. State the hypothesis as a specific, falsifiable claim (e.g. "hooks that
   open with a number get more replies than hooks that open with a
   question"), not a vague goal ("improve engagement").
2. Isolate exactly one variable. Everything else — topic, length,
   publishing time, platform — must stay constant across variants, or the
   result won't be attributable to the tested variable.
3. Define the success metric before running the test, and the minimum
   sample needed to draw a conclusion (e.g. "at least 6 posts per variant").
   If `available_volume` is too low to reach that minimum, say so rather
   than proceeding with an underpowered test.
4. Define variants precisely enough that someone else could reproduce them
   without guessing (not "make it punchier" — specify exactly what changes).
5. State in advance what result would confirm, reject, or be inconclusive
   for the hypothesis.

## Output format

```markdown
## Experiment: [variable_to_test]

**Hypothesis:** [specific, falsifiable]
**Variable isolated:** [what changes]
**Held constant:** [everything else]
**Variants:** [A, B, ...]
**Success metric:** [specific metric]
**Minimum sample:** [count per variant]
**Interpretation:** what confirms / rejects / is inconclusive
```

## Examples

**Input:** Variable: hook style (number-led vs. question-led) for LinkedIn posts.

**Output:**

```markdown
## Experiment: Hook style (number-led vs. question-led)

**Hypothesis:** Number-led hooks get a higher reply rate than question-led hooks on LinkedIn, for this account
**Variable isolated:** Opening line style only
**Held constant:** Topic, pillar, posting day/time, post length, author
**Variants:** A — hook opens with a specific number/stat; B — hook opens with a direct question
**Success metric:** Reply rate (replies / impressions)
**Minimum sample:** 6 posts per variant (12 total)
**Interpretation:** A result showing >20% relative difference in reply rate, sustained across the full sample, confirms or rejects the hypothesis; smaller or inconsistent differences are inconclusive given this sample size
```

## Safety and quality checks

- Reject test designs that vary more than one thing — flag them instead of
  proceeding, since results wouldn't be attributable.
- State sample size limitations honestly; don't imply statistical
  confidence a small sample can't support.
- No guarantee that any tested variant will outperform another — the point
  of the design is a fair test, not a predetermined outcome.

## Related skills

- [`performance-insight-analyzer`](performance-insight-analyzer.md) — surfaces patterns worth testing, and analyzes results after the test runs
- [`short-form-video-hook-generator`](../video/short-form-video-hook-generator.md) — a common source of variant candidates
