---
name: Product Launch Content Planner
description: Builds a coordinated content plan across platforms and time for a product or feature launch.
version: 0.1.0
author: replynodes
license: MIT
category: content-strategy
platforms: [agnostic]
agent_compatibility: [agent-agnostic]
tags: [product-launch, planning, campaign]
---

# Product Launch Content Planner

## Purpose

Given launch details (what's shipping, when, for whom), produces a
before/during/after content plan across platforms so a launch isn't a single
announcement post but a coordinated sequence.

## When to use

- A product, feature, or major update has a confirmed launch date
- Launch content needs to span multiple platforms and several days
- Coordinating founder posts, company account posts, and supporting content

## Inputs

| Input | Required | Description |
|---|---|---|
| `launch_details` | Yes | What's launching, key benefit, launch date |
| `audience` | Yes | Who this matters to and why |
| `platforms` | Yes | Where the launch will be promoted |
| `assets_available` | No | Demo video, screenshots, docs, changelog — what exists to draw on |

## Instructions

1. Split the plan into three phases: **pre-launch** (build anticipation,
   optional), **launch day** (the core announcement across platforms), and
   **post-launch** (results, use cases, follow-up).
2. For launch day, assign one primary announcement post per platform with a
   distinct angle per platform (e.g. LinkedIn: business impact; X: quick
   demo/thread; not the identical post copy-pasted).
3. For post-launch, plan 2–4 follow-up pieces spaced over the following 1–2
   weeks: a use-case example, an FAQ/objection-handling piece, early
   results or feedback if available.
4. Note which assets each piece depends on, and flag any piece that needs an
   asset not listed in `assets_available`.
5. Do not include pre-launch teaser content unless explicitly requested —
   default to launch day + post-launch only, since teasers require lead
   time many launches don't have.

## Output format

```markdown
## Launch Plan: [Product/Feature]

**Launch date:** [date] **Audience:** [who]

### Launch day
| Platform | Angle | Format | Asset needed |
|---|---|---|---|

### Post-launch (following 2 weeks)
| Day offset | Platform | Topic | Format | Asset needed |
|---|---|---|---|---|

**Missing assets:** [list, if any]
```

## Examples

**Input:** New MCP integration launching Tuesday, audience is developers already using the product's API.

**Output:**

```markdown
## Launch Plan: MCP Integration

**Launch date:** Tuesday **Audience:** Developers already using the API

### Launch day
| Platform | Angle | Format | Asset needed |
|---|---|---|---|
| X | "You can now do X directly from your agent" + short demo | Thread with clip | Screen recording |
| LinkedIn | Why this matters for teams building agent workflows | Text post | None |

### Post-launch (following 2 weeks)
| Day offset | Platform | Topic | Format | Asset needed |
|---|---|---|---|---|
| +3 | X | A real workflow someone built with it | Text post | User example (pending) |
| +7 | LinkedIn | Common setup questions answered | Text post | None |

**Missing assets:** Screen recording of the integration in use; user example for day +3 not yet confirmed.
```

## Safety and quality checks

- Don't fabricate results, user quotes, or metrics for post-launch content —
  flag them as pending if not yet available.
- Distinguish clearly between confirmed launch details and assumptions;
  don't invent a launch date or feature scope not provided.
- No guarantee of launch-day engagement or adoption numbers.

## Related skills

- [`founder-story-extractor`](../writing/founder-story-extractor.md) — a source for the "why this matters" angle
- [`multi-platform-content-adapter`](../repurposing/multi-platform-content-adapter.md) — turns each planned piece into final platform copy
- [`content-quality-reviewer`](../publishing/content-quality-reviewer.md) — final check before launch content goes out
