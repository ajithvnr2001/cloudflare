---
url: https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/
title: Pay Per Crawl advanced configuration \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:58.256757+00:00
---

# Pay Per Crawl advanced configuration · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 16, 2026

## Pay Per Crawl advanced configuration

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure advanced Pay Per Crawl settings for your zone, including:

  * **Disable Pay Per Crawl by URI pattern** using [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) to offer free access to specific pages while charging for others.
  * **Dynamic pricing** by having your origin return a `crawler-price` response header, or by using a [Cloudflare Worker](https://developers.cloudflare.com/workers/) to set prices based on request properties.



When dynamic pricing is enabled, Pay Per Crawl adds a `cf-pay-per-crawl` request header to origin requests so your origin or Worker can determine the appropriate price.

Refer to the [Advanced configuration documentation](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/) for details.
