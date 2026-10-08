---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-412/
title: Error 412 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.970135+00:00
---

# Error 412 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-412/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 412



# Error 412

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-412/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview412 Precondition Failed Common use cases Cloudflare-specific information

## 412 Precondition Failed

The `412 Precondition Failed` status code indicates that the server denies the request because the resource does not meet the conditions specified by the client.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.13).

### Common use cases

One common use case for the `412 Precondition Failed` status code is version control. For example, a client modifying an existing resource may set the `If-Unmodified-Since` header to ensure the resource has not been changed since the client downloaded it for editing. If another client edits the resource after the specified date but before the original client uploads their changes, the server will return a `412` response to prevent overwriting the newer updates.

### Cloudflare-specific information

Cloudflare may serve this response: for more information please refer to [ETag Headers](https://developers.cloudflare.com/cache/reference/etag-headers/).

[PreviousError 411](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-411/)[NextError 413](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/)

Was this helpful?

YesNo
