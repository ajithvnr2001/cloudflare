---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-415/
title: Error 415 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:54.408613+00:00
---

# Error 415 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-415/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 415



# Error 415

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-415/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview415 Unsupported Media Type Common use cases Cloudflare-specific information

## 415 Unsupported Media Type

The `415 Unsupported Media Type` status code indicates that the server refuses to process the request because the format of the payload is not supported. One way to identify and fix this issue would be to look at the `Content-Type` or `Content-Encoding` headers sent in the client's request.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.16).

### Common use cases

This may be triggered by submitting a file type or format that the server is not configured to handle, such as uploading an unsupported image or document format, may also trigger this error.

### Cloudflare-specific information

Cloudflare typically passes this response from the origin server if it encounters an unsupported media type in the client's request payload.

[PreviousError 414](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-414/)[NextError 416](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-416/)

Was this helpful?

YesNo
