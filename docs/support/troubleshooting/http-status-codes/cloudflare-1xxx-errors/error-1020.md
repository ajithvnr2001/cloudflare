---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/
title: Error 1020 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.687075+00:00
---

# Error 1020 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1020



# Error 1020

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1020: Access denied Common cause Resolution

## Error 1020: Access denied

This error indicates that access to the website is denied by a Cloudflare firewall rule.

### Common cause

A client or browser is blocked by a Cloudflare customer's Firewall Rules (deprecated).

### Resolution

If you are not the website owner, provide the website owner with a screenshot of the `1020` error message you received.

If you are the website owner:

  1. Retrieve a screenshot of the 1020 error from your customer.

  2. Search the [Security Events log](https://developers.cloudflare.com/waf/analytics/security-events/) (available at **Security** > **Analytics** , in the **Events** tab) for the [Ray ID](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/) or client IP address from the visitor's 1020 error message.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)

Note

Convert the UTC timestamp of the `1020` error to your local timezone when searching in the Security Events log.

  3. Assess the cause of the block and either update the Firewall Rule or allow the visitor's IP address in [IP Access Rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/).




[PreviousError 1019](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1019/)[NextError 1023](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1023/)

Was this helpful?

YesNo
