---
url: https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/
title: Deploy larger Workers \u2014 up to 64 MiB for both free and paid plans \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:12.981346+00:00
---

# Deploy larger Workers — up to 64 MiB for both free and paid plans · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 4, 2026

## Deploy larger Workers — up to 64 MiB for both free and paid plans

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now deploy Workers with larger dependencies, heavier frameworks, and more code without hitting size limits.

When you deploy a Worker, Wrangler bundles your code and compresses it before uploading. Previously, Cloudflare checked that compressed size and rejected deploys over 3 MB (Free) or 10 MB (Paid). That limit has been removed. Cloudflare now only checks the uncompressed size of your bundle, which is 64 MiB across all plans.

To check your Worker's bundle size before deploying:
    
    
    wrangler deploy --outdir bundled/ --dry-run
    
    
    Total Upload: 259.61 KiB / gzip: 47.23 KiB

The `Total Upload` value is your uncompressed bundle size. This is what counts against the 64 MiB limit. The `gzip` value is shown for reference but is no longer a limit.

For more information, refer to the [Worker size limits documentation](https://developers.cloudflare.com/workers/platform/limits/#worker-size).
