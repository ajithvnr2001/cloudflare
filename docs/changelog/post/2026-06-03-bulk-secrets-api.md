---
url: https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/
title: New Workers bulk secrets API endpoint \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:55.861977+00:00
---

# New Workers bulk secrets API endpoint · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 3, 2026

## New Workers bulk secrets API endpoint

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-03-bulk-secrets-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create, update, or delete multiple secrets for your Worker in a single request using the [bulk secrets endpoint](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/).

  * Include a secret with a value to create or update.
  * Set a secret to `null` to delete.
  * Secrets not included in the request are left unchanged.



The following example creates `API_KEY`, updates the already existing `DB_PASSWORD`, and deletes `OLD_SECRET`:
    
    
    {
      "secrets": {
        "API_KEY": { "type": "secret_text", "name": "API_KEY", "text": "my-api-key" },
        "DB_PASSWORD": { "type": "secret_text", "name": "DB_PASSWORD", "text": "my-db-password" },
        "OLD_SECRET": null
      }
    }

You can do the same from the command line using [`wrangler secret bulk`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#secret-bulk):
    
    
    npx wrangler secret bulk < secrets.json

To delete a key, set its value to `null` in the JSON file. Deletion is not supported with `.env` files.

Each request supports up to **100 total operations** (creates, updates, and deletes combined).
