---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-414/
title: Error 414 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:54.207048+00:00
---

# Error 414 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-414/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 414



# Error 414

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-414/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview414 URI Too Long Common use cases Cloudflare-specific information

## 414 URI Too Long

The `414 URI Too Long` status code indicates that the server refuses to process the request because the URI provided by the client is excessively long.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.15).

### Common use cases

For example, if a client is attempting a `GET` request with an unusually long URI, such as one containing an excessive number of query parameters, after a `POST`, this could be seen as a security risk and a `414` is generated.

### Cloudflare-specific information

Cloudflare will generate a `414` response if the URI length exceeds 32KB.

[PreviousError 413](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/)[NextError 415](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-415/)

Was this helpful?

YesNo
