---
url: https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/
title: DeepSeek V4 Flash and Pro now available on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:08.553199+00:00
---

# DeepSeek V4 Flash and Pro now available on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 14, 2026

## DeepSeek V4 Flash and Pro now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/deepseek-ai/deepseek-v4-pro-0813`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-pro-0813/) and [`@cf/deepseek-ai/deepseek-v4-flash-0731`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/) are now available on Workers AI.

DeepSeek V4 Flash and DeepSeek V4 Pro are the first Workers AI models with a full **one million (1,048,576) token context window**. Use them for long-horizon agentic workflows, large codebases, and multi-step reasoning that exceed the context limits of every other model hosted on the platform.

DeepSeek V4 Flash is the faster, lower-cost sibling. This release supersedes the preview version with substantially enhanced agentic capabilities.

**Key capabilities:**

  * **Reasoning** : Both models support thinking mode for complex, step-by-step problem-solving.
  * **Function calling** : Build agents that invoke tools and APIs across multiple conversation turns.
  * **Long context** : Both models support a full 1,048,576 token context window.



Both models require the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use these models through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [DeepSeek V4 Pro model page](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-pro-0813/), the [DeepSeek V4 Flash model page](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/), and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).
