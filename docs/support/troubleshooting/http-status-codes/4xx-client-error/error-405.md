---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-405/
title: Error 405 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.665919+00:00
---

# Error 405 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-405/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 405



# Error 405

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-405/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview405 Method Not Allowed Common use cases Cloudflare-specific information

## 405 Method Not Allowed

The 405 Method Not Allowed status code indicates that the origin server recognizes the requested resource but does not support the HTTP method used in the request.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6).

### Common use cases

This error typically occurs when the client uses an unsupported HTTP method to interact with a specific resource. The origin server must include an `Allow` header in the response, which lists the HTTP methods supported for that resource.

For example, attempting a `POST` request on a resource that is unchangeable and only supports `GET` requests will result in a `405` error.

### Cloudflare-specific information

Cloudflare does not directly generate `405` errors. These errors are returned by the origin server when it does not allow the HTTP method used in the request. If you encounter a `405` error, review the configuration of your origin server to ensure the correct methods are enabled for the resource in question.

[PreviousError 404](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-404/)[NextError 406](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-406/)

Was this helpful?

YesNo
