---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.origin_ttfb_msec/
title: cf.timings.origin_ttfb_msec \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:05.694668+00:00
---

# cf.timings.origin_ttfb_msec · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.origin_ttfb_msec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Timings.Origin_ttfb_msec



# cf.timings.origin_ttfb_msec

`cf.timings.origin_ttfb_msec``Integer`

The round-trip time (RTT) between the Cloudflare global network and the origin server in milliseconds.

This field provides insight into origin server latency. It represents the Time to First Byte (TTFB) from the perspective of the Cloudflare edge server.

This metric includes both the network RTT and the time the origin server spent handling the request.

If the request was served from the Cloudflare CDN cache and the origin server was not reached, the value of this field will be `0`.

Example value:
    
    
    150

Example usage:
    
    
    # Matches requests where the origin response time (TTFB) was greater than 2 seconds:
    cf.timings.origin_ttfb_msec > 2000

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
