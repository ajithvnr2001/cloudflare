---
url: https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/
title: Smart Tiered Cache \u00b7 Cloudflare Smart Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:32.129209+00:00
---

# Smart Tiered Cache · Cloudflare Smart Shield docs

> Source: https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Smart Shield](https://developers.cloudflare.com/smart-shield/)
  3. /Configuration
  4. /Smart Tiered Cache



# Smart Tiered Cache

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Availability

Available in all Smart Shield packages.

With data centers around the world, Cloudflare caches content very close to end users. However, if a piece of content is not in cache, the Cloudflare data centers must contact the origin server to receive the cacheable content. Tiered cache works by dividing Cloudflare's data centers into a hierarchy of lower-tiers and upper-tiers, where only upper-tiers can ask your origin for content.

Smart Tiered Cache dynamically selects the single closest upper tier for each of your website’s origins with no configuration required, using our in-house performance and routing data. Cloudflare collects latency data for each request to an origin, and uses the latency data to determine how well any upper-tier data center is connected with an origin. As a result, Cloudflare can select the data center with the lowest latency to be the upper-tier for an origin.

#### Public cloud origins

Origins hosted on public cloud providers (AWS, GCP, Azure, or Oracle Cloud) often use [anycast ↗︎](https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/) or regional unicast networking, which prevents Smart Tiered Cache from determining the origin location through latency probing alone. To solve this, you can set a **cloud region hint** that tells Smart Tiered Cache which cloud provider and region your origin is in. Smart Tiered Cache then selects a primary upper-tier data center close to that cloud region, plus a fallback in a different location for resilience. To set up a cloud region hint, refer to [Set a cloud region hint](https://developers.cloudflare.com/cache/how-to/tiered-cache/#set-a-cloud-region-hint).

#### Load Balancing interaction

While Smart Tiered Cache selects one Upper Tier per origin, when using Load Balancing, Smart Tiered Cache will select the single best Upper Tier for the entire [Load Balancing Pool](https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-components/#pools).

#### Caveats

You need to be careful when updating your origin IPs/DNS records while Smart Tiered Cache is enabled. Depending on the changes made, it may cause the existing assigned upper tiers to change, resulting in an increased `MISS` rate as cache is refilled in the new upper tiers. If the origin is switched to a network behind anycast, it will significantly reduce the effectiveness of Smart Tiered Cache unless you set a [cloud region hint](https://developers.cloudflare.com/cache/how-to/tiered-cache/#set-a-cloud-region-hint).

[PreviousConnection reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/)[NextRegional Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/smart-shield/configuration/smart-tiered-cache.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
