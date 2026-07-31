# Agent Compatibility

Skills in this repository are plain markdown with structured frontmatter —
not tied to a single agent runtime. Compatibility labels describe how
directly a skill can be used in a given environment, nothing more.

## What compatibility means (and doesn't)

A compatibility label means: *this skill's format and instructions can be
used or adapted in this environment.* It does **not** mean:

- Official support or endorsement by that agent's maintainers
- That the skill has been tested against that specific agent
- Any partnership between this repository and the named agent projects

Claude Code, Codex, OpenClaw, Hermes, and MCP are independent projects.
Their names are used here only to describe compatibility, not affiliation.

## Labels

| Label | What it means |
|---|---|
| `agent-agnostic` | Plain instructions and structured output with no runtime-specific syntax. Usable as a prompt, a system message, or pasted directly into any agent's context. |
| `claude-code-compatible` | Structured to work well as a [Claude Code skill](https://docs.claude.com/en/docs/claude-code) — can be dropped into a `.claude/skills/` directory largely as-is. |
| `codex-compatible` | Written in a way that works as a reusable instruction set for Codex-based agents. |
| `openclaw-compatible` | Compatible with OpenClaw's agent skill conventions. |
| `mcp-compatible` | The skill's instructions reference or assume MCP tool calls (e.g. a publishing or scheduling MCP server) rather than being purely text-generation. |

A skill can carry more than one label. Most skills in this repo are
`agent-agnostic` by default, since the instructions are plain markdown — the
more specific labels flag where a skill has been structured with a
particular runtime's conventions in mind.

## How to apply a label

If you're submitting a skill, add every label that honestly applies. If
you're not sure whether a label applies, default to `agent-agnostic` and let
a maintainer or later contributor add more specific labels once it's been
tried in that environment.

## Using a skill in your agent

Most skills can be used by:

1. Copying the skill's markdown into your agent's system prompt, skill
   directory, or tool description, depending on your runtime's conventions.
2. Supplying the inputs listed in the skill's **Inputs** section.
3. Letting the agent follow the **Instructions** and produce output in the
   documented **Output format**.

For MCP-based publishing (moving from drafted content to actually posting or
scheduling it), see [Publish with ReplyNodes](../README.md#publish-with-replynodes)
in the main README — publishing is intentionally kept separate from content
creation so any MCP-compatible publishing layer can be swapped in.
