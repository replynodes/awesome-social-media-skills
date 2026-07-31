---
name: YouTube-to-Social Repurposer
description: Extracts distinct, standalone content ideas from a YouTube video transcript, ready to adapt into platform-specific posts.
version: 0.1.0
author: replynodes
license: MIT
category: repurposing
platforms: [youtube, x, linkedin, instagram]
agent_compatibility: [agent-agnostic, mcp-compatible]
tags: [repurposing, youtube, video-to-text]
---

# YouTube-to-Social Repurposer

## Purpose

Reads a YouTube video's transcript and extracts a set of distinct,
self-contained ideas or moments — each one substantial enough to become its
own social post — rather than a single generic summary of the video.

## When to use

- After publishing a long-form video, to plan the week of social content from it
- Transcript is available (auto-generated captions or a script)

## Inputs

| Input | Required | Description |
|---|---|---|
| `transcript` | Yes | Full or near-full video transcript |
| `video_topic` | No | One-line description of the video, for context |
| `target_count` | No | Number of ideas to extract (default 5-7) |

## Instructions

1. Read the full transcript and mark moments that work as standalone ideas:
   a specific claim, a surprising number, a mini-story, a clear
   before/after, or a strong opinion — not general topic summaries.
2. For each moment, extract: a one-line idea statement, the supporting
   detail from the transcript (quote or close paraphrase), and which
   platform format it best suits (thread, single post, carousel, short-form
   video clip).
3. Discard moments that only make sense with the full video's context —
   each extracted idea must stand alone.
4. Avoid extracting near-duplicate ideas; if two moments make the same
   point, keep the stronger one.
5. Output as a numbered list, each ready to hand to a platform-specific
   writing skill.

## Output format

```markdown
## Repurposing extract: [video topic]

1. **Idea:** [one line]
   **Supporting detail:** "[quote or paraphrase from transcript]"
   **Best format:** [platform/format]

[repeat for target_count ideas]
```

## Examples

**Input:** Transcript of a 20-minute video about a company's pricing model change, including a moment where the founder says churn dropped 30% after simplifying from 5 tiers to 2.

**Output:**

```markdown
## Repurposing extract: Why we cut our pricing tiers

1. **Idea:** Cutting 5 pricing tiers to 2 dropped churn by 30%
   **Supporting detail:** "The moment we went from five tiers to two, churn dropped almost a third within the quarter."
   **Best format:** X thread (specific number as hook)

2. **Idea:** More pricing options didn't reduce cancellations — it created decision paralysis at signup
   **Supporting detail:** Founder describes support tickets asking "which tier is right for me" as the top pre-signup question
   **Best format:** LinkedIn post (business-reasoning angle)

3. **Idea:** The actual tier cut process took one internal debate everyone regretted delaying
   **Supporting detail:** Founder describes the internal resistance to simplifying before finally doing it
   **Best format:** Short-form video clip (uses existing video footage of this moment)
```

## Safety and quality checks

- Every extracted idea and detail must be traceable to the transcript —
  run output through [Content Claim Verifier](../research/content-claim-verifier.md)
  before publishing if any numbers are involved.
- Don't compress a nuanced claim into a stronger, simpler one than the
  source actually supports.
- No claim about how many posts "should" come from one video beyond what's
  actually extractable as standalone ideas.

## Related skills

- [`multi-platform-content-adapter`](multi-platform-content-adapter.md) — turns each extracted idea into final platform copy
- [`content-claim-verifier`](../research/content-claim-verifier.md) — verify extracted claims before publishing
- [`content-calendar-planner`](../content-strategy/content-calendar-planner.md) — schedule the extracted ideas
