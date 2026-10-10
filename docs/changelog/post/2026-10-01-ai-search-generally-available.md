---
url: https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/
title: AI Search is generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.852606+00:00
---

# AI Search is generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2026

## AI Search is generally available

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Search is now generally available. Usage-based billing begins on November 1, 2026, with included monthly ingestion, storage, semantic query, and full-text query usage. Cloudflare will send a reminder email the week before billing begins.

Refer to [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for rates and included usage.

#### Hybrid search is on by default

New AI Search instances use hybrid search by default. Hybrid search combines semantic vector retrieval with full-text matching. You can choose a different index method when you create an instance.

Refer to [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for details.

#### Workers AI embeddings and reranking are included

Workers AI embedding and reranking calls made by AI Search are included in AI Search pricing. These calls no longer appear on your Workers AI bill or in your AI Gateway logs. Generation, query rewriting, and external providers continue to use your account and gateway.

Refer to [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for details.

#### Multimodal model and image support

AI Search supports the `@cf/qwen/qwen3-vl-embedding-2b` and `google-ai-studio/gemini-embedding-2` multimodal embedding models. Search and chat requests can include images through the REST API and public endpoint.

Refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/) for the full list of embedding models.

#### OCR availability and increased file limits

Optical character recognition (OCR) is available on every account for scanned PDFs. Plain-text or code files and PDFs with OCR enabled can be up to 10 MiB. PDFs without OCR and other supported formats remain limited to 4 MiB.

Refer to [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/#file-limits) for file limits and [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for OCR pricing.

#### Source type inference

When you create an AI Search instance, the `type` field is optional. AI Search infers a website source from an HTTP or HTTPS URL, or an R2 source from an existing bucket name.

Refer to [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) for details.
