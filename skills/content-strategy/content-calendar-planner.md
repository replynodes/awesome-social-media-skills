---
name: Content Calendar Planner
description: Converts content pillars and a posting cadence into a scheduled, platform-aware content calendar.
version: 0.1.0
author: replynodes
license: MIT
category: content-strategy
platforms: [agnostic]
agent_compatibility: [agent-agnostic, mcp-compatible]
tags: [calendar, scheduling, planning]
---

# Content Calendar Planner

## Purpose

Takes content pillars, a posting cadence, and target platforms, and
produces a dated content calendar with topics, formats, and platforms
assigned — ready to hand to writing skills or a publishing queue.

## When to use

- After defining [content pillars](content-pillar-generator.md), before writing individual posts
- Planning a specific window (a week, a month, a launch period)
- Re-planning after a gap in posting to rebuild a consistent cadence

## Inputs

| Input | Required | Description |
|---|---|---|
| `pillars` | Yes | Output from [Content Pillar Generator](content-pillar-generator.md) or an equivalent list |
| `platforms` | Yes | Which platforms to plan for |
| `cadence` | Yes | Posts per week, per platform |
| `date_range` | Yes | Start and end date for this calendar |
| `key_dates` | No | Launches, events, or dates that need dedicated content |

## Instructions

1. Calculate total post slots for the date range from the cadence.
2. Distribute slots across pillars using the suggested mix from the pillar
   definitions, adjusting for any key dates that require off-pillar content.
3. For each slot, assign: date, platform, pillar, a specific topic (not a
   generic pillar restatement), and format (text, thread, video, carousel).
4. Avoid scheduling the same pillar or format on consecutive days for a
   single platform unless cadence requires it.
5. Flag any key date that doesn't yet have a specific topic assigned.
6. Output as a table, sorted by date.

## Output format

```markdown
## Content Calendar: [date range]

| Date | Platform | Pillar | Topic | Format |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

**Notes:** [key dates without an assigned topic, gaps, or conflicts to resolve]
```

## Examples

**Input:** 3 pillars, LinkedIn + X, 3 posts/week on LinkedIn and 5/week on X, 2-week range, one product launch date.

**Output:**

```markdown
## Content Calendar: Mar 3 – Mar 14

| Date | Platform | Pillar | Topic | Format |
|---|---|---|---|---|
| Mar 3 | LinkedIn | Pitch mechanics | The 3 places pitches lose attention | Text post |
| Mar 3 | X | Investor psychology | What "stay in touch" really means | Thread |
| Mar 4 | X | Case studies | Anonymized raise story, part 1 | Text post |
| Mar 5 | LinkedIn | Launch | New feature announcement | Text post |
...

**Notes:** Mar 5 launch post topic is placeholder — needs final feature copy before writing.
```

## Safety and quality checks

- Don't invent key dates or launch details not provided in inputs.
- Every slot must map to a real pillar — no "TBD" pillar assignments in the
  final calendar; flag gaps separately in Notes instead.
- This skill schedules topics, not guaranteed outcomes — no claims about
  optimal posting times or algorithm behavior beyond what's explicitly provided.

## Related skills

- [`content-pillar-generator`](content-pillar-generator.md) — provides the pillar mix this skill schedules
- [`content-brief-generator`](content-brief-generator.md) — expands a calendar slot into a writing brief
- [`cross-platform-publishing-formatter`](../publishing/cross-platform-publishing-formatter.md) — turns scheduled slots into publish-ready, platform-formatted posts
