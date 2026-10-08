---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/
title: ip.src.asnum \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:12.932630+00:00
---

# ip.src.asnum · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Ip.Src.Asnum



# ip.src.asnum

`ip.src.asnum``Number`

The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address.

This field has the same value as the `ip.geoip.asnum` field, which is deprecated. The `ip.geoip.asnum` field is still available for new and existing rules, but you should use the `ip.src.asnum` field instead.

_GeoIP is the registered trademark of MaxMind, Inc._

Categories: 

  * Request
  * Geolocation



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
