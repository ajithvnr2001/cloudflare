---
url: https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/
title: Symmetric key support for JWT validation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.241804+00:00
---

# Symmetric key support for JWT validation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 25, 2026

## Symmetric key support for JWT validation

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

API Shield [JSON Web Token validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) now supports symmetric keys that use the `HS256`, `HS384`, and `HS512` algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API.

Cloudflare never stores symmetric credentials in plaintext. API responses do not include the credential.

Refer to [Configure JWT validation via the API](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/#credentials) for supported key formats and credential requirements.
