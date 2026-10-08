---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.subdivision_2_iso_code/
title: ip.src.subdivision_2_iso_code \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:13.566286+00:00
---

# ip.src.subdivision_2_iso_code · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.subdivision_2_iso_code/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Ip.Src.Subdivision_2_iso_code



# ip.src.subdivision_2_iso_code

`ip.src.subdivision_2_iso_code``String`

The ISO 3166-2 code for the second-level region associated with the IP address.

When the actual value is not available, this field contains an empty string.

Requires a Cloudflare Business or Enterprise plan.

For more information on the ISO 3166-2 standard and the available regions, refer to [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) on Wikipedia.

This field has the same value as the `ip.geoip.subdivision_2_iso_code` field, which is deprecated. The `ip.geoip.subdivision_2_iso_code` field is still available for new and existing rules, but you should use the `ip.src.subdivision_2_iso_code` field instead.

_GeoIP is the registered trademark of MaxMind, Inc._

Example value:
    
    
    "GB-SWK"

Categories: 

  * Request
  * Geolocation



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
