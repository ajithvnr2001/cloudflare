---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1005/
title: Error 1005 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:56.744755+00:00
---

# Error 1005 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1005/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1005



# Error 1005

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1005/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewErrors 1005 Access Denied: Autonomous System Number (ASN) banned Common causes Resolution

## Errors 1005 Access Denied: Autonomous System Number (ASN) banned

This error indicates that access to the website is denied due to the banning of the Autonomous System Number (ASN).

### Common causes

The owner of the website (for example, `example.com`) has banned the autonomous system number (ASN) from accessing the website.

### Resolution

If you are not the website owner, provide the website owner with a screenshot of the 1005 error message you received.

If you are the website owner:

  1. Retrieve a screenshot of the `1005` error from your customer
  2. Search the [**Security Events log**](https://developers.cloudflare.com/waf/analytics/security-events/) (available at **Security** > **Events**) for the [**Ray ID**](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/), or client IP Address from the visitor's 1005 error message.



Note

Convert the UTC timestamp of the `1005` error to your local timezone when searching in the **Security Events log**.

  3. Assess the cause of the block and ensure the ASN is allowed under the [IP Access Rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/) security feature.



[PreviousError 1004](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1004/)[NextError 1006, 1007, 1008 or 1106](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1006/)

Was this helpful?

YesNo
