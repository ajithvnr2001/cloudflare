---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-451/
title: Error 451 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:54.736015+00:00
---

# Error 451 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-451/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 451



# Error 451

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-451/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview451 Unavailable For Legal Reason Common use cases Cloudflare-specific information

## 451 Unavailable For Legal Reason

The `451` status code indicates that the server cannot deliver the requested resource due to legal actions or restrictions.

For more details, refer to [RFC 7725 ↗︎](https://tools.ietf.org/html/rfc7725).

### Common use cases

This occurs when access to a resource is blocked due to court orders, copyright claims, or other legal demands. Typically search engines (for example, Google) and ISP (for example, ATT) are the ones affected by this response code, rather than the origin server itself. The server should include an explanation in the response body, detailing the legal demand or reason for the restriction.

### Cloudflare-specific information

Cloudflare may pass through a `451` response from the origin server if the requested resource is legally restricted.

[PreviousError 429](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-429/)[NextError 499](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/)

Was this helpful?

YesNo
