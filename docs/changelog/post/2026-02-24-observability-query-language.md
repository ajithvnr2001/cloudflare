---
url: https://developers.cloudflare.com/changelog/post/2026-02-24-observability-query-language/
title: Write structured queries to filter and search your Workers logs and traces \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:38.392559+00:00
---

# Write structured queries to filter and search your Workers logs and traces · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-24-observability-query-language/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 25, 2026

## Write structured queries to filter and search your Workers logs and traces

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-24-observability-query-language/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Observability](https://developers.cloudflare.com/workers/observability/) now includes a query language that lets you write structured queries directly in the search bar to filter your logs and traces. The search bar doubles as a free text search box — type any term to search across all metadata and attributes, or write field-level queries for precise filtering.

![Workers Observability search bar with autocomplete suggestions and Query Builder sidebar filters](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2630,height=1302,format=webp/_astro/2026-02-24-query-language.Ol8UX7m0.png)

Queries written in the search bar sync with the [Query Builder](https://developers.cloudflare.com/workers/observability/) sidebar, so you can write a query by hand and then refine it visually, or build filters in the Query Builder and see the corresponding query syntax. The search bar provides autocomplete suggestions for metadata fields and operators as you type.

The query language supports:

  * **Free text search** — search everywhere with a keyword like `error`, or match an exact phrase with `"exact phrase"`
  * **Field queries** — filter by specific fields using comparison operators (for example, `status = 500` or `$workers.wallTimeMs > 100`)
  * **Operators** — `=`, `!=`, `>`, `>=`, `<`, `<=`, and `:` (contains)
  * **Functions** — `contains(field, value)`, `startsWith(field, prefix)`, `regex(field, pattern)`, and `exists(field)`
  * **Boolean logic** — add conditions with `AND`, `OR`, and `NOT`



Select the help icon next to the search bar to view the full syntax reference, including all supported operators, functions, and keyboard shortcuts.

Go to the [Workers Observability dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/) to try the query language.
