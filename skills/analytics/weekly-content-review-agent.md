---
name: Weekly Content Review Agent
description: Runs a recurring weekly review that summarizes what published, how it performed, and what to adjust for the next cycle.
version: 0.1.0
author: replynodes
license: MIT
category: analytics
platforms: [agnostic]
agent_compatibility: [agent-agnostic, mcp-compatible]
tags: [analytics, weekly-review, workflow]
---

# Weekly Content Review Agent

## Purpose

A recurring workflow skill that closes the loop each week: what was
published, how it performed relative to the prior period, and specific
adjustments to carry into next week's [content calendar](../content-strategy/content-calendar-planner.md).

## When to use

- On a fixed weekly (or other regular) cadence, as a standing review step
- After a batch of content has had enough time to accumulate meaningful engagement data

## Inputs

| Input | Required | Description |
|---|---|---|
| `published_this_period` | Yes | List of posts published, with metadata |
| `performance_data` | Yes | Metrics for those posts |
| `prior_period_summary` | No | Last period's summary, for comparison |
| `upcoming_calendar` | No | Next period's planned content, to check against findings |

## Instructions

1. Summarize what published this period: count by platform and pillar.
2. Run [Performance Insight Analyzer](performance-insight-analyzer.md)-style
   analysis on `performance_data`, comparing against `prior_period_summary`
   if available.
3. Identify 1–3 specific adjustments for next period — pillar mix, format
   mix, or a hypothesis worth testing with [Social Post Experiment Designer](social-post-experiment-designer.md).
4. If `upcoming_calendar` is provided, check whether it already reflects
   the recommended adjustments and flag any mismatch.
5. Keep the summary short — this is a recurring digest, not a full report;
   link out to a full [Performance Insight Analyzer](performance-insight-analyzer.md)
   pass if deeper analysis is warranted.

## Output format

```markdown
## Weekly review: [date range]

**Published:** [count by platform/pillar]
**Performance vs. prior period:** [brief comparison, or "no prior period to compare" if unavailable]

**Adjustments for next period:**
1. ...
2. ...

**Calendar check:** [matches recommendations / flagged mismatches]
```

## Examples

**Input:** 12 posts published this week across LinkedIn and X, compared against a 10-post prior week.

**Output:**

```markdown
## Weekly review: Mar 3 - Mar 9

**Published:** 7 LinkedIn (4 case-study, 3 pitch-mechanics), 5 X threads (all investor-psychology)
**Performance vs. prior period:** LinkedIn comment rate up ~15% vs. prior week, driven mostly by case-study posts. X thread engagement roughly flat.

**Adjustments for next period:**
1. Keep the shift toward case-study pillar on LinkedIn — still the strongest performer
2. X pillar mix hasn't varied in 2 weeks — worth testing a different pillar there to see if flat engagement is pillar-related or platform-related
3. No pitch-mechanics content ran on X this week — check if that's intentional or a calendar gap

**Calendar check:** Upcoming calendar already shifts LinkedIn toward case studies. No X pillar variation planned yet — flagged for next planning session.
```

## Safety and quality checks

- Base every comparison on actual provided data — if `prior_period_summary`
  is missing, say so rather than fabricating a comparison baseline.
- Keep recommendations specific and limited to 1-3 — a long list of
  adjustments isn't actionable.
- No performance guarantees for recommended adjustments; they're informed
  suggestions, not predictions.

## Related skills

- [`performance-insight-analyzer`](performance-insight-analyzer.md) — the deeper analysis this weekly digest summarizes
- [`content-calendar-planner`](../content-strategy/content-calendar-planner.md) — where recommended adjustments get applied
