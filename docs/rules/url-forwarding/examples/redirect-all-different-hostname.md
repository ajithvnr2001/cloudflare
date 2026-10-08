---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/
title: Redirect requests to a different hostname \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.076315+00:00
---

# Redirect requests to a different hostname · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect requests to a different hostname



# Redirect requests to a different hostname

Create a redirect rule to redirect all requests for `smallshop.example.com` to a different hostname using HTTPS, keeping the original path and query string.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect will redirect all requests for `smallshop.example.com` to a different hostname `globalstore.example.net` using HTTPS, keeping the original path and query string.

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `http*://smallshop.example.com/*`



**Then**

  * **Target URL** : `https://globalstore.example.net/${2}`
  * **Status code:** _301_
  * **Preserve query string:** Enabled



For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`http://smallshop.example.com/` | `https://globalstore.example.net/` | `301`  
`http://smallshop.example.com/admin/?logged_out=true` | `https://globalstore.example.net/admin/?logged_out=true` | `301`  
`https://smallshop.example.com/?all_items=1` | `https://globalstore.example.net/?all_items=1` | `301`  
`http://example.com/about/` | (unchanged) | n/a  
  
[PreviousRedirect requests from one domain to another](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/)[NextRedirect visitors to a new page URL](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-all-different-hostname.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
