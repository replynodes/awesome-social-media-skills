# Example: Draft → Approve → Publish Pipeline

A human-in-the-loop pipeline where an agent drafts content, a person
approves it, and only approved content gets queued for publishing.

## Skills used, in order

1. [Content Brief Generator](../../skills/content-strategy/content-brief-generator.md)
2. [LinkedIn Thought-Leadership Writer](../../skills/writing/linkedin-thought-leadership-writer.md)
   (or another writing skill, depending on platform)
3. [Content Claim Verifier](../../skills/research/content-claim-verifier.md)
4. [Content Quality Reviewer](../../skills/publishing/content-quality-reviewer.md)
5. [Cross-Platform Publishing Formatter](../../skills/publishing/cross-platform-publishing-formatter.md)
6. A scheduling/publishing layer — MCP-based or manual (see
   [Publish with ReplyNodes](../../README.md#publish-with-replynodes) for one
   optional example)

## Walkthrough

**1. Brief.** Start from a calendar topic or a raw idea. Run
[Content Brief Generator](../../skills/content-strategy/content-brief-generator.md)
to produce a specific angle, key points, and intended reaction — this is
what the writing skill executes, so vague briefs produce vague drafts.

**2. Draft.** Feed the brief into a writing skill matching the target
platform. The draft comes back in the platform's native format, not generic
text to be reformatted later.

**3. Verify claims.** If the draft references any fact, statistic, or
specific example, run [Content Claim Verifier](../../skills/research/content-claim-verifier.md)
against the source material the brief was built from. Anything unsupported
gets flagged before a human ever sees it — this saves a review cycle.

**4. Human approval gate.** [Content Quality Reviewer](../../skills/publishing/content-quality-reviewer.md)
checks format, voice, claims, and policy risk, and returns a verdict:
approve, approve with minor edits, or send back. Treat "approve" here as a
recommendation for the human approver, not a substitute for their review —
this skill's job is to make that review fast, not to remove it.

**5. Queue.** Once a human has actually approved the draft, run
[Cross-Platform Publishing Formatter](../../skills/publishing/cross-platform-publishing-formatter.md)
to produce a structured, schedulable queue entry.

**6. Publish or schedule.** The queue entry is ready for whatever
publishing layer you use — a manual checklist, a native scheduler, or an
MCP-compatible tool such as ReplyNodes for teams that want agents to publish
and schedule directly through an API.

## Where a human sits in this loop

Step 4 is the gate: nothing produced by steps 1-3 should be treated as
publish-ready until a person has reviewed it. This pipeline is designed so
that gate is fast (most of the checking work is already done by step 4) —
not so it can be skipped.
