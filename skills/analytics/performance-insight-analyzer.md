---
name: Performance Insight Analyzer
description: Analyzes provided post performance data and surfaces specific, actionable patterns rather than a generic summary.
version: 0.1.0
author: replynodes
license: MIT
category: analytics
platforms: [agnostic]
agent_compatibility: [agent-agnostic, mcp-compatible]
tags: [analytics, performance, insights]
---

# Performance Insight Analyzer

## Purpose

Reads a set of post performance data (metrics per post, with content
metadata) and surfaces specific patterns — what's correlated with stronger
or weaker performance — instead of restating the raw numbers.

## When to use

- Periodic performance review (weekly, monthly) — see [Weekly Content Review Agent](weekly-content-review-agent.md)
- After running an experiment designed with [Social Post Experiment Designer](social-post-experiment-designer.md)

## Inputs

| Input | Required | Description |
|---|---|---|
| `performance_data` | Yes | Posts with metrics (impressions, engagement, clicks, etc.) and content metadata (pillar, format, platform, date) |
| `metric_of_interest` | No | Which metric to prioritize if multiple are present |

## Instructions

1. Group posts by the metadata dimensions available (pillar, format,
   platform, length, posting day) and compare performance across each
   grouping.
2. Surface only patterns with enough data to be meaningful — note sample
   size next to every claimed pattern, and flag patterns based on fewer
   than 5 posts as low-confidence.
3. State findings as specific, checkable claims (e.g. "carousel posts
   averaged 2.3x the saves of single-image posts across 14 posts") rather
   than vague takeaways ("visual content does well").
4. Distinguish correlation from explanation — note plausible reasons for a
   pattern, but label them as hypotheses, not confirmed causes, unless a
   controlled experiment produced the data.
5. Rank findings by how actionable they are — a pattern the content owner
   can act on ranks above an interesting but unchangeable one (e.g. "posts
   published by the founder personally outperform" may not be actionable
   if the founder can't personally post more).

## Output format

```markdown
## Performance analysis: [period/dataset]

| Finding | Sample size | Confidence | Actionable? |
|---|---|---|---|
| ... | ... | High/Medium/Low | Yes/No — why |

**Top recommendation:** [the single most actionable finding, and what to do about it]
```

## Examples

**Input:** 30 LinkedIn posts over 6 weeks with pillar, format, and engagement data.

**Output:**

```markdown
## Performance analysis: 6-week LinkedIn review

| Finding | Sample size | Confidence | Actionable? |
|---|---|---|---|
| Case-study pillar posts averaged 1.8x the comments of pitch-mechanics posts | 12 case-study, 10 pitch-mechanics | Medium | Yes — shift pillar mix toward case studies |
| Posts under 800 characters had lower comment rates than posts 1,300-1,800 characters | 30 posts | Medium | Yes — favor longer-form posts for this account |
| Posts published Tuesday/Wednesday outperformed Monday/Friday | 30 posts, but only 4 on Monday/Friday | Low | No — too few posts on those days to conclude a real day effect |

**Top recommendation:** Shift pillar mix toward case studies — largest, most confident effect with a direct action available.
```

## Safety and quality checks

- Never state a finding without its sample size attached.
- Don't claim a causal mechanism unless the data comes from a controlled
  experiment — otherwise, label proposed reasons as hypotheses.
- This skill analyzes provided data only — it does not access live
  platform analytics itself and makes no promises about future performance.

## Related skills

- [`social-post-experiment-designer`](social-post-experiment-designer.md) — turns a hypothesis from this analysis into a proper test
- [`weekly-content-review-agent`](weekly-content-review-agent.md) — runs this analysis on a recurring cadence
