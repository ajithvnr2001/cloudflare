---
url: https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/
title: Introducing EmbeddingGemma from Google on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.179311+00:00
---

# Introducing EmbeddingGemma from Google on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-05-embeddinggemma/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 5, 2025

## Introducing EmbeddingGemma from Google on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to be a launch partner alongside [Google ↗︎](https://developers.googleblog.com/en/introducing-embeddinggemma/) to bring their newest embedding model, **EmbeddingGemma** , to Workers AI that delivers best-in-class performance for its size, enabling RAG and semantic search use cases.

[`@cf/google/embeddinggemma-300m`](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-300m/) is a 300M parameter embedding model from Google, built from Gemma 3 and the same research used to create Gemini models. This multilingual model supports 100+ languages, making it ideal for RAG systems, semantic search, content classification, and clustering tasks.

**Using EmbeddingGemma in AI Search:** Now you can leverage EmbeddingGemma directly through AI Search for your RAG pipelines. EmbeddingGemma's multilingual capabilities make it perfect for global applications that need to understand and retrieve content across different languages with exceptional accuracy.

To use EmbeddingGemma for your AI Search projects:

  1. Go to **Create** in the [AI Search dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/ai-search)
  2. Follow the setup flow for your new RAG instance
  3. In the **Generate Index** step, open up **More embedding models** and select `@cf/google/embeddinggemma-300m` as your embedding model
  4. Complete the setup to create an AI Search



Try it out and let us know what you think!
