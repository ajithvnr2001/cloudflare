---
url: https://developers.cloudflare.com/analytics/graphql-api/getting-started/execute-graphql-query/
title: Execute a GraphQL query with curl \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:13.374731+00:00
---

# Execute a GraphQL query with curl · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/getting-started/execute-graphql-query/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /[Get started](https://developers.cloudflare.com/analytics/graphql-api/getting-started/)
  5. /Execute a GraphQL query with curl



# Execute a GraphQL query with curl

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/getting-started/execute-graphql-query/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Using a plain curl to send a query provides the ability to slice-n-dice with the results and apply post-processing if needed. For example, converting results received from GraphQL API into a CSV format.

For more functionality, like auto-completion, schema exploring, etc., you can look at GraphQL [clients](https://developers.cloudflare.com/analytics/graphql-api/getting-started/compose-graphql-query/).

GraphQL API expects JSON with two essentials fields: "query" and "variables".

A query should be stripped from newline symbols and sent as a single-line string when the variables is an object full of values for all placeholders used in the query:

A payload structure for GraphQL APIjson
    
    
    {
      "query": "{viewer { ... }}",
      "variables": {}
    }

It is still possible to use a human-friendly query though. In the example below you can see how `echo` piped together with `tr` to provide a proper payload with `curl`:

Example bash script that uses curl to query Analytics APIbash
    
    
    echo '{ "query":
      "{
        viewer {
          zones(filter: { zoneTag: $zoneTag }) {
            firewallEventsAdaptive(
              filter: $filter
              limit: 10
              orderBy: [datetime_DESC]
            ) {
              action
              clientAsn
              clientCountryName
              clientIP
              clientRequestPath
              clientRequestQuery
              datetime
              source
              userAgent
            }
          }
        }
      }",
      "variables": {
        "zoneTag": "<zone-tag>",
        "filter": {
          "datetime_geq": "2022-07-24T11:00:00Z",
          "datetime_leq": "2022-07-24T12:00:00Z"
        }
      }
    }' | tr -d '\n' | curl --silent \
    https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data @-

[PreviousCompose a query in GraphiQL](https://developers.cloudflare.com/analytics/graphql-api/getting-started/compose-graphql-query/)[NextConfidence Intervals](https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/getting-started/execute-graphql-query.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
