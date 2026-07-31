---
name: Long-Form to Clips Planner
description: Identifies clip-worthy moments in a long-form video transcript, with timestamps, for an editor to cut into short-form video.
version: 0.1.0
author: replynodes
license: MIT
category: video
platforms: [tiktok, instagram, youtube]
agent_compatibility: [agent-agnostic]
tags: [video-repurposing, clips, long-form-video, timestamps]
---

# Long-Form to Clips Planner

## Purpose

Reads a timestamped long-form video transcript (a podcast, interview, or
YouTube video) and identifies specific moments worth cutting into
short-form clips — with in/out timestamps and a reason each moment works —
so an editor can cut directly instead of re-watching the full source.

## When to use

- After recording or publishing a long-form video or podcast episode
- Distinct from [YouTube-to-Social Repurposer](../repurposing/youtube-to-social-repurposer.md):
  that skill extracts *ideas* for text posts; this one extracts *video
  moments* with timestamps for an editor to physically cut

## Inputs

| Input | Required | Description |
|---|---|---|
| `timestamped_transcript` | Yes | Transcript with timestamps (auto-captions or manual) |
| `target_clip_count` | No | Number of clips to identify (default 4-6) |
| `target_clip_length` | No | Rough target length per clip (default 30-90s) |

## Instructions

1. Read the transcript and mark moments that work as a standalone clip: a
   complete thought with a beginning and end within the target length, a
   strong or surprising statement, a concrete story, or a clear
   demonstration — not a fragment that depends on earlier context to make
   sense.
2. For each candidate, note the exact in and out timestamps. The clip must
   be trimmable at those points without cutting off a sentence or losing
   the setup needed to understand the payoff.
3. Write one line explaining why the moment works as a clip (specific
   claim, emotional beat, concrete story, surprising number) — this is what
   an editor uses to judge if it's worth the cut.
4. Suggest a caption/hook line for each clip, separate from the spoken
   content, to accompany it when posted — pair with
   [Short-Form Video Hook Generator](short-form-video-hook-generator.md) if
   a stronger hook option set is needed.
5. Discard moments that only work with earlier context the clip wouldn't
   include — flag them as "needs setup" rather than silently dropping
   promising material.

## Output format

```markdown
## Clip candidates: [source video]

1. **[in timestamp] - [out timestamp]** (~[length])
   **Why it works:** [reason]
   **Suggested caption:** "[caption/hook]"

[repeat for target_clip_count]

**Needs setup (not standalone):** [list, if any, with timestamps]
```

## Examples

**Input:** Podcast transcript, timestamps included, a segment from 14:20-15:05 where the guest describes losing a major client and what they changed afterward.

**Output:**

```markdown
## Clip candidates: Founder podcast episode 12

1. **14:20 - 15:05** (~45s)
   **Why it works:** Complete story arc — specific loss, specific cause, specific change made. Stands alone without needing earlier context.
   **Suggested caption:** "We lost our biggest client over one Slack message. Here's what we changed."

**Needs setup (not standalone):** 22:10-22:40 — strong statement about pricing, but only makes sense after the pricing context established at 20:00; would need a longer clip or an on-screen caption bridging the gap.
```

## Safety and quality checks

- Timestamps must correspond to a complete thought — verify the in-point
  doesn't start mid-sentence and the out-point doesn't cut one off.
- Don't present a "needs setup" moment as standalone — flag it explicitly instead.
- No guarantee that identified clips will perform well once posted.

## Related skills

- [`short-form-video-hook-generator`](short-form-video-hook-generator.md) — generates stronger hook/caption options for a chosen clip
- [`youtube-to-social-repurposer`](../repurposing/youtube-to-social-repurposer.md) — the text-post equivalent of this extraction
