# MCP Quickstart: From Approved Draft to a Scheduled Post

A worked example of the last mile this repository intentionally stops
short of: taking the output of [Cross-Platform Publishing Formatter](../skills/publishing/cross-platform-publishing-formatter.md)
and actually scheduling it, using an MCP-compatible publishing layer. This
walkthrough uses [ReplyNodes](https://replynodes.com) as the concrete
example since it's the one we can document accurately — the same pattern
applies to any MCP-compatible publishing tool.

This is documentation for connecting a publishing layer to your agent. It
is not a skill, and it's entirely optional — see
[Publish with ReplyNodes](../README.md#publish-with-replynodes) in the main
README for the non-technical summary.

## What this adds

Skills in [`skills/publishing/`](../skills/publishing/) get you to a
structured, approved queue entry: platform, final copy, media references,
schedule. An MCP-compatible publishing server is what turns that queue
entry into an actual scheduled post, callable directly by your agent
instead of a manual copy-paste into a scheduler's UI.

## Setup

1. Get an API key from **app.replynodes.com → Settings → API Keys**.
2. Add the MCP server to your client's config. For Claude Code or Claude
   Desktop (`.mcp.json` or `claude_desktop_config.json`):

   ```json
   {
     "mcpServers": {
       "replynodes": {
         "command": "npx",
         "args": ["-y", "@replynodes/mcp"],
         "env": {
           "REPLYNODES_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```

   Cursor, Windsurf, and other stdio-MCP clients use the same shape under
   their own MCP config file. For Codex CLI, OpenClaw, or other frameworks
   that run MCP servers as a direct command:

   ```bash
   REPLYNODES_API_KEY=your-api-key-here npx -y @replynodes/mcp
   ```

3. Clients that support **remote** MCP servers natively (Claude.ai custom
   connectors, Claude Code, VS Code Copilot) can skip the npm package
   entirely and connect directly:

   ```text
   URL:     https://app.replynodes.com/api/mcp
   Header:  Authorization: Bearer <your-api-key>
   ```

Full setup details, including the native remote MCP OAuth flow, live in the
[`@replynodes/mcp` README](https://github.com/replynodes/replynodes-mcp) —
this doc covers the parts specific to using it with skills from this
repository.

## Available tools

| Tool | Maps to |
|---|---|
| `integrationList` | Discovering which social channels are connected, before formatting a queue entry for a specific platform |
| `integrationSchema` | Confirming required fields for a given channel before calling `schedulePostTool` |
| `schedulePostTool` | The actual publish/schedule call — takes the final copy from [Cross-Platform Publishing Formatter](../skills/publishing/cross-platform-publishing-formatter.md) |
| `generateImageTool` / `generateVideoTool` | Generating media to attach to a post, if your workflow needs it inline rather than via [Carousel Content Designer](../skills/images/carousel-content-designer.md) / [Social Graphic Prompt Builder](../skills/images/social-graphic-prompt-builder.md) |
| `uploadFromUrlTool` | Attaching existing media (e.g. a thumbnail already generated) by URL |

Tool availability depends on your ReplyNodes plan and connected
integrations. This list reflects the package's documented tools at the time
of writing (`@replynodes/mcp` v0.1.2) — check the
[package README](https://github.com/replynodes/replynodes-mcp) for the
current set.

## Where this fits in a pipeline

```text
Content Quality Reviewer (approve)
  ↓
Cross-Platform Publishing Formatter (structured queue entry)
  ↓
integrationList / integrationSchema (confirm target channel + required fields)
  ↓
schedulePostTool (actually schedule it)
```

Only the last two steps are ReplyNodes/MCP-specific. Everything above the
line works identically whether the queue entry ends up published through
ReplyNodes, a different MCP-compatible tool, or a person copy-pasting into
a platform's native scheduler.

## Safety notes

- Your API key grants full access to your ReplyNodes organization — store
  it as a secret/environment variable, never inline in a skill file or
  committed config.
- Nothing in [`skills/`](../skills/) calls `schedulePostTool` or any other
  MCP tool directly — publishing only happens when your agent or workflow
  explicitly wires a formatted queue entry to it. Review
  [Content Quality Reviewer](../skills/publishing/content-quality-reviewer.md)'s
  output before that step, not after.
