---
name: Content Brief Generator
description: Expands a topic and pillar into a structured brief a writer or agent can execute without further clarification.
version: 0.1.0
author: replynodes
license: MIT
category: content-strategy
platforms: [agnostic]
agent_compatibility: [agent-agnostic, claude-code-compatible]
tags: [brief, planning, writing-handoff]
---

# Content Brief Generator

## Purpose

Turns a bare topic (often a single row from a [content calendar](content-calendar-planner.md))
into a full brief: angle, key points, format, and constraints — so a writing
skill or human writer can execute it without asking follow-up questions.

## When to use

- Handing off a calendar topic to a writing skill or a person
- A topic is approved but the specific angle hasn't been decided yet
- Multiple writers need to produce consistent output from the same topic list

## Inputs

| Input | Required | Description |
|---|---|---|
| `topic` | Yes | The subject to write about |
| `pillar` | No | Which content pillar this belongs to |
| `platform` | Yes | Target platform, which determines format constraints |
| `voice_profile` | No | Output from [Brand Voice Extractor](brand-voice-extractor.md) |
| `supporting_material` | No | Research, data, or source content to draw from |

## Instructions

1. State the specific angle — the one idea this piece argues or demonstrates,
   not just the general subject.
2. List 3–5 key points that must appear, in the order they build the
   argument or narrative.
3. Note format constraints from the platform (length, structure — e.g. X
   thread vs. single post, LinkedIn text limit).
4. Specify the intended reader reaction (e.g. "recognize their own mistake,"
   "save this for later," "reply with their experience") — this shapes tone
   more usefully than a generic "engaging" instruction.
5. Note anything explicitly out of scope for this piece, if relevant (e.g.
   "don't mention pricing — that's a separate post").

## Output format

```markdown
## Brief: [Topic]

**Platform:** [platform] **Pillar:** [pillar]
**Angle:** [the one idea this piece argues]
**Key points:**
1. ...
2. ...
3. ...

**Format:** [constraints]
**Intended reaction:** [what the reader should think/do/feel]
**Out of scope:** [if any]
```

## Examples

**Input:** Topic "Why 'stay in touch' usually means no," platform X, pillar Investor psychology.

**Output:**

```markdown
## Brief: Why "stay in touch" usually means no

**Platform:** X **Pillar:** Investor psychology
**Angle:** "Stay in touch" is a specific, low-cost way for investors to decline without confrontation — founders should read it as a soft no, not a maybe.
**Key points:**
1. What the phrase actually signals in investor behavior
2. How to distinguish a real "stay in touch" (rare, specific) from the default one
3. What to do instead of following up passively

**Format:** X thread, 5-7 posts, hook in post 1
**Intended reaction:** Founder recognizes a pattern from their own fundraise and reconsiders how they're following up
**Out of scope:** General fundraising advice unrelated to investor communication signals
```

## Safety and quality checks

- The angle must be a specific claim, not a restatement of the topic.
- Don't include supporting facts or statistics not present in
  `supporting_material` — flag where a claim needs a source instead of
  inventing one.
- No promise that following the brief produces a specific engagement outcome.

## Related skills

- [`content-calendar-planner`](content-calendar-planner.md) — supplies the topic this brief expands
- [`linkedin-thought-leadership-writer`](../writing/linkedin-thought-leadership-writer.md) — one of several writing skills that can execute a brief
- [`x-thread-creator`](../writing/x-thread-creator.md) — executes briefs formatted for X
