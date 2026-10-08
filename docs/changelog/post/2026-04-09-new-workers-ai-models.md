---
url: https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/
title: New Workers AI models for text generation and embedding in AI Search \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:45.766559+00:00
---

# New Workers AI models for text generation and embedding in AI Search · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 8, 2026

## New Workers AI models for text generation and embedding in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-09-new-workers-ai-models/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports four additional [Workers AI](https://developers.cloudflare.com/workers-ai/) models across text generation and embedding.

#### Text generation

Model | Context window (tokens)  
---|---  
`@cf/zai-org/glm-4.7-flash` | 131,072  
`@cf/qwen/qwen3-30b-a3b-fp8` | 32,000  
  
GLM-4.7-Flash is a lightweight model from Zhipu AI with a 131,072 token context window, suitable for long-document summarization and retrieval tasks. Qwen3-30B-A3B is a mixture-of-experts model from Alibaba that activates only 3 billion parameters per forward pass, keeping inference fast while maintaining strong response quality.

#### Embedding

Model | Vector dims | Input tokens | Metric  
---|---|---|---  
`@cf/qwen/qwen3-embedding-0.6b` | 1,024 | 4,096 | cosine  
`@cf/google/embeddinggemma-300m` | 768 | 512 | cosine  
  
Qwen3-Embedding-0.6B supports up to 4,096 input tokens, making it a good fit for indexing longer text chunks. EmbeddingGemma-300M from Google produces 768-dimension vectors and is optimized for low-latency embedding workloads.

All four models are available without additional provider keys since they run on Workers AI. Select them when creating or updating an AI Search instance in the dashboard or through the API.

For the full list of supported models, refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/).
