---
url: https://developers.cloudflare.com/ssl/
title: Overview \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:36.575604+00:00
---

# Overview · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/

  1. [Home](https://developers.cloudflare.com/)
  2. /SSL/TLS



# Cloudflare SSL/TLS

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesRelated products

Encrypt your web traffic to prevent data theft and other tampering.

Available on all plans

SSL/TLS certificates encrypt traffic between visitors and your website, preventing eavesdropping and data tampering. Because Cloudflare sits between your visitors and your origin server, two certificates can be involved in a single request: an [edge certificate](https://developers.cloudflare.com/ssl/concepts/#edge-certificate) (visitor to Cloudflare) and an [origin certificate](https://developers.cloudflare.com/ssl/concepts/#origin-certificate) (Cloudflare to your server).

Cloudflare automatically issues free certificates through [Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) and offers additional options for custom certificate management. Refer to [Get started](https://developers.cloudflare.com/ssl/get-started/) to set up SSL/TLS for your domain.

* * *

## Features

[Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/)

Universal SSL covers your apex domain and first-level subdomains. Total TLS extends that coverage by automatically issuing certificates for proxied hostnames at any subdomain level.

Use Total TLS

[Delegated DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/)

Before issuing a certificate, a certificate authority (CA) must verify you control the domain. If you manage DNS outside of Cloudflare, you can delegate this verification to Cloudflare so certificate renewals happen automatically.

Use Delegated DCV

[Custom TLS settings](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/)

Specify the minimum TLS version that visitors must use to connect to your website or application, and [restrict cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/) to meet compliance or security requirements.

Use Custom TLS settings

* * *

## Related products

[Cloudflare DNS](https://developers.cloudflare.com/dns/)

When you use Cloudflare DNS, all DNS queries for your domain are answered by Cloudflare's global anycast network. This network delivers performance and global availability.

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

Cloudflare for SaaS allows you to extend the security and performance benefits of Cloudflare's network to your customers via their own custom or vanity domains.

[NextConcepts](https://developers.cloudflare.com/ssl/concepts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
