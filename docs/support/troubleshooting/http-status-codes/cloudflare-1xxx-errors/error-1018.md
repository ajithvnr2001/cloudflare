---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/
title: Error 1018 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.487803+00:00
---

# Error 1018 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1018



# Error 1018

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1018: Could not find host Common causes Resolution

## Error 1018: Could not find host

This error indicates that the host could not be found.

### Common causes

  * The Cloudflare domain was recently activated and there is a delay propagating the domain's settings to the Cloudflare edge network.
  * The Cloudflare domain was created via a Cloudflare partner (for example, a hosting provider) and the provider's DNS failed.



Note

Error 1018 is returned via a HTTP `409` response code.

### Resolution

Contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) with the following details:

  * Your domain name.
  * A screenshot of the `1018` error including the [**Ray ID**](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/) mentioned in the error message.
  * A [HAR file](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/) captured while duplicating the error.



[PreviousError 1016](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1016/)[NextError 1019](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1019/)

Was this helpful?

YesNo
