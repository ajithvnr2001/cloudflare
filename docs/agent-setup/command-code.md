---
url: https://developers.cloudflare.com/agent-setup/command-code/
title: Command Code + Cloudflare \u00b7 Agent setup docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:06.368325+00:00
---

# Command Code + Cloudflare · Agent setup docs

> Source: https://developers.cloudflare.com/agent-setup/command-code/

[All agents](https://developers.cloudflare.com/agent-setup/)

![](https://developers.cloudflare.com/icons/agents/command-code/light.svg)![](https://developers.cloudflare.com/icons/agents/command-code/dark.svg)

Command Code

# Command Code + Cloudflare

Command Code is one of the most used coding agents for open models. It automatically learns your coding taste and self-improves as you work.

TerminalStandaloneCloudExtension

[Cloudflare Skills](https://github.com/cloudflare/skills)·[Cloudflare Code Mode API MCP](https://github.com/cloudflare/mcp)·[Cloudflare Domain Specific MCPs](https://github.com/cloudflare/mcp-server-cloudflare)·[CLI](https://commandcode.ai/docs/reference/cli)·[Command Code Docs](https://commandcode.ai/docs)

## Quick start

  1. **Install Command Code**

Install [Command Code ↗︎](https://commandcode.ai). For the full walkthrough, refer to the [Command Code quickstart ↗︎](https://commandcode.ai/docs/quickstart).
         
         npm i -g command-code@latest

This installs the `command-code` CLI, with the alias `cmd`. On Windows, the alias is `cmdc`. For the full list of models you can run, refer to [Available Models ↗︎](https://commandcode.ai/docs/reference/cli/models).

  2. **Open your Cloudflare project**

Change into the directory that contains your Cloudflare project, where `wrangler.jsonc` lives (if it already exists):
         
         cd my-worker

  3. **Install Cloudflare Skills**
         
         cmd skills add https://github.com/cloudflare/skills

This installs the Cloudflare Skills into `.commandcode/skills/`, including `wrangler`, `workers-best-practices`, `durable-objects`, and `agents-sdk`. Pass `--skill <name>` to install a single skill, or `--global` to install into `~/.commandcode/skills/` for every project. For more information, refer to [Command Code Skills ↗︎](https://commandcode.ai/docs/skills).

  4. **Add the Cloudflare MCP server**
         
         cmd mcp add --transport http cloudflare https://mcp.cloudflare.com/mcp

Complete the OAuth flow in your browser when Command Code prompts you, then choose the permissions to grant. For scopes, transports, and per-project configuration, refer to [Command Code MCP ↗︎](https://commandcode.ai/docs/mcp).

  5. **Start a session and try a prompt**
         
         cmd

Ask Command Code to investigate a task, make changes, and run the relevant tests. Review its diffs and command output before keeping changes.

For example:
         
         Add a D1 database to my Worker and create a users table with full CRUD endpoints.




## Cloudflare platform access

Expand any section to learn more.

Cloudflare Skills

Persistent platform context that teaches the agent how Cloudflare works.

Skills are instructions the agent loads on demand. The [cloudflare/skills](https://github.com/cloudflare/skills) bundle covers every layer of the platform — so the agent knows your conventions without you re-explaining them.

  * agents-sdkBuild, debug, or review Cloudflare Agents SDK applications using the agents package.
  * basinBuild and troubleshoot Cloudflare Basin analytics workflows with Basin Pipelines, Basin Catalog, and Basin SQL. Use for streaming data into R2 Iceberg tables, managing catalogs, or querying those tables; also use for requests using the former Data Platform, Pipelines, R2 Data Catalog, or R2 SQL names.
  * cloudflareDiscover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. Use for architecture and product selection, including when the user describes a need without naming a Cloudflare product; then find the relevant skill or documentation.
  * cloudflare-email-serviceImplement or troubleshoot Cloudflare Email Sending and Email Routing integrations and their delivery configuration.
  * cloudflare-oneDesign, configure, troubleshoot, or review Cloudflare One Zero Trust and SASE deployments. Use cloudflare-one-migrations for migration planning from other vendors.
  * cloudflare-one-migrationsAssess and plan migrations from existing VPN, SWG, or SASE platforms to Cloudflare One, including policy mapping, parity gaps, and rollout.
  * durable-objectsBuild, debug, or review Cloudflare Durable Objects code for persistent state and coordination.
  * k2Build and troubleshoot Cloudflare K2 or K2 Streams durable logs. Use for stream setup, producing from Workers or HTTP, configuring retention and inputs, and consuming through subscriptions.
  * nextjs-on-cloudflareBuild, migrate, and deploy Next.js apps on Cloudflare Workers with vinext. Use when starting a Next.js project on Cloudflare, moving an existing app to Workers, choosing between vinext and OpenNext, or setting up vinext for Workers. For setup, migration, or deployment, install vinext's upstream skills with `npx skills add cloudflare/vinext` if missing, then read and follow the applicable skill and docs.
  * sandbox-migrate-to-nextMigrate Cloudflare Sandbox apps from stable @cloudflare/sandbox to @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-next for apps already on the preview.
  * sandbox-nextBuild or maintain Cloudflare Sandbox apps on @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-migrate-to-next when porting a stable app.
  * sandbox-stableBuild or maintain Cloudflare Sandbox apps on the stable @cloudflare/sandbox package. Use sandbox-next for preview apps and sandbox-migrate-to-next for stable-to-preview migrations.
  * turnstile-spinSet up, repair, or migrate to Cloudflare Turnstile bot verification in an existing frontend and backend, including server-side Siteverify.
  * web-perfAudit, diagnose, or optimize website loading and interaction performance, Core Web Vitals, and Lighthouse performance scores.
  * workers-best-practicesCloudflare Workers best practices for production applications. Use when writing, reviewing, or configuring Workers.
  * wranglerRun or troubleshoot Wrangler CLI commands and configure Worker projects for local development, Previews, deployment, and Cloudflare resource management.



MCP servers

Live access to the Cloudflare API, docs, and observability.

MCP servers provide typed tools to call into Cloudflare at runtime. There are two options: [Code Mode](https://blog.cloudflare.com/code-mode-mcp/) — a single server that covers the entire Cloudflare API (2,500+ endpoints in ~1,000 tokens) — or a set of focused, domain-specific servers hosted in the [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) repo. The full catalog is also in the [MCP servers for Cloudflare](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) docs.

  * Code mode APIcode modeBroad access to the full Cloudflare API via code execution, with minimal token overheadhttps://mcp.cloudflare.com/mcp
  * Code Mode servercode modeBest when you want broad access across Cloudflare's APIs through code executionhttps://mcp.cloudflare.com/mcp
  * Browser Run serverFetch web pages, convert them to markdown and take screenshotshttps://browser.mcp.cloudflare.com/mcp
  * Cloudflare Blog serverSearch and read posts from the Cloudflare Bloghttps://blog.mcp.cloudflare.com/mcp
  * Cloudflare One CASB serverQuickly identify any security misconfigurations for SaaS applications to safeguard users & datahttps://casb.mcp.cloudflare.com/mcp
  * Container serverSpin up a sandbox development environmenthttps://containers.mcp.cloudflare.com/mcp
  * Demo Day serverDemonstrate a minimal Cloudflare MCP serverhttps://demo-day.mcp.cloudflare.com/mcp
  * Digital Experience Monitoring serverGet quick insight on critical applications for your organizationhttps://dex.mcp.cloudflare.com/mcp
  * Documentation serverGet up-to-date reference information on Cloudflarehttps://docs.mcp.cloudflare.com/mcp



Wrangler CLI

Local dev, deploys, and Workers-specific commands.

Use [Wrangler](https://developers.cloudflare.com/workers/wrangler/) for local development, deploys, and product-specific commands like `wrangler d1 migrations apply` or `wrangler tail`. The bundled **wrangler** Skill teaches the agent when to reach for it.

Cloudflare CLI (beta)

The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, covers the public Cloudflare API and prints JSON output. Install it with `npm install -g cf`, then follow [Use cf with AI agents](https://developers.cloudflare.com/cf/agents/).

Agent-friendly docs

Token-efficient references optimized for agents.

Append `/index.md` to any Cloudflare docs URL for a clean markdown version. Every top-level product section also has its own `llms.txt` — a page index sized for a single context window. A few useful ones:

  * [developers.cloudflare.com/llms.txt](https://developers.cloudflare.com/llms.txt) — directory of every Cloudflare product.
  * [developers.cloudflare.com/workers/llms.txt](https://developers.cloudflare.com/workers/llms.txt)
  * [developers.cloudflare.com/agents/llms.txt](https://developers.cloudflare.com/agents/llms.txt)
  * [developers.cloudflare.com/r2/llms.txt](https://developers.cloudflare.com/r2/llms.txt)
  * [developers.cloudflare.com/d1/llms.txt](https://developers.cloudflare.com/d1/llms.txt)



For a full overview of how these docs are structured for agents, refer to the [Docs for Agents guide](https://developers.cloudflare.com/docs-for-agents/).

## Example prompts
    
    
    Set up WAF rules to block SQL injection and XSS attacks on my application.
    
    
    Configure Zero Trust access policies to protect my internal staging environment.
    
    
    Add a cron trigger to my Worker that processes a job queue every hour.
    
    
    Build an AI chat agent using the Cloudflare Agents SDK with persistent conversation history stored in D1.
    
    
    Set up custom domains with automatic SSL for my SaaS customers using SSL for SaaS.

## Tips

  * Install Cloudflare Skills first. They give Command Code persistent Cloudflare knowledge without spending tokens on tool schemas, so reach for them before adding MCP servers.
  * `cmd skills add` writes to `.commandcode/skills/` for the current project. Add `--global` to install into `~/.commandcode/skills/` and make the skills available everywhere.
  * The MCP server is saved to your local config by default. Optionally, add `--scope project` to save it to `.mcp.json` instead and share it with your team.
  * Use the Cloudflare API MCP server for account resources and domain-specific servers for focused workflows.
  * Record project conventions in `AGENTS.md` so they carry across sessions. Refer to [Memory ↗︎](https://commandcode.ai/docs/memory) for where Command Code reads and writes them.



## FAQ

Should I use Skills, the MCP server, Wrangler CLI, or all of them?

All three, and start with Skills. Skills give Command Code persistent Cloudflare expertise: when to reach for Durable Objects over KV, how to structure a Workers project, and when to call the CLI instead of the API. The Cloudflare API MCP server handles account operations, such as DNS, WAF, R2, and Zero Trust. Wrangler handles local development, deployments, and migrations. Command Code runs local shell commands, so it can call Wrangler directly.

How do I give Command Code access to my Cloudflare account?

Run `cmd mcp add --transport http cloudflare https://mcp.cloudflare.com/mcp`. When Command Code prompts you, complete the OAuth flow in your browser and choose the permissions to grant.

Where does cmd skills add install the Cloudflare Skills?

Into `.commandcode/skills/` for the current project, or `~/.commandcode/skills/` when you pass `--global`. Run `cmd skills list` to confirm what is installed.

What does Code Mode mean for MCP?

Code Mode is how the Cloudflare API MCP server fits all 2,500+ API endpoints into about 1,000 tokens. Instead of exposing every endpoint as a separate tool, it exposes `search()` and `execute()`. Command Code writes JavaScript to call them. For more information, refer to [Code Mode ↗︎](https://blog.cloudflare.com/code-mode-mcp/).

Which models can I use with Command Code?

Command Code works with models from Anthropic, OpenAI, Moonshot, DeepSeek, Z.ai, Alibaba, MiniMax, and others. Run `cmd --list-models` to see what is available to you, or `/model` to switch inside a session. For the current list, refer to [Available Models ↗︎](https://commandcode.ai/docs/reference/cli/models).

How does Command Code learn my coding style?

Through Taste. Every accept, reject, and edit becomes a signal, and the learned preferences are stored in taste packages that you can share across projects and with your team. For more information, refer to [Taste ↗︎](https://commandcode.ai/docs/taste).

Can I run Command Code in CI against my Workers project?

Yes. Headless mode runs Command Code non-interactively, so it can lint, test, or deploy a Worker from a pipeline. For more information, refer to [Headless Mode ↗︎](https://commandcode.ai/docs/headless).

Is Command Code open source?

No. Command Code is a commercial product with a subscription plan. For details, refer to [Pricing and Limits ↗︎](https://commandcode.ai/docs/resources/pricing-limits).

## Troubleshooting

MCP server not connecting

Run `cmd mcp list` to check the server status. Confirm that the server URL is `https://mcp.cloudflare.com/mcp` and that you passed `--transport http`. Remove the server with `cmd mcp remove cloudflare` and add it again.

Getting outdated information about Cloudflare products

Point Command Code to [developers.cloudflare.com/llms.txt](https://developers.cloudflare.com/llms.txt) for a directory of all products, or `developers.cloudflare.com/<product>/llms.txt` for a product-specific index.

MCP server authentication fails

Remove and re-add the MCP server. When Command Code prompts you, complete the OAuth flow in your browser.

## Build agents on Cloudflare

Cloudflare is not just a deploy target for agents, it is a full stack for building your own.

[Agents SDKStateful AI agents with state, scheduling, RPC, email, streaming chat — and the Code Mode SDK for token-efficient tool use.Learn more](https://developers.cloudflare.com/agents/)[Build an MCP serverShip a remote MCP server on Workers with OAuth, durable state, and streamable HTTP transport.Learn more](https://developers.cloudflare.com/agents/model-context-protocol/)[Workers AIRun open-source LLMs, embedding models, and image models at the edge. Use it as your agent's model provider.Learn more](https://developers.cloudflare.com/workers-ai/)[Worker LoaderLoad user-generated code into isolated Workers on demand. The secure sandbox behind Code Mode.Learn more](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/)

## Other agents

[![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)AnthropicClaude CodeTerminal-based coding agent that understands your codebase, runs commands, edits files, and manages git. Made by Anthropic.View guide](https://developers.cloudflare.com/agent-setup/claude-code/)[![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)OpenAICodexOpenAI coding agent available as a terminal CLI and desktop app. It reads and writes files, runs commands, and browses the web in a sandbox.View guide](https://developers.cloudflare.com/agent-setup/codex/)[![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)CursorCursorAI-first IDE built on VS Code with multi-file Composer edits and background agents. Made by Cursor.View guide](https://developers.cloudflare.com/agent-setup/cursor/)[![](https://developers.cloudflare.com/icons/agents/copilot/light.svg)![](https://developers.cloudflare.com/icons/agents/copilot/dark.svg)GitHubGitHub CopilotEditor extension and CLI with agent mode, workspace context, and native PR integration. Made by GitHub.View guide](https://developers.cloudflare.com/agent-setup/github-copilot/)[![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)AnomalyOpenCodeOpen-source terminal agent with a rich TUI that works with 75+ LLMs. Made by Anomaly.View guide](https://developers.cloudflare.com/agent-setup/opencode/)[![](https://developers.cloudflare.com/icons/agents/vibe/light.svg)![](https://developers.cloudflare.com/icons/agents/vibe/dark.svg)Mistral AIVibeCoding agent for terminal, IDE, and cloud workflows that reads files, runs commands, writes code, and opens pull requests. Made by Mistral AI.View guide](https://developers.cloudflare.com/agent-setup/vibe/)[![](https://developers.cloudflare.com/icons/agents/devin/light.svg)![](https://developers.cloudflare.com/icons/agents/devin/dark.svg)CognitionDevinA full IDE with an agent manager built in — the command center for managing all your agents in one place. Made by Cognition.View guide](https://developers.cloudflare.com/agent-setup/devin/)[![](https://developers.cloudflare.com/icons/agents/visual-studio-code/light.svg)![](https://developers.cloudflare.com/icons/agents/visual-studio-code/dark.svg)MicrosoftVisual Studio CodeFree, open-source code editor with native Model Context Protocol (MCP) client support and Copilot Chat integration. Made by Microsoft.View guide](https://developers.cloudflare.com/agent-setup/visual-studio-code/)[![](https://developers.cloudflare.com/icons/agents/bionic/light.svg)![](https://developers.cloudflare.com/icons/agents/bionic/dark.svg)LM StudioBionicPowerful agent for coding and work. Natively local, with open models in the cloud. By LM Studio.View guide](https://developers.cloudflare.com/agent-setup/bionic/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agent-setup/command-code.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
