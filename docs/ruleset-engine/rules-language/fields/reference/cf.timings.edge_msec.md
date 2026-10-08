---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.edge_msec/
title: cf.timings.edge_msec \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:05.671124+00:00
---

# cf.timings.edge_msec · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.edge_msec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Timings.Edge_msec



# cf.timings.edge_msec

`cf.timings.edge_msec``Integer`

The time spent processing a request within the Cloudflare global network in milliseconds.

The value corresponds to the time interval between when the Cloudflare edge server accepted the HTTP request headers for processing and just before the HTTP response headers were available to be sent to the client.

The value does not include:

  * The time spent forwarding the request to the origin server (refer to [`cf.timings.origin_ttfb_msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.origin_ttfb_msec/)).
  * The network transfer time to the client.



Example value:
    
    
    28

Example usage:
    
    
    # Matches requests where Cloudflare's edge processing time was greater than 500 milliseconds
    cf.timings.edge_msec > 500

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
