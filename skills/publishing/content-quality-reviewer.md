---
name: Content Quality Reviewer
description: Reviews a finished draft against voice, claims, platform constraints, and policy risk before it moves to publishing.
version: 0.1.0
author: replynodes
license: MIT
category: publishing
platforms: [agnostic]
agent_compatibility: [agent-agnostic, mcp-compatible]
tags: [review, approval, quality-gate]
---

# Content Quality Reviewer

## Purpose

Acts as the last check before a draft is approved to publish: does it match
the brand voice, does it fit the platform's constraints, are its claims
supported, and does it avoid obvious policy or reputational risk.

## When to use

- Immediately before publishing or scheduling any draft
- As the approval gate in a human-in-the-loop pipeline — see
  [examples/content-pipeline](../../examples/content-pipeline/README.md)

## Inputs

| Input | Required | Description |
|---|---|---|
| `draft` | Yes | The finished content to review |
| `platform` | Yes | Target platform, for format constraints |
| `voice_profile` | No | Output from [Brand Voice Extractor](../content-strategy/brand-voice-extractor.md) |
| `source_material` | No | For claim verification — see [Content Claim Verifier](../research/content-claim-verifier.md) |

## Instructions

1. Check format fit: length limits, structure conventions, and any
   platform-specific norm (e.g. no hashtag stuffing on LinkedIn, no
   promotional tone on Reddit).
2. Check voice fit against `voice_profile` if provided — flag tone,
   vocabulary, or structural mismatches with specific examples from the draft.
3. Check for unverifiable or unsupported claims — if `source_material` is
   provided, defer to [Content Claim Verifier](../research/content-claim-verifier.md)
   for a full pass; otherwise flag any claim that reads as a specific fact
   without attribution.
4. Check for policy or reputational risk: language that could violate a
   platform's content policy, claims of guaranteed outcomes, or anything
   that misrepresents a product, person, or result.
5. Give a final verdict: **approve**, **approve with minor edits** (list
   them), or **send back** (list blocking issues). Only "send back" for
   issues that are actually blocking — cosmetic preferences aren't blockers.

## Output format

```markdown
## Review: [draft identifier]

**Format fit:** pass / issues — [detail]
**Voice fit:** pass / issues — [detail]
**Claims:** pass / issues — [detail]
**Policy/risk:** pass / issues — [detail]

**Verdict:** approve / approve with minor edits / send back
**Blocking issues:** [list, if any]
```

## Examples

**Input:** LinkedIn draft with a strong hook but a hashtag block at the end and an unsupported "90% of founders" statistic.

**Output:**

```markdown
## Review: LinkedIn draft — fundraising narrative post

**Format fit:** issues — hashtag block doesn't match LinkedIn conventions used elsewhere in this account's content
**Voice fit:** pass
**Claims:** issues — "90% of founders fail because of narrative" has no supporting source in provided material
**Policy/risk:** pass

**Verdict:** send back
**Blocking issues:** Remove or source the 90% statistic before this can be approved.
```

## Safety and quality checks

- Never approve a draft with an unsupported specific statistic — send it
  back or require the claim be softened to match what's actually known.
- This skill is a documentation/structure check, not a legal or compliance
  review — for regulated industries, route drafts through actual legal
  review in addition to this skill.
- No guarantee that an approved draft will perform well once published.

## Related skills

- [`content-claim-verifier`](../research/content-claim-verifier.md) — full claim-checking pass
- [`cross-platform-publishing-formatter`](cross-platform-publishing-formatter.md) — next step after approval
