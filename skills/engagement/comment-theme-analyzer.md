---
name: Comment Theme Analyzer
description: Groups raw comments into recurring themes to surface what an audience is actually reacting to or asking.
version: 0.1.0
author: replynodes
license: MIT
category: engagement
platforms: [agnostic]
agent_compatibility: [agent-agnostic]
tags: [comments, community, engagement-analysis]
---

# Comment Theme Analyzer

## Purpose

Reads a set of raw comments (from one post or a period) and groups them into
recurring themes — questions, objections, agreement, requests — so the
volume of individual comments becomes a small set of actionable signals.

## When to use

- A post generated enough comments that reading each one individually loses the pattern
- Before drafting replies with [Reply Suggestion Assistant](reply-suggestion-assistant.md), to reply to themes efficiently rather than one-off
- Feeding recurring questions back into content ideas or [audience pain-point research](../research/audience-pain-point-researcher.md)

## Inputs

| Input | Required | Description |
|---|---|---|
| `comments` | Yes | Raw comment text, one post or a batch |
| `post_context` | No | What the post said, for interpreting comment intent accurately |

## Instructions

1. Read all comments and classify each as one of: question, objection/
   pushback, agreement/validation, personal anecdote, spam/irrelevant.
2. Group non-spam comments into themes — recurring specific questions or
   objections, not a single catch-all "positive feedback" bucket.
3. For each theme, note the count and 1–2 representative comments.
4. Flag any theme that suggests a factual correction is needed in the
   original post (e.g. multiple commenters pointing out the same error).
5. Exclude spam and clearly irrelevant comments from theme counts, but note
   the spam volume separately if it's notable.

## Output format

```markdown
## Comment themes: [post/period]

| Theme | Type | Count | Representative comment |
|---|---|---|---|
| ... | Question/Objection/Agreement/Anecdote | ... | "..." |

**Correction needed:** [flag if applicable]
**Spam/irrelevant:** [count, if notable]
```

## Examples

**Input:** 40 comments on a post about pricing tier changes.

**Output:**

```markdown
## Comment themes: Pricing tier post

| Theme | Type | Count | Representative comment |
|---|---|---|---|
| "Will existing customers be grandfathered?" | Question | 11 | "Does this affect people already on the old plan?" |
| "This should have happened sooner" | Agreement | 8 | "Finally — the 5 tiers never made sense" |
| "What happens to the tier I'm currently on?" | Question | 6 | "I'm on tier 3, which new tier am I now?" |
| Concern the new tiers remove a needed feature | Objection | 4 | "Tier 2 doesn't have the API access I need" |

**Correction needed:** Grandfathering policy isn't addressed in the original post — high-volume question, worth a follow-up clarification post.
**Spam/irrelevant:** 3 unrelated promotional comments, excluded from above.
```

## Safety and quality checks

- Don't merge distinct questions into one vague theme — specificity is what
  makes this useful for follow-up content or replies.
- Exclude spam from theme counts so it doesn't distort signal.
- This skill summarizes comment content; it does not assess sentiment
  toward the brand beyond what's explicitly stated in the comments.

## Related skills

- [`reply-suggestion-assistant`](reply-suggestion-assistant.md) — drafts replies to the themes surfaced here
- [`audience-pain-point-researcher`](../research/audience-pain-point-researcher.md) — recurring questions here can feed pain-point research
