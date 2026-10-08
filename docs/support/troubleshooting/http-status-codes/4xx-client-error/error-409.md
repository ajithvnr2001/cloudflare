---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-409/
title: Error 409 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.915536+00:00
---

# Error 409 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-409/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 409



# Error 409

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-409/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview409 Conflict Common use cases Cloudflare-specific information

## 409 Conflict

The `409 Conflict` status code indicates that the request could not be completed due to a conflict with the current state of the target resource.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.10).

### Common use cases

This error typically happens with a `PUT` request when multiple clients are attempting to edit the same resource. To solve this issue:

  * The server should generate a payload that includes enough information for the client to recognize the source of the conflict.
  * Clients should retry the request again after resolving the conflict.



### Cloudflare-specific information

Cloudflare will return a 409 response for a [Error 1001: DNS Resolution Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1001/).

[PreviousError 408](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-408/)[NextError 410](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-410/)

Was this helpful?

YesNo
