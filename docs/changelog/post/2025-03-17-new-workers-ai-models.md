---
url: https://developers.cloudflare.com/changelog/post/2025-03-17-new-workers-ai-models/
title: New models in Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:06.301988+00:00
---

# New models in Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-17-new-workers-ai-models/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 17, 2025

## New models in Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-17-new-workers-ai-models/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers AI is excited to add 4 new models to the catalog, including 2 brand new classes of models with a text-to-speech and reranker model. Introducing:

  * [@cf/baai/bge-m3](https://developers.cloudflare.com/workers-ai/models/bge-m3/) \- a multi-lingual embeddings model that supports over 100 languages. It can also simultaneously perform dense retrieval, multi-vector retrieval, and sparse retrieval, with the ability to process inputs of different granularities.
  * [@cf/baai/bge-reranker-base](https://developers.cloudflare.com/workers-ai/models/bge-reranker-base/) \- our first reranker model! Rerankers are a type of text classification model that takes a query and context, and outputs a similarity score between the two. When used in RAG systems, you can use a reranker after the initial vector search to find the most relevant documents to return to a user by reranking the outputs.
  * [@cf/openai/whisper-large-v3-turbo](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/) \- a faster, more accurate speech-to-text model. This model was added earlier but is graduating out of beta with pricing included today.
  * [@cf/myshell-ai/melotts](https://developers.cloudflare.com/workers-ai/models/melotts/) \- our first text-to-speech model that allows users to generate an MP3 with voice audio from inputted text.



Pricing is available for each of these models on the [Workers AI pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

This docs update includes a few minor bug fixes to the model schema for llama-guard, llama-3.2-1b, which you can review on the [product changelog](https://developers.cloudflare.com/workers-ai/changelog/).

Try it out and let us know what you think! Stay tuned for more models in the coming days.
