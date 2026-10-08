---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-417/
title: Error 417 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:54.541462+00:00
---

# Error 417 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-417/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 417



# Error 417

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-417/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview417 Expectation Failed Common use cases Cloudflare-specific information

## 417 Expectation Failed

The `417 Expectation Failed` status code indicates that the server could not meet the requirements specified in the `Expect` header of the client's request.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.18).

### Common use cases

Some clients use the `Expect` header, such as `Expect: 100-continue`, to verify if the server is ready to receive a large payload, and if the server cannot fulfill this expectation, it returns a 417 response. Similarly, a server may reject a request with this error if the client includes an `Expect` header with unsupported or invalid values.

### Cloudflare-specific information

Cloudflare typically forwards this response from the origin server if it encounters an issue related to unsupported or unfulfilled `Expect` headers in the client's request.

[PreviousError 416](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-416/)[NextError 421](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-421/)

Was this helpful?

YesNo
