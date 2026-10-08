---
url: https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/
title: Moonshot AI Kimi K2.7 Code now available on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:57.651287+00:00
---

# Moonshot AI Kimi K2.7 Code now available on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 12, 2026

## Moonshot AI Kimi K2.7 Code now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.

#### Improved coding and agent performance

K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:

  * **+21.8%** on Kimi Code Bench v2
  * **+11.0%** on Program Bench
  * **+31.5%** on MLS Bench Lite



#### Reasoning efficiency

K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.

#### Key capabilities

  * **262.1k token context window** for retaining full conversation history, tool definitions, and codebases across long-running agent sessions
  * **Long-horizon coding** with improved instruction following and higher end-to-end coding task success rates
  * **Vision inputs** for processing images alongside text
  * **Thinking mode** with configurable reasoning depth via `chat_template_kwargs.thinking`
  * **Multi-turn tool calling** for building agents that invoke tools across multiple conversation turns
  * **Structured outputs** with JSON schema support



#### Differences from Kimi K2.6

If you are migrating from Kimi K2.6, note the following:

  * K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency
  * Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)
  * API usage is identical — no parameter changes required



#### Get started

Use Kimi K2.7 Code through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/ai/run`, or the OpenAI-compatible endpoint at `/v1/chat/completions`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with any of these endpoints.

For more information, refer to the [Kimi K2.7 Code model page](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).
