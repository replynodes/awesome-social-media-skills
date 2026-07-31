# Submission Guide

A walkthrough for submitting a skill, tool, or workflow. For the acceptance
criteria themselves, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## 1. Check it doesn't already exist

Browse the relevant `skills/<category>/README.md` or search the repository
for similar entries. If something close already exists, consider improving
it with a pull request instead of adding a near-duplicate.

## 2. Pick the right category

| Category | Covers |
|---|---|
| `content-strategy` | Audience research framing, brand voice, content pillars, calendars, campaign and launch planning |
| `research` | Topic and claim research, competitor research, trend and pain-point discovery |
| `writing` | Platform-specific post writing, hooks, storytelling, editing |
| `video` | Scripts, hooks, and structure for short- and long-form video |
| `images` | Visual and carousel content generation prompts and structure |
| `repurposing` | Turning one piece of content into multiple platform-native pieces |
| `publishing` | Formatting, queuing, approval workflows, and publishing/scheduling integrations |
| `analytics` | Performance analysis, experiment design, reporting |
| `engagement` | Comment analysis, reply drafting, community monitoring |

If a submission genuinely spans two categories, put it where its primary
output lives and cross-link it from the other category's README.

## 3. Use the template

Copy [templates/SKILL.md](../templates/SKILL.md) and fill in every section.
See [docs/skill-format.md](skill-format.md) for what belongs in each one.
Skip nothing — a section left as a placeholder is a common reason for a
submission to be sent back for changes.

## 4. Write a real example

Every skill needs at least one full input/output example using realistic
(not placeholder) content. This is usually the fastest way to tell whether
your own instructions are specific enough — if you can't produce a clean
example from your own instructions, tighten them.

## 5. Add it to the category README

Add a row to the relevant `skills/<category>/README.md` table so it shows
up in navigation, not just in the file tree.

## 6. Regenerate the skill index

Run `python3 scripts/generate_index.py` and commit the updated `index.json`
alongside your skill. This also validates your frontmatter — it will fail
loudly if a required field is missing or `category` doesn't match the
directory your file is in. CI runs the same check (`--check` mode) and
will fail the pull request if `index.json` wasn't regenerated.

## 7. Open a pull request

Use the pull request template. Reference any related issue. If you have a
commercial affiliation with what you're submitting, disclose it in the PR
description — see [CONTRIBUTING.md](../CONTRIBUTING.md#disclosure-requirement).

## 8. Respond to review

A maintainer will check the submission against the acceptance criteria and
may ask for changes — most accepted skills go through at least one round of
feedback. Once merged, new skills start labeled **Community**; see
[docs/quality-standards.md](quality-standards.md) for how promotion works.

## Submitting a tool, MCP server, or integration instead of a skill

These don't use the SKILL.md format. Open an issue with the **Tool
submission** template, or a pull request that adds the tool to the relevant
README section with: what it does, a link, and — if it's an agent
integration — which agents or MCP clients it works with.
