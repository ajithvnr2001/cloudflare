---
url: https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/
title: Regional Tiered Cache \u00b7 Cloudflare Smart Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:32.031911+00:00
---

# Regional Tiered Cache · Cloudflare Smart Shield docs

> Source: https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Smart Shield](https://developers.cloudflare.com/smart-shield/)
  3. /Configuration
  4. /Regional Tiered Cache



# Regional Tiered Cache

Last updated Jun 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Availability

Regional Tiered Cache is included with Enterprise plans. Smart Shield Advanced, which includes Regional Tiered Cache, is currently only available to Enterprise customers. If you are interested in Smart Shield Advanced, contact our [Enterprise Sales team ↗︎](https://www.cloudflare.com/resource/contact-enterprise-sales/).

Regional Tiered Cache provides an additional layer of caching for customers who have a global traffic footprint and want to serve content faster by avoiding network latency when there is a cache `MISS` in a lower-tier, resulting in an upper-tier fetch in a data center located far away.

Regional Tiered Cache instructs Cloudflare to check a regional hub data center near the lower tier before going to the upper tier that may be outside of the region.

[PreviousSmart Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/)[NextOverview](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/smart-shield/configuration/regional-tiered-cache.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
