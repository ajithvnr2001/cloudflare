---
url: https://developers.cloudflare.com/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/
title: R2 Data Catalog now supports read-only API tokens \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:02.395705+00:00
---

# R2 Data Catalog now supports read-only API tokens · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 13, 2026

## R2 Data Catalog now supports read-only API tokens

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin](https://developers.cloudflare.com/basin/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) now accepts read-only API tokens, so query engines and clients that only read data no longer need a read-write token. Previously, every catalog operation required an **Admin Read & Write** token, which granted read-only clients more access than they needed.

You can now authenticate your Iceberg engine based on your workload:

  * **Read-only** operations (such as listing namespaces, loading tables, and querying data) work with an **Admin Read only** token (R2 Data Catalog read and R2 storage read).
  * **Write** operations (such as creating or dropping tables and committing transactions) continue to require an **Admin Read & Write** token.



This lets you follow the principle of least privilege — for example, using a read-write token for the pipeline that writes to your tables and read-only tokens for engines like [R2 SQL](https://developers.cloudflare.com/basin-sql/), [DuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/), or [PyIceberg](https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/) that query them.

Note that credentials vended by the catalog inherit the R2 storage permissions of the token used to authenticate. To ensure read-only access to your underlying data, scope the R2 storage permission to read-only as well.

For details on choosing and creating the right token, refer to [Authenticate your Iceberg engine](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#authenticate-your-iceberg-engine).
