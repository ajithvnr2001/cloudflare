---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/
title: Redirect requests from one domain to another \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:59.977956+00:00
---

# Redirect requests from one domain to another · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect requests from one domain to another



# Redirect requests from one domain to another

Create a redirect rule to redirect all requests to a different domain, maintaining all functionality, except for the discontinued HTTP service (port 80).

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In this example the original domain was replaced with a different domain. All functionality was maintained, except for the HTTP service (port 80) which was discontinued.

[Create a redirect rule](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/create-dashboard/) with the following configuration:

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `http*://example.com/*`



**Then**

  * **Target URL** : `https://example.net/${2}`
  * **Status code:** _301_
  * **Preserve query string:** Enabled



This configuration will perform the following redirects:

Request URL | URL after redirect | Status code  
---|---|---  
`http://example.com/` | `https://example.net/` | `301`  
`https://example.com/` | `https://example.net/` | `301`  
`https://example.com/my/path/to/page.htm` | `https://example.net/my/path/to/page.htm` | `301`  
`https://example.com/search?q=term` | `https://example.net/search?q=term` | `301`  
  
[PreviousRedirect requests from one country to a domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/)[NextRedirect requests to a different hostname](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-all-another-domain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
