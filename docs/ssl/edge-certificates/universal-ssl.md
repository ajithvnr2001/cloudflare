---
url: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/
title: Free Universal SSL/TLS certificates \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:41.075088+00:00
---

# Free Universal SSL/TLS certificates · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)
  4. /Universal SSL



# Universal SSL

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityRelated resources

By default, Cloudflare issues — and [renews](https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/#universal-ssl) — free, unshared, publicly trusted SSL certificates to all domains [added to](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/) and [activated on](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/) Cloudflare.

On a [full setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/), Universal SSL certificates cover your root domain (for example, `example.com`) and first-level subdomains (for example, `www.example.com`). On a [partial (CNAME) setup](https://developers.cloudflare.com/dns/zone-setups/partial-setup/), each proxied subdomain receives its own certificate regardless of depth. Cloudflare handles issuance, renewal, and deployment automatically.

For full setup zones that need coverage beyond first-level subdomains, use [Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/) or [advanced certificates](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/).

Universal certificates are [Domain Validated (DV)](https://developers.cloudflare.com/ssl/concepts/#validation-level), which means the certificate authority verifies domain ownership but does not validate organization identity. For setup details, refer to [Enable Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/).

Note

Universal SSL certificates are issued after your domain is active on Cloudflare. If you need an SSL certificate before migrating traffic, or if you need to [customize cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/), use [Advanced](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) or [Custom](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/) certificates.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
## Related resources

  * [Limitations](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/limitations/)
  * [Backup certificates](https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/)
  * [Validity period and renewal](https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/#universal-ssl)



[PreviousOverview](https://developers.cloudflare.com/ssl/edge-certificates/)[NextEnable Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/universal-ssl/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
