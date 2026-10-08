---
url: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/disable-universal-ssl/
title: Disable Universal SSL certificates \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:41.162910+00:00
---

# Disable Universal SSL certificates · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/disable-universal-ssl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /[Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/)
  5. /Disable Universal SSL certificates



# Disable Universal SSL certificates

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/disable-universal-ssl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPotential errorsDisable Universal SSL certificateRe-enable Universal SSL

Some customers may need to manage their own SSL certificates or rely on specific Certificate Authorities.

If you disable your domain's Universal SSL certificate, Cloudflare removes that certificate from our network and will not order or renew any additional Universal SSL certificates.

Disabling Universal SSL will not cause any interruption to ongoing TLS connections to your domain on Cloudflare's network, they will continue to be served according to the Universal SSL certificate used when they were first established. Eventually these connections will naturally end.

New TLS connections are expected to succeed as long as you have another valid certificate active, such as a [custom](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/)) or [advanced](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) certificate. New TLS connections will receive the highest priority certificate from our edge as per our [certificate and hostname priority](https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/). If a valid certificate is not active before disabling, TLS connections will fail. For more information, refer to Potential errors below.

## Potential errors

To avoid errors with your domain, either [upload a custom certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/) or purchase [Advanced Certificate Manager](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) before disabling Universal SSL.

If you disable Universal SSL, you may experience errors with the following scenarios:

  * **Enabled features** :

    * [HTTP Strict Transport Security (HSTS)](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/http-strict-transport-security/)
    * [Always Use HTTPS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/)
    * [Opportunistic Encryption](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/opportunistic-encryption/)
  * **Other setups** :

    * [Page Rules](https://developers.cloudflare.com/rules/page-rules/) that redirect traffic to HTTPS
    * HTTP to HTTPS redirects at your origin web server



## Disable Universal SSL certificate

Before you disable Universal SSL/TLS, make sure you have [uploaded a custom certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/) or purchased [Advanced Certificate Manager](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) to protect your domain.

To disable Universal SSL in the dashboard:

  1. In the Cloudflare dashboard, go to the **Edge Certificates** page.

[ Go to **Edge Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates)
  2. For **Disable Universal SSL** , select **Disable Universal SSL**.

  3. Read the warnings in the **Acknowledgement**.

  4. Select **I Understand** and select **Confirm**.




To disable Universal SSL with the Cloudflare API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/ssl/subresources/universal/subresources/settings/methods/edit/) request and include the `"enabled": false` parameter.

## Re-enable Universal SSL

To re-enable Universal SSL in the dashboard:

  1. In the Cloudflare dashboard, go to the **Edge Certificates** page.

[ Go to **Edge Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates)
  2. For **Disable Universal SSL** , select **Enable Universal SSL**.




To re-enable Universal SSL with the Cloudflare API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/ssl/subresources/universal/subresources/settings/methods/edit/) request and include the `"enabled": true` parameter.

[PreviousEnable Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/)[NextAlerts](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/alerts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/universal-ssl/disable-universal-ssl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
