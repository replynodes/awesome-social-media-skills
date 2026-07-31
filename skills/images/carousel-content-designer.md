---
name: Carousel Content Designer
description: Structures a topic into a slide-by-slide carousel outline for LinkedIn or Instagram, with per-slide text and visual notes.
version: 0.1.0
author: replynodes
license: MIT
category: images
platforms: [linkedin, instagram]
agent_compatibility: [agent-agnostic]
tags: [carousel, visual-content, image-generation-prompts]
---

# Carousel Content Designer

## Purpose

Breaks a topic or piece of long-form content into a slide-by-slide carousel
outline — one idea per slide, a cover slide that earns the swipe, and
per-slide visual direction — ready for a designer or image-generation
workflow to produce.

## When to use

- Turning a blog post or thread into carousel format — pair with [Blog-to-Multi-Platform Repurposer](../repurposing/blog-to-multi-platform-repurposer.md)
- Presenting a process, comparison, or list visually rather than as a single text post
- Before generating actual slide images, to lock the content structure first

## Inputs

| Input | Required | Description |
|---|---|---|
| `topic_or_source` | Yes | The topic, or source content to adapt |
| `platform` | Yes | LinkedIn (up to ~20 slides typical) or Instagram (up to 10 typical) |
| `slide_count_target` | No | Default: 6-10 slides |

## Instructions

1. Write the cover slide first: one line that states the value of swiping
   through, specific enough to not be generic ("5 tips" is weak; "the exact
   sequence that got our first 10 customers" is stronger).
2. Break the body into one idea per slide — each slide must stand alone if
   seen out of sequence, since carousels are often screenshotted individually.
3. Keep on-slide text short: a headline (under 8 words) plus, if needed, one
   supporting line. Anything longer belongs in a caption, not the slide.
4. Add a visual note per slide describing what should appear beyond text
   (a diagram, a before/after, a quote treatment, a plain background) —
   this skill outlines structure, it does not generate the images.
5. End with a closing slide that states the takeaway, not a generic
   "follow for more" unless that's an explicit part of the brief.

## Output format

```markdown
## Carousel: [topic] ([platform], [slide count] slides)

**Slide 1 (cover):** [headline] — [visual note]
**Slide 2:** [headline + supporting line] — [visual note]
...
**Slide n (close):** [takeaway] — [visual note]
```

## Examples

**Input:** Topic: how a founder validated a product idea before building it. Platform: LinkedIn, 7 slides.

**Output:**

```markdown
## Carousel: How we validated before building (LinkedIn, 7 slides)

**Slide 1 (cover):** The 3-week test that stopped us building the wrong product — [visual: bold text on plain background]
**Slide 2:** Step 1: List the assumption we were most scared was wrong — [visual: simple text list]
**Slide 3:** Step 2: Find 10 people who'd feel the pain today, not "someday" — [visual: icon-based, 10 dots]
**Slide 4:** Step 3: Ask them to pay before it existed — [visual: mock invoice graphic]
**Slide 5:** What we got wrong on the first attempt — [visual: before/after comparison]
**Slide 6:** What changed once real money was on the table — [visual: simple stat callout]
**Slide 7 (close):** Validation isn't a survey. It's someone paying before it exists. — [visual: bold closing statement]
```

## Safety and quality checks

- Every slide's claim must trace back to `topic_or_source` — no invented
  statistics or steps not present in the source.
- Slide text must fit stated length limits; flag any slide that doesn't fit
  instead of silently truncating meaning.
- This skill outlines carousel structure; it does not generate final images
  and makes no claim about resulting engagement.

## Related skills

- [`blog-to-multi-platform-repurposer`](../repurposing/blog-to-multi-platform-repurposer.md) — common source for carousel content
- [`multi-platform-content-adapter`](../repurposing/multi-platform-content-adapter.md) — adapts the same idea into text-only formats
- [`social-graphic-prompt-builder`](social-graphic-prompt-builder.md) — the single-graphic equivalent for one quote or stat instead of a sequence
