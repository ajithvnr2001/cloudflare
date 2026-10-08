---
url: https://developers.cloudflare.com/radar/concepts/aggregation-intervals/
title: Aggregation intervals \u00b7 Cloudflare Radar docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:49.609216+00:00
---

# Aggregation intervals · Cloudflare Radar docs

> Source: https://developers.cloudflare.com/radar/concepts/aggregation-intervals/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Radar](https://developers.cloudflare.com/radar/)
  3. /[Concepts](https://developers.cloudflare.com/radar/concepts/)
  4. /Aggregation intervals



# Aggregation intervals

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethod

Aggregation intervals allow you to return data in a specified interval (or frequency). If no interval is defined, data will be returned in the default aggregation interval (or frequency). As a general principle, the longer the date range, the bigger the aggregation interval.

For example, when requesting one day of data, the default aggregation interval is 15 minutes. When requesting more than one month of data, the default is one day.

## Method

Aggregation Interval | Description  
---|---  
`15m` | 15 minutes frequency.  
`1h` | One hour frequency.  
`1d` | One day frequency.  
`1w` | One week frequency.  
  
[PreviousOverview](https://developers.cloudflare.com/radar/concepts/)[NextBot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/radar/concepts/aggregation-intervals.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
