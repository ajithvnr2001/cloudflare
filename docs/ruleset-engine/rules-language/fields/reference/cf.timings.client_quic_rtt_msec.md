---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/
title: cf.timings.client_quic_rtt_msec \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:34.751501+00:00
---

# cf.timings.client_quic_rtt_msec · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Timings.Client_quic_rtt_msec



# cf.timings.client_quic_rtt_msec

`cf.timings.client_quic_rtt_msec``Integer`

The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds.

This field is only populated for QUIC (HTTP/3) connections. For TCP connections, the value is `0`.

Example value:
    
    
    42

Example usage:
    
    
    # Match requests over QUIC where the RTT exceeds 200 ms
    cf.timings.client_quic_rtt_msec > 200

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
