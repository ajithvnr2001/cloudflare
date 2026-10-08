---
url: https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/
title: New Confidence Intervals in GraphQL Analytics API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:24.887030+00:00
---

# New Confidence Intervals in GraphQL Analytics API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2025

## New Confidence Intervals in GraphQL Analytics API

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The GraphQL Analytics API now supports confidence intervals for `sum` and `count` fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.

  * **Supported datasets** : Adaptive (sampled) datasets only.
  * **Supported fields** : All `sum` and `count` fields.
  * **Usage** : The confidence `level` must be provided as a decimal between 0 and 1 (e.g. `0.90`, `0.95`, `0.99`).
  * **Default** : If no confidence level is specified, no intervals are returned.



For examples and more details, see the [GraphQL Analytics API documentation](https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/).
