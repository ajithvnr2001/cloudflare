---
url: https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/
title: Public stats \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:02.129991+00:00
---

# Public stats · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Build the page](https://developers.cloudflare.com/style-guide/build-the-page/)

  4. /[Components](https://developers.cloudflare.com/style-guide/build-the-page/components/)
  5. /Public stats



# Public stats

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/build-the-page/components/public-stats/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAssociated content types

The `PublicStats` component is used `16` times on `8` pages.

See all examples of pages that use PublicStats

Used **16** times.

**Pages**

  * [/learning-paths/data-center-protection/concepts/benefits-magic-transit/](https://developers.cloudflare.com/learning-paths/data-center-protection/concepts/benefits-magic-transit/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/learning-paths/data-center-protection/concepts/benefits-magic-transit.mdx)
  * [/reference-architecture/architectures/cdn/](https://developers.cloudflare.com/reference-architecture/architectures/cdn/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/reference-architecture/architectures/cdn.mdx)
  * [/reference-architecture/architectures/load-balancing/](https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/reference-architecture/architectures/load-balancing.mdx)
  * [/reference-architecture/architectures/sase/](https://developers.cloudflare.com/reference-architecture/architectures/sase/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/reference-architecture/architectures/sase.mdx)
  * [/reference-architecture/architectures/security/](https://developers.cloudflare.com/reference-architecture/architectures/security/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/reference-architecture/architectures/security.mdx)
  * [/reference-architecture/design-guides/securing-guest-wireless-networks/](https://developers.cloudflare.com/reference-architecture/design-guides/securing-guest-wireless-networks/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/reference-architecture/design-guides/securing-guest-wireless-networks.mdx)
  * [/reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/](https://developers.cloudflare.com/reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/reference-architecture/diagrams/sase/deploying-self-hosted-VoIP-services-for-hybrid-users.mdx)
  * [/style-guide/documentation-content-strategy/component-attributes/introductions/](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/introductions/)-[Source](https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/docs/style-guide/documentation-content-strategy/component-attributes/introductions.mdx)



**Partials**




The `PublicStats` component allows you to reference specific values about Cloudflare's network without maintaining those values in multiple files.

Refer to the examples below for more information.
    
    
    import { PublicStats } from "~/components";
    
    Cloudflare has data centers in <PublicStats id="data_center_cities" />.
    
    Our network has <PublicStats id="total_bandwidth" />.
    
    Cloudflare also has <PublicStats id="network_peers" />.

Note

If you need more stats or to update these stats, submit a pull request to update [PublicStats.astro ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/src/components/PublicStats.astro)

## Associated content types

The `PublicStats` component is commonly used on the following type of pages:

  * [Overview](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/overview/)
  * [Reference Architecture](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/)
  * [Reference Architecture Diagrams](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/#reference-architecture-diagrams)



[PreviousProduct changelog](https://developers.cloudflare.com/style-guide/build-the-page/components/product-changelog/)[NextRelated product](https://developers.cloudflare.com/style-guide/build-the-page/components/related-product/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/build-the-page/components/public-stats.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
