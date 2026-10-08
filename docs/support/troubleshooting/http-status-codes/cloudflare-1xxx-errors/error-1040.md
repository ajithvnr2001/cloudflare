---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1040/
title: Error 1040 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.130374+00:00
---

# Error 1040 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1040/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1040



# Error 1040

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1040/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1040: Invalid request rewrite (header modification not allowed) Common cause Resolution

## Error 1040: Invalid request rewrite (header modification not allowed)

This error indicates that an attempt was made to modify a restricted HTTP header.

### Common cause

You are trying to modify an HTTP header that Request Header Transform Rules cannot change.

### Resolution

Make sure you are not trying to modify one of the [reserved HTTP request headers](https://developers.cloudflare.com/rules/transform/request-header-modification/#important-remarks).

[PreviousError 1037](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1037/)[NextError 1041](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1041/)

Was this helpful?

YesNo
