---
url: https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/
title: Redirecting *.pages.dev to a Custom Domain \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:35.561761+00:00
---

# Redirecting *.pages.dev to a Custom Domain · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /How to
  4. /Redirecting *.pages.dev to a Custom Domain



# Redirecting *.pages.dev to a Custom Domain

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupRelated resources

Learn how to use [Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/) to redirect your `*.pages.dev` subdomain to your [custom domain](https://developers.cloudflare.com/pages/configuration/custom-domains/).

You may want to do this to ensure that your site's content is served only on the custom domain, and not the `<project>.pages.dev` site automatically generated on your first Pages deployment.

## Setup

To redirect a `<project>.pages.dev` subdomain to your custom domain:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project.

  3. Go to **Custom domains** and make sure that your custom domain is listed. If it is not, add it by clicking **Set up a custom domain**.

  4. Go **Bulk Redirects**.

  5. [Create a bulk redirect list](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list) modeled after the following (but replacing the values as appropriate):




Source URL | Target URL | Status | Parameters  
---|---|---|---  
`<project>.pages.dev` | `https://example.com` | `301` | 

  * Preserve query string
  * Subpath matching
  * Preserve path suffix
  * Include subdomains

  
  
  6. [Create a bulk redirect rule](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#2-create-a-bulk-redirect-rule) using the list you just created.



To test that your redirect worked, go to your `<project>.pages.dev` domain. If the URL is now set to your custom domain, then the rule has propagated.

## Related resources

  * [Redirect www to domain apex](https://developers.cloudflare.com/pages/how-to/www-redirect/)
  * [Handle redirects with Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)



[PreviousPreview Local Projects with Cloudflare Tunnel](https://developers.cloudflare.com/pages/how-to/preview-with-cloudflare-tunnel/)[NextRedirecting www to domain apex](https://developers.cloudflare.com/pages/how-to/www-redirect/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/how-to/redirect-to-custom-domain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
