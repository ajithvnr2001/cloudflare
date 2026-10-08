---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-401/
title: Error 401 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.390052+00:00
---

# Error 401 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-401/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 401



# Error 401

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-401/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview401 Unauthorized Common use cases Cloudflare-specific information

## 401 Unauthorized

This error indicates that the request was not sent with the proper authentication credentials. The server requires authentication to process the request.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.2).

### Common use cases

A `401 Unauthorized` error occurs when the client fails to provide valid authentication credentials. The server responds with at least one challenge in the form of a `WWW-Authenticate` header field, as outlined in [section 4.1 ↗︎](https://datatracker.ietf.org/doc/html/rfc7235#section-4.1).

If the client resends the request with the same credentials and the challenge remains unchanged, the server may return an entity to assist the client in identifying the correct credentials needed.

### Cloudflare-specific information

When encountering a `401` error while using the Cloudflare API, ensure that you are providing the correct authentication credentials (for example, [API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) or [keys](https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/)). Double-check that the credentials are active and properly formatted. If the error persists, refer to the `WWW-Authenticate` header in the response for guidance on resolving the issue.

[PreviousError 400](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-400/)[NextError 403](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/)

Was this helpful?

YesNo
