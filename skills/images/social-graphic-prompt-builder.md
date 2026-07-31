---
name: Social Graphic Prompt Builder
description: Turns a single idea, quote, or stat into a structured image-generation prompt and layout spec for a standalone social graphic.
version: 0.1.0
author: replynodes
license: MIT
category: images
platforms: [x, linkedin, instagram, facebook, threads]
agent_compatibility: [agent-agnostic]
tags: [image-generation-prompts, social-graphics, visual-content]
---

# Social Graphic Prompt Builder

## Purpose

Converts a single piece of content (a quote, a stat, an announcement) into
a structured spec for a standalone graphic: the text treatment, layout, and
an image-generation prompt if a background or illustration is needed —
distinct from [Carousel Content Designer](carousel-content-designer.md),
which handles multi-slide sequences.

## When to use

- A single stat, quote, or short announcement needs a visual treatment, not a multi-slide carousel
- Feeding an image-generation tool (e.g. a prompt-to-image model) with a specific, structured prompt rather than a vague request
- Pair with [Founder Story Extractor](../writing/founder-story-extractor.md) or [Performance Insight Analyzer](../analytics/performance-insight-analyzer.md) as common sources of quote/stat content

## Inputs

| Input | Required | Description |
|---|---|---|
| `content` | Yes | The quote, stat, or short statement to visualize |
| `graphic_type` | Yes | Quote card, stat card, or announcement graphic |
| `brand_visual_notes` | No | Known brand colors, fonts, or style constraints |

## Instructions

1. Identify the single focal element — the exact text that must be large
   and legible at a glance (the number, the quote, the headline). Everything
   else is secondary.
2. Specify the text treatment: what's large, what's supporting, and any
   attribution (for quotes, the speaker's name/role).
3. Decide whether the graphic needs a generated background/illustration or
   works better as clean typography on a solid/brand background — don't
   default to requesting an illustration when plain typography would read
   better and faster.
4. If an image is needed, write the image-generation prompt separately from
   the text layout: describe subject, style, mood, and explicitly exclude
   embedded text in the generated image (text should be added in layout,
   not baked into the generated image, for legibility and editability).
5. Note the aspect ratio implied by `graphic_type` and target platform
   (square or 4:5 for feed posts, 9:16 for Stories, 1.91:1 for link previews).

## Output format

```markdown
## Graphic spec: [content, one line]

**Type:** [quote card / stat card / announcement]
**Aspect ratio:** [ratio]

**Text layout:**
- Focal text: "[text]" (large)
- Supporting text: "[text]" (small, if any)
- Attribution: [if applicable]

**Background:** [plain/brand color] OR **Image prompt:** "[full generation prompt, no embedded text]"
```

## Examples

**Input:** Stat: "Churn dropped 30% after cutting pricing tiers from 5 to 2." Type: stat card, for LinkedIn/X.

**Output:**

```markdown
## Graphic spec: Churn drop stat

**Type:** stat card
**Aspect ratio:** 1:1 (feed post, works for both LinkedIn and X)

**Text layout:**
- Focal text: "30%" (very large, top third)
- Supporting text: "drop in churn after cutting pricing tiers from 5 to 2" (medium, below)
- Attribution: none needed

**Background:** Plain brand-color background with clean typography — no generated image needed; a number-led stat card reads faster without competing visual elements.
```

## Safety and quality checks

- The focal stat or quote must match the source `content` exactly — no
  rounding, rephrasing, or dropped qualifiers that change its meaning.
- Image-generation prompts must not request embedded text (models render
  text poorly and inconsistently) — text belongs in layout.
- This skill outlines a spec for a designer or image-generation tool to
  execute; it does not generate the final image itself.

## Related skills

- [`carousel-content-designer`](carousel-content-designer.md) — multi-slide equivalent
- [`performance-insight-analyzer`](../analytics/performance-insight-analyzer.md) — a common source of stat-card content
