---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1006/
title: Error 1006, 1007, 1008 or 1106 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.052526+00:00
---

# Error 1006, 1007, 1008 or 1106 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1006/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1006, 1007, 1008 or 1106



# Error 1006, 1007, 1008 or 1106

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1006/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewErrors 1006, 1007, 1008 or 1106 Access Denied: Your IP address has been banned Common causes Resolution

## Errors 1006, 1007, 1008 or 1106 Access Denied: Your IP address has been banned

This error indicates that access is denied because your IP address has been banned.

### Common causes

A Cloudflare customer blocked traffic from your client or browser.

Note

Error 1006 also occurs in the Cloudflare **Workers** app under the **Preview** tab when a customer uses **[Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/)** or any other Cloudflare security feature to block the Google Cloud Platform IPs that the **Preview** tab relies upon.

### Resolution

Request the website owner to investigate their Cloudflare security settings or allow your client IP address. Since the website owner blocked your request, Cloudflare support cannot override a customer's security settings.

[PreviousError 1005](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1005/)[NextError 1009](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1009/)

Was this helpful?

YesNo
