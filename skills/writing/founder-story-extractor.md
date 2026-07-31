---
name: Founder Story Extractor
description: Extracts a specific, narrative-ready story from a founder's raw account of an event, decision, or lesson.
version: 0.1.0
author: replynodes
license: MIT
category: writing
platforms: [agnostic]
agent_compatibility: [agent-agnostic]
tags: [storytelling, founder-content, narrative]
---

# Founder Story Extractor

## Purpose

Takes a founder's raw, unstructured account of an event (a mistake, a
decision, a turning point) and extracts the narrative elements — stakes,
turning point, specific detail, lesson — needed to turn it into content,
without inventing details that weren't given.

## When to use

- Turning a founder interview, voice note transcript, or rambling account into usable story content
- Product launches or milestones that benefit from a "why this matters to us" narrative — see [Product Launch Content Planner](../content-strategy/product-launch-content-planner.md)
- When existing founder content reads as generic ("we're passionate about X") instead of specific

## Inputs

| Input | Required | Description |
|---|---|---|
| `raw_account` | Yes | Unstructured transcript, notes, or interview text |
| `intended_use` | No | What the story will support (launch, brand story, specific post) |

## Instructions

1. Identify the concrete event at the center of the account — a specific
   moment, not a general theme. If the raw account only contains general
   themes with no specific event, say so rather than inventing one.
2. Extract: the stakes (what was at risk or uncertain), the turning point
   (the specific decision or realization), and one vivid, concrete detail
   (a number, a quote, a physical detail) that makes the story feel real
   rather than generic.
3. Identify the lesson or takeaway as the founder themselves framed it —
   don't substitute a more "marketable" lesson if it's not what they said.
4. Note anything in the raw account that reads as sensitive (financial
   specifics, other people's names, legal exposure) and flag it for the
   founder to confirm before it's used publicly.
5. Output the extracted structure, not a finished post — this skill feeds a
   writing skill, it doesn't write the final piece itself.

## Output format

```markdown
## Story extract: [short label]

**Event:** [specific, concrete]
**Stakes:** [what was at risk/uncertain]
**Turning point:** [the specific decision or realization]
**Concrete detail:** [number, quote, or physical detail]
**Lesson (as stated):** [in the founder's own framing]
**Flag for confirmation:** [sensitive details, if any]
```

## Examples

**Input:** Raw transcript: founder rambling about almost running out of runway before a key renewal, mentions a specific number ("we had six weeks of cash left"), and that they almost didn't send a renewal email out of embarrassment.

**Output:**

```markdown
## Story extract: The renewal email

**Event:** Nearly skipped sending a customer renewal email out of embarrassment about company state
**Stakes:** Six weeks of runway left; this renewal was material to survival
**Turning point:** Sent the email anyway despite the instinct to avoid it
**Concrete detail:** "Six weeks of cash left" — specific and verifiable-sounding
**Lesson (as stated):** The founder said the lesson was "the outcome you're avoiding is usually less bad than avoiding it"
**Flag for confirmation:** Confirm the six-week figure is OK to state publicly before using it in content
```

## Safety and quality checks

- Never invent stakes, details, or a lesson not present in the raw account
  — mark missing elements as such instead of filling gaps.
- Always flag financially or legally sensitive specifics for confirmation
  before they're used in a public-facing draft.
- This skill extracts narrative structure; it makes no claim about how the
  resulting content will perform.

## Related skills

- [`product-launch-content-planner`](../content-strategy/product-launch-content-planner.md) — often the destination for extracted stories
- [`linkedin-thought-leadership-writer`](linkedin-thought-leadership-writer.md) — turns a story extract into a finished post
