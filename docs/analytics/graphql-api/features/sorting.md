---
url: https://developers.cloudflare.com/analytics/graphql-api/features/sorting/
title: Sorting \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:12.799324+00:00
---

# Sorting · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/features/sorting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Features
  5. /Sorting



# Sorting

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/features/sorting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExamples Raw data sorting Raw data sorting using multiple fields Group sorting by aggregation function

You can specify the order of the query result elements using the `orderBy` argument. By default, the results are sorted by the primary key of a dataset (table). If you specify another field to sort on, the primary key is also used in the sorting key, allowing results to remain consistent for pagination.

The default order for an aggregated dataset is by the fields on which the aggregated data is grouped. If you specify a different order, the aggregation group is appended to your specified ordering.

Note

Ordering within nested structures is not supported.

## Examples

### Raw data sorting
    
    
    firewallEventsAdaptive (orderBy: [clientCountryName_ASC]) {
        clientCountryName
    }

### Raw data sorting using multiple fields
    
    
    firewallEventsAdaptive (orderBy: [clientCountryName_ASC, datetime_DESC]) {
        clientCountryName
        datetime
    }

### Group sorting by aggregation function
    
    
    httpRequests1hGroups (orderBy: [sum_bytes_DESC]){
        sum {
            bytes
            requests
        }
        dimensions {
            datetime
        }
    }

[PreviousFiltering](https://developers.cloudflare.com/analytics/graphql-api/features/filtering/)[NextPagination](https://developers.cloudflare.com/analytics/graphql-api/features/pagination/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/features/sorting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
