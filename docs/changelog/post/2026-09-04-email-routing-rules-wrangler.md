---
url: https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/
title: Manage Email Routing rules with Wrangler \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:12.454483+00:00
---

# Manage Email Routing rules with Wrangler · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 4, 2026

## Manage Email Routing rules with Wrangler

[Email Service](https://developers.cloudflare.com/email-service/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now manage Email Routing rules that route emails to Workers from your Wrangler configuration. Add literal addresses or a catch-all address to the top-level `addresses` field:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "invoice-handler",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "addresses": [
        "invoice@yourdomain.com"
      ]
    }
    
    
    name = "invoice-handler"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    addresses = ["invoice@yourdomain.com"]

When you run `wrangler deploy`, Wrangler creates rules for new addresses, updates existing rules managed by the Worker, and removes managed rules that are no longer in the configuration. Wrangler shows the planned changes and asks for confirmation before applying potentially destructive changes.

Email Routing rules created by Wrangler also appear in the dashboard but with an icon that identifies them.

![Email Routing rule created by Wrangler in dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2440,height=526,format=webp/_astro/wrangler-email-routing-rules-dash.BZQZlAJI.png)

Refer to [Configure rules with Wrangler](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#configure-rules-with-wrangler) for more information.
