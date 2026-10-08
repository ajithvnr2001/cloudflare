---
url: https://developers.cloudflare.com/analytics/graphql-api/
title: GraphQL Analytics API \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:11.949316+00:00
---

# GraphQL Analytics API · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /GraphQL Analytics API



# GraphQL Analytics API

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewClientsLimitations

The GraphQL Analytics API provides data regarding HTTP requests passing through Cloudflare's network, as well as data from specific products, such as Firewall or Load Balancing. Network Analytics users also have access to packet-level data. Use the GraphQL Analytics API to select specific datasets and metrics of interest, filter and aggregate the data along various dimensions, and integrate the results with other applications.

The basis of the API is the [GraphQL framework ↗︎](https://graphql.org/), created and open-sourced by Facebook. There is an active developer community for GraphQL and powerful clients for running queries, which makes it easy to get started. GraphQL is especially useful for building visualizations and powers the analytics in the Cloudflare dashboard.

GraphQL models a business domain as a graph using a schema. In the schema, there are logical definitions for different types of nodes and their connections (edges). These nodes are the datasets you use for your analytics. You write queries in GraphQL much like in SQL: you specify the dataset (table), the metrics to retrieve (such as requests and bytes), and filter or group by dimensions (for example, a time period).

GraphQL differs from a traditional API: it has one single endpoint:
    
    
    https://api.cloudflare.com/client/v4/graphql

You pass the query parameters as a JSON object in the payload of a `POST` request to this endpoint.

You can use `curl` to make requests to the GraphQL Analytics API. Alternatively, you can use a GraphQL client to construct queries and pass requests to the GraphQL Analytics API.

## Clients

We are using [GraphiQL ↗︎](https://github.com/skevy/graphiql-app) for our example GraphQL queries. There are many other popular open-source clients that you can find online, such as [Altair ↗︎](https://altairgraphql.dev) and [Insomnia ↗︎](https://insomnia.rest).

## Limitations

The purpose of the GraphQL API is to provide aggregated analytics about various Cloudflare products. These datasets should not be used as a measure for usage that Cloudflare uses for billing purposes. Billable traffic [excludes things like DDoS traffic ↗︎](https://blog.cloudflare.com/unmetered-mitigation), while GraphQL is a measure of overall consumption/usage, so it will include all measurable traffic.

[PreviousData collection](https://developers.cloudflare.com/analytics/network-analytics/reference/data-collection/)[NextOverview](https://developers.cloudflare.com/analytics/graphql-api/getting-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
