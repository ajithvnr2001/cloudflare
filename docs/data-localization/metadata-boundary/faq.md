---
url: https://developers.cloudflare.com/data-localization/metadata-boundary/faq/
title: FAQs \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:43.612487+00:00
---

# FAQs · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/metadata-boundary/faq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /[Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/)
  4. /FAQs



# FAQs

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/metadata-boundary/faq/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat data is covered by the Customer Metadata Boundary?What data is not covered by the Customer Metadata Boundary?Who can use the Customer Metadata Boundary?What are the analytics products available for Metadata Boundary?

## What data is covered by the Customer Metadata Boundary?

Nearly all end user metadata is covered by the Customer Metadata Boundary. This includes all of the end user data for which Cloudflare is a processor, as defined in the [Cloudflare Privacy Policy ↗︎](https://www.cloudflare.com/privacypolicy/). Cloudflare is a data processor of Customer Logs, which are defined as end user logs that we make available to our customers via the dashboard or other online interfaces. End users are those who access or use our customers' domains, networks, websites, application programming interfaces, and applications.

Specific examples of this data include all of the analytics in our dashboard and APIs on requests, responses, and security products associated and all of the logs received through Logpush.

## What data is not covered by the Customer Metadata Boundary?

Some of the data for which Cloudflare is a controller, as defined in the [Cloudflare Privacy Policy ↗︎](https://www.cloudflare.com/privacypolicy/).

Some examples:

  * Customer account data (for example, name and billing information).
  * Customer configuration data (for example, the content of WAF custom rules).
  * Metadata that is "operational" in nature — data needed for Cloudflare to properly operate our network. This includes metadata such as: 
    * System data generated for debugging (for example, internal application logs, core dumps).
    * Networking flow data (for example, sFlow samples from routers), including data on DDoS attacks.



## Who can use the Customer Metadata Boundary?

Currently, this is available for Enterprise customers as part of the Data Localization Suite.

The Customer Metadata Boundary is for customers who want to limit personal data transfer outside the EU or the US (depending on the selected region). These customers should already be using Regional Services, which ensures that traffic content is only ever decrypted within the geographic region specified by the customer.

## What are the analytics products available for Metadata Boundary?

HTTP and Firewall analytics are available.

At the moment, there are no analytics available for Workers, DNS, and Load Balancing. Additionally, there are no dashboard logs or analytics for [Gateway](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#limitations). Enterprise users can still export Gateway logs via [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

[PreviousOut of region access](https://developers.cloudflare.com/data-localization/metadata-boundary/out-of-region-access/)[NextOverview](https://developers.cloudflare.com/data-localization/regional-services/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/metadata-boundary/faq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
