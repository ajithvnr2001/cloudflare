---
url: https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/
title: New Workers AI text generation models in AI Search \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:11.112071+00:00
---

# New Workers AI text generation models in AI Search · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 26, 2026

## New Workers AI text generation models in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-new-workers-ai-models/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports six additional [Workers AI](https://developers.cloudflare.com/workers-ai/) models for text generation:

Model | Context window (tokens)  
---|---  
`@cf/deepseek-ai/deepseek-v4-flash-0731` | 1,048,576  
`@cf/deepseek-ai/deepseek-v4-pro-0813` | 1,048,576  
`@cf/openai/gpt-oss-120b` | 128,000  
`@cf/openai/gpt-oss-20b` | 128,000  
`@cf/qwen/qwen3.8-27b` | 262,144  
`@cf/moonshotai/kimi-k2.7-code` | 262,144  
  
These models run on Workers AI, so they do not require an additional provider key. Select a model when creating or updating an AI Search instance in the dashboard or through the API.

For the full list of supported models, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).
