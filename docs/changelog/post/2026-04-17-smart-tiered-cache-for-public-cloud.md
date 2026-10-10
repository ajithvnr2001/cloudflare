---
url: https://developers.cloudflare.com/changelog/post/2026-04-17-smart-tiered-cache-for-public-cloud/
title: Smart Tiered Cache optimizes public cloud origins \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.181200+00:00
---

# Smart Tiered Cache optimizes public cloud origins · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-17-smart-tiered-cache-for-public-cloud/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 17, 2026

## Smart Tiered Cache optimizes public cloud origins

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now achieve higher cache HIT rates and reduce origin load for origins hosted on public cloud providers with [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#smart-tiered-cache). By setting a cloud region hint for your origin, Cloudflare selects the optimal upper-tier data center for that cloud region, funneling all cache MISSes through a single location close to your origin.

Previously, Smart Tiered Cache could not reliably select an optimal upper tier for origins behind anycast or regional unicast networks commonly used by cloud providers. Origins on AWS, GCP, Azure, and Oracle Cloud would fall back to a multi-upper-tier topology, resulting in lower cache HIT rates and more requests reaching your origin.

#### How it works

Set a cloud region hint (for example, `aws/us-east-1` or `gcp/europe-west1`) for your origin IP or hostname. Smart Tiered Cache uses this hint along with real-time latency data to select a primary upper tier close to your cloud region, plus a fallback in a different location for resilience.

  * **Supported providers** : AWS, GCP, Azure, and Oracle Cloud.
  * **All plans** : Available on Free, Pro, Business, and Enterprise plans at no additional cost.
  * **Dashboard and API** : Configure from **Caching** > **Tiered Cache** > **Origin Configuration** , or use the API and Terraform.



#### Get started

To get started, enable [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) and set a cloud region hint for your origin in the [Tiered Cache settings](https://developers.cloudflare.com/cache/how-to/tiered-cache/#public-cloud-origins).
