---
url: https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/
title: Bidirectional tunnel health checks are compatible with all Magic on-ramps \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:21.825929+00:00
---

# Bidirectional tunnel health checks are compatible with all Magic on-ramps · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 5, 2025

## Bidirectional tunnel health checks are compatible with all Magic on-ramps

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-05-bidirectional-health-check-any-on-ramp/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.

Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.

There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.

Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.
