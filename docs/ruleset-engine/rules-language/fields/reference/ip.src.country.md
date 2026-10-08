---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.country/
title: ip.src.country \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:13.163825+00:00
---

# ip.src.country · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.country/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Ip.Src.Country



# ip.src.country

`ip.src.country``String`

The 2-letter country code in [ISO 3166-1 Alpha 2](https://www.iso.org/obp/ui/#search/code/) format.

For more information on the ISO 3166-1 Alpha 2 format, refer to [ISO 3166-1 Alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) on Wikipedia.

This field has the same value as the `ip.geoip.country` field, which is deprecated. The `ip.geoip.country` field is still available for new and existing rules, but you should use the `ip.src.country` field instead.

_GeoIP is the registered trademark of MaxMind, Inc._

Example value:
    
    
    "GB"

Categories: 

  * Request
  * Geolocation



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
