---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/
title: Redirect local visitors to specific subdomains \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.118748+00:00
---

# Redirect local visitors to specific subdomains · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect local visitors to specific subdomains



# Redirect local visitors to specific subdomains

Create a redirect rule to redirect United Kingdom and France visitors from the `example.com` website's root path (`/`) to their localized subdomains `https://gb.example.com` and `https://fr.example.com`, respectively.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect United Kingdom and France visitors requesting the website's root path (`/`) to their localized subdomains `https://gb.example.com` and `https://fr.example.com`, respectively.

**When incoming requests match**

Using the Expression Editor:  
`(ip.src.country eq "GB" or ip.src.country eq "FR") and http.request.uri.path eq "/"`

**Then**

  * **Type:** _Dynamic_
  * **Expression:** `lower(concat("https://", ip.src.country, ".example.com"))`
  * **Status code:** _301_



For example, the redirect rule would perform the following redirects:

Visitor country | Request URL | Target URL | Status code  
---|---|---|---  
United Kingdom | `example.com` | `https://gb.example.com` | `301`  
France | `example.com` | `https://fr.example.com` | `301`  
United States | `example.com` | (unchanged) | n/a  
  
[PreviousRedirect from WWW to root](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/)[NextRedirect requests for a domain to a new domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-country-subdomains.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
