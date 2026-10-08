---
url: https://developers.cloudflare.com/changelog/product/hyperdrive/
title: Hyperdrive Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:46.682918+00:00
---

# Hyperdrive Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/hyperdrive/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Sep 16, 2026

## [Hyperdrive support for Python Workers](https://developers.cloudflare.com/changelog/post/2026-09-16-hyperdrive-python-workers/)

[Workers](https://developers.cloudflare.com/workers/)[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

[Python Workers](https://developers.cloudflare.com/workers/languages/python/) can now connect to PostgreSQL and MySQL through Hyperdrive.

For setup, code examples, and limitations, refer to [Use Hyperdrive from Python Workers](https://developers.cloudflare.com/hyperdrive/examples/python-workers/).

Aug 7, 2026

## [MySQL support in Hyperdrive is now generally available](https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

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

Aug 7, 2026

## [Restart a Hyperdrive configuration from the dashboard](https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.

Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.

To restart, select your Hyperdrive configuration in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com), go to the **Settings** tab, and select **Restart** under **Danger zone**. Restarting requires the [**Hyperdrive Admin** role](https://developers.cloudflare.com/fundamentals/manage-members/roles/). After a restart, the **Settings** tab shows when the configuration was last manually restarted.

![The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1698,height=468,format=webp/_astro/dashboard-restart-danger-zone.D1h69zVU.png)

Caution

Restarting drops all active connections in the pool and forces them to be re-established. In-flight queries may see brief errors while the pool rebuilds.

For more information, refer to [Connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).

Jun 18, 2026

## [Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account](https://developers.cloudflare.com/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)[Workers](https://developers.cloudflare.com/workers/)

You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer. Cloudflare contract customers will be able to add PlanetScale usage to their contract in July so reach out to your Cloudflare account team if interested.

Create a PlanetScale database from the Cloudflare dashboard to check out globally distributed Workers optimized for regional data access.

[ Go to **Create a PlanetScale database** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/hyperdrive?modal=1&type=planetscale&step=1) ![Request flow from a user to Workers, Hyperdrive caches, connection pools, and PlanetScale.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=240,format=svg/_astro/planetscale-request-flow.CYsRfKtG.svg)

PlanetScale databases created from Cloudflare work with [Workers](https://developers.cloudflare.com/workers/) through [Hyperdrive](https://developers.cloudflare.com/hyperdrive/). Hyperdrive manages database connection pools and query caching, so you can use PlanetScale as a centralized relational database for Workers applications without changing your database drivers, object-relational mapping (ORM) libraries, or SQL tooling.

PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard [pricing ↗︎](https://planetscale.com/pricing). You can introspect per-database billing usage via PlanetScale's [dashboard ↗︎](https://planetscale.com/docs/billing#organization-usage-and-billing-page).

When you create a PlanetScale database from the Cloudflare dashboard, you receive the same PlanetScale developer experience, including development branches, query insights, and Model Context Protocol (MCP) server support for agents.

To get started, refer to [PlanetScale Postgres and MySQL with Hyperdrive](https://developers.cloudflare.com/hyperdrive/planetscale/).

May 15, 2026

## [Hyperdrive exposes database connection pool size metrics](https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)[Workers](https://developers.cloudflare.com/workers/)

You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the `hyperdrivePoolSizesAdaptiveGroups` dataset in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/), you can see `waitingClients`, `currentPoolSize`, `availablePoolSlots`, and `maxPoolSize` for each of your configurations.

A new **Pool connections** chart has been added to the **Metrics** tab of each Hyperdrive configuration in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com). You can use the location selector to drill down into specific locations hosting your connection pool by airport code.

![Hyperdrive pool size metrics chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2604,height=890,format=webp/_astro/hyperdrive-pool-size-metrics-chart.DZxLTFgB.png)

The chart shows:

  * **Waiting clients** : Client requests waiting for an available connection.
  * **Open connections** : Active connections to your database.
  * **Pool size maximum** : Your configured origin connection limit.



Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to [increase your Hyperdrive connection limit](https://developers.cloudflare.com/hyperdrive/platform/limits/#request-a-limit-increase).

#### Pool size metrics

The `hyperdrivePoolSizesAdaptiveGroups` dataset in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/) exposes the following key connection pool metrics for each Hyperdrive configuration:

Under `avg`:

  * **`currentPoolSize`** — Average number of connections currently open in the pool.
  * **`availablePoolSlots`** — Average number of pool connections available for checkout.
  * **`waitingClients`** — Average number of clients waiting for a connection from the pool.



Under `max`:

  * **`maxPoolSize`** — Configured maximum size of the connection pool.
  * **`currentPoolSize`** — Peak number of connections open in the pool.
  * **`waitingClients`** — Peak number of clients waiting for a connection from the pool.



For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/hyperdrive/observability/metrics/) and [Connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).

Apr 29, 2026

## [Hyperdrive support for private databases with Workers VPC](https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

You can now connect Hyperdrive to a private database through a [Workers VPC service](https://developers.cloudflare.com/workers-vpc/). This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.

When creating a Hyperdrive configuration in the Cloudflare dashboard, choose **Connect to private database** and then **Workers VPC**. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.

You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:
    
    
    npx wrangler hyperdrive create my-vpc-database \
      --service-id <YOUR_VPC_SERVICE_ID> \
      --database <DATABASE_NAME> \
      --user <DATABASE_USER> \
      --password <DATABASE_PASSWORD> \
      --scheme postgresql

Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.

To get started, refer to [Connect Hyperdrive to a private database using Workers VPC](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/).

Mar 19, 2026

## [Hyperdrive now supports custom TLS/SSL certificates for MySQL](https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive now supports custom TLS/SSL certificates for MySQL databases, bringing the same certificate options previously available for PostgreSQL to MySQL connections.

You can now configure:

  * **Server certificate verification** with `VERIFY_CA` or `VERIFY_IDENTITY` SSL modes to verify that your MySQL database server's certificate is signed by the expected certificate authority (CA).
  * **Client certificates** (mTLS) for Hyperdrive to authenticate itself to your MySQL database with credentials beyond username and password.



Create a Hyperdrive configuration with custom certificates for MySQL:
    
    
    # Upload a CA certificate
    npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name
    
    # Create a Hyperdrive with VERIFY_IDENTITY mode
    npx wrangler hyperdrive create your-hyperdrive-config \
      --connection-string="mysql://user:password@hostname:port/database" \
      --ca-certificate-id <CA_CERT_ID> \
      --sslmode VERIFY_IDENTITY

For more information, refer to [SSL/TLS certificates for Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/) and [MySQL TLS/SSL modes](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/).

Feb 23, 2026

## [Hyperdrive no longer caches queries using STABLE PostgreSQL functions](https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive now treats queries containing PostgreSQL `STABLE` functions as uncacheable, in addition to `VOLATILE` functions.

Previously, only functions [that PostgreSQL categorizes ↗︎](https://www.postgresql.org/docs/current/xfunc-volatility.html) as `VOLATILE` (for example, `RANDOM()`, `LASTVAL()`) were detected as uncacheable. `STABLE` functions (for example, `NOW()`, `CURRENT_TIMESTAMP`, `CURRENT_DATE`) were incorrectly allowed to be cached.

Because `STABLE` functions can return different results across different SQL statements within the same transaction, caching their results could serve stale or incorrect data. This change aligns Hyperdrive's caching behavior with PostgreSQL's function volatility semantics.

If your queries use `STABLE` functions, and you were relying on them being cached, move the function call to your application code and pass the result as a query parameter. For example, instead of `WHERE created_at > NOW()`, compute the timestamp in your Worker and pass it as `WHERE created_at > $1`.

Hyperdrive uses text-based pattern matching to detect uncacheable functions. References to function names like `NOW()` in SQL comments also cause the query to be marked as uncacheable.

For more information, refer to [Query caching](https://developers.cloudflare.com/hyperdrive/concepts/query-caching/) and [Troubleshoot and debug](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/).

Dec 4, 2025

## [Connect to remote databases during local development with wrangler dev](https://developers.cloudflare.com/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

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

Jul 3, 2025

## [Hyperdrive now supports configuring the amount of database connections](https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.

All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the [Hyperdrive limits of your Workers plan](https://developers.cloudflare.com/hyperdrive/platform/limits/).

This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.

Refer to the [Hyperdrive configuration documentation](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/) for more information.

May 14, 2025

## [Hyperdrive achieves FedRAMP Moderate-Impact Authorization](https://developers.cloudflare.com/changelog/post/2025-05-14-hyperdrive-fedramp/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive has been approved for FedRAMP Authorization and is now available in the [FedRAMP Marketplace ↗︎](https://marketplace.fedramp.gov/products/FR2000863987).

FedRAMP is a U.S. government program that provides standardized assessment and authorization for cloud products and services. As a result of this product update, Hyperdrive has been approved as an authorized service to be used by U.S. federal agencies at the Moderate Impact level.

For detailed information regarding FedRAMP and its implications, please refer to the [official FedRAMP documentation for Cloudflare ↗︎](https://marketplace.fedramp.gov/products/FR2000863987).

Apr 9, 2025

## [Hyperdrive now supports custom TLS/SSL certificates](https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive now supports more SSL/TLS security options for your database connections:

  * Configure Hyperdrive to verify server certificates with `verify-ca` or `verify-full` SSL modes and protect against man-in-the-middle attacks
  * Configure Hyperdrive to provide client certificates to the database server to authenticate itself (mTLS) for stronger security beyond username and password



Use the new `wrangler cert` commands to create certificate authority (CA) certificate bundles or client certificate pairs:
    
    
    # Create CA certificate bundle
    npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name
    
    # Create client certificate pair
    npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name your-client-cert-name

Then create a Hyperdrive configuration with the certificates and desired SSL mode:
    
    
    npx wrangler hyperdrive create your-hyperdrive-config \
      --connection-string="postgres://user:password@hostname:port/database" \
      --ca-certificate-id <CA_CERT_ID> \
      --mtls-certificate-id <CLIENT_CERT_ID>
      --sslmode verify-full

Learn more about [configuring SSL/TLS certificates for Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/) to enhance your database security posture.

Apr 8, 2025

## [Hyperdrive Free plan makes fast, global database access available to all](https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-free-plan/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive is now available on the Free plan of Cloudflare Workers, enabling you to build Workers that connect to PostgreSQL or MySQL databases without compromise.

Low-latency access to SQL databases is critical to building full-stack Workers applications. We want you to be able to build on fast, global apps on Workers, regardless of the tools you use. So we made Hyperdrive available for all, to make it easier to build Workers that connect to PostgreSQL and MySQL.

If you want to learn more about how Hyperdrive works, read the [deep dive ↗︎](https://blog.cloudflare.com/how-hyperdrive-speeds-up-database-access) on how Hyperdrive can make your database queries up to 4x faster.

![Hyperdrive provides edge connection setup and global connection pooling for optimal latencies.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=4800,height=2400,format=webp/_astro/hyperdrive-global-placement.DHxlaFbz.png)

Visit the docs to [get started](https://developers.cloudflare.com/hyperdrive/get-started/) with Hyperdrive for PostgreSQL or MySQL.

Apr 8, 2025

## [Hyperdrive introduces support for MySQL and MySQL-compatible databases](https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

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

Mar 7, 2025

## [Hyperdrive reduces query latency by up to 90% and now supports IP access control lists](https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive now pools database connections in one or more regions close to your database. This means that your uncached queries and new database connections have up to 90% less latency as measured from connection pools.

![Hyperdrive query latency decreases by 90% during Hyperdrive's gradual rollout of regional pooling.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1732,height=836,format=webp/_astro/hyperdrive-regional-pooling-query-latency-improvement.Bzz_xvHZ.png)

By improving placement of Hyperdrive database connection pools, Workers' Smart Placement is now more effective when used with Hyperdrive, ensuring that your Worker can be placed as close to your database as possible.

With this update, Hyperdrive also uses [Cloudflare's standard IP address ranges ↗︎](https://www.cloudflare.com/ips/) to connect to your database. This enables you to configure the firewall policies (IP access control lists) of your database to only allow access from Cloudflare and Hyperdrive.

Refer to [documentation on how Hyperdrive makes connecting to regional databases from Cloudflare Workers fast](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).

This improvement is enabled on all Hyperdrive configurations.

Jan 28, 2025

## [Automatic configuration for private databases on Hyperdrive](https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.

![Automatic configuration of Cloudflare Access and Service Token in the Cloudflare dashboard for Hyperdrive.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1814,height=922,format=webp/_astro/hyperdrive-private-database-automatic-configuration.BT4_KLwW.png)

When creating a Hyperdrive configuration for a private database, you only need to provide your database credentials and set up a Cloudflare Tunnel within the private network where your database is accessible. Hyperdrive will automatically create the Cloudflare Access, Service Token, and Policies needed to secure and restrict your Cloudflare Tunnel to the Hyperdrive configuration.

To create a Hyperdrive for a private database, you can follow the [Hyperdrive documentation](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/). You can still manually create the Cloudflare Access, Service Token, and Policies if you prefer.

This feature is available from the Cloudflare dashboard.

Dec 11, 2024

## [Up to 10x faster cached queries for Hyperdrive](https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/)

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.

When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.

This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.

![Hyperdrive edge caching improves average session duration for database queries](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1746,height=734,format=webp/_astro/hyperdrive-edge-caching-metrics.BR7svphB.png)

_P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period._

This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.

For more details on how Hyperdrive performs query caching, refer to the [Hyperdrive documentation](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching).
