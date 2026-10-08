---
url: https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/
title: Pipelines pricing announced \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:52.370575+00:00
---

# Pipelines pricing announced · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## Pipelines pricing announced

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-11-pipelines-pricing-announced/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Pipelines](https://developers.cloudflare.com/basin-pipelines/) is a streaming data platform that ingests events, transforms them with SQL, and writes to [R2](https://developers.cloudflare.com/r2/) as JSON, Parquet, or [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables. Pipelines now has published pricing based on two usage dimensions: the volume of data processed by SQL transforms and the volume of data delivered to sinks. Ingress into a Pipeline stream is free.

**Billing is not yet enabled. We will provide at least 30 days notice before we start charging for Pipelines usage.**

Pipelines pricing model is designed to charge per GB based on what you use:

  * **Streams (ingress)** : Free, regardless of volume.
  * **SQL transforms** : $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).
  * **Sinks** : $0.03 / GB for JSON, $0.06 / GB for Parquet or Iceberg output.



Workers Free plans include 1 GB / month for each dimension. Workers Paid plans include 50 GB / month.

For full pricing details and billing examples, refer to [Pipelines pricing](https://developers.cloudflare.com/basin-pipelines/platform/pricing/).
