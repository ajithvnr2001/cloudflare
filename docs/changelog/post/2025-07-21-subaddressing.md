---
url: https://developers.cloudflare.com/changelog/post/2025-07-21-subaddressing/
title: Subaddressing support in Email Routing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:17.182561+00:00
---

# Subaddressing support in Email Routing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-21-subaddressing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 21, 2025

## Subaddressing support in Email Routing

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-21-subaddressing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Subaddressing, as defined in [RFC 5233 ↗︎](https://www.rfc-editor.org/rfc/rfc5233), also known as plus addressing, is now supported in Email Routing. This enables using the "+" separator to augment your custom addresses with arbitrary detail information.

Now you can send an email to `user+detail@example.com` and it will be captured by the `user@example.com` custom address. The `+detail` part is ignored by Email Routing, but it can be captured next in the processing chain in the logs, an [Email Worker](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) or an [Agent application ↗︎](https://github.com/cloudflare/agents/tree/main/examples/email-agent).

Customers can use this feature to dynamically add context to their emails, such as tracking the source of an email or categorizing emails without needing to create multiple custom addresses.

![Subaddressing](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1316,height=678,format=webp/_astro/subaddressing.x65bljxx.png)

Check our [Developer Docs](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#subaddressing) to learn how to enable subaddressing in Email Routing.
