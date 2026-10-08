---
url: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/
title: Coding agents \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:30.544832+00:00
---

# Coding agents · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Integrations
  4. /Coding agents



# Coding agents

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhy route a coding agent through AI GatewaySet up your agentProtect sensitive code with DLPVerify it works

Coding agents send model requests to a provider on your behalf. By pointing the agent at AI Gateway instead of the provider, you observe and control that traffic without changing how you work.

## Why route a coding agent through AI Gateway

Routing a coding agent through AI Gateway gives you:

  * **Observability** — view every request, token count, and latency in the dashboard.
  * **Caching** — return [cached responses](https://developers.cloudflare.com/ai-gateway/features/caching/) for repeated prompts.
  * **Rate limiting** — cap request volume with [rate limiting](https://developers.cloudflare.com/ai-gateway/features/rate-limiting/).
  * **Cost tracking** — attribute spend across sessions and models.
  * **Data Loss Prevention** — scan prompts and responses for secrets, credentials, and other sensitive data with [DLP](https://developers.cloudflare.com/ai-gateway/features/dlp/).



## Set up your agent

Follow the setup guide for your coding agent:

  * [Claude Code](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/)
  * [Claude Desktop](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-desktop/)
  * [Gemini CLI](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/gemini-cli/)
  * [GitHub Copilot CLI](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/github-copilot-cli/)
  * [OpenAI Codex](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/openai-codex/)
  * [OpenCode](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/)
  * [Pi](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/)
  * [Visual Studio Code](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/vs-code/)
  * [Xcode](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/xcode/)



## Protect sensitive code with DLP

Coding agents routinely send source code, configuration files, and snippets to model providers. That traffic can include API keys, customer data, or other sensitive material. Because AI Gateway sits between the agent and the provider, you can inspect and control it without changing the agent.

[Data Loss Prevention (DLP)](https://developers.cloudflare.com/ai-gateway/features/dlp/) scans request and response bodies against [detection profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/) and either flags or blocks matches. Use it to catch secrets, credentials, or regulated data leaving (or returning to) the agent.

Note

Many coding agents stream responses by default. When DLP response scanning is enabled, AI Gateway buffers the full provider response before returning it, which increases time-to-first-token. If you need low-latency streaming, set the DLP policy **Check** to **Request** only, or use a separate gateway for latency-sensitive traffic. Refer to [streaming behavior](https://developers.cloudflare.com/ai-gateway/features/dlp/#streaming-behavior).

## Verify it works

After you configure a tool, confirm that traffic reaches AI Gateway.

  1. Send a prompt from the coding agent.

  2. In the Cloudflare dashboard, go to the **AI Gateway** page.

[ Go to **AI Gateway** ↗ ](https://dash.cloudflare.com/?to=/:account/ai/ai-gateway)
  3. Select your gateway, then select **Logs**. Confirm that the request appears with its model, token count, and latency.




For more information on logs, refer to [Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/).

[PreviousSet up Workers AI with AI Gateway](https://developers.cloudflare.com/ai-gateway/integrations/aig-workers-ai-binding/)[NextClaude Code](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/coding-agents/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
