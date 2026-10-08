---
url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/
title: Total TLS error messages \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:38.676407+00:00
---

# Total TLS error messages · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)Additional options

  4. /[Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/)
  5. /Error messages



# Error messages

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPending domainsActive domains

To help avoid [`ERR_SSL_VERSION_OR_CIPHER_MISMATCH`](https://developers.cloudflare.com/ssl/troubleshooting/version-cipher-mismatch/) errors, Cloudflare automatically shows an error message - `This hostname is not covered by a certificate` \- on proxied DNS records not covered by a TLS certificate.

## Pending domains

If you recently [added your domain](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/) to Cloudflare - meaning that your zone is in a [pending state](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/) \- you can often ignore this warning.

Once most domains becomes **Active** , Cloudflare will automatically issue a Universal SSL certificate, which will provide SSL/TLS coverage and remove the warning message.

Note

Since there are a few nuances to certificate coverage and issuance timing, review [Enable Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/) to make sure your domain will receive SSL/TLS coverage automatically.

## Active domains

If your zone is already active on Cloudflare, this warning identifies subdomains that are not covered by your current SSL/TLS certificate.

By default, Cloudflare [Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) only cover your apex domain and one level of subdomain.

Hostname | Covered by Universal certificate?  
---|---  
`example.com` | Yes  
`www.example.com` | Yes  
`docs.example.com` | Yes  
`dev.docs.example.com` | No  
`test.dev.api.example.com` | No  
  
To prevent insecure connections on a multi-level subdomain, do one of the following:

  * Enable [Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/), which automatically issues individual certificates to your proxied hostnames not covered by a Universal certificate.
  * Order an [Advanced Certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/) covering the subdomain.
  * Upload a [Custom Certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/) covering the subdomain.



If none of these solutions work, you could also remove the multi-level subdomain.

[PreviousEnable](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/enable/)[NextAlways Use HTTPS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/additional-options/total-tls/error-messages.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
