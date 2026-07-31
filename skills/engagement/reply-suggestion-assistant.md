---
name: Reply Suggestion Assistant
description: Drafts reply suggestions for comments or questions, in brand voice, for a human to review and send.
version: 0.1.0
author: replynodes
license: MIT
category: engagement
platforms: [agnostic]
agent_compatibility: [agent-agnostic]
tags: [replies, community, engagement]
---

# Reply Suggestion Assistant

## Purpose

Drafts reply suggestions for individual comments or comment themes,
matching brand voice — intended as suggestions for a human to review and
send, not to auto-post replies.

## When to use

- After [Comment Theme Analyzer](comment-theme-analyzer.md) surfaces themes needing a response
- Responding to a high volume of similar comments consistently
- A team wants draft replies ready for a human to approve quickly, not to skip review entirely

## Inputs

| Input | Required | Description |
|---|---|---|
| `comment_or_theme` | Yes | The comment text, or a theme with a representative comment |
| `voice_profile` | No | Output from [Brand Voice Extractor](../content-strategy/brand-voice-extractor.md) |
| `factual_context` | No | Any facts needed to answer accurately (e.g. actual policy details) |

## Instructions

1. Identify what the comment actually needs: an answer to a question, an
   acknowledgment, a correction, or no response warranted (e.g. pure spam).
2. If it's a factual question, only answer using `factual_context` provided
   — if the fact isn't available, draft a reply that says the answer is
   being confirmed rather than guessing.
3. Match tone to `voice_profile` if provided; default to direct and
   specific rather than generic ("thanks for sharing!") replies.
4. Keep replies short — a reply that over-explains reads as defensive.
5. Flag any comment that needs a human decision beyond drafting (a
   complaint requiring escalation, a legal/sensitive topic) rather than
   drafting a reply for it.

## Output format

```markdown
## Reply suggestions

**Comment:** "[original]"
**Suggested reply:** "[draft]"
**Needs human review because:** [if flagged, why — otherwise omit this line]
```

## Examples

**Input:** Comment: "Does this affect people already on the old plan?" Factual context: existing customers keep current pricing until renewal.

**Output:**

```markdown
## Reply suggestions

**Comment:** "Does this affect people already on the old plan?"
**Suggested reply:** "No — if you're already on a plan, you keep your current pricing until your next renewal. New tiers apply to new signups first."
```

**Input:** Comment: "This is a scam, you're just raising prices." No factual context provided on pricing rationale.

**Output:**

```markdown
## Reply suggestions

**Comment:** "This is a scam, you're just raising prices."
**Suggested reply:** [not drafted]
**Needs human review because:** Accusatory comment involving a claim about company intent — needs a human decision on tone and whether/how to respond, not a templated reply.
```

## Safety and quality checks

- Never draft a factual answer without a factual basis in `factual_context`
  — say the answer needs confirming instead of guessing.
- These are suggestions for human review, not auto-post replies — nothing
  in this skill's output should be treated as already sent.
- Escalate rather than draft for hostile, legal, or sensitive comments.

## Related skills

- [`comment-theme-analyzer`](comment-theme-analyzer.md) — supplies the themes this skill drafts replies for
- [`brand-voice-extractor`](../content-strategy/brand-voice-extractor.md) — keeps replies consistent with published content
