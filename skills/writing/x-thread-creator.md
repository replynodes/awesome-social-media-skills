---
name: X Thread Creator
description: Converts a brief or long-form idea into a structured X/Twitter thread with a hook post and a coherent post sequence.
version: 0.1.0
author: replynodes
license: MIT
category: writing
platforms: [x]
agent_compatibility: [agent-agnostic, claude-code-compatible]
tags: [x, twitter, threads, writing]
---

# X Thread Creator

## Purpose

Turns a brief or a longer piece of content into an X thread: a hook post
that earns the click to expand, followed by a sequence of posts that each
carry one idea and connect to the next.

## When to use

- Executing a brief for X specifically
- Breaking a longer piece (blog post, video transcript) into thread form — pair with [Blog-to-Multi-Platform Repurposer](../repurposing/blog-to-multi-platform-repurposer.md) for the source extraction step

## Inputs

| Input | Required | Description |
|---|---|---|
| `brief` | Yes | Angle and key points — see [Content Brief Generator](../content-strategy/content-brief-generator.md) |
| `source_content` | No | Longer source material to draw specific points from |
| `target_length` | No | Approximate number of posts (default 5-8) |

## Instructions

1. Write the hook post first, independent of the rest. It must state a
   specific, non-obvious claim or result — not "a thread about X" — since
   this is the only post most readers see before deciding to expand.
2. Sequence the body posts so each one advances a single point from the
   brief's key points, in the order they build the argument. One idea per
   post, under 280 characters each.
3. Use the first few words of each post to keep momentum (a specific detail
   or number, not "Next," "Also," or other filler transitions).
4. End with a closing post that states the takeaway plainly. Do not add a
   generic "if you found this useful, RT" — end on the idea, not a
   solicitation.
5. Number posts only if the thread exceeds 6 posts and the sequence order
   matters for comprehension.

## Output format

```text
1/ [Hook post]

2/ [Body point 1]

3/ [Body point 2]

...

n/ [Closing takeaway]
```

## Examples

**Input:** Brief on investor psychology, "stay in touch" angle, source is the LinkedIn post from the LinkedIn Thought-Leadership Writer example.

**Output:**

```text
1/ "Stay in touch" is the most polite rejection in fundraising. Here's how
to actually tell it apart from a real maybe.

2/ Most founders read "stay in touch" as an open door. It's rarely one —
investors have a cheaper way to signal real interest.

3/ The real signal: a specific follow-up question, or a concrete ask about
your next update. That's interest.

4/ "Stay in touch" with nothing else attached is the low-conflict way to
end a meeting without saying no directly.

5/ The tell isn't the phrase — it's what's attached to it. Specific ask,
real maybe. Nothing else, soft no.

6/ Stopped chasing vague "stay in touch" replies. Saved a lot of follow-up
emails that were never going anywhere.
```

## Safety and quality checks

- Hook must accurately represent the thread's content — no clickbait that
  the body doesn't deliver on.
- Each post must be self-contained enough to make sense read alone, since
  X threads are often read out of order via retweets/quotes.
- No fabricated statistics or claims beyond what's in the brief or source content.
- No guarantee of reach, retweets, or virality.

## Related skills

- [`content-brief-generator`](../content-strategy/content-brief-generator.md) — supplies the input this skill executes
- [`linkedin-thought-leadership-writer`](linkedin-thought-leadership-writer.md) — equivalent skill for LinkedIn
- [`blog-to-multi-platform-repurposer`](../repurposing/blog-to-multi-platform-repurposer.md) — extracts thread-ready points from long-form source
