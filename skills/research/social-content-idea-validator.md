---
name: Social Content Idea Validator
description: Pressure-tests a content idea against audience relevance, specificity, and differentiation before time is spent writing it.
version: 0.1.0
author: replynodes
license: MIT
category: research
platforms: [agnostic]
agent_compatibility: [agent-agnostic]
tags: [validation, idea-screening, research]
---

# Social Content Idea Validator

## Purpose

Takes a raw content idea and evaluates it against a short set of criteria —
relevance, specificity, differentiation, and evidence — before it moves to a
[brief](../content-strategy/content-brief-generator.md) or gets written, to
catch weak ideas early.

## When to use

- Screening a batch of idea candidates down to the ones worth writing
- Before committing calendar slots to unvetted ideas
- When an idea "feels generic" but it's unclear why

## Inputs

| Input | Required | Description |
|---|---|---|
| `idea` | Yes | The content idea, as a sentence or short description |
| `audience_pain_points` | No | Output from [Audience Pain-Point Researcher](audience-pain-point-researcher.md), for relevance scoring |
| `existing_content` | No | Prior posts, to check for repetition |

## Instructions

1. Score the idea on four dimensions, each **pass / weak / fail**:
   - **Relevance** — connects to a known audience pain point or interest
   - **Specificity** — makes a concrete claim or shows a concrete example,
     not a generic statement anyone could make
   - **Differentiation** — says something not already said the same way in
     `existing_content` or common in the space
   - **Evidence** — the idea can be supported with a real example, data
     point, or experience, not asserted with nothing behind it
2. For any "weak" or "fail" score, give one specific suggestion to fix it
   (e.g. "narrow the claim," "add a real example," "check for duplication
   with post from March 3").
3. Give an overall verdict: **write it**, **revise first**, or **drop it** —
   drop only if 2+ dimensions fail and the suggested fixes don't resolve it.

## Output format

```markdown
## Idea validation: "[idea]"

| Dimension | Score | Note |
|---|---|---|
| Relevance | pass/weak/fail | ... |
| Specificity | pass/weak/fail | ... |
| Differentiation | pass/weak/fail | ... |
| Evidence | pass/weak/fail | ... |

**Verdict:** write it / revise first / drop it
**If revising:** [specific suggestion]
```

## Examples

**Input:** Idea: "5 tips for better productivity."

**Output:**

```markdown
## Idea validation: "5 tips for better productivity"

| Dimension | Score | Note |
|---|---|---|
| Relevance | weak | No specific audience pain point behind this — too general |
| Specificity | fail | "Better productivity" isn't a concrete claim |
| Differentiation | fail | This exact framing exists thousands of times already |
| Evidence | fail | No example or data referenced |

**Verdict:** drop it
**If revising:** Narrow to one specific, evidence-backed claim tied to a real pain point — e.g. "why calendar blocking made my meetings worse, not better" with a real before/after.
```

## Safety and quality checks

- Verdicts must be justified by the scored dimensions, not a gut call.
- Don't score "differentiation" as pass without a stated reason grounded in
  `existing_content` or explicit reasoning — avoid vague claims of novelty.
- This skill screens idea quality; it does not predict engagement or reach.

## Related skills

- [`audience-pain-point-researcher`](audience-pain-point-researcher.md) — supplies the relevance baseline
- [`content-brief-generator`](../content-strategy/content-brief-generator.md) — next step for ideas that pass
