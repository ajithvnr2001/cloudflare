---
url: https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/
title: Web Assets fields now available in GraphQL Analytics API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:42.500801+00:00
---

# Web Assets fields now available in GraphQL Analytics API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 23, 2026

## Web Assets fields now available in GraphQL Analytics API

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Two new fields are now available in the `httpRequestsAdaptive` and `httpRequestsAdaptiveGroups` [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) datasets:

  * `webAssetsOperationId` — the ID of the [saved endpoint](https://developers.cloudflare.com/api-shield/management-and-monitoring/) that matched the incoming request.
  * `webAssetsLabelsManaged` — the [managed labels](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#managed-labels) mapped to the matched operation at the time of the request (for example, `cf-llm`, `cf-log-in`). At most 10 labels are returned per request.



Both fields are empty when no operation matched. `webAssetsLabelsManaged` is also empty when no managed labels are assigned to the matched operation.

These fields allow you to determine, per request, which Web Assets operation was matched and which managed labels were active. This is useful for troubleshooting downstream security detection verdicts — for example, understanding why [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/) did or did not flag a request.

Refer to [Endpoint labeling service](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#analytics) for GraphQL query examples.
