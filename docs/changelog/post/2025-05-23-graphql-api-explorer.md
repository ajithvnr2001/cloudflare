---
url: https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/
title: New GraphQL Analytics API Explorer and MCP Server \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.173166+00:00
---

# New GraphQL Analytics API Explorer and MCP Server · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 23, 2025

## New GraphQL Analytics API Explorer and MCP Server

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:

#### GraphQL API Explorer

The new [GraphQL API Explorer ↗︎](https://graphql.cloudflare.com/explorer) helps you build, test, and run queries directly in your browser. Features include:

  * In-browser schema documentation to browse available datasets and fields
  * Interactive query editor with autocomplete and inline documentation
  * A "Run in GraphQL API Explorer" button to execute example queries from our docs
  * Seamless OAuth authentication — no manual setup required

![GraphQL API Explorer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2626,height=974,format=webp/_astro/graphql-api-explorer.CPUNZZ5B.png)

#### GraphQL Model Context Protocol (MCP) Server

MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our [blog post ↗︎](https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/) for details on how they work and which servers are available. The new [GraphQL MCP server ↗︎](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql) helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:

  * Explore what data is available to query
  * Generate and refine queries using natural language, with one-click links to run them in the API Explorer
  * Build dashboards and visualizations from structured query outputs



Example prompts include:

  * “Show me HTTP traffic for the last 7 days for example.com”
  * “What GraphQL node returns firewall events?”
  * “Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”



We’re continuing to expand these tools, and your feedback helps shape what’s next. [Explore the documentation](https://developers.cloudflare.com/analytics/graphql-api/) to learn more and get started.
