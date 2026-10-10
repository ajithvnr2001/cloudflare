---
url: https://developers.cloudflare.com/changelog/post/2026-05-27-cloudy-regex-assistance/
title: Write regex using natural language in Cloudflare One \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.774128+00:00
---

# Write regex using natural language in Cloudflare One · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-27-cloudy-regex-assistance/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 27, 2026

## Write regex using natural language in Cloudflare One

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) policy selectors which support regular expressions can now be authored in the dashboard using natural language. When building a [policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/) with a regex-based selector (like `matches regex`), you can describe what you want to match in plain English and the Cloudflare Agent will generate and validate a corresponding regular expression.

![Write policy regex using natural language](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1000,height=638,format=webp/_astro/gateway-regex-ai-generation.CtJ0S6FS.png)

To get started, select a regex-compatible selector in the [Gateway policy builder](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) and select the icon. You'll see an input field for natural language, such as "any URL starting with /api/v1" or ".com, .net, and .app hosts which contain `gooogle` in the host."

You can also use the tool to explain existing regular expressions. If a policy already contains a regex pattern, you can instantly generate a plain-language description.

A built-in feedback mechanism allows you to rate each interaction to help improve output quality over time.

For more information, refer to [Cloudflare One firewall policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) and expect to see the same functionality supported soon in [Data loss prevention profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/).
