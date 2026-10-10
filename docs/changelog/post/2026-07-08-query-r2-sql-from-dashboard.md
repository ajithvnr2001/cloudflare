---
url: https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/
title: Query R2 Data Catalog tables with R2 SQL from the dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.225029+00:00
---

# Query R2 Data Catalog tables with R2 SQL from the dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-08-query-r2-sql-from-dashboard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 8, 2026

## Query R2 Data Catalog tables with R2 SQL from the dashboard

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now query your [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) tables with [R2 SQL](https://developers.cloudflare.com/basin-sql/) directly from the Cloudflare dashboard, without installing a CLI or wiring up a client. This makes it easy to explore your [Apache Iceberg ↗︎](https://iceberg.apache.org/) data, validate queries, and inspect results in one place.

![R2 SQL Query Editor](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3080,height=1696,format=webp/_astro/r2-sql-studio.DCmHJaqy.png)

To get started, go to [R2 Data Catalog ↗︎](https://dash.cloudflare.com/?to=/:account/data-catalog/overview) in the Cloudflare dashboard and select **Query data** to launch the built-in SQL editor. From there you can:

  * **Write and run queries interactively** — Iterate on R2 SQL directly in the browser with syntax highlighting and autocomplete, instead of re-running commands through Wrangler or the REST API.
  * **Explore your data** — Explore your namespaces and tables alongside the editor so you can discover what's queryable without leaving the page or using other tools.
  * **Understand results and performance** — View result sets with per-query statistics, export them, and get helpful `EXPLAIN` outputs to see exactly how a query runs.



Note

Your R2 SQL credential is generated and stored for you and can be rotated in the R2 Data Catalog settings page.
