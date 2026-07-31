---
name: Brand Voice Extractor
description: Analyzes a sample of existing content and produces a reusable brand voice profile agents can apply to new writing.
version: 0.1.0
author: replynodes
license: MIT
category: content-strategy
platforms: [agnostic]
agent_compatibility: [agent-agnostic, claude-code-compatible]
tags: [brand-voice, tone, style-guide, consistency]
---

# Brand Voice Extractor

## Purpose

Reads a sample of existing content (posts, blog articles, transcripts) and
produces a structured brand voice profile — tone, vocabulary, sentence
patterns, and things to avoid — that other skills or writers can apply
consistently.

## When to use

- Before writing content for a brand or person for the first time
- When multiple people or agents are producing content and drift is showing
- When someone can describe their voice as "just sounds like us" but hasn't written it down

Not for: analyzing a single post (too little signal). Use at least 5–10
pieces of representative content.

## Inputs

| Input | Required | Description |
|---|---|---|
| `sample_content` | Yes | 5+ existing posts, articles, or transcripts from the brand/person |
| `audience_description` | No | Who the content is written for, if known |
| `explicit_dos_donts` | No | Any known style rules already in place (e.g. "never use emoji") |

## Instructions

1. Read all sample content. Note recurring word choices, sentence length,
   use of humor, first- vs. third-person, formality level, and how claims
   are qualified or hedged.
2. Identify 3–5 tone attributes using concrete adjective pairs (e.g. "direct,
   not blunt" / "confident, not hyped") rather than single vague words like
   "professional."
3. Extract 5–10 words or phrases the source uses repeatedly, and 5–10 words
   or patterns it visibly avoids (jargon, hype words, filler phrases).
4. Note structural patterns: typical opening line style, how CTAs are
   phrased (if at all), typical post length by platform if evident.
5. Write the profile in the output format below. Where the sample doesn't
   give enough evidence for a field, mark it "insufficient signal" rather
   than guessing.

## Output format

```markdown
## Brand Voice Profile: [Name]

**Tone:** [3-5 adjective pairs]
**Formality:** [scale or description]
**Person:** [first/second/third, singular/plural]

**Characteristic phrases:** [list]
**Avoid:** [list — words, phrases, patterns]

**Sentence pattern:** [typical length, structure]
**Opening style:** [how posts/pieces typically start]
**CTA style:** [how, if at all, the source asks for action]

**Example rewrite:** [one generic sentence, rewritten in this voice, to show the profile in action]
```

## Examples

**Input:** 8 LinkedIn posts from a solo B2B SaaS founder — short paragraphs,
no emoji, frequent use of specific numbers, occasional dry humor, never
uses "excited to announce."

**Output:**

```markdown
## Brand Voice Profile: [Founder]

**Tone:** direct, not blunt / confident, not hyped / dry, not sarcastic
**Formality:** casual-professional — contractions used, no slang
**Person:** first-person singular

**Characteristic phrases:** "here's what actually happened", "the numbers", "worth noting"
**Avoid:** "excited to announce", exclamation points, emoji, "game-changer"

**Sentence pattern:** short sentences, 1-2 sentence paragraphs, specific numbers over vague claims
**Opening style:** states the outcome or number first, context after
**CTA style:** rare — usually a direct question, not "let me know your thoughts"

**Example rewrite:** "We're excited to announce a big milestone!" → "We crossed 500 paying customers last week. Took 14 months."
```

## Safety and quality checks

- Base the profile only on the provided sample — don't infer a voice from
  the brand's industry or assumptions about its audience.
- Flag fields with insufficient signal instead of inventing detail.
- This skill describes tone; it makes no claims about how a voice performs
  in terms of engagement or growth.

## Related skills

- [`content-pillar-generator`](content-pillar-generator.md) — apply voice to a content strategy
- [`content-quality-reviewer`](../publishing/content-quality-reviewer.md) — checks drafts against a voice profile before publishing
