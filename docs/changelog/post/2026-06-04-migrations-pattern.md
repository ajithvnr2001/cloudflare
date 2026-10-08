---
url: https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/
title: D1 migrations support nested layouts via `migrations_pattern` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:56.479975+00:00
---

# D1 migrations support nested layouts via `migrations_pattern` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 29, 2026

## D1 migrations support nested layouts via `migrations_pattern`

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now point `wrangler d1 migrations apply` at a nested migrations layout — such as the one produced by [Drizzle ↗︎](https://orm.drizzle.team/) (`migrations/0001_init/migration.sql`) — using the new `migrations_pattern` D1 binding config:
    
    
    {
    	"d1_databases": [
    		{
    			"binding": "DB",
    			"database_name": "my-database",
    			"database_id": "<UUID>",
    			"migrations_dir": "migrations",
    			"migrations_pattern": "migrations/*/migration.sql",
    		},
    	],
    }

`migrations_pattern` is a glob (relative to your Wrangler config file) used to discover migration files. It defaults to `${migrations_dir}/*.sql`, so existing projects keep working unchanged. Each migration's name is recorded in the migrations table as a path relative to `migrations_dir`.

To learn more, visit D1's [migrations documentation](https://developers.cloudflare.com/d1/reference/migrations/#nested-migration-layouts).
