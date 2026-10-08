---
url: https://developers.cloudflare.com/email-service/platform/pricing/
title: Pricing \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.177371+00:00
---

# Pricing · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Platform
  4. /Pricing



# Pricing

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/platform/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPlan pricing

Cloudflare Email Service pricing is based on your Cloudflare plan and email usage.

## Plan pricing

Email Routing is available on both the Workers Free and Workers Paid plans. Sending to arbitrary recipients requires the Workers Paid plan. Sending to [verified destination addresses](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#destination-addresses) in your account is free on all plans, including when only Email Routing is configured.

| Workers Free | Workers Paid  
---|---|---  
**Outbound emails (Email Sending)** | Not available | 3,000 included per month, then $0.35 per 1,000 emails  
**Inbound emails (Email Routing)** | Unlimited | Unlimited  
  
The 3,000 included emails apply per account, per month, aligned with your Cloudflare subscription billing cycle. Emails that hard-bounce or are otherwise accepted by Email Service count toward the quota. Emails rejected at the API boundary, including sends blocked by the [suppression list](https://developers.cloudflare.com/email-service/concepts/suppressions/), do not count toward the quota.

Sends to verified destination addresses are free and do not count toward the included quota.

Email Routing Workers is billed according to [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

[PreviousLimits](https://developers.cloudflare.com/email-service/platform/limits/)[NextEvent subscriptions](https://developers.cloudflare.com/email-service/platform/event-subscriptions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
