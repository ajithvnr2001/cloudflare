---
url: https://developers.cloudflare.com/workers/previews/custom-domains/
title: Custom domains \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:40.068176+00:00
---

# Custom domains · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/previews/custom-domains/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Previews](https://developers.cloudflare.com/workers/previews/)
  4. /Custom domains



# Custom domains

Last updated Sep 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/previews/custom-domains/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you startEnable custom domain Preview URLsEnable workers.dev Preview URLsProtect Preview content

Preview URLs can use a custom domain, `workers.dev`, or both. Enable at least one host to get a Preview URL.

Host | Preview URL | Unique deployment URL  
---|---|---  
Custom domain | `<preview-name>.app.example.com` | `<deployment-id>-<preview-name>.app.example.com`  
`workers.dev` | `<preview-name>-<worker-name>.<subdomain>.workers.dev` | `<deployment-id>-<worker-name>.<subdomain>.workers.dev`  
  
## Before you start

Configure Previews in the same system that manages your custom domain:

Managed with | Configuration  
---|---  
Wrangler | Use the **Wrangler** tab, then run `npx wrangler deploy`.  
Dashboard | Use the **Dashboard** tab.  
Terraform | Update and apply your Terraform configuration.  
  
## Enable custom domain Preview URLs

The following example configures `app.example.com` for Preview traffic only. Add `previews_enabled` and set `enabled` to `false`, then run `npx wrangler deploy` to apply the configuration.
    
    
    {
      "routes": [
        {
          "pattern": "app.example.com",
          "custom_domain": true,
          "previews_enabled": true,
          "enabled": false
        }
      ]
    }
    
    
    [[routes]]
    pattern = "app.example.com"
    custom_domain = true
    previews_enabled = true
    enabled = false

Choose which traffic the custom domain serves:

Traffic | `previews_enabled` | `enabled`  
---|---|---  
Preview only | `true` | `false`  
Production and Preview | `true` | Omit or set `true`  
  
  1. In the Cloudflare dashboard, go to **Workers & Pages** and select your Worker.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. On the **Domains** tab, under **Custom Domains and Routes** , select **\+ Add Domain**.

  3. Enter your domain. For **Enable for** , select _Preview_ or _Production and Preview_. Then select **Add domain**.

![Add Domain modal with Enable for set to Preview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1040,height=756,format=webp/_astro/replace.D64Ztqrs.png)
  4. Confirm that the domain appears under **Custom Domains and Routes**.

![Domains tab showing a custom domain enabled for Preview traffic](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2876,height=1454,format=webp/_astro/customdomainonly.8AG_6tc-.png)



DNS and certificate behavior

Cloudflare creates a wildcard DNS record and SSL certificate for the custom domain, such as `*.app.example.com`. Certificate issuance can take time after you create the first Preview.

Use a dedicated hostname such as `previews.example.com` if your production domain already has subdomains. This avoids wildcard conflicts.

Preview URLs add another subdomain to your hostname. For example, `app.preview.example.com` creates `<preview-name>.app.preview.example.com`. For deeper hostnames, you may need [Advanced Certificate Manager](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) with [Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/) or another certificate that covers the Preview hostname.

## Enable `workers.dev` Preview URLs

Production and Preview `workers.dev` URLs are configured separately.

Set `preview_urls` in your Wrangler configuration file, then run `npx wrangler deploy`.
    
    
    {
      "preview_urls": true
    }
    
    
    preview_urls = true

If `preview_urls` is omitted, Wrangler does not change an existing Preview URL setting. If no setting exists, its initial value depends on `workers_dev`. Set `preview_urls` explicitly to change the Preview URL setting.

  1. In the Cloudflare dashboard, go to **Workers & Pages** and select your Worker.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. On the **Domains** tab, under **Worker URL** , turn on **Preview**.

![Domains tab showing workers.dev Preview URLs enabled with no custom domains configured](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2876,height=1488,format=webp/_astro/emptydomain.C1zwEW1b.png)



## Protect Preview content

To restrict access to custom domain and `workers.dev` Preview URLs, use [Cloudflare Access](https://developers.cloudflare.com/workers/configuration/cloudflare-access/). This prevents unauthenticated users and crawlers from viewing your Preview.

To keep a Preview public while discouraging search engine indexing, add an `X-Robots-Tag: noindex` response header. Cloudflare adds this header automatically to `workers.dev` Preview URLs, but not to custom domain Preview URLs.

For static assets, add the header through a [`_headers` file](https://developers.cloudflare.com/workers/static-assets/headers/). For Worker-generated responses, add it directly in your Worker code.

[PreviousResources and isolation](https://developers.cloudflare.com/workers/previews/resources/)[NextTest and debug](https://developers.cloudflare.com/workers/previews/test-and-debug/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/previews/custom-domains.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
