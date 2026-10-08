---
url: https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/
title: Migrate to new GraphQL nodes \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:06.381302+00:00
---

# Migrate to new GraphQL nodes · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

Reference

  4. /Migration guides
  5. /Migrate to new GraphQL nodes



# Migrate to new GraphQL nodes

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample query

After 30 September 2021, Cloudflare will make the following changes to the Load Balancing GraphQL schema:

  * Deprecate nodes: 
    * `loadBalancingRequestsGroups` will be deprecated for `loadBalancingRequestsAdaptiveGroups`
    * `loadBalancingRequests` will be deprecated for `loadBalancingRequestsAdaptive`
  * Deprecate the `date` field (replace it with the existing `datetime` field)
  * Add the `sampleInterval` field



## Example query

The following example:

  * Replaces `loadBalancingRequestsGroups` with `loadBalancingRequestsAdaptiveGroups`
  * Replaces `date` with `datetime`
  * Uses the new `sampleInterval` field


    
    
    query {
      viewer {
        zones(filter: { zoneTag: "your Zone ID" }) {
          loadBalancingRequestsAdaptiveGroups(
            filter: {
              datetime_gt: "2021-06-12T04:00:00Z",
              datetime_lt: "2021-06-13T06:00:00Z"
            }
          ) {
            dimensions {
              datetime
              coloCode
              ...
            }
            avg {
              sampleInterval
            }
          }
        }
      }
    }

[PreviousAdditional DNS records](https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/)[NextHealth monitor notifications](https://developers.cloudflare.com/load-balancing/reference/migration-guides/health-monitor-notifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/reference/migration-guides/load-balancing-graphql-nodes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
