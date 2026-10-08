---
url: https://developers.cloudflare.com/pages/how-to/www-redirect/
title: Redirecting www to domain apex \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:36.005265+00:00
---

# Redirecting www to domain apex · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/how-to/www-redirect/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /How to
  4. /Redirecting www to domain apex



# Redirecting www to domain apex

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/how-to/www-redirect/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupRelated resources

Learn how to redirect a `www` subdomain to your apex domain (`example.com`).

This setup assumes that you already have a [custom domain](https://developers.cloudflare.com/pages/configuration/custom-domains/) attached to your Pages project.

## Setup

To redirect your `www` subdomain to your domain apex:

  1. In the Cloudflare dashboard, go to the **Bulk Redirects** page.

[ Go to **Bulk redirects** ↗ ](https://dash.cloudflare.com/?to=/:account/bulk-redirects)
  2. [Create a bulk redirect list](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list) modeled after the following (but replacing the values as appropriate):




Source URL | Target URL | Status | Parameters  
---|---|---|---  
`www.example.com` | `https://example.com` | `301` | 

  * Preserve query string
  * Subpath matching
  * Preserve path suffix
  * Include subdomains

  
  
  4. [Create a bulk redirect rule](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#2-create-a-bulk-redirect-rule) using the list you just created.
  5. Go to **DNS**.
  6. [Create a DNS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records) for the `www` subdomain using the following values:



Type | Name | IPv4 address | Proxy status  
---|---|---|---  
`A` | `www` | `192.0.2.1` | Proxied  
  
It may take a moment for this DNS change to propagate, but once complete, you can run the following command in your terminal.
    
    
    curl --head -i https://www.example.com/

Then, inspect the output to verify that the `location` header and status code are being set as configured.

## Related resources

  * [Redirect `*.pages.dev` to a custom domain](https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/)
  * [Handle redirects with Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)



[PreviousRedirecting *.pages.dev to a Custom Domain](https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/)[NextSet build commands per branch](https://developers.cloudflare.com/pages/how-to/build-commands-branches/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/how-to/www-redirect.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
