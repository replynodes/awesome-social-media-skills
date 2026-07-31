---
name: Audience Pain-Point Researcher
description: Synthesizes audience pain points from provided source material (forums, reviews, support tickets, interviews) into ranked, content-ready themes.
version: 0.1.0
author: replynodes
license: MIT
category: research
platforms: [agnostic]
agent_compatibility: [agent-agnostic]
tags: [audience-research, pain-points, discovery]
---

# Audience Pain-Point Researcher

## Purpose

Reads raw audience signal (forum threads, reviews, support tickets, survey
responses, interview notes) and produces a ranked list of pain points,
phrased in the audience's own language, ready to feed content strategy.

## When to use

- Before generating [content pillars](../content-strategy/content-pillar-generator.md) or topic ideas
- When content feels like it's guessing at what the audience cares about
- Periodically, to keep pillar and topic decisions grounded in current signal

Requires real source material as input — this skill does not invent pain
points from a general description of an audience.

## Inputs

| Input | Required | Description |
|---|---|---|
| `source_material` | Yes | Raw text: forum posts, reviews, tickets, interview transcripts, survey responses |
| `audience_description` | No | Who this material came from, for context |
| `existing_pain_points` | No | Previously identified pain points, to avoid duplicates and track new ones |

## Instructions

1. Read through all source material. Extract direct quotes or close
   paraphrases that express frustration, confusion, a workaround, or an
   unmet need — not general opinions or praise.
2. Group extracted items into distinct pain point themes. Merge near-
   duplicates; keep themes specific enough to be actionable (not "pricing is
   hard" but "unclear which plan tier includes X feature").
3. For each theme, count how many source items support it and note 1–2
   representative quotes.
4. Rank themes by frequency, then by how directly the content owner can
   address them (a pain point that content can actually help with ranks
   above one requiring a product change).
5. Flag any theme that appeared only once — include it but mark it as
   low-confidence rather than dropping it silently.

## Output format

```markdown
## Pain Points: [source/audience]

| Rank | Pain point | Frequency | Confidence | Representative quote |
|---|---|---|---|---|
| 1 | ... | ... | High/Medium/Low | "..." |
```

## Examples

**Input:** 40 support tickets and 15 review snippets for a scheduling tool.

**Output:**

```markdown
## Pain Points: Scheduling tool users

| Rank | Pain point | Frequency | Confidence | Representative quote |
|---|---|---|---|---|
| 1 | Can't tell which plan includes team calendars | 12 | High | "Had to email support just to find out if this was on the free plan" |
| 2 | Timezone display confusing when scheduling across regions | 9 | High | "I keep double-booking because it shows my time, not theirs" |
| 3 | No way to preview how a booking page looks before publishing | 3 | Medium | "Wish I could see it before sending the link out" |
| 4 | Import from another tool loses custom fields | 1 | Low | "Lost all my custom questions when I switched over" |
```

## Safety and quality checks

- Every pain point must trace back to actual source material — do not
  add general "common" pain points not present in the input.
- Quotes must be real excerpts or close paraphrases, not invented examples.
- This skill identifies pain points; it does not claim addressing them will
  produce specific engagement or business results.

## Related skills

- [`content-pillar-generator`](../content-strategy/content-pillar-generator.md) — consumes ranked pain points to shape pillars
- [`social-content-idea-validator`](social-content-idea-validator.md) — checks whether a specific idea addresses a real pain point
