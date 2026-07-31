# Security Policy

This repository is a curated collection of documentation, prompts, and
markdown-based agent skills. It does not ship executable application code or
run a hosted service, but skills and examples can include shell commands,
API usage patterns, and links to third-party tools — so security issues are
still possible and worth reporting.

## What counts as a security issue here

- A skill or example that instructs an agent to run unsafe commands
  (destructive shell operations, credential exfiltration, unsafe `eval`, etc.)
- A submitted tool or MCP integration with a known vulnerability
- A workflow that could leak API keys, tokens, or private content by design
- Malicious links or supply-chain risks in referenced packages

## Reporting a vulnerability

Please **do not** open a public issue for security reports.

Instead, email `security@replynodes.com` (placeholder — update once a
dedicated address exists) with:

- A description of the issue and where it lives in the repository
- Steps to reproduce or a proof of concept, if applicable
- The potential impact as you understand it

We aim to acknowledge reports within 5 business days. Once a fix or removal
is agreed, we'll credit the reporter (if desired) in the relevant pull
request or release notes.

## Supported scope

Security review here means "structurally sound and not obviously harmful,"
not a formal audit. See [docs/quality-standards.md](docs/quality-standards.md)
for what the **Featured**, **Verified**, and **Community** labels do and do
not guarantee.
