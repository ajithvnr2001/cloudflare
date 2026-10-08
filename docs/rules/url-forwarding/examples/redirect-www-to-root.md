---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/
title: Redirect from WWW to root \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.241874+00:00
---

# Redirect from WWW to root · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect from WWW to root



# Redirect from WWW to root

Create a redirect rule to forward HTTPS requests from the WWW subdomain to the root (also known as the “apex” or “naked” domain).

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example creates a redirect rule that forwards HTTPS requests from the WWW subdomain (`www.example.com`) to the root domain (`example.com`), while retaining the original path and query string.

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `https://www.*`



**Then**

  * **Target URL** : `https://${1}`
  * **Status code** : _301_
  * **Preserve query string** : Enabled



This rule ensures that only HTTPS requests from `www.` subdomains are redirected to the root domain, leaving other requests (such as HTTP or non-WWW) unchanged.

For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`https://www.example.com/products/` | `https://example.com/products/` | `301`  
`https://www.store.example.com/products/` | `https://store.example.com/products/` | `301`  
`https://store.example.com/products/` | (unchanged) | n/a  
`https://www.example.com/admin/?logged_out=true` | `https://example.com/admin/?logged_out=true` | `301`  
`http://www.example.com/?all_items=true` | (unchanged) | n/a  
`http://example.com/admin/` | (unchanged) | n/a  
  
[PreviousRedirect from root to WWW](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/)[NextRedirect local visitors to specific subdomains](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-www-to-root.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
