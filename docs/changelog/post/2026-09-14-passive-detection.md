---
url: https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/
title: Discover where sensitive data goes before you create a Data Loss Prevention policy \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:13.632788+00:00
---

# Discover where sensitive data goes before you create a Data Loss Prevention policy · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 14, 2026

## Discover where sensitive data goes before you create a Data Loss Prevention policy

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-14-passive-detection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Passive Detection** for [Cloudflare Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) lets you learn from your Gateway traffic before deciding what to log or block. Discover the sensitive data types in sampled traffic, explore their destinations, and use the findings to build policies around your organization's needs.

The dashboard brings together detections from sampled HTTP request and response bodies. Select an entry to follow its detections over time, review destinations, and check policy coverage. You do not need a Gateway DLP policy to get these insights, and existing Gateway policies continue to apply.

![Passive Detection dashboard showing detection totals, data type distribution, policy coverage, and detection entries](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=593,format=webp/_astro/passive-detection.B_-_POtg.gif)

Passive Detection is generally available. The detection entries available to your account depend on your [Zero Trust plan](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

To get started, refer to the [Passive Detection documentation](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/).
