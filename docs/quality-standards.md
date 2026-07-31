# Quality Standards

This repository uses three labels to describe review depth. None of them
imply a security audit, and none imply official endorsement of a linked
product.

## Labels

**Featured**
Highly useful, clearly documented, and actively maintained. Featured skills
have realistic examples, precise instructions, and have been used enough to
confirm they hold up outside the original author's context. Maintainers
assign this label; contributors cannot self-nominate.

**Verified**
Reviewed by a maintainer for structural correctness: the format matches
[docs/skill-format.md](skill-format.md), links resolve, instructions are
reproducible, and no acceptance-criteria violations were found. Verified is
a quality-of-documentation check, not a test of real-world results.

**Community**
Submitted and merged, meeting the baseline acceptance criteria in
[CONTRIBUTING.md](../CONTRIBUTING.md), but not yet deeply reviewed. This is
the default label for new submissions. Community skills are useful — they
just haven't accumulated enough usage or maintainer review time to be
promoted yet.

## What these labels do not mean

- **Not a security audit.** See [SECURITY.md](../SECURITY.md) for how
  security issues are handled separately from quality review.
- **Not an endorsement of linked third-party tools or products**, including
  ReplyNodes' own entry — it is held to the same criteria as any other
  submission.
- **Not a performance guarantee.** No label implies a skill will produce
  higher engagement, more followers, or revenue. See the acceptance
  criterion against misleading claims in [CONTRIBUTING.md](../CONTRIBUTING.md).

## How a skill moves between labels

1. New submissions merge as **Community** once they pass the acceptance
   criteria in [CONTRIBUTING.md](../CONTRIBUTING.md).
2. A maintainer can promote a skill to **Verified** after confirming format,
   links, and reproducibility.
3. A maintainer can promote a **Verified** skill to **Featured** based on
   real usage, quality of documentation, and durability over time.
4. Labels can also move down — if a skill's instructions go stale, links
   break, or it stops meeting criteria, a maintainer can revert it to
   **Community** or open an issue asking the author to update it.

## Reporting a quality problem

If a skill is inaccurate, broken, or making claims it shouldn't, open an
issue using the **Bug report** template rather than a pull request removing
it outright — this keeps the discussion visible and gives the original
author a chance to respond.
