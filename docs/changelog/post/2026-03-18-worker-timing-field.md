---
url: https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/
title: Worker execution timing field now available in Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.209692+00:00
---

# Worker execution timing field now available in Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-18-worker-timing-field/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 18, 2026

## Worker execution timing field now available in Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `cf.timings.worker_msec` field is now available in the Ruleset Engine. This field reports the wall-clock time that a Cloudflare Worker spent handling a request, measured in milliseconds.

You can use this field to identify slow Worker executions, detect performance regressions, or build rules that respond differently based on Worker processing time, such as logging requests that exceed a latency threshold.

#### Field details

Field | Type | Description  
---|---|---  
`cf.timings.worker_msec` | Integer | The time spent executing a Cloudflare Worker in milliseconds. Returns `0` if no Worker was invoked.  
  
Example filter expression:
    
    
    cf.timings.worker_msec > 500

For more information, refer to the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/).
