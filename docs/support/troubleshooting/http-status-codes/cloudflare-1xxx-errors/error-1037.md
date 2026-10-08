---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1037/
title: Error 1037 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.103863+00:00
---

# Error 1037 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1037/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1037



# Error 1037

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1037/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1037: Invalid rewrite rule (failed to evaluate expression) Common cause Resolution

## Error 1037: Invalid rewrite rule (failed to evaluate expression)

This error indicates that the rewrite rule expression could not be evaluated.

### Common cause

There are several causes for this error, but it can mean that one expression element contained an undefined value when it was evaluated.

For example, you get a 1037 error when using the following URL rewrite dynamic expression and the `X-Source` header is not included in the request:

`http.request.headers["x-source"][0]`

### Resolution

Make sure that all the elements of your rewrite expression are defined. For example, if you are referring to a header value, ensure the header is set.

[PreviousError 1036](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1036/)[NextError 1040](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1040/)

Was this helpful?

YesNo
