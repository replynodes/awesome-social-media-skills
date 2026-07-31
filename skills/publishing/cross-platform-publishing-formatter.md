---
name: Cross-Platform Publishing Formatter
description: Takes approved content and formats it into a structured, platform-tagged publishing queue ready for a scheduling or publishing layer.
version: 0.1.0
author: replynodes
license: MIT
category: publishing
platforms: [x, linkedin, instagram, tiktok, youtube, threads, reddit, facebook, bluesky, mastodon]
agent_compatibility: [agent-agnostic, mcp-compatible]
tags: [publishing, scheduling, queue, mcp]
---

# Cross-Platform Publishing Formatter

## Purpose

Converts approved, platform-adapted content into a structured queue —
platform, post text, media references, and suggested timing — in a format
that's ready to hand to a scheduling or publishing layer, whether that's a
manual posting checklist or an MCP-based publishing tool.

## When to use

- After content has passed [Content Quality Reviewer](content-quality-reviewer.md)
- Batching a week or campaign's worth of approved posts into one queue
  before publishing or scheduling them

## Inputs

| Input | Required | Description |
|---|---|---|
| `approved_content` | Yes | One or more approved posts, with their target platform |
| `schedule` | No | Desired publish dates/times per post; if omitted, output is unscheduled |
| `media_references` | No | Links or file references to images/video attached to each post |

## Instructions

1. For each approved piece, produce a queue entry with: platform, final
   post text (unchanged from the approved draft — this skill formats and
   queues, it does not rewrite content), media references, and scheduled
   time if provided.
2. Validate platform-specific structural requirements are still met (e.g. a
   thread's individual post lengths, character limits) — flag anything that
   was approved but doesn't fit hard platform limits.
3. If multiple posts are scheduled for the same platform on the same day,
   flag potential timing conflicts rather than silently keeping them as-is.
4. Output the queue in a structured format (table or list) that a
   publishing tool — manual or MCP-based — can consume directly.
5. Do not invent a publishing time if none was provided; leave it marked
   "unscheduled" rather than guessing at optimal timing.

## Output format

```markdown
## Publishing queue: [batch label]

| Platform | Scheduled | Content | Media | Status |
|---|---|---|---|---|
| ... | ... | ... | ... | ready / needs review |
```

## Examples

**Input:** Two approved posts — an X thread and a LinkedIn post — both for the same campaign, LinkedIn scheduled, X not yet scheduled.

**Output:**

```markdown
## Publishing queue: Pricing tier campaign

| Platform | Scheduled | Content | Media | Status |
|---|---|---|---|---|
| LinkedIn | Mar 5, 9:00am | "We cut 5 pricing tiers to 2..." (approved) | None | ready |
| X | unscheduled | "1/ We cut 5 pricing tiers to 2..." (approved, 3-post thread) | None | needs review — no schedule set |
```

## Safety and quality checks

- Never alter approved post text while formatting — formatting changes only
  (structure, metadata), not content changes.
- Flag, don't silently fix, anything that violates a hard platform
  constraint (character limits, media requirements).
- This skill prepares a queue; it does not itself publish — actual
  publishing requires a scheduling tool or MCP-compatible publishing layer.
  See [Publish with ReplyNodes](../../README.md#publish-with-replynodes) for
  one optional example of that layer.

## Related skills

- [`content-quality-reviewer`](content-quality-reviewer.md) — approval step that precedes queuing
- [`multi-platform-content-adapter`](../repurposing/multi-platform-content-adapter.md) — produces the platform-specific content this skill queues
