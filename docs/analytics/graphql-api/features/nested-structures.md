---
url: https://developers.cloudflare.com/analytics/graphql-api/features/nested-structures/
title: Nested Structures \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:12.735187+00:00
---

# Nested Structures · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/features/nested-structures/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Features
  5. /Nested Structures



# Nested Structures

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/features/nested-structures/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArraysMapsExamples

Two kinds of nested structures that are supported: **arrays** and **maps**. Fields of either of these types are arrays; when they are part of a query result, which is already an array of objects, they become nested arrays.

## Arrays

The GraphQL API supports two different sorts of arrays:

  * Some arrays contain scalar types (for example, `[String]`) and function like ordinary fields that [can be filtered](https://developers.cloudflare.com/analytics/graphql-api/features/filtering/)
  * Some arrays contain more complex types (for example, `[Subrequest]`.) The following section describes their behaviour.



Arrays of non-scalar types behave as a single value. There is no way to paginate through, filter, filter by, group, or group by the array.

On the other hand, you can choose which fields of the underlying type you want fetched.

For example, given arrays like this:
    
    
    type SubRequest {
        url: String!
        status: Int
    }
    
    type Request {
        date: Date!
        datetime: DateTime!
        subRequests: [SubRequest!]!
    }

You can run a query to get the status by subrequest:
    
    
    {
        requests {
            date
            subRequests {
                # discard the url, only need the status
                status
            }
        }
    }

The results would be:
    
    
    {
        "requests": [
            {
                "date": "2018-01-01",
                "subRequests": [{"status": 404}, {"status": 200}, {"status": 404}]
            },
            {
                "date": "2018-01-01",
                "subRequests": [{"status": 200}]
            }
        ]
    }

## Maps

Maps behave like arrays, but can be grouped using the `sum` function. They are used in aggregated datasets, such as `httpRequest1dGroups`.

Example maps:
    
    
    type URLStatsMapElem {
        url: String!
        requests: Int
        bytes: Int
    }
    
    type Request {
        date: Date!
        datetime: DateTime!
        urlStatsMap: [URLStatsMapElem!]!
    }

Query:
    
    
    {
        requests {
            sum {
                urlStatsMap {
                    url
                    requests
                    bytes
                }
            }
            dimensions {
                date
            }
        }
    }

Response:
    
    
    {
        "requests": [
            {
                "sum": {
                    "urlStatsMap": [
                        {
                            "url": "hello-world.org/1",
                            "requests": 123,
                            "bytes": 1024
                        },
                        {
                            "url": "hello-world.org/10",
                            "requests": 1230,
                            "bytes": 10240
                        }
                    ]
                }
                "dimensions" {
                    "date": "2018-10-19"
                }
            },
            ...
        ]
    }

## Examples

Query array fields in raw datasets:
    
    
    query NestedFields($zoneTag: string, $start: Time, $end: Time) {
    	viewer {
    		zones(filter: { zoneTag: $zoneTag }) {
    			events(limit: 2, filter: { datetime_geq: $start, datetime_leq: $end }) {
    				matches {
    					ruleId
    					action
    					source
    				}
    			}
    		}
    	}
    }

Example response:
    
    
    {
      "data": {
        "viewer": {
          "zones": [
            {
              "events": [
                {
                  "matches": [
                    {
                      "action": "allow",
                      "ruleId": "rule-id-one",
                      "source": "asn"
                    },
                    {
                      "action": "block",
                      "ruleId": "rule-id-two",
                      "source": "asn"
                    }
                  ]
                }
              ]
            }
          ]
        }
      },
      "errors": null
    }

Query maps fields in aggregated datasets:
    
    
    query MapCapacity(
    	$zoneTag: string
    	$dateStart: Date
    	$dateEnd: Date
    	$start: Time
    	$end: Time
    ) {
    	viewer {
    		zones(filter: { zoneTag: $zoneTag }) {
    			httpRequests1mGroups(
    				limit: 10
    				filter: {
    					date_geq: $dateStart
    					date_leq: $dateEnd
    					datetime_geq: $start
    					datetime_lt: $end
    				}
    			) {
    				sum {
    					countryMap {
    						clientCountryName
    						requests
    						bytes
    						threats
    					}
    				}
    				dimensions {
    					datetimeHour
    				}
    			}
    		}
    	}
    }

Example response:
    
    
    {
      "data": {
        "viewer": {
          "zones": [
            {
              "httpRequests1mGroups": [
                {
                  "dimensions": {
                    "datetime": "2019-03-08T17:00:00Z"
                  },
                  "sum": {
                    "countryMap": [
                      {
                        "bytes": 51911317,
                        "clientCountryName": "XK",
                        "requests": 4492,
                        "threats": 0
                      },
                      {
                        "bytes": 1816103586,
                        "clientCountryName": "T1",
                        "requests": 132423,
                        "threats": 0
                      },
                      ...
                    ]
                  }
                }
              ]
            }
          ]
        }
      },
      "errors": null
    }

[PreviousPagination](https://developers.cloudflare.com/analytics/graphql-api/features/pagination/)[NextError responses](https://developers.cloudflare.com/analytics/graphql-api/errors/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/features/nested-structures.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
