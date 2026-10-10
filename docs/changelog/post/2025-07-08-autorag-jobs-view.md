---
url: https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/
title: Faster indexing and new Jobs view in AutoRAG \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.216742+00:00
---

# Faster indexing and new Jobs view in AutoRAG · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-08-autorag-jobs-view/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 8, 2025

## Faster indexing and new Jobs view in AutoRAG

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now expect **3-5× faster indexing** in AutoRAG, and with it, a brand new **Jobs view** to help you monitor indexing progress.

With each AutoRAG, indexing jobs are automatically triggered to sync your data source (i.e. R2 bucket) with your Vectorize index, ensuring new or updated files are reflected in your query results. You can also trigger jobs manually via the [Sync API](https://developers.cloudflare.com/api/resources/ai-search/subresources/rags/) or by clicking “Sync index” in the dashboard.

With the new jobs observability, you can now:

  * View the status, job ID, source, start time, duration and last sync time for each indexing job
  * Inspect real-time logs of job events (e.g. `Starting indexing data source...`)
  * See a history of past indexing jobs under the Jobs tab of your AutoRAG



This makes it easier to understand what’s happening behind the scenes.

**Coming soon:** We’re adding APIs to programmatically check indexing status, making it even easier to integrate AutoRAG into your workflows.

Try it out today on the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/autorag).
