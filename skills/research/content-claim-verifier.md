---
name: Content Claim Verifier
description: Checks factual claims in a content draft against provided sources and flags anything unsupported before publishing.
version: 0.1.0
author: replynodes
license: MIT
category: research
platforms: [agnostic]
agent_compatibility: [agent-agnostic]
tags: [fact-checking, verification, quality]
---

# Content Claim Verifier

## Purpose

Reads a content draft, extracts every factual or statistical claim, and
checks each one against provided source material — flagging anything
unsupported, outdated, or misrepresented before the draft moves to review or
publishing.

## When to use

- Before publishing any content that cites statistics, research, or specific facts
- After [repurposing](../repurposing/) content from a long-form source, to make sure claims survived the compression accurately
- As a standing check before [Content Quality Reviewer](../publishing/content-quality-reviewer.md)

## Inputs

| Input | Required | Description |
|---|---|---|
| `draft` | Yes | The content to check |
| `source_material` | Yes | The material the draft's claims should be traceable to |

## Instructions

1. Extract every factual claim from the draft: statistics, named studies,
   quotes, specific numbers, or statements presented as fact rather than
   opinion.
2. For each claim, check whether it appears in `source_material` and
   whether the draft represents it accurately — same number, same scope,
   same conclusion (a claim can be technically present but misrepresented,
   e.g. a stat about one segment applied to the whole population).
3. Classify each claim: **supported**, **misrepresented** (present but
   distorted), or **unsupported** (not found in source material).
4. For misrepresented or unsupported claims, quote the exact sentence from
   the draft and explain the gap.
5. Do not attempt to verify claims using outside knowledge not present in
   `source_material` — if a claim can't be checked against what was
   provided, mark it unsupported rather than assuming it's correct.

## Output format

```markdown
## Claim check: [draft title/identifier]

| Claim (as written) | Status | Note |
|---|---|---|
| "..." | Supported/Misrepresented/Unsupported | ... |

**Blocking issues:** [count of misrepresented + unsupported claims]
```

## Examples

**Input:** Draft states "90% of founders fail because of poor fundraising narrative." Source material is an interview transcript where the subject said "in my experience, most of the founders I see struggle more with narrative than product."

**Output:**

```markdown
## Claim check: Draft on fundraising narrative

| Claim (as written) | Status | Note |
|---|---|---|
| "90% of founders fail because of poor fundraising narrative" | Unsupported | Source gives a qualitative, first-person impression ("most," "in my experience") — no 90% figure or fail-rate claim exists in source material |

**Blocking issues:** 1
```

## Safety and quality checks

- Never mark a claim "supported" based on plausibility alone — it must
  actually appear in the provided source material.
- Precision language matters: "most" in a source does not support a
  specific percentage in the draft.
- This skill checks traceability to provided sources, not real-world truth
  beyond those sources — note that limitation if source material itself is
  thin or unverified.

## Related skills

- [`content-quality-reviewer`](../publishing/content-quality-reviewer.md) — broader review that should run after claims are verified
- [`youtube-to-social-repurposer`](../repurposing/youtube-to-social-repurposer.md) — a common source of claims that need re-verification after compression
