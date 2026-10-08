---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/
title: Error 1000 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:56.563128+00:00
---

# Error 1000 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1000



# Error 1000

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1000: DNS points to prohibited IP Common causes Resolution

## Error 1000: DNS points to prohibited IP

This error indicates that a Cloudflare DNS record points to a prohibited IP, blocking access to the requested domain.

### Common causes

Cloudflare halted the request for one of the following reasons:

  * An A record within your Cloudflare DNS app points to a [Cloudflare IP address ↗︎](https://www.cloudflare.com/ips/), or a Load Balancer Origin points to a proxied record.
  * Your Cloudflare DNS A or CNAME record references another reverse proxy (such as an nginx web server that uses the proxy_pass function) that then proxies the request to Cloudflare a second time.
  * The request `X-Forwarded-For` header is longer than 100 characters.
  * The request includes two `X-Forwarded-For` headers.
  * The request includes a `CF-Connecting-IP` header.
  * A Server Name Indication (SNI) issue or mismatch at the origin.
  * Your DNS record points to a SaaS provider that uses [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) with [BYOIP](https://developers.cloudflare.com/byoip/) (Bring Your Own IP). Because the provider's IP addresses are advertised through Cloudflare's network, requests resolve to Cloudflare infrastructure. If the provider has not configured a [custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/) for your domain, this error is returned.



### Resolution

  * If an A record within your Cloudflare DNS app points to a [Cloudflare IP address ↗︎](https://www.cloudflare.com/ips/), update the IP address to your origin web server IP address. Reach out to your hosting provider if you need help obtaining the origin IP address.
  * There is a reverse-proxy at your origin that sends the request back through the Cloudflare proxy. Instead of using a reverse-proxy, contact your hosting provider or site administrator to configure an HTTP redirect at your origin.
  * If your domain points to a SaaS provider that uses Cloudflare, contact the SaaS provider to verify that a custom hostname is properly configured for your domain. The error originates from the provider's Cloudflare account, not yours.



[PreviousOverview](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)[NextError 1001](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1001/)

Was this helpful?

YesNo
