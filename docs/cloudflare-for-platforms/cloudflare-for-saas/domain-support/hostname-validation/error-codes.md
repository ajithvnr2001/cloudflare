---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/
title: Error codes - Custom Hostname Validation \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:59.895885+00:00
---

# Error codes - Custom Hostname Validation · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/)

  4. /[Hostname validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/)
  5. /Error codes



# Error codes

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you [validate a custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/), you might encounter the following error codes.

Error | Cause  
---|---  
Zone does not have a fallback origin set. | Fallback is not active.  
Fallback origin is in a status of `initializing`, `pending_deployment`, `pending_deletion`, or `deleted`. | Fallback is not active.  
Custom hostname does not `CNAME` to this zone. | Zone does not have [apex proxying entitlement](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/) and custom hostname does not CNAME to zone.  
None of the `A` or `AAAA` records are owned by this account and the pre-generated ownership validation token was not found. | Account has [apex proxying enabled](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/) but the custom hostname failed the hostname validation check on the `A` record.  
This account and the pre-generated ownership validation token was not found. | Hostname does not `CNAME` to zone or none of the `A`/`AAAA` records match reserved IPs for zone.  
  
[PreviousValidation status](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/)[NextMove hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
