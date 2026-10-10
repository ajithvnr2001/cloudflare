---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/
title: cf.edge.l4.delivery_rate \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:35.496400+00:00
---

# cf.edge.l4.delivery_rate · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Edge.L4.Delivery_rate



# cf.edge.l4.delivery_rate

`cf.edge.l4.delivery_rate``Integer`

The most recent data delivery rate estimate for the client connection, in bytes per second.

This metric reflects the rate at which data is being successfully delivered over the connection.

Returns `0` when L4 statistics are not available for the request.

Example value:
    
    
    123456

Example usage:
    
    
    # Match requests where the delivery rate is below 100 KB/s
    cf.edge.l4.delivery_rate < 100000

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
