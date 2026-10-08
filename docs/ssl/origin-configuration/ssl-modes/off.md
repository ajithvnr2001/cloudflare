---
url: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/
title: Off - SSL/TLS encryption modes \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:44.297158+00:00
---

# Off - SSL/TLS encryption modes · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

Origin server

  4. /[Encryption modes](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/)
  5. /Off (no encryption)



# Off (no encryption)

Last updated Jul 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse whenRequired setupLimitations Incompatible settings

Setting your encryption mode to **Off (not recommended)** redirects any HTTPS request to plaintext HTTP.
    
    
        flowchart LR
            accTitle: No SSL/TLS Encryption
            accDescr: With an encryption mode of Off, your application does not encrypt traffic between the visitor and Cloudflare or between Cloudflare and your server.
            A[Visitor] <--Unencrypted--> B((Cloudflare))<--Unencrypted--> C[(Origin server)]
    

## Use when

Cloudflare does not recommend setting your encryption mode to **Off**.

## Required setup

To change your encryption mode in the dashboard:

  1. In the Cloudflare dashboard, go to the **SSL/TLS Overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls)
  2. Choose an encryption mode.




To adjust your encryption mode with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `ssl` as the setting name in the URI path, and the `value` parameter set to your desired setting (`off`, `flexible`, `full`, `strict`, or `origin_pull`).

## Limitations

When you set your encryption mode to **Off** , your application:

  * Leaves your visitors and your application [vulnerable to attacks ↗︎](https://www.cloudflare.com/learning/ssl/why-use-https/).
  * Will be marked as "not secure" by Chrome and other browsers, reducing visitor trust.
  * Will be penalized in [SEO rankings ↗︎](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html).



### Incompatible settings

When you set your SSL/TLS encryption mode to **Off** , you will not see the options for [**Always Use HTTPS**](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/) or [**Onion Routing**](https://developers.cloudflare.com/network/onion-routing/).

[Authenticated Origin Pull](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/) does not work when your [**SSL/TLS encryption mode**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/) is set to **Off** or **Flexible**.

  


[PreviousOverview](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/)[NextFlexible](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/flexible/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/ssl-modes/off.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
