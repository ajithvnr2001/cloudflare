---
url: https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/
title: Integrate with PagerDuty \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:04.989850+00:00
---

# Integrate with PagerDuty · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)
  4. /Integrate with PagerDuty



# Integrate with PagerDuty

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To integrate Cloudflare health monitor notifications with PagerDuty, follow the steps outlined in PagerDuty’s [Email Integration Guide ↗︎](https://www.pagerduty.com/docs/guides/email-integration-guide/). If you do not have a PagerDuty account, you will first need to set that up.

PagerDuty will generate an email address that will create incidents based on emails sent to that address. For help locating that email address, refer to the [PagerDuty documentation ↗︎](https://www.pagerduty.com/docs/guides/email-integration-guide/).

When creating the Notifier object, configure the email to go to the PagerDuty integration email. Consequently, whenever a pool or endpoint goes down, an Incident will be created to capture it.

[PreviousSupported fields and operators](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/)[NextAdditional DNS records](https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/pagerduty-integration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
