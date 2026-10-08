---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-408/
title: Error 408 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.863324+00:00
---

# Error 408 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-408/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 408



# Error 408

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-408/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview408 Request Timeout Common use cases Cloudflare-specific information

## 408 Request Timeout

The `408 Request Timeout` status code indicates that the origin server did not receive the complete request within a reasonable time frame and does not wish to continue waiting for the connection. This response is not commonly used, as servers often prefer to use the "close" connection option to terminate idle connections

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.9).

### Common use cases

This error typically occurs when a client fails to send a complete request within the server's timeout period. Common scenarios include slow network connections, server overload or client-side delays to complete the request.

### Cloudflare-specific information

If a `408` error occurs on a Cloudflare-powered site, it is most often being proxied from the origin. In these cases, it is essential to review the origin server's timeout settings and ensure that the server is not overloaded. Additionally, verify that the client's Internet connection is stable and that the request is being sent promptly.

Cloudflare may return a `408` error response if public client requests to our network exceed certain internally-defined timeouts. These timeouts are configured as a protective measure and cannot be changed.

[PreviousError 407](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-407/)[NextError 409](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-409/)

Was this helpful?

YesNo
