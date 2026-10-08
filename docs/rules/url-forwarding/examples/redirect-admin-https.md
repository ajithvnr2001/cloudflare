---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/
title: Redirect admin area requests to HTTPS \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:59.824747+00:00
---

# Redirect admin area requests to HTTPS · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect admin area requests to HTTPS



# Redirect admin area requests to HTTPS

Create a redirect rule to redirect requests for the administration area of `store.example.com` to HTTPS, keeping the original path and query string.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect requests for the administration area of a specific subdomain (`store.example.com`) to HTTPS, keeping the original path and query string.

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `http://store.example.com/admin*`



**Then**

  * **Target URL** : `https://store.example.com/admin${1}`
  * **Status code:** _301_
  * **Preserve query string:** Enabled



For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`http://store.example.com/admin/products/` | `https://store.example.com/admin/products/` | `301`  
`https://store.example.com/admin/products/` | (unchanged) | n/a  
`http://store.example.com/admin/?logged_out=true` | `https://store.example.com/admin/?logged_out=true` | `301`  
`http://store.example.com/?all_items=true` | (unchanged) | n/a  
`http://example.com/admin/` | (unchanged) | n/a  
  
[PreviousPerform mobile redirects](https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/)[NextRedirect from root to WWW](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-admin-https.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
