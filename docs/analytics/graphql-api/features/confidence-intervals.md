---
url: https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/
title: Confidence Intervals \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:12.330528+00:00
---

# Confidence Intervals · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Features
  5. /Confidence Intervals



# Confidence Intervals

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityUsage example Request Response

Confidence intervals help assess accuracy and quantify uncertainty in results from sampled datasets. When querying sum or count fields on adaptive datasets, you can request a confidence interval to understand the possible range around an estimate. For example, specifying a confidence level of `0.95` returns the estimate, along with the range of values that likely contains the true value 95% of the time.

## Availability

  * **Supported datasets** : Adaptive (sampled) datasets only.
  * **Supported fields** : All `sum` and `count` fields.
  * **Usage** : Confidence `level` must be provided as a decimal between 0 and 1 (for example,`0.90`, `0.95`, `0.99`).
  * **Default** : If no confidence level is specified, intervals are not returned.



## Usage example

The following example shows how to query a confidence interval and interpret the response.

### Request

To request a confidence interval, use the `confidence(level: X)` argument in your query.

A GraphQL querygraphql
    
    
    query SingleDatasetWithConfidence($zoneTag: string, $start: Time, $end: Time) {
      viewer {
        zones(filter: {zoneTag: $zoneTag}) {
          firewallEventsAdaptiveGroups(
            filter: {datetime_gt: $start, datetime_lt: $end}
            limit: 1000
          ) {
            count
            avg {
              sampleInterval
            }
            confidence(level: 0.95) {
              count {
                estimate
                lower
                upper
                sampleSize
              }
            }
          }
        }
      }
    }

### Response

The response includes the following values:

  * `estimate`: The estimated value, based on sampled data.
  * `lower`: The lower bound of the confidence interval.
  * `sampleSize`: The number of sampled data points used to calculate the estimate.
  * `upper`: The upper bound of the confidence interval.



In this example, the interpretation of the response is that, based on a sample of 40,054, the estimated number of events is 42,939, with 95% confidence that the true value lies between 42,673 and 43,204.
    
    
    {
      "data": {
        "viewer": {
          "zones": [
            {
              "firewallEventsAdaptiveGroups": [
                {
                  "avg": {
                    "sampleInterval": 1.0720277625205972
                  },
                  "confidence": {
                    "count": {
                      "estimate": 42939,
                      "lower": 42673.44115335711,
                      "sampleSize": 40054,
                      "upper": 43204.55884664289
                    }
                  },
                  "count": 42939
                }
              ]
            }
          ]
        }
      },
      "errors": null
    }

[PreviousExecute a GraphQL query with curl](https://developers.cloudflare.com/analytics/graphql-api/getting-started/execute-graphql-query/)[NextDatasets (tables)](https://developers.cloudflare.com/analytics/graphql-api/features/data-sets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/features/confidence-intervals.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
