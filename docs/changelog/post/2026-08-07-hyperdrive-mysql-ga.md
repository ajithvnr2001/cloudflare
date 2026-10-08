---
url: https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/
title: MySQL support in Hyperdrive is now generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:07.095173+00:00
---

# MySQL support in Hyperdrive is now generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2026

## MySQL support in Hyperdrive is now generally available

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Support for MySQL in Hyperdrive is now generally available. You can connect to any MySQL database from your Workers using Hyperdrive.

Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.

You can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, with no code changes required. MySQL support is available at the same [pricing](https://developers.cloudflare.com/hyperdrive/platform/pricing/) as Postgres.
    
    
    import { createConnection } from "mysql2/promise";
    
    export default {
    	async fetch(request, env, ctx) {
    		const connection = await createConnection({
    			host: env.HYPERDRIVE.host,
    			user: env.HYPERDRIVE.user,
    			password: env.HYPERDRIVE.password,
    			database: env.HYPERDRIVE.database,
    			port: env.HYPERDRIVE.port,
    			disableEval: true, // Required for Workers compatibility
    		});
    
    		const [results, fields] = await connection.query("SHOW tables;");
    
    		ctx.waitUntil(connection.end());
    
    		return new Response(JSON.stringify({ results, fields }), {
    			headers: {
    				"Content-Type": "application/json",
    				"Access-Control-Allow-Origin": "*",
    			},
    		});
    	},
    };
    
    
    import { createConnection } from "mysql2/promise";
    
    export interface Env {
    	HYPERDRIVE: Hyperdrive;
    }
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		const connection = await createConnection({
    			host: env.HYPERDRIVE.host,
    			user: env.HYPERDRIVE.user,
    			password: env.HYPERDRIVE.password,
    			database: env.HYPERDRIVE.database,
    			port: env.HYPERDRIVE.port,
    			disableEval: true, // Required for Workers compatibility
    		});
    
    		const [results, fields] = await connection.query("SHOW tables;");
    
    		ctx.waitUntil(connection.end());
    
    		return new Response(JSON.stringify({ results, fields }), {
    			headers: {
    				"Content-Type": "application/json",
    				"Access-Control-Allow-Origin": "*",
    			},
    		});
    	},
    } satisfies ExportedHandler<Env>;

Learn more about [how Hyperdrive works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/) and [get started building Workers that connect to MySQL with Hyperdrive](https://developers.cloudflare.com/hyperdrive/get-started/).
