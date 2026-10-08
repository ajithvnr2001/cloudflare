---
url: https://developers.cloudflare.com/analytics/graphql-api/features/pagination/
title: Pagination \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:13.084014+00:00
---

# Pagination · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/features/pagination/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Features
  5. /Pagination



# Pagination

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/features/pagination/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewQuery pages without cursors Get the first n results of a query Query for the next page using filters Query the previous page

Pagination – breaking up your query results into smaller parts – can be done using `limit`, `orderBy`, and filtering parameters. The GraphQL Analytics API does not support cursors for pagination.

  * `limit` (integer) defines how many records to return.
  * `orderBy` (string) defines the sort order for the data.



## Query pages without cursors

Our examples assume that the `date` and `clientCountryName` relationships are unique.

### Get the first _n_ results of a query

To limit results, add the `limit` parameter as an integer. For example, query the first two records:
    
    
    firewallEventsAdaptive (limit: 2, orderBy: [datetime_ASC, clientCountryName_ASC]) {
        datetime
        clientCountryName
    }

Note

Specifying a sort order by date returns less specific results than specifying a sort order by date and country.

**Response**
    
    
    {
      "firewallEventsAdaptive" : [
        {
          "datetime": "2018-11-12T00:00:00Z",
          "clientCountryName": "UM"
        },
        {
          "datetime": "2018-11-12T00:00:00Z",
          "clientCountryName": "US"
        }
      ]
    }

### Query for the next page using filters

To get the next _n_ results, specify a filter to exclude the last result from the previous query. Taking the previous example, you can do this by appending the greater-than operator (`_gt`) to the `clientCountryName` field and the greater-or-equal operator (`_geq`) to the `datetime` field. This is where being specific about sort order comes into play. You are less likely to miss results using a more granular sort order.
    
    
    firewallEventsAdaptive (limit: 2, orderBy: [datetime_ASC, clientCountryName_ASC], filter: {datetime_geq: "2018-11-12T00:00:00Z", clientCountryName_gt: "US"}) {
        datetime
        clientCountryName
    }

**Response**
    
    
    {
      "firewallEventsAdaptive" : [
        {
          "datetime": "2018-11-12T00:00:00Z",
          "clientCountryName": "UY"
        },
        {
          "datetime": "2018-11-12T00:00:00Z",
          "clientCountryName": "UZ"
        }
      ]
    }

### Query the previous page

To get the previous _n_ results, reverse the filters and sort order.
    
    
    firewallEventsAdaptive (limit: 2, orderBy: [datetime_DESC, clientCountryName_DESC, filter: {datetime_leq: "2018-11-12T00:00:00Z", clientCountryName_lt: "UY"}]) {
      datetime
      clientCountryName
    }

**Response**
    
    
    {
      "firewallEventsAdaptive" : [
        {
          "datetime": "2018-11-12T00:00:00Z",
          "clientCountryName": "US"
        },
        {
          "datetime": "2018-11-12T00:00:00Z",
          "clientCountryName": "UM"
        }
      ]
    }

[PreviousSorting](https://developers.cloudflare.com/analytics/graphql-api/features/sorting/)[NextNested Structures](https://developers.cloudflare.com/analytics/graphql-api/features/nested-structures/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/features/pagination.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
