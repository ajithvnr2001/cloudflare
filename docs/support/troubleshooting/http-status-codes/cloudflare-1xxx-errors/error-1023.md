---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1023/
title: Error 1023 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.745444+00:00
---

# Error 1023 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1023/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1023



# Error 1023

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1023/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1023: Could not find host Common causes Resolution

## Error 1023: Could not find host

This error indicates that the host could not be found due to a configuration issue or propagation delay.

### Common causes

  * If the owner just signed up for Cloudflare it can take a few minutes for the website's information to be distributed to our global network. Something is wrong with the site's configuration.
  * Usually, this happens when accounts have been signed up with a partner organization (for example, hosting provider) and the provider's DNS fails.



Note

Error `1023` is returned via a HTTP `503` response code.

### Resolution

Contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) with the following details:

  * Your domain name.
  * A screenshot of the `1023` error including the [**Ray ID**](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/) mentioned in the error message.
  * A [HAR file](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/) captured while duplicating the error.



[PreviousError 1020](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/)[NextError 1025](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1025/)

Was this helpful?

YesNo
