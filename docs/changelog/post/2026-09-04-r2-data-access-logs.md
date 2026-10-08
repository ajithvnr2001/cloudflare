---
url: https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/
title: R2 Data Access Logs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:12.577145+00:00
---

# R2 Data Access Logs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 4, 2026

## R2 Data Access Logs

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-04-r2-data-access-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 Data Access Logs are now generally available. Turn on logging for a bucket to record object read, write, list, multipart upload, and delete operations with response status codes below `400`.

Data Access Logs cover requests made through the S3-compatible API, Cloudflare API and dashboard, Workers bindings, and public buckets through `r2.dev` or custom domains. Events are available in Workers Observability, where you can filter by bucket, operation, interface, actor, and other request fields.

Log delivery is asynchronous and best effort. Events may be delayed or omitted, so do not rely on Data Access Logs as a complete record of bucket activity.

Data Access Logs are available for non-jurisdictional buckets. For setup instructions, supported operations, and the event field reference, refer to [R2 Data Access Logs](https://developers.cloudflare.com/r2/buckets/data-access-logs/).
