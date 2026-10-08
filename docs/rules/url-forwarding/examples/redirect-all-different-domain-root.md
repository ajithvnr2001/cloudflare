---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/
title: Redirect requests for a domain to a new domain \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.536595+00:00
---

# Redirect requests for a domain to a new domain · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect requests for a domain to a new domain



# Redirect requests for a domain to a new domain

Create a redirect rule to redirect all URLs for a domain to point to the root of a new domain, including any subdomains of the old domain.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In this example, an old website was discontinued and replaced by a new one in a different domain. The functionality is different, and all URLs should now point to the root of the new domain. The same applies to any subdomains of the old domain.

[Create a redirect rule](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/create-dashboard/) with the following configuration:

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `http*://*example.com/*`



**Then**

  * **Target URL** : `https://example.net/`
  * **Status code:** _301_



For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`http://example.com/` | `https://example.net/` | `301`  
`https://example.com/` | `https://example.net/` | `301`  
`https://subdomain.example.com/` | `https://example.net/` | `301`  
`https://example.com/my/path/to/page.htm` | `https://example.net/` | `301`  
`https://example.com/search?q=term` | `https://example.net/` | `301`  
  
[PreviousRedirect local visitors to specific subdomains](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/)[NextRedirect requests from one country to a domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-all-different-domain-root.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
