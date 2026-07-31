---
name: Short-Form Video Hook Generator
description: Generates multiple opening-line candidates for a short-form video, built to survive the first 2-3 seconds of scroll attention.
version: 0.1.0
author: replynodes
license: MIT
category: video
platforms: [tiktok, instagram, youtube]
agent_compatibility: [agent-agnostic]
tags: [short-form-video, hooks, tiktok, reels, shorts]
---

# Short-Form Video Hook Generator

## Purpose

Produces a set of distinct hook options — the first spoken or on-screen line
of a short-form video — for a given topic, so a creator can choose or test
one instead of writing a single, unvalidated opener.

## When to use

- Planning a short-form video (TikTok, Reels, Shorts) before scripting the rest
- The existing hook is vague ("today I want to talk about...") and needs sharpening
- Pair with [Video Script Writer](video-script-writer.md) for the full script

## Inputs

| Input | Required | Description |
|---|---|---|
| `topic` | Yes | What the video is about |
| `key_point` | Yes | The one thing the viewer should walk away knowing |
| `format` | No | Talking-head, voiceover-over-b-roll, on-screen-text-only |

## Instructions

1. Generate 5–8 hook candidates using distinct patterns, not variations of
   the same sentence. Use a mix of these patterns: a specific claim or
   number, a direct question the viewer is already asking themselves, a
   visible contradiction ("everyone says X, but..."), a stakes statement
   ("if you're doing X, stop"), and an in-progress moment ("I just found out...").
2. Each hook must be sayable or readable in under 3 seconds (roughly 8-12
   words for spoken hooks).
3. Each hook must connect directly to `key_point` — reject hooks that are
   attention-grabbing but disconnected from what the video actually delivers.
4. Mark which hooks require an on-screen visual to land (e.g. showing
   something) versus which work as pure voiceover/text.
5. Do not use unverifiable superlatives ("the best," "nobody knows this")
   unless the claim is actually substantiated by the source material.

## Output format

```markdown
## Hooks: [topic]

1. "[hook]" — [pattern used] — [visual-dependent: yes/no]
2. ...
```

## Examples

**Input:** Topic: a common mistake in cold outreach emails. Key point: personalization templates often make emails feel less personal, not more.

**Output:**

```markdown
## Hooks: Cold outreach mistake

1. "Your 'personalized' cold email probably feels the least personal thing in their inbox." — contradiction — no
2. "I read 200 cold emails last month. The 'personalized' ones were the worst." — specific claim — no
3. "If your outreach template has a merge field, read this before you send the next one." — stakes — no
4. "Why does 'personalized' outreach feel so impersonal?" — direct question — no
5. "Just found the reason templated 'personalization' backfires — and it's not what you think." — in-progress moment — no
```

## Safety and quality checks

- No hook may promise a result the video doesn't deliver (bait-and-switch).
- No unverifiable superlatives or fabricated statistics.
- This skill produces hook candidates for a human or agent to select from —
  it doesn't claim any one hook will outperform others without testing.

## Related skills

- [`video-script-writer`](video-script-writer.md) — builds the full script around the chosen hook
- [`social-post-experiment-designer`](../analytics/social-post-experiment-designer.md) — for testing multiple hooks against each other
