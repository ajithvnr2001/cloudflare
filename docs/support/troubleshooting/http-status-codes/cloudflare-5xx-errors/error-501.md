---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/
title: Error 501 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.504029+00:00
---

# Error 501 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 5xx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)
  5. /Error 501



# Error 501

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 501: not implemented Common causes Resolution

## Error 501: not implemented

Cloudflare Workers returns a `501` error when a request uses an HTTP method that is not supported by the Workers Runtime.

### Common causes

  * A client sent a request to a Workers script using a custom or non-standard HTTP method (methods outside of `GET`, `POST`, `PUT`, etc.).
  * A typo in the HTTP method (for example, `POT` instead of `POST`).



### Resolution

  * Update the client to use a valid, standard [HTTP request method ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).



[PreviousError 500](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/)[NextError 502 or 504](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/)

Was this helpful?

YesNo
