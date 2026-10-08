---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-523/
title: Error 523 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.954526+00:00
---

# Error 523 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-523/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 5xx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)
  5. /Error 523



# Error 523

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-523/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 523: origin is unreachable Common causes Resolution

## Error 523: origin is unreachable

This error occurs when Cloudflare cannot contact your origin web server.

### Common causes

This typically occurs when a network device between Cloudflare and the origin web server does not have a route to the origin's IP address.

In AWS environments, a common cause is an overly broad route such as `172.0.0.0/8` in a VPC route table. Cloudflare uses public IP ranges in `172.64.0.0/13`, and a broad route can accidentally capture traffic intended for Cloudflare.

### Resolution

Contact your hosting provider and share the necessary [error details](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider) to exclude the following common causes at your origin web server:

  * Confirm the correct origin IP address is listed for A or AAAA records within your Cloudflare DNS app.
  * Troubleshoot Internet routing issues between your origin and Cloudflare, or with the origin itself.
  * In AWS, review VPC route tables and make sure you are not sending `172.64.0.0/13` toward a private destination. If required, add a more specific route for `172.64.0.0/13` to your Internet Gateway.



If none of the above leads to a resolution, request the following information from your hosting provider or site administrator:

  * An [MTR or traceroute](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#perform-a-traceroute) from your origin web server to a [Cloudflare IP address ↗︎](http://www.cloudflare.com/ips) that most commonly connected to your origin web server before the issue occurred. Identify a connecting Cloudflare IP from the logs of the origin web server.



[PreviousError 522](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/)[NextError 524](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/)

Was this helpful?

YesNo
