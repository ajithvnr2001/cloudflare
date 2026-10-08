---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/
title: Real-time validation methods - Custom Hostname Validation \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:00.110205+00:00
---

# Real-time validation methods - Custom Hostname Validation · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/)

  4. /[Hostname validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/)
  5. /Real-time validation



# Real-time validation

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse whenHow to Normal setup (CNAME target) Apex proxying

When you use a real-time validation method, Cloudflare verifies your customer's hostname when your customers adds their [DNS routing record](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record) to their authoritative DNS.

## Use when

Real-time validation methods put less burden on your customers because it does not require any additional actions.

However, it may cause some downtime since Cloudflare takes a few seconds to iterate over DNS records. This downtime also can increase - due to the increasing [validation backoff schedule](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/) \- if your customer takes additional time to add their DNS routing record.

To minimize this downtime, you can continually send no-change [`PATCH` requests](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/) for the specific custom hostname until it validates (which resets the validation backoff schedule).

To avoid any chance of downtime, use a [pre-validation method](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/)

## How to

Real-time validation occurs automatically when your customer adds their [DNS routing record](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record).

The exact record depends on your Cloudflare for SaaS setup.

### Normal setup (CNAME target)

Most customers will have a `CNAME` target, which requires their customers to create a `CNAME` record similar to:
    
    
    mystore.com CNAME customers.saasprovider.com

### Apex proxying

With [apex proxying](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/), SaaS customers need to create an `A` record for their hostname that points to the IP prefix allocated to the SaaS provider's account.
    
    
    example.com.  60  IN  A   192.0.2.1

Note

For [BYOIP](https://developers.cloudflare.com/byoip/) customers, Cloudflare automatically enables the Apex Proxy Access feature on your BYOIP block, which allows Custom Hostnames to be activated via [Apex proxying](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/#apex-proxying) when Authoritative DNS for a customer's hostname targets any IP addresses in your BYOIP block.

[PreviousPre-validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/)[NextZero-downtime migration](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/zero-downtime-migration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
