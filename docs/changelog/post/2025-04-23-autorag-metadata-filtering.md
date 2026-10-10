---
url: https://developers.cloudflare.com/changelog/post/2025-04-23-autorag-metadata-filtering/
title: Metadata filtering and multitenancy support in AutoRAG \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.804641+00:00
---

# Metadata filtering and multitenancy support in AutoRAG · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-23-autorag-metadata-filtering/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 23, 2025

## Metadata filtering and multitenancy support in AutoRAG

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now filter [AutoRAG](https://developers.cloudflare.com/ai-search/) search results by `folder` and `timestamp` using [metadata filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/) to narrow down the scope of your query.

This makes it easy to build [multitenant experiences](https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/) where each user can only access their own data. By organizing your content into per-tenant folders and applying a `folder` filter at query time, you ensure that each tenant retrieves only their own documents.

**Example folder structure:**
    
    
    customer-a/logs/
    customer-a/contracts/
    customer-b/contracts/

**Example query:**
    
    
    const response = await env.AI.autorag("my-autorag").search({
    	query: "When did I sign my agreement contract?",
    	filters: {
    		type: "eq",
    		key: "folder",
    		value: "customer-a/contracts/",
    	},
    });

You can use metadata filtering by creating a new AutoRAG or reindexing existing data. To reindex all content in an existing AutoRAG, update any chunking setting and select **Sync index**. Metadata filtering is available for all data indexed on or after **April 21, 2025**.

If you are new to AutoRAG, get started with the [Get started AutoRAG guide](https://developers.cloudflare.com/ai-search/get-started/).
