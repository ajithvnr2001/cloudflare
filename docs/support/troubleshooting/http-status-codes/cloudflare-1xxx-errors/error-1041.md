---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1041/
title: Error 1041 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.308432+00:00
---

# Error 1041 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1041/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1041



# Error 1041

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1041/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1041: Invalid request rewrite (invalid header value) Common causes Resolution

## Error 1041: Invalid request rewrite (invalid header value)

This error indicates that the header value is not valid.

### Common causes

The added/modified header value is too long or it contains characters that are not allowed.

### Resolution

  * Use a shorter value or expression to define the header value.
  * Remove the characters that are not allowed. Refet to [Format of HTTP request header names and values](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/header-format/) in Developer Docs for more information on the allowed characters.



[PreviousError 1040](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1040/)[NextError 1101](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/)

Was this helpful?

YesNo
