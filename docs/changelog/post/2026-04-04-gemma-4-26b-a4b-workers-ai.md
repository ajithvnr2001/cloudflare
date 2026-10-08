---
url: https://developers.cloudflare.com/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/
title: Google Gemma 4 26B A4B now available on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:44.750997+00:00
---

# Google Gemma 4 26B A4B now available on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 4, 2026

## Google Gemma 4 26B A4B now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are partnering with Google to bring [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/) to Workers AI. Gemma 4 26B A4B is a Mixture-of-Experts (MoE) model built from Gemini 3 research, with 26B total parameters and only 4B active per forward pass. By activating a small subset of parameters during inference, the model runs almost as fast as a 4B-parameter model while delivering the quality of a much larger one.

Gemma 4 is Google's most capable family of open models, designed to maximize intelligence-per-parameter.

#### Key capabilities

  * **Mixture-of-Experts architecture** with 8 active experts out of 128 total (plus 1 shared expert), delivering frontier-level performance at a fraction of the compute cost of dense models
  * **256,000 token context window** for retaining full conversation history, tool definitions, and long documents across extended sessions
  * **Built-in thinking mode** that lets the model reason step-by-step before answering, improving accuracy on complex tasks
  * **Vision understanding** for object detection, document and PDF parsing, screen and UI understanding, chart comprehension, OCR (including multilingual), and handwriting recognition, with support for variable aspect ratios and resolutions
  * **Function calling** with native support for structured tool use, enabling agentic workflows and multi-step planning
  * **Multilingual** with out-of-the-box support for 35+ languages, pre-trained on 140+ languages
  * **Coding** for code generation, completion, and correction



Use Gemma 4 26B A4B through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, or the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/).

For more information, refer to the [Gemma 4 26B A4B model page](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/).
