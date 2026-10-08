---
url: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/flexible/
title: Flexible - SSL/TLS encryption modes \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:44.076909+00:00
---

# Flexible - SSL/TLS encryption modes · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/flexible/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

Origin server

  4. /[Encryption modes](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/)
  5. /Flexible



# Flexible

Last updated Sep 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/flexible/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse whenRequired setup Prerequisites ProcessLimitations

Setting your encryption mode to **Flexible** makes your site partially secure. Cloudflare allows HTTPS connections between your visitor and Cloudflare, but all connections between Cloudflare and your origin are made through HTTP. As a result, an SSL certificate is not required on your origin.
    
    
    flowchart LR
        accTitle: Flexible SSL/TLS Encryption
        accDescr: With an encryption mode of Flexible, your application encrypts traffic between the visitor and Cloudflare, but not between Cloudflare and your server.
        A[Visitor] <--Encrypted--> B((Cloudflare))<--Unencrypted--> C[(Origin server)]
    

## Use when

Choose this option when you cannot set up an SSL certificate on your origin or your origin does not support SSL/TLS.

## Required setup

### Prerequisites

Depending on your origin configuration, you may have to adjust settings to avoid [Mixed Content errors](https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/) or [redirect loops](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/).

### Process

To change your encryption mode in the dashboard:

  1. In the Cloudflare dashboard, go to the **SSL/TLS Overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls)
  2. Choose an encryption mode.




To adjust your encryption mode with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `ssl` as the setting name in the URI path, and the `value` parameter set to your desired setting (`off`, `flexible`, `full`, `strict`, or `origin_pull`).

## Limitations

Caution

If your origin forces HTTPS by automatically redirecting HTTP requests to HTTPS, do not use Flexible mode. Because Cloudflare connects to your origin over HTTP, this creates a redirect loop that makes your site inaccessible. Use [**Full**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/) or [**Full (strict)**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/) mode instead.

Refer to [ERR_TOO_MANY_REDIRECTS](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/) for troubleshooting guidance, or [Enforce HTTPS connections](https://developers.cloudflare.com/ssl/edge-certificates/encrypt-visitor-traffic/) to redirect traffic to HTTPS at the Cloudflare edge without setting up redirects at your origin.

Flexible mode is only supported for HTTPS connections on port 443 (default port). Other ports using HTTPS will fall back to [**Full** mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/).

If your application contains sensitive information (personalized data, user login), use [**Full**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/) or [**Full (Strict)**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/) modes instead.

[Authenticated Origin Pull](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/) does not work when your [**SSL/TLS encryption mode**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/) is set to **Off** or **Flexible**.

  


[PreviousOff (no encryption)](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/)[NextFull](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/ssl-modes/flexible.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
