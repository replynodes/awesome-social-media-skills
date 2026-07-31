---
name: LinkedIn Thought-Leadership Writer
description: Writes a LinkedIn post from a brief, in a specific voice, following LinkedIn-native structure and length conventions.
version: 0.1.0
author: replynodes
license: MIT
category: writing
platforms: [linkedin]
agent_compatibility: [agent-agnostic, claude-code-compatible]
tags: [linkedin, writing, thought-leadership]
---

# LinkedIn Thought-Leadership Writer

## Purpose

Converts a [content brief](../content-strategy/content-brief-generator.md)
and voice profile into a finished LinkedIn post, using LinkedIn-native
structure: a hook that survives the "see more" cutoff, short paragraphs, and
a clear point.

## When to use

- Executing a brief specifically for LinkedIn
- Adapting an idea already written for another platform into LinkedIn-native form (pair with [Multi-Platform Content Adapter](../repurposing/multi-platform-content-adapter.md) for the reverse direction)

## Inputs

| Input | Required | Description |
|---|---|---|
| `brief` | Yes | Angle, key points, and intended reaction — see [Content Brief Generator](../content-strategy/content-brief-generator.md) |
| `voice_profile` | No | Output from [Brand Voice Extractor](../content-strategy/brand-voice-extractor.md) |
| `length_preference` | No | Short (under 900 characters) or long (1,300–2,000 characters) |

## Instructions

1. Write a hook as the first 1–2 lines — this is what shows before LinkedIn's
   "see more" cutoff (roughly the first 210 characters). It must work as a
   standalone reason to click "see more," not a generic opener.
2. Structure the body around the brief's key points, one idea per short
   paragraph (1–3 sentences). Avoid dense blocks of text.
3. Support the argument with the specific example or evidence from the
   brief — generic claims without a concrete anchor read as filler on this
   platform.
4. End with a clear closing line that matches the brief's intended reaction
   — a question only if the voice profile shows the source actually asks
   questions; otherwise a stated takeaway.
5. Do not add hashtags unless explicitly requested. Do not use engagement-
   bait phrasing ("agree?", "thoughts?" with nothing else).

## Output format

```text
[Hook — 1-2 lines, must work standalone]

[Body — short paragraphs, one idea each]

[Closing line]
```

Plain text, no markdown formatting (LinkedIn doesn't render it).

## Examples

**Input:** Brief on "why 'stay in touch' usually means no," direct/dry voice.

**Output:**

```text
"Stay in touch" is the most polite rejection in fundraising.

Most founders read it as a maybe. It's rarely a maybe.

Investors have a much cheaper way to say "keep me posted, I'm actually
interested": they ask a specific follow-up question, or they ask when your
next round update goes out. "Stay in touch" with nothing else attached is
usually the low-conflict way to end a meeting.

The tell isn't the phrase. It's what comes with it. Specific ask, real
maybe. Nothing else, soft no.

I've stopped chasing "stay in touch" replies and started reading the
specificity instead. Saved me a lot of follow-up emails that were never
going anywhere.
```

## Safety and quality checks

- Hook must not misrepresent what the post actually delivers (no bait-and-switch).
- No fabricated statistics or examples not present in the brief or source material.
- No engagement-manipulation patterns (fake vulnerability, "this will get me cancelled but," artificial controversy).
- No guarantee of reach, impressions, or engagement — this skill produces a draft, not a result.

## Related skills

- [`content-brief-generator`](../content-strategy/content-brief-generator.md) — supplies the input this skill executes
- [`x-thread-creator`](x-thread-creator.md) — equivalent skill for X
- [`content-quality-reviewer`](../publishing/content-quality-reviewer.md) — review step after drafting
