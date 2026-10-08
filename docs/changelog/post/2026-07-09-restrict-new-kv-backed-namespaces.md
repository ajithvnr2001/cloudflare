---
url: https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/
title: New Durable Object namespaces must use the SQLite storage backend \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:02.501495+00:00
---

# New Durable Object namespaces must use the SQLite storage backend · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 9, 2026

## New Durable Object namespaces must use the SQLite storage backend

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the [SQLite storage backend](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class), which has been recommended for all new Durable Objects since it became [generally available ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/) in 2024.

Create a new class with a `new_sqlite_classes` migration:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "migrations": [
        {
          "tag": "v1",
          "new_sqlite_classes": [
            "MyDurableObject"
          ]
        }
      ]
    }
    
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = ["MyDurableObject"]

SQLite-backed Durable Objects have feature parity with the key-value backend — including the [key-value storage API](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#synchronous-kv-api) — and additionally support relational [SQL queries](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#sql-api) and [point-in-time recovery](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api) to restore an object's storage to any point in the past 30 days.

If you attempt to create a new key-value backed namespace (a `new_classes` migration) on an affected account, the deployment fails with the following error:
    
    
    Creating new key-value backed Durable Object namespaces is no longer supported on this account. Please create a namespace using a `new_sqlite_classes` migration instead.

This change only affects accounts that are not already using the key-value storage backend. Accounts with at least one existing key-value backed namespace can still create new ones for now, and the Workers Free plan has only ever supported SQLite-backed Durable Objects. It is part of a broader move toward SQLite as the single storage backend for Durable Objects, ahead of a future migration path for existing key-value backed objects.

For more information, refer to [Durable Objects migrations](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/).
