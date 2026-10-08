---
url: https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/
title: New CPU Pricing for Containers and Sandboxes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:30.122427+00:00
---

# New CPU Pricing for Containers and Sandboxes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 21, 2025

## New CPU Pricing for Containers and Sandboxes

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) and [Sandboxes](https://developers.cloudflare.com/sandbox/) pricing for CPU time is now based on active usage only, instead of provisioned resources.

This means that you now pay less for Containers and Sandboxes.

#### An Example Before and After

Imagine running the `standard-2` instance type for one hour, which can use up to 1 vCPU, but on average you use only 20% of your CPU capacity.

CPU-time is priced at _$0.00002 per vCPU-second_.

Previously, you would be charged for the CPU allocated to the instance multiplied by the time it was active, in this case 1 hour.

CPU cost would have been: **$0.072** — 1 vCPU * 3600 seconds * $0.00002

Now, since you are only using 20% of your CPU capacity, your CPU cost is cut to 20% of the previous amount.

CPU cost is now: **$0.0144** — 1 vCPU * 3600 seconds * $0.00002 * 20% utilization

This can significantly reduce costs for Containers and Sandboxes.

Note

Memory cost and disk pricing remain unchanged, and is still calculated based on _provisioned_ resources.

See the documentation to learn more about [Containers](https://developers.cloudflare.com/containers/get-started/), [Sandboxes](https://developers.cloudflare.com/sandbox/), and [associated pricing](https://developers.cloudflare.com/containers/platform/pricing).
