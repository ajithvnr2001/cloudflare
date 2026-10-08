---
url: https://developers.cloudflare.com/analytics/graphql-api/features/data-sets/
title: Datasets (tables) \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:12.235897+00:00
---

# Datasets (tables) · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/features/data-sets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Features
  5. /Datasets (tables)



# Datasets (tables)

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/features/data-sets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWorking with datasets Aggregated fields Schema type definitions

Cloudflare Analytics offers a range of datasets, including both general and product-specific ones. Datasets use a consistent naming scheme that explicitly identifies the type of data they return:

  * **Domain** \- Each dataset is named after the field it describes and is associated with a set of nodes. Product-specific data nodes incorporate the name of the relevant product, for instance `loadBalancingRequests*` nodes.

  * **Adaptive Sampling** \- Nodes that represent data acquired using adaptive sampling incorporate the `Adaptive` suffix. For more details, refer to [sampling](https://developers.cloudflare.com/analytics/graphql-api/sampling/).

  * **Aggregated data** \- Nodes that represent aggregated data include the `Groups` suffix. For example, the `loadBalancingRequestsAdaptiveGroups` node represents aggregated data for Load Balancing requests. Aggregated data is returned in an array of `...Group` objects. Please note: we have a node that currently excluded from that naming convention - `workersInvocationsAdaptive` (beta).

  * **Raw data** \- Raw data nodes, such as `loadBalancingRequestsAdaptive`, are not aggregated and so do not incorporate the `Groups` suffix. Raw data is returned in arrays containing objects of the relevant data type. For example, a query to `loadBalancingRequestsAdaptive` returns a variety of `LoadBalancingRequest` objects.




To find out more information about datasets, availability, beta, and deprecation statuses, please refer to GraphQL [discovery](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/) features.

## Working with datasets

### Aggregated fields

This example illustrates the structure for Groups:
    
    
    type WhateverGroup {
        count # No subfields, it is just the group size. Not available for roll-up tables.
        sum {
            # fields that support summing (numbers, maps of numbers)
        }
        avg {
            # fields that support averaging (numbers)
        }
        uniq {
            # fields that support uniqueing (numbers, strings, enums, IPs, dates, etc.)
        }
    }

Unique values are not available as a dimension but can be queried as demonstrated in this example:
    
    
    {
      # Get number of bytes and unique IPs in each minute.
      httpRequests1mGroups {
        sum {
          bytes
        }
        uniq {
          uniques # unique IPs
        }
        dimensions {
          datetimeMinute
        }
      }
    
      # Count the number of events in each hour.
      firewallEventsAdaptiveGroups {
        count
        dimensions {
          datetimeHour
        }
      }
    }

### Schema type definitions

Every exposed table has a GraphQL type definition. Type definitions observe the following rules:

  * Regular fields represent themselves.
  * Every field, including nested fields, has a type and represents a list of that type.
  * The `enum` type represents an enumerated field.



Here is an example type definition for `ContentTypeMapElem`:
    
    
    type ContentTypeMapElem {
        edgeResponseContentType: UInt32!
        requests: UInt64!
        bytes: UInt64!
    }
    
    # An array of httpRequestsGroup is the result of httpRequests1hGroups or
    # httpRequests1mGroups query.
    type httpRequestsGroup {
        date: Date!
        timeslot: DateTime!
        requests: UInt64!
        contentTypeMap: [ContentTypeMapElem!]!
        # ... other fields
    }
    
    enum TrustedClientCategory {
        UNKNOWN
        REAL_BROWSER
        HONEST_BOT
    }
    
    # An array of Request is the result of httpRequests query.
    type Request {
        trustedClientCategory: TrustedClientCategory!
        # ... other fields
    }

[PreviousConfidence Intervals](https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/)[NextOverview](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/features/data-sets.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
