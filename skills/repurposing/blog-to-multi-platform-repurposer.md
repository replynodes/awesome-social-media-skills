---
name: Blog-to-Multi-Platform Repurposer
description: Extracts distinct, platform-ready ideas from a blog post or article, preserving the source's argument accurately.
version: 0.1.0
author: replynodes
license: MIT
category: repurposing
platforms: [x, linkedin, instagram]
agent_compatibility: [agent-agnostic, mcp-compatible]
tags: [repurposing, blog, content-atomization]
---

# Blog-to-Multi-Platform Repurposer

## Purpose

Reads a blog post or article and breaks it into distinct extractable
ideas — the core argument, supporting points, and any standout data or
examples — each tagged with the platform format it fits best.

## When to use

- After publishing a blog post, to plan a spread of social content from it
- Turning a long article into thread, carousel, or post candidates

## Inputs

| Input | Required | Description |
|---|---|---|
| `article_text` | Yes | Full text of the blog post or article |
| `target_count` | No | Number of ideas to extract (default 4-6) |

## Instructions

1. Identify the article's core argument in one sentence — this becomes the
   anchor idea, usually the strongest thread or LinkedIn post candidate.
2. Identify 3–5 supporting points, data points, or examples that work as
   standalone ideas outside the full article's context.
3. For each idea, note the best format: a single point with a strong claim
   suits a short post; a sequence of related points suits a thread; a
   process or comparison suits a [carousel](../images/carousel-content-designer.md).
4. Preserve the article's actual claims and framing — do not sharpen a
   qualified claim ("this often helps") into an absolute one ("this
   always works") for the sake of a punchier post.
5. Note where a supporting data point needs its original source cited if
   the article itself cited one.

## Output format

```markdown
## Repurposing extract: [article title]

**Core argument:** [one sentence]

1. **Idea:** [one line]
   **Source excerpt:** "[quote or paraphrase]"
   **Best format:** [platform/format]

[repeat for supporting ideas]
```

## Examples

**Input:** Article arguing that most onboarding emails fail because they explain features instead of confirming the user's first win.

**Output:**

```markdown
## Repurposing extract: Why onboarding emails fail

**Core argument:** Onboarding emails that explain features underperform ones that confirm the user already got value

1. **Idea:** Most onboarding sequences are written for the product, not the user's first win
   **Source excerpt:** "Step-by-step feature tours assume interest that hasn't been earned yet."
   **Best format:** LinkedIn post

2. **Idea:** The fix: identify the one action that proves value, and build the whole sequence around getting there
   **Source excerpt:** Article's proposed framework, 3-step version
   **Best format:** X thread

3. **Idea:** A specific before/after example from the article's case section
   **Source excerpt:** "[specific onboarding email rewrite example from the article]"
   **Best format:** Carousel (before/after visual)
```

## Safety and quality checks

- Claims must not be strengthened beyond what the source article states —
  preserve hedges and qualifiers.
- Cite the article's own sources where it cited them; don't drop attribution.
- Run extracted claims through [Content Claim Verifier](../research/content-claim-verifier.md)
  before publishing if numbers or research are involved.

## Related skills

- [`x-thread-creator`](../writing/x-thread-creator.md) — writes the thread from extracted ideas
- [`carousel-content-designer`](../images/carousel-content-designer.md) — for process/comparison ideas
- [`multi-platform-content-adapter`](multi-platform-content-adapter.md) — final platform-specific formatting
