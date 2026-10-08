---
url: https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/
title: Cloudflare Load Balancing Regions API \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:06.707153+00:00
---

# Cloudflare Load Balancing Regions API · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /Reference
  4. /Regions API



# Regions API

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewList of Load Balancer regions

Cloudflare’s Load Balancing Regions API has several uses:

  * Identify which countries/areas (states/provinces in the case of the U.S. and Canada) are part of a specific Cloudflare Load Balancer region.
  * Identify the Cloudflare Load Balancer region for a particular country/area (states/provinces in the case of the U.S. and Canada).



The Region API uses 2-letter [ISO-3166-1 alpha-2 codes ↗︎](https://www.iso.org/iso-3166-country-codes.html) for countries/areas and, in the case of the U.S. and Canada, ISO-3166-2 subdivision codes for states/provinces. Only the U.S. and Canada are provided with these subdivisions.

There are two main optional parameters for the Region API:

  * country_code is a string containing a two-letter alpha-2 country code per ISO 3166-1. For example: /load_balancers/regions?country_code=US
  * subdivision_code is a string containing a two-letter subdivision code for the U.S. and Canada per ISO 3166-2. For example: /load_balancers/regions?subdivision_code=CA



For additional details and examples on using the Region Mapping API, see [Cloudflare’s API documentation](https://developers.cloudflare.com/api/resources/load_balancers/subresources/regions/methods/list/).

## List of Load Balancer regions

Region code | Region name  
---|---  
EEU | Eastern Europe  
ENAM | Eastern North America  
ME | Middle East  
NAF | Northern Africa  
NEAS | Northeast Asia  
NSAM | Northern South America  
OC | Oceania  
SAF | Southern Africa  
SAS | Southern Asia  
SEAS | Southeast Asia  
SSAM | Southern South America  
WEU | Western Europe  
WNAM | Western North America  
  
[PreviousAnalytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/)[NextLimitations](https://developers.cloudflare.com/load-balancing/reference/limitations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/reference/region-mapping-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
