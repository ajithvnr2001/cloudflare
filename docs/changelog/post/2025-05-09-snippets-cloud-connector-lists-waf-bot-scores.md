---
url: https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/
title: More ways to match \u2014 Snippets now support Custom Lists, Bot Score, and WAF Attack Score \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:11.795946+00:00
---

# More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 9, 2025

## More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use IP, Autonomous System (AS), and Hostname [custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) to route traffic to [Snippets](https://developers.cloudflare.com/rules/snippets/) and [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/), giving you greater precision and control over how you match and process requests at the edge.

In Snippets, you can now also match on [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/), unlocking smarter edge logic for everything from request filtering and mitigation to [tarpitting](https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/) and logging.

**What’s new:**

  * [Custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or [Lists API](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/list/). Great for shared logic across zones.
  * [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/) – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.

![New fields in Snippets](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1383,height=1351,format=webp/_astro/snippets-lists-scores.D05l6zgc.png)

These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.

Learn more in the [Snippets](https://developers.cloudflare.com/rules/snippets/) and [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) documentation.
