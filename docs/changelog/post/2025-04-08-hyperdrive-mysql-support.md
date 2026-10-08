---
url: https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/
title: Hyperdrive introduces support for MySQL and MySQL-compatible databases \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:08.956417+00:00
---

# Hyperdrive introduces support for MySQL and MySQL-compatible databases · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 8, 2025

## Hyperdrive introduces support for MySQL and MySQL-compatible databases

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now supports connecting to MySQL and MySQL-compatible databases, including Amazon RDS and Aurora MySQL, Google Cloud SQL for MySQL, Azure Database for MySQL, PlanetScale and MariaDB.

Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.

Best of all, you can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, no code changes required.
    
    
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
