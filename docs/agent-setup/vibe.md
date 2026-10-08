---
url: https://developers.cloudflare.com/agent-setup/vibe/
title: Vibe + Cloudflare \u00b7 Agent setup docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:06.132615+00:00
---

# Vibe + Cloudflare · Agent setup docs

> Source: https://developers.cloudflare.com/agent-setup/vibe/

[All agents](https://developers.cloudflare.com/agent-setup/)

![](https://developers.cloudflare.com/icons/agents/vibe/light.svg)![](https://developers.cloudflare.com/icons/agents/vibe/dark.svg)

Mistral AI

# Vibe + Cloudflare

Coding agent for terminal, IDE, and cloud workflows that reads files, runs commands, writes code, and opens pull requests. Made by Mistral AI.

IDETerminalStandaloneCloudExtensionOpen Source

[Cloudflare Skills](https://github.com/cloudflare/skills)·[Cloudflare Code Mode API MCP](https://github.com/cloudflare/mcp)·[Cloudflare Domain Specific MCPs](https://github.com/cloudflare/mcp-server-cloudflare)·[CLI](https://docs.mistral.ai/vibe/code/cli/install-setup)·[Vibe Docs](https://docs.mistral.ai/vibe/code/overview)

## Quick start

  1. **Install Vibe**

Install the Vibe command-line interface (CLI) on macOS or Linux. For other installation methods, refer to the [Vibe installation guide ↗︎](https://docs.mistral.ai/vibe/code/cli/install-setup).
         
         curl -LsSf https://mistral.ai/vibe/install.sh | bash

  2. **Set up Vibe**

Complete the setup flow. Sign in with your Mistral account or enter an API key.
         
         vibe --setup

  3. **Install Cloudflare Skills**

From your project root, install Cloudflare Skills for the current project. Vibe discovers project Skills from `.agents/skills/`.

npmyarnpnpm
         
         npx skills add cloudflare/skills --skill '*' --yes
         
         yarn dlx skills add cloudflare/skills --skill '*' --yes
         
         pnpx skills add cloudflare/skills --skill '*' --yes

  4. **Add the Cloudflare MCP server**

Add the Cloudflare Model Context Protocol (MCP) server to `~/.vibe/config.toml`. Back up an existing file and preserve unrelated settings. Update entries that already exist instead of adding duplicates.
         
         [[mcp_servers]]
         name = "cloudflare"
         transport = "streamable-http"
         url = "https://mcp.cloudflare.com/mcp"
         
         [mcp_servers.auth]
         type = "oauth"
         scopes = []

For source and configuration details, refer to [cloudflare/mcp ↗︎](https://github.com/cloudflare/mcp) and [cloudflare/mcp-server-cloudflare ↗︎](https://github.com/cloudflare/mcp-server-cloudflare).

  5. **Launch and authorize Vibe**

Start Vibe from your project root. For an existing project, use the directory that contains `wrangler.jsonc`.
         
         vibe

If Vibe is already running, enter `/reload` instead. Then enter `/mcp status` to check the server. Authorize the Cloudflare MCP server:
         
         /mcp login cloudflare

Complete the OAuth flow in your browser.

  6. **Try a prompt**

For example:
         
         Optimize my Worker to serve WebP images with responsive resizing using Cloudflare Images.




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
    
    
    Connect my Worker to an existing Postgres database using Hyperdrive for connection pooling.
    
    
    Set up a Waiting Room to handle flash sale traffic spikes without dropping requests.
    
    
    Check my Workers deployment logs for errors and suggest fixes.
    
    
    Build a multi-tenant SaaS backend where each customer gets an isolated D1 database.
    
    
    Add a cron trigger to my Worker that processes a job queue every hour.

## Tips

  * The Cloudflare API MCP server uses Code Mode — Vibe writes JavaScript against a typed API to reach any of 2,500+ endpoints in ~1,000 tokens.
  * Store project instructions in `AGENTS.md`. Vibe loads instructions from the project root and relevant subdirectories.
  * Start Vibe with `vibe --agent plan` to inspect a project without modifying it.



## FAQ

Should I use Skills, MCP servers, Wrangler CLI, or all three?

Use all three. Skills provide Cloudflare implementation guidance. MCP servers provide current documentation and authenticated API tools. Wrangler handles local development, deployments, and Workers-specific commands.

How do I give Vibe access to my Cloudflare account?

Run `/mcp login cloudflare`, then complete the authorization flow in your browser.

Can I use another model provider with Vibe?

Yes. Vibe supports Mistral-hosted models, compatible API providers, and local models. Configure models and providers in `~/.vibe/config.toml`.

Is Vibe open source?

Yes. The Vibe CLI is available under the Apache 2.0 license in the [mistralai/mistral-vibe ↗︎](https://github.com/mistralai/mistral-vibe) repository.

## Troubleshooting

MCP server not connecting

Confirm that the entries in `~/.vibe/config.toml` match the quick start. Enter `/reload`, then enter `/mcp status`. If a server reports `needs_auth`, enter `/mcp login <name>`.

MCP server authentication fails

Enter `/mcp logout cloudflare`, then enter `/mcp login cloudflare`. Complete the new authorization flow in your browser.

Cloudflare Skills are not available

Enter `/reload` to reload Vibe configuration and Skills. If the Skills still do not load, confirm that the installer wrote them to the project `.agents/skills/` directory.

Getting outdated information about Cloudflare products

Point Vibe to [developers.cloudflare.com/llms.txt](https://developers.cloudflare.com/llms.txt) for a directory of all products. Use `developers.cloudflare.com/<product>/llms.txt` for a product-specific index.

## Build agents on Cloudflare

Cloudflare is not just a deploy target for agents, it is a full stack for building your own.

[Agents SDKStateful AI agents with state, scheduling, RPC, email, streaming chat — and the Code Mode SDK for token-efficient tool use.Learn more](https://developers.cloudflare.com/agents/)[Build an MCP serverShip a remote MCP server on Workers with OAuth, durable state, and streamable HTTP transport.Learn more](https://developers.cloudflare.com/agents/model-context-protocol/)[Workers AIRun open-source LLMs, embedding models, and image models at the edge. Use it as your agent's model provider.Learn more](https://developers.cloudflare.com/workers-ai/)[Worker LoaderLoad user-generated code into isolated Workers on demand. The secure sandbox behind Code Mode.Learn more](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/)

## Other agents

[![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)AnthropicClaude CodeTerminal-based coding agent that understands your codebase, runs commands, edits files, and manages git. Made by Anthropic.View guide](https://developers.cloudflare.com/agent-setup/claude-code/)[![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)OpenAICodexOpenAI coding agent available as a terminal CLI and desktop app. It reads and writes files, runs commands, and browses the web in a sandbox.View guide](https://developers.cloudflare.com/agent-setup/codex/)[![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)CursorCursorAI-first IDE built on VS Code with multi-file Composer edits and background agents. Made by Cursor.View guide](https://developers.cloudflare.com/agent-setup/cursor/)[![](https://developers.cloudflare.com/icons/agents/copilot/light.svg)![](https://developers.cloudflare.com/icons/agents/copilot/dark.svg)GitHubGitHub CopilotEditor extension and CLI with agent mode, workspace context, and native PR integration. Made by GitHub.View guide](https://developers.cloudflare.com/agent-setup/github-copilot/)[![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)AnomalyOpenCodeOpen-source terminal agent with a rich TUI that works with 75+ LLMs. Made by Anomaly.View guide](https://developers.cloudflare.com/agent-setup/opencode/)[![](https://developers.cloudflare.com/icons/agents/devin/light.svg)![](https://developers.cloudflare.com/icons/agents/devin/dark.svg)CognitionDevinA full IDE with an agent manager built in — the command center for managing all your agents in one place. Made by Cognition.View guide](https://developers.cloudflare.com/agent-setup/devin/)[![](https://developers.cloudflare.com/icons/agents/visual-studio-code/light.svg)![](https://developers.cloudflare.com/icons/agents/visual-studio-code/dark.svg)MicrosoftVisual Studio CodeFree, open-source code editor with native Model Context Protocol (MCP) client support and Copilot Chat integration. Made by Microsoft.View guide](https://developers.cloudflare.com/agent-setup/visual-studio-code/)[![](https://developers.cloudflare.com/icons/agents/command-code/light.svg)![](https://developers.cloudflare.com/icons/agents/command-code/dark.svg)Command CodeCommand CodeCommand Code is one of the most used coding agents for open models. It automatically learns your coding taste and self-improves as you work.View guide](https://developers.cloudflare.com/agent-setup/command-code/)[![](https://developers.cloudflare.com/icons/agents/bionic/light.svg)![](https://developers.cloudflare.com/icons/agents/bionic/dark.svg)LM StudioBionicPowerful agent for coding and work. Natively local, with open models in the cloud. By LM Studio.View guide](https://developers.cloudflare.com/agent-setup/bionic/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agent-setup/vibe.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
