---
url: https://developers.cloudflare.com/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/
title: New SAML and OIDC Fields and SAML transforms for Access for SaaS \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.346383+00:00
---

# New SAML and OIDC Fields and SAML transforms for Access for SaaS · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 3, 2025

## New SAML and OIDC Fields and SAML transforms for Access for SaaS

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Access for SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/) now include more configuration options to support a wider array of SaaS applications.

**SAML and OIDC Field Additions**

OIDC apps now include:

  * Group Filtering via RegEx
  * OIDC Claim mapping from an IdP
  * OIDC token lifetime control
  * Advanced OIDC auth flows including hybrid and implicit flows

![OIDC field additions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1021,height=192,format=webp/_astro/oidc-claims.2di8l9Lv.png)

SAML apps now include improved SAML attribute mapping from an IdP.

![SAML field additions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1051,height=202,format=webp/_astro/saml-attribute-statements.CW45j5Qi.png)

**SAML transformations**

SAML identities sent to Access applications can be fully customized using JSONata expressions. This allows admins to configure the precise identity SAML statement sent to a SaaS application.

![Configured SAML statement sent to application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1030,height=254,format=webp/_astro/transformation-box.DyKn-DdN.png)
