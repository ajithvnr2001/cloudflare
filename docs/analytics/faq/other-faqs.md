---
url: https://developers.cloudflare.com/analytics/faq/other-faqs/
title: Other FAQs \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:11.840179+00:00
---

# Other FAQs · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/faq/other-faqs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /FAQs
  4. /Other FAQs



# Other FAQs

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/faq/other-faqs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhy do I see a large amount of traffic from CLOUDFLARENET ASN 13335 in Analytics? Does this indicate a DDoS attack?

## Why do I see a large amount of traffic from CLOUDFLARENET ASN 13335 in Analytics? Does this indicate a DDoS attack?

There is a number of different types of traffic which may originate from **CLOUDFLARENET ASN 13335** ; just because there is a lot of traffic from this AS, it likely does not indicate a DDoS attack.

Some sources of traffic from ASN13335 include:

  * [Workers subrequests](https://developers.cloudflare.com/workers/runtime-apis/fetch/)
  * [WARP](https://developers.cloudflare.com/warp-client/known-issues-and-faq/#does-warp-reveal-my-ip-address-to-websites-i-visit)
  * [iCloud Private Relay ↗︎](https://blog.cloudflare.com/icloud-private-relay/) (For reference, iCloud Private Relay’s egress IP addresses are available in this [CSV form ↗︎](https://mask-api.icloud.com/egress-ip-ranges.csv))
  * [Cloudflare Privacy Proxy ↗︎](https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/)
  * Other Cloudflare features like [Health Checks](https://developers.cloudflare.com/health-checks/)



[PreviousWorkers Analytics Engine FAQs](https://developers.cloudflare.com/analytics/faq/wae-faqs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/faq/other-faqs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
