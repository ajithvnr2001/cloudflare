---
url: https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/
title: Filter your AutoRAG search by file name \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:14.730962+00:00
---

# Filter your AutoRAG search by file name · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 19, 2025

## Filter your AutoRAG search by file name

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-19-autorag-filename-filter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In [AutoRAG](https://developers.cloudflare.com/ai-search/), you can now [filter](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/) by an object's file name using the `filename` attribute, giving you more control over which files are searched for a given query.

This is useful when your application has already determined which files should be searched. For example, you might query a PostgreSQL database to get a list of files a user has access to based on their permissions, and then use that list to limit what AutoRAG retrieves.

For example, your search query may look like:
    
    
    const response = await env.AI.autorag("my-autorag").search({
    	query: "what is the project deadline?",
    	filters: {
    		type: "eq",
    		key: "filename",
    		value: "project-alpha-roadmap.md",
    	},
    });

This allows you to connect your application logic with AutoRAG's retrieval process, making it easy to control what gets searched without needing to reindex or modify your data.

Learn more in AutoRAG's [metadata filtering documentation](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).
