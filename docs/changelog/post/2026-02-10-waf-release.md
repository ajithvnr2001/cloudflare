---
url: https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/
title: WAF Release - 2026-02-10 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.042363+00:00
---

# WAF Release - 2026-02-10 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-10-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 10, 2026

## WAF Release - 2026-02-10

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release changes the rule action from BLOCK to Disabled for Anomaly:Header:User-Agent - Fake Google Bot.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...6aa0bef8| N/A| Anomaly:Header:User-Agent - Fake Google Bot| Enabled| Disabled| We are changing the action for this rule from BLOCK to Disabled
