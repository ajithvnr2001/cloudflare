---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.is_in_european_union/
title: ip.src.is_in_european_union \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:13.215500+00:00
---

# ip.src.is_in_european_union · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.is_in_european_union/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Ip.Src.Is_in_european_union



# ip.src.is_in_european_union

`ip.src.is_in_european_union``Boolean`

Whether the request originates from a country in the European Union (EU).

Requires a Cloudflare Business or Enterprise plan.

Countries in the EU (from geolocation data):

Country code | Country name  
---|---  
`AT` | Austria  
`AX` | Åland Islands  
`BE` | Belgium  
`BG` | Bulgaria  
`CY` | Cyprus  
`CZ` | Czechia  
`DE` | Germany  
`DK` | Denmark  
`EE` | Estonia  
`ES` | Spain  
`FI` | Finland  
`FR` | France  
`GF` | French Guiana  
`GP` | Guadeloupe  
`GR` | Greece  
`HR` | Croatia  
`HU` | Hungary  
`IE` | Ireland  
`IT` | Italy  
`LT` | Lithuania  
`LU` | Luxembourg  
`LV` | Latvia  
`MF` | Saint Martin  
`MQ` | Martinique  
`MT` | Malta  
`NL` | The Netherlands  
`PL` | Poland  
`PT` | Portugal  
`RE` | Réunion  
`RO` | Romania  
`SE` | Sweden  
`SI` | Slovenia  
`SK` | Slovakia  
`YT` | Mayotte  
  
This field has the same value as the `ip.geoip.is_in_european_union` field, which is deprecated. The `ip.geoip.is_in_european_union` field is still available for new and existing rules, but you should use the `ip.src.is_in_european_union` field instead.

_GeoIP is the registered trademark of MaxMind, Inc._

Categories: 

  * Request
  * Geolocation



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
