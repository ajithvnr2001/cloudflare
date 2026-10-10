---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/
title: cf.timings.worker_msec \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:34.630511+00:00
---

# cf.timings.worker_msec · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Timings.Worker_msec



# cf.timings.worker_msec

`cf.timings.worker_msec``Integer`

The time spent executing a Cloudflare Worker in milliseconds.

This field provides the wall-clock time that a Cloudflare Worker spent handling the request, measured in milliseconds.

Use this field to identify slow Worker executions, set up alerts for performance regressions, or add Worker execution time as a request header using Transform Rules for downstream observability.

If the request did not invoke a Worker, the value of this field will be `0`.

Example value:
    
    
    12

Example usage:
    
    
    # Matches requests where the Worker execution time exceeded 500 milliseconds
    cf.timings.worker_msec > 500

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
