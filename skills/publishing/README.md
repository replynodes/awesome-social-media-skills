# Publishing

Skills for the approval gate and the handoff from finished content to
publishing or scheduling — platform-agnostic by design, so any scheduling
tool or MCP-compatible publishing layer can sit downstream.

| Skill | What it does |
|---|---|
| [Content Quality Reviewer](content-quality-reviewer.md) | Final approval check: voice, claims, format, policy risk |
| [Cross-Platform Publishing Formatter](cross-platform-publishing-formatter.md) | Formats approved content into a structured publishing queue |

## Typical order

Approved draft → [Content Quality Reviewer](content-quality-reviewer.md) →
[Cross-Platform Publishing Formatter](cross-platform-publishing-formatter.md) →
a scheduling/publishing tool

These skills produce a publish-ready queue but don't publish anything
themselves — that last step needs a scheduling or publishing layer, manual
or MCP-based. See [Publish with ReplyNodes](../../README.md#publish-with-replynodes)
in the main README for one optional example.
