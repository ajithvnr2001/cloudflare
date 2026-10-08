---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/
title: Quotas and billing \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:00.534082+00:00
---

# Quotas and billing · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)
  4. /Quotas and billing



# Quotas and billing

Last updated Jul 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewQuota behaviorCheck quota usageBillable hostnames

Cloudflare for SaaS plans include a number of custom hostnames. Additional hostnames are billed according to your plan. For included hostnames, maximum hostnames, and current usage pricing, refer to [Plans](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/).

## Quota behavior

Custom hostname quotas apply at either the zone or account level. A zone-level quota includes hostnames in one zone. An account-level quota includes hostnames across every zone in the account.

The assigned quota is a soft limit. When usage reaches this limit, you can continue creating custom hostnames. The [Create Custom Hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/) response then includes a billing warning.

Non-Enterprise plans also have an API enforcement threshold. After usage reaches this threshold, the API rejects requests to create custom hostnames. Enterprise plans can continue to create custom hostnames after reaching this threshold.

The quota API returns current usage, the soft quota, and the enforcement threshold for the applicable scope.

## Check quota usage

Send a `GET` request to the custom hostname quota endpoint:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames/quota" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

The response contains these quota fields:

Field | Description  
---|---  
`allocated` | The operational soft quota for the zone or account.  
`used` | The custom hostnames counted toward the allocation.  
`exceeded` | Whether usage has reached or exceeded the allocation.  
`hard_cap` | The API enforcement threshold for non-Enterprise plans. Enterprise plans can exceed this value.  
  
Use `used` and `allocated` to monitor operational capacity. The `exceeded` field becomes `true` when `used` is greater than or equal to `allocated`.

## Billable hostnames

Each custom hostname counts toward usage until you delete it. This includes hostnames that are pending validation or activation. Deleting an unused custom hostname removes it from the usage count.

[PreviousPlans](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/)[NextEnable](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/enable/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/quotas-and-billing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
