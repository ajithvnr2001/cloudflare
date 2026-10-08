---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/
title: Apex proxying \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:03.875182+00:00
---

# Apex proxying · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)Get started

  4. /Advanced Settings
  5. /Apex proxying



# Apex proxying

Last updated Jun 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBenefitsSetup

Apex proxying allows your customers to use their apex domains (`example.com`) with your SaaS application.

Note

Only certain customers have access to this feature. For more details, see the [Plans page](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/).

## Benefits

In a normal Cloudflare for SaaS [setup](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/), your customers route traffic to your hostname by creating a `CNAME` record pointing to your CNAME target.

However, most DNS providers do not allow `CNAME` records at the zone's root1. This means that your customers have to use a subdomain as a vanity domain (`shop.example.com`) instead of their domain apex (`example.com`).

This limitation does not apply with apex proxying. Cloudflare assigns a set of [Static IP prefixes](https://developers.cloudflare.com/byoip/concepts/static-ips/) \- cost associated, reach out to your account team - to your account (or uses your own if you have [BYOIP](https://developers.cloudflare.com/byoip/)). This means then that customers can create a standard `A` record to route traffic to your domain, which can support the domain apex.

## Setup

  * [Set up Apex Proxying](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/setup/)



## Footnotes

  1. Cloudflare offers this functionality through [CNAME flattening](https://developers.cloudflare.com/dns/cname-flattening/). ↩




[PreviousConfiguring Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/)[NextSetup](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
