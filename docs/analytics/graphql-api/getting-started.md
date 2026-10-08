---
url: https://developers.cloudflare.com/analytics/graphql-api/getting-started/
title: Get started \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:13.115053+00:00
---

# Get started · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/getting-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)
  4. /Get started



# Get started

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/getting-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Use these articles to get started with the Cloudflare GraphQL API:

  * [Authentication](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/) \- walks you through the options and the steps required to set up your access to Cloudflare API successfully,
  * [Querying basics](https://developers.cloudflare.com/analytics/graphql-api/getting-started/querying-basics/) \- brings simple query examples for you to start exploring the GraphQL API,
  * [Introspect the GraphQL schema](https://developers.cloudflare.com/analytics/graphql-api/getting-started/explore-graphql-schema/) \- explains how-to surf the schema with GraphQL client,
  * [Create a query in a GraphQL client](https://developers.cloudflare.com/analytics/graphql-api/getting-started/compose-graphql-query/) \- describes how to build and run a query against the Cloudflare GraphQL API in the GraphQL clients,
  * [Use curl to query the GraphQL API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/execute-graphql-query/) \- walks you through running a query against the Cloudflare GraphQL API from the command line.



For examples of how to build your own GraphQL Analytics dashboard and query specific information, such as Firewall and Workers events, please refer to [Tutorials](https://developers.cloudflare.com/analytics/graphql-api/tutorials/).

Data unavailability: Customer Metadata Boundary configuration

If you encounter a message on the dashboard indicating that your data is unavailable due to your account's Metadata Boundary configuration, this is because you are trying to access data that is not stored in your region (that is, you are in the US and trying to access data that is only stored in the EU, or vice versa). If you receive this error message while being in the region where your data is stored, there are two potential reasons why you might get this message:

  * Your account has Customer Metadata Boundary (CMB) enabled, and your request is being directed to an incorrect region. For example, if you are in the EU and CMB is configured to store your data in the US.

  * If you are trying to access your data from the correct region, such as being in the EU with CMB configured to save your data in the EU, the issue may be caused by network congestion. Typically, this problem resolves within a few minutes.




[PreviousOverview](https://developers.cloudflare.com/analytics/graphql-api/)[NextOverview](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/getting-started/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
