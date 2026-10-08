---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/
title: Error 521 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.876404+00:00
---

# Error 521 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 5xx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)
  5. /Error 521



# Error 521

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 521: web server is down Common causes Resolution

## Error 521: web server is down

Error `521` occurs when the origin web server refuses connections from Cloudflare. Security solutions at your origin may block legitimate connections from certain [Cloudflare IP addresses ↗︎](https://www.cloudflare.com/ips).

### Common causes

The two most common causes of `521` errors are:

  * Offlined origin web server application.
  * Blocked Cloudflare requests.



### Resolution

Contact your hosting provider or site administrator and share the necessary [error details](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider) to assist in troubleshooting these common causes:

  * Ensure your origin web server is responsive.
  * Review origin web server error logs to identify web server application crashes or outages.
  * Confirm [Cloudflare IP addresses ↗︎](https://www.cloudflare.com/ips) are not blocked or rate limited.
  * Allow all [Cloudflare IP ranges ↗︎](https://www.cloudflare.com/ips) in your origin web server's firewall or other security software.
  * Confirm that — if you have your **SSL/TLS mode** set to **Full** or **Full (Strict**) — your origin supports HTTPS and/or you have installed a [Cloudflare Origin Certificate](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca) or a certificate matching the [requirements for these modes](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/#custom-ssltls).
  * Ensure that your origin web server application is actively bound and listening on the port required by your SSL/TLS mode: Port 80 for **Flexible** , or Port 443 for **Full** and **Full (Strict)**.
  * Find additional troubleshooting information on the [Cloudflare Community ↗︎](https://community.cloudflare.com/t/community-tip-fixing-error-521-web-server-is-down/42461).



[PreviousError 520](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/)[NextError 522](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/)

Was this helpful?

YesNo
