---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/
title: Redirect from root to WWW \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.193693+00:00
---

# Redirect from root to WWW · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect from root to WWW



# Redirect from root to WWW

Create a redirect rule to forward HTTPS requests from the root (also known as the “apex” or “naked” domain) to the WWW subdomain.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example creates a redirect rule that forwards HTTPS requests from the root domain (`example.com`) to the WWW subdomain (`www.example.com`), while retaining the original path and query string.

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `https://example.com/*`



**Then**

  * **Target URL** : `https://www.example.com/${1}`
  * **Status code** : _301_
  * **Preserve query string** : Enabled



This rule ensures that only HTTPS requests from the root domain are redirected to the WWW subdomain, leaving other requests (such as HTTP or requests to other subdomains) unchanged.

For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`https://example.com/products/` | `https://www.example.com/products/` | `301`  
`https://store.example.com/products/` | (unchanged) | n/a  
`https://example.com/admin/?logged_out=true` | `https://www.example.com/admin/?logged_out=true` | `301`  
`http://example.com/?all_items=true` | (unchanged) | n/a  
`http://www.example.com/admin/` | (unchanged) | n/a  
  
Make sure to replace `example.com` with your actual hostname before deploying your rule.

[PreviousRedirect admin area requests to HTTPS](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/)[NextRedirect from WWW to root](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-root-to-www.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
