---
url: https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/
title: D1 enforces free tier daily query limits \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:11.992544+00:00
---

# D1 enforces free tier daily query limits · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 1, 2026

## D1 enforces free tier daily query limits

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Beginning September 1, 2026, D1 queries on the [Workers Free plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) will fail when an account exceeds the daily [row read or row write limits](https://developers.cloudflare.com/d1/platform/pricing/). Queries via the [Workers Binding API](https://developers.cloudflare.com/d1/worker-api/) and the [REST API](https://developers.cloudflare.com/d1/rest-api/) will return errors until the limit resets at midnight UTC. Stored data is not affected.

You will receive email alerts when the daily limit is reached. The following errors indicate that a limit has been exceeded:

Error | Description  
---|---  
Your account has exceeded D1's free tier daily row read limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue. | The account has reached its daily row read limit.  
Your account has exceeded D1's free tier daily row write limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue. | The account has reached its daily row write limit.  
  
Inspect database query activity before the enforcement date to identify queries that may exceed these limits. To reduce row reads, add [indexes](https://developers.cloudflare.com/d1/best-practices/use-indexes/) to tables and review queries that perform full table scans. If usage requires higher limits after optimization, upgrade to a [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers).

For more information on D1 errors and how to handle them, refer to the [D1 error list](https://developers.cloudflare.com/d1/observability/debug-d1/#error-list).
