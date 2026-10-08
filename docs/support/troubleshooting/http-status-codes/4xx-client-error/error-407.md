---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-407/
title: Error 407 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.784872+00:00
---

# Error 407 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-407/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 407



# Error 407

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-407/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview407 Authentication Required Common use cases Cloudflare-specific information

## 407 Authentication Required

The `407 Proxy Authentication Required` status code indicates that the client did not provide the necessary authentication credentials to access the requested resource through a proxy server. For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.8).

### Common use cases

This error typically occurs in environments where a proxy server is used as an intermediary between the client and the target server. To resolve this, the client must include the appropriate `Proxy-Authorization` header in the request with valid credentials.

### Cloudflare-specific information

Cloudflare does not generate `407` errors but proxies them from the origin server or an upstream proxy. If a `407` error occurs on a Cloudflare-powered site, review the origin server's proxy configuration to ensure authentication requirements are properly set, and verify that the client is providing the required credentials.

[PreviousError 406](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-406/)[NextError 408](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-408/)

Was this helpful?

YesNo
