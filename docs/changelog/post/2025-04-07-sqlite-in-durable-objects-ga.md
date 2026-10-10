---
url: https://developers.cloudflare.com/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/
title: SQLite in Durable Objects GA with 10GB storage per object \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.378108+00:00
---

# SQLite in Durable Objects GA with 10GB storage per object · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 7, 2025

## SQLite in Durable Objects GA with 10GB storage per object

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

SQLite in Durable Objects is now generally available (GA) with 10GB SQLite database per Durable Object. Since the [public beta ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/) in September 2024, we've added feature parity and robustness for the SQLite storage backend compared to the preexisting key-value (KV) storage backend for Durable Objects.

SQLite-backed Durable Objects are recommended for all new Durable Object classes, using `new_sqlite_classes` [Wrangler configuration](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class). Only SQLite-backed Durable Objects have access to Storage API's [SQL](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#sql-api) and [point-in-time recovery](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api) methods, which provide relational data modeling, SQL querying, and better data management.
    
    
    export class MyDurableObject extends DurableObject {
      sql: SqlStorage
      constructor(ctx: DurableObjectState, env: Env) {
        super(ctx, env);
        this.sql = ctx.storage.sql;
      }
    
      async sayHello() {
        let result = this.sql
          .exec("SELECT 'Hello, World!' AS greeting")
          .one();
        return result.greeting;
      }
    }

KV-backed Durable Objects remain for backwards compatibility, and a migration path from key-value storage to SQL storage for existing Durable Object classes will be offered in the future.

For more details on SQLite storage, checkout [Zero-latency SQLite storage in every Durable Object blog ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/).
