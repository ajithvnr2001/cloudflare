---
url: https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/
title: Customize queue message retention periods \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.786784+00:00
---

# Customize queue message retention periods · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 14, 2025

## Customize queue message retention periods

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.

![Customize a queue's message retention period](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1898,height=986,format=webp/_astro/customize-retention-period.CpK7s10q.png)

You can customize the retention period on the settings page for your queue, or using Wrangler:

Update message retention periodbash
    
    
    $ wrangler queues update my-queue --message-retention-period-secs 600

This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).
