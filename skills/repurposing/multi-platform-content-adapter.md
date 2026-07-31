---
name: Multi-Platform Content Adapter
description: Adapts one piece of content into platform-native versions for multiple platforms without simply copy-pasting the same text.
version: 0.1.0
author: replynodes
license: MIT
category: repurposing
platforms: [x, linkedin, instagram, tiktok, threads, reddit, facebook, bluesky, mastodon]
agent_compatibility: [agent-agnostic, mcp-compatible]
tags: [repurposing, cross-platform, adaptation]
---

# Multi-Platform Content Adapter

## Purpose

Takes one finished idea (a post, a script, an extracted idea) and produces
platform-native versions for each target platform — adjusting length,
structure, and tone conventions rather than posting identical text
everywhere.

## When to use

- An idea has been written for one platform and needs versions for others
- Publishing the same campaign message across multiple platforms — pairs
  with [Cross-Platform Publishing Formatter](../publishing/cross-platform-publishing-formatter.md)
  for the final formatting/queue step

## Inputs

| Input | Required | Description |
|---|---|---|
| `source_content` | Yes | The original piece, in any platform's format |
| `target_platforms` | Yes | List of platforms to adapt for |
| `voice_profile` | No | Output from [Brand Voice Extractor](../content-strategy/brand-voice-extractor.md) |

## Instructions

1. Identify the core idea in `source_content` independent of its original
   platform formatting.
2. For each target platform, apply that platform's conventions:
   - **X** — thread or single post under 280 chars/post, hook-first
   - **LinkedIn** — short paragraphs, hook must survive "see more" cutoff, no hashtags by default
   - **Instagram** — caption supports longer text but leads with a scroll-stopping first line; visual is primary, caption supports it
   - **Threads** — conversational, shorter than LinkedIn, more casual than X
   - **Reddit** — no marketing tone; value-first, community-specific norms must be respected, avoid promotional framing entirely
   - **Facebook** — conversational, works with slightly longer text than X
   - **Bluesky / Mastodon** — similar brevity to X; Mastodon audiences often dislike overtly promotional content, so lead with substance
3. Do not simply trim or pad the same sentence — restructure for how each
   platform's format actually gets read (skimmed vs. read top-to-bottom,
   single view vs. swipe/expand).
4. Flag any platform where the source idea doesn't adapt well (e.g. a
   heavily visual idea with no image asset, or a promotional idea for
   Reddit) instead of forcing a weak adaptation.

## Output format

```markdown
## Adapted: [source idea, one line]

### X
[adapted version]

### LinkedIn
[adapted version]

[one section per target platform]

**Flags:** [platforms where adaptation is weak or needs an asset]
```

## Examples

**Input:** Source: LinkedIn post about cutting pricing tiers from 5 to 2. Targets: X, Threads.

**Output:**

```markdown
## Adapted: Cutting pricing tiers from 5 to 2

### X
1/ We cut 5 pricing tiers to 2. Churn dropped 30% the same quarter.

2/ Turns out more options at signup wasn't helping anyone decide faster —
it was creating a support queue full of "which tier is right for me."

3/ Fewer choices, faster signup, less churn. The tier count was the
problem, not the pricing itself.

### Threads
We had 5 pricing tiers. Cut it to 2. Churn dropped 30% that quarter.

Most of our pre-signup support tickets were just "which tier do I need?"
Fewer options fixed that faster than any of our actual pricing debates did.

**Flags:** None — this idea adapts cleanly to both platforms.
```

## Safety and quality checks

- Core claims and numbers must stay identical across all adapted versions —
  no platform gets a stronger or weaker version of the same fact.
- Respect platform-specific norms, especially Reddit's anti-promotional
  culture — flag rather than force an adaptation that would read as spam there.
- No guarantee that adaptation improves engagement on any given platform.

## Related skills

- [`youtube-to-social-repurposer`](youtube-to-social-repurposer.md) — common source of ideas to adapt
- [`blog-to-multi-platform-repurposer`](blog-to-multi-platform-repurposer.md) — common source of ideas to adapt
- [`cross-platform-publishing-formatter`](../publishing/cross-platform-publishing-formatter.md) — final formatting before publishing/scheduling
