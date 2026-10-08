---
url: https://developers.cloudflare.com/sandbox/coding-agents/
title: Run coding agents in a sandbox \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:16.492115+00:00
---

# Run coding agents in a sandbox · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/coding-agents/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /Coding agents



# Run coding agents in a sandbox

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/coding-agents/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewThe agent runs in your sandboxThe vendor runs the agent loopBuild your own agent

Coding agents such as Claude Code, Codex, and OpenCode can run a task on their own: they read a repository, edit files, and run commands until the task is done. Run the agent in a Linux sandbox so its commands stay inside a [Container](https://developers.cloudflare.com/containers/) that belongs to one task.

## The agent runs in your sandbox

Your Worker starts the sandbox, holds the credentials, and decides which hostnames the sandbox can reach. The agent calls its model over HTTP, for example through [AI Gateway](https://developers.cloudflare.com/ai-gateway/). Your Worker adds the API token to each request, so the sandbox never receives it.

Each guide in this section changes only the agent-specific parts of one runner. Build the runner first:

### [Build a coding agent runner](https://developers.cloudflare.com/sandbox/get-started/build-a-coding-agent-runner/)

Build a Worker that runs Claude Code on a GitHub repository in a sandbox and returns its changes as a diff.

Then switch the runner to another agent:

### [Claude Code](https://developers.cloudflare.com/sandbox/coding-agents/claude-code/)

Edit a GitHub repository with Claude Code, which calls Anthropic models through AI Gateway.

### [Codex](https://developers.cloudflare.com/sandbox/coding-agents/codex/)

Edit a GitHub repository with the Codex CLI, which calls OpenAI models through AI Gateway.

### [OpenCode](https://developers.cloudflare.com/sandbox/coding-agents/opencode/)

Edit a GitHub repository with OpenCode, which calls models through AI Gateway.

### [Pi](https://developers.cloudflare.com/sandbox/coding-agents/pi/)

Edit a GitHub repository with Pi, which calls models through its built-in AI Gateway provider.

## The vendor runs the agent loop

Devin, Cursor, Claude Managed Agents, and the OpenAI Agents API run their agent loop in their own service. The loop sends commands and file edits to sandboxes in your Cloudflare account. Each vendor template gives every session its own sandbox. In the Devin, Cursor, and OpenAI Agents API templates, the vendor worker process runs inside the sandbox, so the sandbox also holds a vendor credential.

### [Devin](https://developers.cloudflare.com/sandbox/coding-agents/devin/)

Deploy a Devin Outpost that runs each Devin session in its own sandbox on Containers.

### [Cursor Cloud Agents](https://developers.cloudflare.com/sandbox/coding-agents/cursor/)

Deploy self-hosted machines that run each Cursor session in its own sandbox on Containers.

### [Claude Managed Agents](https://developers.cloudflare.com/sandbox/coding-agents/claude-managed-agents/)

Run Claude Managed Agents sessions in sandboxes on Containers and Dynamic Workers.

### [OpenAI Agents API](https://developers.cloudflare.com/sandbox/coding-agents/openai-agents-api/)

Deploy a self-hosted environment that runs each Codex session in its own sandbox on Containers.

## Build your own agent

To give an agent that runs in a Durable Object a container to run commands in, refer to [Sandbox](https://developers.cloudflare.com/agents/tools/sandbox/) in the Agents SDK documentation.

[PreviousRun code when a sandbox stops](https://developers.cloudflare.com/sandbox/manage/run-code-when-a-sandbox-stops/)[NextClaude Code](https://developers.cloudflare.com/sandbox/coding-agents/claude-code/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/coding-agents/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
