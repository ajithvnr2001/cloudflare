---
url: https://developers.cloudflare.com/analytics/graphql-api/getting-started/compose-graphql-query/
title: Compose a query in GraphiQL \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:13.313592+00:00
---

# Compose a query in GraphiQL · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/getting-started/compose-graphql-query/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /[Get started](https://developers.cloudflare.com/analytics/graphql-api/getting-started/)
  5. /Compose a query in GraphiQL



# Compose a query in GraphiQL

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/getting-started/compose-graphql-query/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSet up a query and choose a datasetSupply required parametersDefine the fields used by your queryVariable substitution

Many clients might need help using [the semantics](https://developers.cloudflare.com/analytics/graphql-api/getting-started/querying-basics/) of GraphQL and exploring the possibilities of Cloudflare GraphQL API.

This page details how to use a [GraphiQL client ↗︎](https://github.com/graphql/graphiql/tree/main/packages/graphiql#readme) to compose and execute a GraphQL query.

## Prerequisites

You can find all details on how to [configure](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/) a client here.

## Set up a query and choose a dataset

Click on the editing pane of GraphiQL and add this base query, replacing `zone-id` with your Cloudflare zone ID:

![Adding a base query in the GraphiQL pane](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=623,height=217,format=webp/_astro/graphiql-base-query.fKm6YnqW.png)

Note

To find the zone's tag, log in to your Cloudflare account and select the site for which you want to obtain the tag. In the Cloudflare dashboard **Overview** page, scroll to the **API** section in the right sidebar, which displays your zone and account tags.

To assist query building, the GraphiQL client has word completion. Insert your cursor in the query, in this case on the line below `zones`, and start entering a value to engage the feature. For example, when you type `firewall`, a popup menu displays the datasets that return firewall information:

![GraphiQL word completion assistant to query building](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=624,height=285,format=webp/_astro/graphiql-word-completion.iSRM-VK6.png)

The text at the bottom of the list displays a short description of the data that the node returns.

Select the dataset you want to query and insert it. Either select the item in the list, or scroll using arrow keys and press the `Return` key.

## Supply required parameters

Hover your mouse over a field to display a tooltip that describes the dataset. In this example, hovering over the `firewallEventsAdaptive` node displays this description:

![Hovering the mouse over a field to display its description](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=619,height=223,format=webp/_astro/graphiql-set-up-base-query.1fPWncy2.png)

To display information about the dataset, including required parameters, select the dataset name (blue text). The **Documentation Explorer** opens and displays details about the dataset:

![Documentation Explorer window displaying dataset details](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=396,height=320,format=webp/_astro/graphiql-parameters.CM7npJ7C.png)

Note that the `filter` and `limit` arguments are required, as indicated by the exclamation mark (`!`) after their type definitions (gold text). In this example, the `orderBy` argument is not required, though when used it requires a value of type `ZoneFirewallEventsAdaptiveOrderBy`.

To browse a list of supported filter fields, select the filter type definition (gold text) in the Documentation Explorer. In this example, the type is `ZoneFirewallEventsAdaptiveFilter_InputObject`:

![Browsing GraphiQL filter fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=392,height=538,format=webp/_astro/graphiql-filter-fields.DeLcvFBV.png)

This example query shows the required `filter` and `limit` arguments for `firewallEventsAdaptive` (as well as for the rest of GraphQL nodes):

![Example of GraphiQL query arguments](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=614,height=279,format=webp/_astro/graphiql-filter-values.vYQN7N4B.png)

## Define the fields used by your query

To browse the fields you can use with your query, hover your cursor over the dataset name in your query, and in the tooltip that displays, select the data type definition (gold text):

![Hovering the mouse over a dataset to display available fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=619,height=223,format=webp/_astro/graphiql-set-up-base-query.1fPWncy2.png)

**The Documentation Explorer** opens and displays a list of fields:

![Documentation Explorer window displaying list of fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=391,height=575,format=webp/_astro/graphiql-return-fields.DaJ56iiT.png)

To add the data fields that you want to read, type an opening brace (`{`) after the closing parenthesis for the parameters, then start typing the name of a field that you want to fetch. Use word completion to choose a field.

This example query returns the `action`, `datetime`, `clientRequestHTTPHost`, and `userAgent` fields:

![Example query with return fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=592,height=388,format=webp/_astro/graphiql-query-return-field-values.D6RsP235.png)

Once you have entered all the fields you want to query, select the **Play** button to submit the query. The response pane will contain the data fetched from the configured GraphQL API endpoint:

![GraphiQL response pane](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=608,height=346,format=webp/_astro/create-query-fw-data-set-play.dQ7w2sGu.png)

## Variable substitution

The GraphiQL client allows you to use placeholders for value and supply them via the `variables` part of the payload.

Placeholder names should start with `$` character, and you do not need to wrap placeholders in quotes when you use them in the query.

Values for placeholders should be provided in JSON format, in which placeholders are addressed without `$` character. As an example, for a placeholder `$zoneTag` GraphQL API will read a value from the `zoneTag` field of supplied variables object.

To supply a value for a placeholder, select the **Query Variables** pane and edit a JSON object that defines your variables.

This example query uses the `zoneTag` query variable to represent the zone ID:

![Example of GraphiQL query variables](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=631,height=461,format=webp/_astro/graphiql-query-variables.D9uAtvLs.png)

[PreviousExplore the GraphQL schema](https://developers.cloudflare.com/analytics/graphql-api/getting-started/explore-graphql-schema/)[NextExecute a GraphQL query with curl](https://developers.cloudflare.com/analytics/graphql-api/getting-started/execute-graphql-query/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/getting-started/compose-graphql-query.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
