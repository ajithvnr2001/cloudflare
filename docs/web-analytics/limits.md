---
url: https://developers.cloudflare.com/web-analytics/limits/
title: Web Analytics - Limits \u00b7 Cloudflare Web Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:53.798912+00:00
---

# Web Analytics - Limits · Cloudflare Web Analytics docs

> Source: https://developers.cloudflare.com/web-analytics/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)
  3. /Limits



# Limits

Last updated Aug 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web-analytics/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSite limitsRules limits

Cloudflare limits the number of sites for which you can track web analytics, as well as the number of rules allowed for each plan type. Refer to the following tables for more information.

## Site limits

Cloudflare limits the number of sites for which you can track web analytics when they are not proxied by Cloudflare.

Site type | Limit  
---|---  
Not proxied through Cloudflare | 10  
Proxied through Cloudflare | No limit  
  
Note

To provide a reliable and fast experience, viewing aggregate data is limited to 1,000 websites in parallel in the dashboard. Customers with large volumes of tracked websites can workaround this restriction by selecting specific websites or using the GraphQL API to extract data.

## Rules limits

Cloudflare limits the number of Web Analytics rules you can have by plan type. For plans with a limit of zero, Web Analytics injects the JS snippet on all subdomains.

Rules are only available for sites proxied through Cloudflare.

Plan type | Rules limit  
---|---  
Free | 0  
Pro | 5  
Business | 20  
Enterprise | 100  
  
[PreviousData origin and collection](https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/)[NextFAQs](https://developers.cloudflare.com/web-analytics/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web-analytics/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
