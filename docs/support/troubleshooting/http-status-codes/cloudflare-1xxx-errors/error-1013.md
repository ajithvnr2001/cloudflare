---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1013/
title: Error 1013 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.361481+00:00
---

# Error 1013 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1013/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1013



# Error 1013

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1013/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1013: HTTP hostname and TLS SNI hostname mismatch Common cause Resolution

## Error 1013: HTTP hostname and TLS SNI hostname mismatch

This error indicates a mismatch between the HTTP hostname and the TLS SNI hostname.

### Common cause

The hostname sent by the client or browser via Server Name Indication (SNI) does not match the request host header.

### Resolution

Error `1013` is commonly caused by the following:

  * Your local browser setting the incorrect SNI host header, or
  * A network proxying SSL traffic caused a mismatch between SNI and the Host header of the request.



Test for an SNI mismatch via an online tool, such as [SSL Shopper ↗︎](https://www.sslshopper.com/ssl-checker.html).

Provide Cloudflare Support the following information:

  * A [HAR file](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/) captured while duplicating the error.



[PreviousError 1012](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1012/)[NextError 1014](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/)

Was this helpful?

YesNo
