---
name: Video Script Writer
description: Writes a structured video script (short-form or YouTube long-form) from a hook, key point, and supporting material.
version: 0.1.0
author: replynodes
license: MIT
category: video
platforms: [tiktok, instagram, youtube]
agent_compatibility: [agent-agnostic]
tags: [video-script, youtube, short-form-video]
---

# Video Script Writer

## Purpose

Turns a chosen hook, key point, and supporting material into a full video
script with spoken lines, structural beats, and on-screen text/visual notes
— for either short-form (under 90 seconds) or YouTube long-form video.

## When to use

- After selecting a hook with [Short-Form Video Hook Generator](short-form-video-hook-generator.md)
- Scripting a YouTube video from an outline or set of talking points
- Converting written content (a blog post, a thread) into a spoken script — for the reverse direction (video to social posts) see [YouTube-to-Social Repurposer](../repurposing/youtube-to-social-repurposer.md)

## Inputs

| Input | Required | Description |
|---|---|---|
| `hook` | Yes | The opening line |
| `key_point` | Yes | What the viewer should know by the end |
| `supporting_material` | No | Facts, examples, or outline points to include |
| `length` | Yes | Short-form (under 90s) or long-form (target minutes) |

## Instructions

1. Open with the given hook verbatim — don't rewrite it.
2. For short-form: structure as hook → 1-2 supporting points → payoff/lesson
   → optional close, aiming for one clear idea only. For long-form: structure
   as hook → context/stakes → 2-4 main sections → summary/close, allowing
   more depth per section.
3. Write spoken lines in a natural, sayable register — short sentences,
   contractions, no written-for-reading phrasing.
4. Add bracketed notes for on-screen text or visual cues at points where
   they reinforce the spoken line (e.g. `[on-screen: the number "6 weeks"]`).
5. Do not pad length with restated points or generic intros/outros
   ("hey guys, welcome back") unless explicitly part of the format request.

## Output format

```markdown
## Script: [topic] ([length])

**[HOOK]**
[spoken line]
[visual note]

**[SECTION]**
[spoken lines with visual notes as needed]

**[CLOSE]**
[spoken line]
```

## Examples

**Input:** Hook: "I read 200 cold emails last month. The 'personalized' ones were the worst." Short-form, key point: templated personalization backfires because it's obviously templated.

**Output:**

```markdown
## Script: Cold outreach mistake (short-form, ~45s)

**[HOOK]**
I read 200 cold emails last month. The "personalized" ones were the worst.
[on-screen: "200 cold emails"]

**[POINT 1]**
Here's why: if the personalization is a mail-merge field — first name,
company name — the reader clocks it in half a second. It doesn't feel
personal. It feels automated with a fig leaf.

**[POINT 2]**
The emails that actually landed referenced something specific about what
the person had done or said recently. Not a template field — something a
human would have had to actually notice.
[on-screen: side-by-side text, templated vs. specific example]

**[CLOSE]**
So if your "personalization" is a variable, it's not personalization.
It's a mail merge with better manners.
```

## Safety and quality checks

- Hook must be used exactly as given, not altered.
- No claims or statistics beyond what's in `supporting_material`.
- No script may promise a viewer outcome ("this will change how you...")
  that the content doesn't substantively deliver.
- No guarantee of watch-through rate, views, or engagement.

## Related skills

- [`short-form-video-hook-generator`](short-form-video-hook-generator.md) — supplies the hook this skill scripts around
- [`youtube-to-social-repurposer`](../repurposing/youtube-to-social-repurposer.md) — the reverse direction, video to social posts
