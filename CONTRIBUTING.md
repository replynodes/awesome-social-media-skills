# Contributing

Thanks for considering a contribution. This repository grows through
community submissions of skills, workflows, prompts, MCP servers, tools, and
integrations for social-media AI agents. This guide covers how to submit one
and what gets accepted.

## What you can contribute

- **Skills** — a single, well-scoped agent capability (see
  [templates/SKILL.md](templates/SKILL.md))
- **Workflows / examples** — a multi-step agent pipeline that chains skills
  together (see [examples/](examples/))
- **Prompts** — reusable, structured prompts that work as standalone skills
- **Tools and MCP servers** — software that agents can call, listed with
  install/usage instructions
- **Integrations** — connectors between agents and platforms or services

## Before you submit

Read [docs/submission-guide.md](docs/submission-guide.md) for the full
walkthrough and [docs/quality-standards.md](docs/quality-standards.md) for
what gets accepted, labeled **Featured**, **Verified**, or **Community**.

## Acceptance criteria

Every submission is checked against:

1. **Relevant and useful** — fits the social-media agent workflow this repo covers
2. **Clear purpose** — a reader understands what it does in one sentence
3. **Reproducible instructions** — another person or agent can follow it and get a comparable result
4. **No misleading claims** — no promises of virality, guaranteed engagement, or guaranteed revenue
5. **No spam** — not a thin wrapper around an unrelated link
6. **No affiliate-only submissions** — the entry must be useful on its own, not just a referral link
7. **No undisclosed commercial promotion** — see disclosure requirement below
8. **Working links** — all referenced URLs resolve
9. **Clear licensing** — compatible with this repository's MIT license, or clearly marked otherwise
10. **Meaningful documentation** — filled-out sections, not placeholders left as `TODO`

## Disclosure requirement

If you are submitting a skill, tool, or integration for a product you build,
maintain, or are paid to promote, say so directly in the pull request
description and in the skill's `author` field. Undisclosed commercial
submissions will be rejected. Disclosed ones are welcome as long as they meet
the acceptance criteria above — this is the same standard ReplyNodes' own
entry in this repository is held to.

## How to submit a skill

1. Fork the repository.
2. Copy [templates/SKILL.md](templates/SKILL.md) into the right category
   under `skills/<category>/your-skill-name.md`.
3. Fill in every section — see [docs/skill-format.md](docs/skill-format.md)
   for what each one should contain.
4. Add your skill to that category's `README.md` table.
5. Run `python3 scripts/generate_index.py` and commit the updated
   `index.json` — this also validates your frontmatter and will error if a
   required field is missing or `category` doesn't match the directory.
6. Open a pull request using the pull request template. For a new skill, you
   can also open an issue first using the **Skill submission** template if
   you want early feedback on the idea.

## How to submit a tool, MCP server, or integration

Open an issue using the **Tool submission** template, or a pull request
adding it to the relevant section of the main `README.md` and, if it's a
publishing/agent integration, `docs/agent-compatibility.md`.

## Review process

- A maintainer checks the submission against the criteria above.
- Small, clear fixes (typos, broken links, formatting) may be merged directly.
- New skills and tools start labeled **Community** and can be promoted to
  **Verified** or **Featured** after review — see
  [docs/quality-standards.md](docs/quality-standards.md).
- We may ask for changes before merging. This isn't a rejection — it's how
  most accepted submissions get merged.

## Style

- Write for a reader skimming in under a minute: short paragraphs, concrete
  examples, no filler.
- Use the terminology already established in this repo (see
  [docs/skill-format.md](docs/skill-format.md)) rather than inventing new
  category names.
- Markdown only for content files. Run a markdown linter locally if you have
  one; CI also checks formatting and links on every pull request.

## Code of conduct

Participation in this project is covered by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
