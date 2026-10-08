---
url: https://developers.cloudflare.com/hyperdrive/platform/limits/
title: Limits \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:33.193267+00:00
---

# Limits · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /Platform
  4. /Limits



# Limits

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfiguration limitsConnection limits Connection errorsQuery limitsRequest a limit increase

The following limits apply to Hyperdrive configurations, connections, and queries made to your configured origin databases.

## Configuration limits

These limits apply when creating or updating Hyperdrive configurations.

Limit | Free | Paid  
---|---|---  
Maximum configured databases | 10 per account | 25 per account  
Maximum username length 1 | 63 characters (bytes) | 63 characters (bytes)  
Maximum database name length 1 | 63 characters (bytes) | 63 characters (bytes)  
  
## Connection limits

These limits apply to connections between Hyperdrive and your origin database.

Limit | Free | Paid  
---|---|---  
Initial connection timeout | 15 seconds | 15 seconds  
Idle connection timeout | 10 minutes | 10 minutes  
Maximum origin database connections (per configuration) 2 | ~20 connections | ~100 connections  
  
Hyperdrive does not limit the number of concurrent client connections from your Workers. However, Hyperdrive limits connections to your origin database because most hosted databases have connection limits.

### Connection errors

When Hyperdrive cannot acquire a connection to your origin database, you may see one of the following errors:

Error message | Cause  
---|---  
`Failed to acquire a connection from the pool.` | The connection pool is exhausted because connections are held open too long. Long-running queries or transactions are a common cause.  
`Server connection attempt failed: connection_refused` | Your origin database is rejecting connections. This can occur when a firewall blocks Hyperdrive, or when your database provider's connection limit is exceeded.  
  
For a complete list of error codes, refer to [Troubleshoot and debug](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/).

## Query limits

These limits apply to queries sent through Hyperdrive.

Limit | Free | Paid  
---|---|---  
Maximum query (statement) duration | 60 seconds | 60 seconds  
Maximum cached query response size | 50 MB | 50 MB  
  
Queries exceeding the maximum duration are terminated. Query responses larger than 50 MB are not cached but are still returned to your Worker.

## Request a limit increase

You can request adjustments to limits that conflict with your project goals by contacting Cloudflare. Not all limits can be increased.

To request an increase, submit a [Limit Increase Request form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5). You can also ask questions in the Hyperdrive channel on [Cloudflare's Discord community ↗︎](https://discord.cloudflare.com/).

## Footnotes

  1. This is a limit enforced by PostgreSQL. Some database providers may enforce smaller limits. ↩ ↩2

  2. Hyperdrive is a distributed system, so a client may be unable to reach an existing pool. In this scenario, a new pool is established with its own connection allocation. This prioritizes availability over strict limit enforcement, which means connection counts may occasionally exceed the listed limits. ↩




[PreviousPricing](https://developers.cloudflare.com/hyperdrive/platform/pricing/)[NextChoose a data or storage product ↗︎](https://developers.cloudflare.com/workers/platform/storage-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
