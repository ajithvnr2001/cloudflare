---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-411/
title: Error 411 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:54.361691+00:00
---

# Error 411 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-411/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 411



# Error 411

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-411/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview411 Length Required Common use cases Cloudflare-specific information

## 411 Length Required

The `411 Length Required` status code indicates that the client did not specify the `Content-Length` of the request body in the headers, and this information is required to obtain the resource. The client may resend the request after adding the required header field.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.12).

### Common use cases

This status code can occur in various scenarios, such as when a client sends an API request without the required `Content-Length` header, when uploading a file where the server needs the header to allocate resources, or when proxies or legacy systems enforce strict HTTP compliance. In each case, the server or intermediary requires the `Content-Length` header to process the request properly.

### Cloudflare-specific information

Cloudflare does not generate `411` for customer websites, we only proxy the request from the origin server. If you encounter a `411` error on a Cloudflare-powered site, the issue lies with the origin server. In such cases, contact your hosting provider for assistance.

[PreviousError 410](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-410/)[NextError 412](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-412/)

Was this helpful?

YesNo
