---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1035/
title: Error 1035 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.005869+00:00
---

# Error 1035 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1035/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1035



# Error 1035

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1035/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1035: Invalid request rewrite (invalid URI path) Common cause Resolution

## Error 1035: Invalid request rewrite (invalid URI path)

This error indicates an invalid URI path in a request rewrite.

### Common cause

The value or expression of your rewritten URI path is not valid.

This error also occurs when the destination of the URL rewrite is a path under `/cdn-cgi/`.

### Resolution

Make sure that the rewritten URI path is not empty and it starts with a `/` (slash) character.

For example, the following URI path rewrite expression is not valid:

`concat(lower(ip.src.country), http.request.uri.path)`

To fix the expression above, add a `/` prefix:

`concat("/", lower(ip.src.country), http.request.uri.path)`

[PreviousError 1034](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1034/)[NextError 1036](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1036/)

Was this helpful?

YesNo
