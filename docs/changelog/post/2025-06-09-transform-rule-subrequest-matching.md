---
url: https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/
title: Match Workers subrequests by upstream zone \u2014 cf.worker.upstream_zone now supported in Transform Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:13.661629+00:00
---

# Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 9, 2025

## Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-09-transform-rule-subrequest-matching/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use the [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field in [Transform Rules](https://developers.cloudflare.com/rules/transform/) to control rule execution based on whether a request originates from [Workers](https://developers.cloudflare.com/workers/), including subrequests issued by Workers in other zones.

![Match Workers subrequests by upstream zone in Transform Rules](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1446,height=988,format=webp/_astro/transform-rule-subrequest-matching.BeUBEN67.png)

**What's new:**

  * `cf.worker.upstream_zone` is now supported in Transform Rules expressions.
  * Skip or apply logic conditionally when handling [Workers subrequests](https://developers.cloudflare.com/workers/platform/limits/#subrequests).



For example, to add a header when the subrequest comes from another zone:

Text in **Expression Editor** (replace `myappexample.com` with your domain):
    
    
    (cf.worker.upstream_zone != "" and cf.worker.upstream_zone != "myappexample.com")

Selected operation under **Modify request header** : _Set static_

**Header name** : `X-External-Workers-Subrequest`

**Value** : `1`

This gives you more granular control in how you handle incoming requests for your zone.

Learn more in the [Transform Rules](https://developers.cloudflare.com/rules/transform/) documentation and [Rules language fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) reference.
