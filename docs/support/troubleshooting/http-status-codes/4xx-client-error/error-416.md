---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-416/
title: Error 416 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:54.441605+00:00
---

# Error 416 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-416/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 416



# Error 416

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-416/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview416 Range Not Satisfiable Common use cases Cloudflare-specific information

## 416 Range Not Satisfiable

The `416 Range Not Satisfiable` status code indicates that the server cannot fulfill the byte range specified in the request's `Range` header.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110.html#name-416-range-not-satisfiable).

### Common use cases

This error can occur when every requested byte range falls outside the selected resource. It can also occur when the server does not support the requested range unit.

A `416` response to a byte-range request should include a `Content-Range` header. The header uses `bytes */<LENGTH>`, where `<LENGTH>` is the current resource length.

### Cloudflare-specific information

Cloudflare can return a `416` response when the origin rejects a range request. Cloudflare can also generate this response when a cached resource cannot satisfy the requested range.

Cloudflare does not cache `416` responses returned by an origin server. This applies even when the response includes explicit cache directives or a matching Cache Rule sets a [Status Code TTL](https://developers.cloudflare.com/cache/how-to/configure-cache-status-code/) for `416`. This behavior prevents one unsatisfiable range request from affecting later requests for the same URL.

[PreviousError 415](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-415/)[NextError 417](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-417/)

Was this helpful?

YesNo
