---
url: https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/
title: Improved SCIM 2.0 group synchronization \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:10.144374+00:00
---

# Improved SCIM 2.0 group synchronization · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 21, 2026

## Improved SCIM 2.0 group synchronization

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Dashboard SCIM now supports replacing groups using HTTP `PUT`, as defined by [RFC 7644 section 3.5.1 ↗︎](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1). This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.

**What's New**

**Group replacement via`PUT`**: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.

Note

SCIM provisioning for the Cloudflare dashboard is available to Enterprise customers. You must be a Super Administrator to complete the initial setup.

For more information:

  * [SCIM provisioning overview](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)


