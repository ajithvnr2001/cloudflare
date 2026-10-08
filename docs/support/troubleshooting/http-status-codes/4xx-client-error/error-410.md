---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-410/
title: Error 410 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.709534+00:00
---

# Error 410 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-410/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 410



# Error 410

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-410/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview410 Gone Common use cases Cloudflare-specific information

## 410 Gone

When a resource is intentionally and permanently removed, servers use the `410 Gone` status code to inform clients that the resource is no longer available. In this case:

  * The server suggests that links referencing the resource should be removed.
  * The server is not obligated to use this status code instead of a `404` response, nor is it required to maintain this response for any specific period of time.



For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.11).

### Common use cases

This status is commonly applied to deprecated content, such as outdated pages or discontinued products.

### Cloudflare-specific information

Cloudflare does not generate `410` for customer websites, we only proxy the request from the origin server. If you encounter a `410` error on a Cloudflare-powered site, the issue lies with the origin server. In such cases, contact your hosting provider for assistance.

[PreviousError 409](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-409/)[NextError 411](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-411/)

Was this helpful?

YesNo
