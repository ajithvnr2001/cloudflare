---
url: https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/
title: Improved reliability for account-wide Web Analytics dashboards \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.690246+00:00
---

# Improved reliability for account-wide Web Analytics dashboards · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 14, 2026

## Improved reliability for account-wide Web Analytics dashboards

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards.

For larger accounts (with >100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.

Accounts with up to 1,000 sites will now be able to load this account-wide aggregate view without experiencing misleading errors.

If you have an account with over 1,000 sites, we cannot currently aggregate over this volume due to processing constraints but you will now be presented with a clear error and instruction to filter to the relevant site(s) you wish to see the data for.
