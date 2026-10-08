---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/
title: Redirect requests from one country to a domain \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.039394+00:00
---

# Redirect requests from one country to a domain · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect requests from one country to a domain



# Redirect requests from one country to a domain

Create a redirect rule to redirect all website visitors from the United Kingdom to a different domain, maintaining the current functionality in the same paths.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In this example, all website visitors from the United Kingdom will be redirected to a different domain, but maintaining current functionality in the same paths.

  1. Create a Bulk Redirect List named `uk_redirect_list` with the following URL redirect:

     * **Source URL** : `https://example.com/`
     * **Target URL** : `https://example.co.uk/`
     * **Subpath matching** : Enabled
     * **Preserve query string** : Enabled
  2. Create a Bulk Redirect Rule that enables the previous Bulk Redirect List and set the rule expression to the following:
         
         ip.src.country == "GB" and http.request.full_uri in $uk_redirect_list




This configuration will perform the following redirects for UK visitors:

Request URL | URL after redirect  
---|---  
`https://example.com/` | `https://example.co.uk/`  
`https://example.com/my/path/to/page.htm` | `https://example.co.uk/my/path/to/page.htm`  
`https://example.com/search?q=term` | `https://example.co.uk/search?q=term`  
  
[PreviousRedirect requests for a domain to a new domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/)[NextRedirect requests from one domain to another](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-another-domain/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-all-country.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
