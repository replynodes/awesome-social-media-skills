---
name: Content Pillar Generator
description: Turns a business or personal brand description into a set of focused content pillars to organize future content around.
version: 0.1.0
author: replynodes
license: MIT
category: content-strategy
platforms: [agnostic]
agent_compatibility: [agent-agnostic, claude-code-compatible]
tags: [content-pillars, strategy, planning]
---

# Content Pillar Generator

## Purpose

Produces 3–5 content pillars — the recurring themes a brand or creator posts
about — from a description of the business, audience, and goals, so future
content has a consistent structure instead of being decided post by post.

## When to use

- Starting content from scratch for a brand, product, or personal account
- Content feels scattered or reactive and needs organizing structure
- Before building a [content calendar](content-calendar-planner.md)

## Inputs

| Input | Required | Description |
|---|---|---|
| `business_description` | Yes | What the brand/person does, for whom |
| `audience_pain_points` | No | Output from [Audience Pain-Point Researcher](../research/audience-pain-point-researcher.md), if available |
| `existing_content_examples` | No | Past posts that performed well, if any |
| `competitor_notes` | No | What competitors post about, to differentiate against |

## Instructions

1. From the business description, identify the 2–3 core expertise areas and
   the 1–2 audience transformations the content should support (what the
   audience should think or do differently after engaging).
2. Draft 5–8 candidate pillar themes covering expertise, audience pain
   points, and behind-the-scenes/perspective content.
3. Narrow to 3–5 pillars. Each must be specific enough to generate distinct
   post ideas repeatedly — reject pillars broad enough to swallow all the
   others (e.g. "business tips" is too broad).
4. For each pillar, write: a one-line definition, the audience benefit, and
   3 example post topics.
5. Check for balance — pillars shouldn't all be the same content type
   (e.g. all "how-to"). Mix perspective, education, and proof/results.

## Output format

```markdown
## Content Pillars: [Brand/Person]

### 1. [Pillar name]
**Definition:** [one line]
**Why it matters to the audience:** [one line]
**Example topics:** [3 bullet points]

[repeat for each pillar, 3-5 total]

**Suggested mix:** [rough % or ratio across pillars for a typical month]
```

## Examples

**Input:** Solo consultant helping early-stage founders with fundraising narrative.

**Output:**

```markdown
## Content Pillars: Fundraising Narrative Consultant

### 1. Pitch mechanics
**Definition:** How the structure and sequencing of a pitch affects investor response
**Why it matters:** Founders don't know what's a structure problem vs. a business problem
**Example topics:**
- The 3 places most pitches lose an investor's attention
- Why "market size" slides usually backfire
- A before/after of a real pitch narrative rewrite

### 2. Investor psychology
**Definition:** What's actually going through an investor's head at each stage
**Why it matters:** Founders write for logic; investors decide on pattern-matching first
**Example topics:**
- What "let's stay in touch" usually means
- The real reason warm intros work
- How investors triage 50 decks in an afternoon

### 3. Founder-side case studies
**Definition:** Real (anonymized) fundraising outcomes and what changed them
**Why it matters:** Proof beats advice
**Example topics:**
- A founder who raised after 40 no's — what changed
- The narrative edit that turned a pass into a term sheet

**Suggested mix:** 40% pitch mechanics, 35% investor psychology, 25% case studies
```

## Safety and quality checks

- Pillars must be specific enough to be falsifiable as "on-pillar" or
  "off-pillar" — vague pillars aren't useful.
- Don't fabricate case studies or results in example topics; mark them as
  illustrative if no real data was provided.
- No claim that following these pillars guarantees growth or engagement.

## Related skills

- [`brand-voice-extractor`](brand-voice-extractor.md) — pairs pillars with a consistent voice
- [`content-calendar-planner`](content-calendar-planner.md) — schedules pillars over time
- [`audience-pain-point-researcher`](../research/audience-pain-point-researcher.md) — feeds pillar selection with real audience data
