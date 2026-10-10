---
url: https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/
title: Service Key authentication deprecated \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.110967+00:00
---

# Service Key authentication deprecated · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-19-service-key-authentication-deprecated/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 19, 2026

## Service Key authentication deprecated

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Service Key authentication for the Cloudflare API is deprecated. Service Keys will stop working on September 30, 2026.

[API Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) replace Service Keys with fine-grained permissions, expiration, and revocation.

#### What you need to do

Replace any use of the `X-Auth-User-Service-Key` header with an [API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) scoped to the permissions your integration requires.

If you use `cloudflared`, update to a version from November 2022 or later. These versions already use API Tokens.

If you use [origin-ca-issuer ↗︎](https://github.com/cloudflare/origin-ca-issuer), update to a version that supports API Token authentication.

For more information, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).
