---
url: https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/
title: Connect to remote databases during local development with wrangler dev \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:30.825063+00:00
---

# Connect to remote databases during local development with wrangler dev · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 4, 2025

## Connect to remote databases during local development with wrangler dev

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now connect directly to remote databases and databases requiring TLS with `wrangler dev`. This lets you run your Worker code locally while connecting to remote databases, without needing to use `wrangler dev --remote`.

The `localConnectionString` field and `CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_<BINDING_NAME>` environment variable can be used to configure the connection string used by `wrangler dev`.
    
    
    {
      "hyperdrive": [
        {
          "binding": "HYPERDRIVE",
          "id": "your-hyperdrive-id",
          "localConnectionString": "postgres://user:password@remote-host.example.com:5432/database?sslmode=require"
        }
      ]
    }

Learn more about [local development with Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/local-development/).
