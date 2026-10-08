---
url: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/
title: Full - SSL/TLS encryption modes \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:44.341366+00:00
---

# Full - SSL/TLS encryption modes · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

Origin server

  4. /[Encryption modes](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/)
  5. /Full



# Full

Last updated Jul 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse whenRequired setup Prerequisites ProcessLimitations

When you set your encryption mode to **Full** , Cloudflare allows HTTPS connections between your visitor and Cloudflare and makes connections to the origin using the scheme requested by the visitor. If your visitor uses `http`, then Cloudflare connects to the origin using plaintext HTTP and vice versa.

## Use when

Choose **Full** mode when your origin can support an SSL certification, but — for various reasons — it cannot support a valid, publicly trusted certificate.

Note

In addition to **Full** encryption, you can also set up [Authenticated Origin Pulls](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/) to ensure all requests to your origin are evaluated before receiving a response.

## Required setup

### Prerequisites

Before enabling **Full** mode, make sure your origin allows HTTPS connections on port 443 and presents a certificate (self-signed, [Cloudflare Origin CA](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/), or purchased from a Certificate Authority). Otherwise, your visitors may experience a [525 error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/).

Depending on your origin configuration, you may have to adjust settings to avoid [Mixed Content errors](https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/) or [redirect loops](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/).

### Process

To change your encryption mode in the dashboard:

  1. In the Cloudflare dashboard, go to the **SSL/TLS Overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls)
  2. Choose an encryption mode.




To adjust your encryption mode with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `ssl` as the setting name in the URI path, and the `value` parameter set to your desired setting (`off`, `flexible`, `full`, `strict`, or `origin_pull`).

## Limitations

The certificate presented by the origin will **not be validated in any way**. It can be expired, self-signed, or not even have a matching CN/SAN entry for the hostname requested.

Without using [**Full (strict)**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/), a malicious party could technically hijack the connection and present their own certificate.

[PreviousFlexible](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/flexible/)[NextFull (strict)](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/ssl-modes/full.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
