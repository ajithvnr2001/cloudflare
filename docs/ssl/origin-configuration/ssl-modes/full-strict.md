---
url: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/
title: Full (strict) - SSL/TLS encryption modes \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:44.246622+00:00
---

# Full (strict) - SSL/TLS encryption modes · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

Origin server

  4. /[Encryption modes](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/)
  5. /Full (strict)



# Full (strict)

Last updated Jul 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse whenRequired setup Prerequisites ProcessLimitations

When you set your encryption mode to **Full (strict)** , Cloudflare does everything in [Full mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/) but also enforces more stringent requirements for origin certificates.
    
    
    flowchart LR
        accTitle: Full - Strict SSL/TLS Encryption
        accDescr: With an encryption mode of Full (strict), your application encrypts traffic going to and coming from Cloudflare.
        A[Visitor] <--Encrypted--> B((Cloudflare))<--Encrypted--> C[("Origin server (verified) #9989;")]
    

## Use when

For the best security, choose **Full (strict)** mode whenever possible (unless you are an [Enterprise customer](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/ssl-only-origin-pull/)).

Your origin needs to be able to support an SSL certificate that is:

  * Unexpired, meaning the certificate presents `notBeforeDate < now() < notAfterDate`.
  * Issued by a [publicly trusted certificate authority ↗︎](https://github.com/cloudflare/cfssl_trust) or [Cloudflare’s Origin CA](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/).
  * Contains a Common Name (CN) or Subject Alternative Name (SAN) that matches the requested or target hostname.



Note

In addition to **Full (strict)** encryption, you can also set up [Authenticated Origin Pulls](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/) to ensure all requests to your origin are evaluated before receiving a response.

## Required setup

### Prerequisites

Before enabling **Full (strict)** mode, make sure your origin:

  * Allows HTTPS connections on port `443`.
  * Presents a certificate matching the requirements above.



Otherwise, your visitors may experience a [526 error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/).

### Process

To change your encryption mode in the dashboard:

  1. In the Cloudflare dashboard, go to the **SSL/TLS Overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls)
  2. Choose an encryption mode.




To adjust your encryption mode with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `ssl` as the setting name in the URI path, and the `value` parameter set to your desired setting (`off`, `flexible`, `full`, `strict`, or `origin_pull`).

## Limitations

Depending on your origin configuration, you may have to adjust settings to avoid [Mixed Content errors](https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/) or [redirect loops](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/).

[PreviousFull](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/)[NextStrict (SSL-Only Origin Pull)](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/ssl-only-origin-pull/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/ssl-modes/full-strict.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
