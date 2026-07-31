# Skill Format

Every skill in this repository follows the same structure so agents and
humans can rely on a consistent shape, regardless of which agent ecosystem
reads it. The format is [templates/SKILL.md](../templates/SKILL.md).

## Frontmatter fields

| Field | Required | Notes |
|---|---|---|
| `name` | Yes | Human-readable name |
| `description` | Yes | One sentence, no marketing language |
| `version` | Yes | Semantic version (`0.1.0` for new submissions) |
| `author` | Yes | Name, handle, or organization. Disclose commercial affiliation here. |
| `license` | Yes | SPDX identifier — `MIT` unless there's a specific reason otherwise |
| `category` | Yes | Must match one of the `skills/` directory names |
| `platforms` | Yes | One or more platforms this applies to, or `agnostic` |
| `agent_compatibility` | Yes | See [agent-compatibility.md](agent-compatibility.md) |
| `tags` | No | Free-form keywords for search |

## Body sections

**Purpose** — What the skill does and the outcome it produces, in one or two
sentences. A reader should be able to tell if this is the right skill
without reading further.

**When to use** — The specific situations that call for this skill. Include
what it's *not* for if there's a common point of confusion with a
similarly named skill.

**Inputs** — Every input the skill needs, in a table, marked required or
optional, with a short description of what it is and where it typically
comes from.

**Instructions** — Numbered, specific steps. This is the core of the skill.
Write it so that two different agents, given the same inputs, produce
comparably structured output. Avoid vague instructions like "write a good
post" — specify structure, constraints, and decision points instead.

**Output format** — The literal shape of the output: fields, ordering,
length limits, formatting. Show it, don't just describe it.

**Examples** — At least one realistic input/output pair. This is often what
makes a skill usable versus theoretical.

**Safety and quality checks** — What the agent should verify before
finalizing output (accuracy, tone, length, platform rules), and an explicit
note that the skill must not claim or imply guaranteed engagement, virality,
or revenue outcomes.

**Related skills** — Links to skills that are commonly used before or after
this one in a workflow.

## Naming and location

- File name: kebab-case, matching the skill name (`brand-voice-extractor.md`)
- Location: `skills/<category>/<skill-name>.md`
- One skill per file. If a submission covers multiple distinct capabilities,
  split it into separate skills and cross-link them under **Related skills**.

## Why a shared format

A consistent structure means a skill written for one agent ecosystem can be
read, evaluated, and adapted by another without guessing at intent. It also
means this repository could later be indexed or served programmatically
(see [templates/skill-metadata.yaml](../templates/skill-metadata.yaml))
without a rewrite.
