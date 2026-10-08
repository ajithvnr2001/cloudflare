---
url: https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/
title: New Zombie API detection for API Shield \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:30.425954+00:00
---

# New Zombie API detection for API Shield · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2025

## New Zombie API detection for API Shield

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

API Shield now automatically detects zombie endpoints — saved endpoints that have not received traffic for an extended period. When detected, the `cf-risk-zombie` [risk label](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#risk-labels) is applied.

The scan runs daily alongside existing risk scans. Endpoints are labeled after 32 days without traffic.

Zombie endpoints may indicate deprecated or forgotten API surface area that could pose a security risk. Review these endpoints and consider removing them from Endpoint Management if they are no longer in use. Also consider using a [fallthrough rule](https://developers.cloudflare.com/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule) to prevent communication with endpoints removed from Endpoint Management.
