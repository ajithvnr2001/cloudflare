---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1001/
title: Error 1001 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:56.606024+00:00
---

# Error 1001 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1001/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1001



# Error 1001

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1001/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1001: DNS resolution error Common causes Resolution

## Error 1001: DNS resolution error

This error indicates a DNS resolution failure preventing access to the requested domain.

### Common causes

  * A web request was sent to a [Cloudflare IP address ↗︎](https://www.cloudflare.com/ips/) for a non-existent Cloudflare domain.
  * An external domain that is not on using Cloudflare has a CNAME record to a domain active on Cloudflare
  * The target of the DNS CNAME record does not resolve.
  * A CNAME record in your Cloudflare DNS app requires resolution via a DNS provider that is currently offline.



### Resolution

A non-Cloudflare domain cannot CNAME to a Cloudflare domain, unless the non-Cloudflare domain is added to a Cloudflare account.

Attempting to directly access DNS records used for [Cloudflare CNAME setups](https://developers.cloudflare.com/dns/zone-setups/partial-setup) also causes error 1001. For example, `www.example.com.cdn.cloudflare.net`.

[PreviousError 1000](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/)[NextError 1002](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1002/)

Was this helpful?

YesNo
