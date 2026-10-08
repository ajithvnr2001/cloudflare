---
url: https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/
title: Super Slurper now transfers data to R2 up to 5x faster \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:03.609736+00:00
---

# Super Slurper now transfers data to R2 up to 5x faster · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 14, 2025

## Super Slurper now transfers data to R2 up to 5x faster

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/) now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to [Cloudflare R2](https://developers.cloudflare.com/r2/) up to 5x faster than it did before.

We moved from a centralized service to a distributed system built on the Cloudflare Developer Platform — using [Cloudflare Workers](https://developers.cloudflare.com/workers/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Queues](https://developers.cloudflare.com/queues/) — to both improve performance and increase system concurrency capabilities (and we'll share more details about how we did it soon!)

![Super Slurper Objects Migrated](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=974,height=493,format=webp/_astro/slurper-objects-over-time-border.BFDkMQUw.png)

_Time to copy 75,000 objects from AWS S3 to R2 decreased from 15 minutes 30 seconds (old) to 3 minutes 25 seconds (after performance improvements)_

For more information on Super Slurper and how to migrate data from existing object storage to R2, refer to our [documentation](https://developers.cloudflare.com/r2/data-migration/super-slurper/).
