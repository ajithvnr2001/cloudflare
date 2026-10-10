---
url: https://developers.cloudflare.com/changelog/post/2025-05-30-d1-rest-api-latency/
title: 50-500ms Faster D1 REST API Requests \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.952854+00:00
---

# 50-500ms Faster D1 REST API Requests · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-30-d1-rest-api-latency/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 29, 2025

## 50-500ms Faster D1 REST API Requests

[D1](https://developers.cloudflare.com/d1/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Users using Cloudflare's [REST API](https://developers.cloudflare.com/api/resources/d1/) to query their D1 database can see lower end-to-end request latency now that D1 authentication is performed at the closest Cloudflare network data center that received the request. Previously, authentication required D1 REST API requests to proxy to Cloudflare's core, centralized data centers, which added network round trips and latency.

Latency improvements range from 50-500 ms depending on request location and [database location](https://developers.cloudflare.com/d1/configuration/data-location/) and only apply to the REST API. REST API requests and databases outside the United States see a bigger benefit since Cloudflare's primary core data centers reside in the United States.

D1 query endpoints like `/query` and `/raw` have the most noticeable improvements since they no longer access Cloudflare's core data centers. D1 control plane endpoints such as those to create and delete databases see smaller improvements, since they still require access to Cloudflare's core data centers for other control plane metadata.
