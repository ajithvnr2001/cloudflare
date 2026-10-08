---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.continent/
title: ip.src.continent \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:13.122786+00:00
---

# ip.src.continent · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.continent/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Ip.Src.Continent



# ip.src.continent

`ip.src.continent``String`

The continent code associated with the client IP address.

Values:

  * `"AF"`: Africa
  * `"AN"`: Antarctica
  * `"AS"`: Asia
  * `"EU"`: Europe
  * `"NA"`: North America
  * `"OC"`: Oceania
  * `"SA"`: South America
  * `"T1"`: Tor network



This field has the same value as the `ip.geoip.continent` field, which is deprecated. The `ip.geoip.continent` field is still available for new and existing rules, but you should use the `ip.src.continent` field instead.

_GeoIP is the registered trademark of MaxMind, Inc._

Categories: 

  * Request
  * Geolocation



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
