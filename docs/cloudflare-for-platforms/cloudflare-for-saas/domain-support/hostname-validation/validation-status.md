---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/
title: Validation status - Custom Hostname Validation \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:00.153992+00:00
---

# Validation status - Custom Hostname Validation · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/)

  4. /[Hostname validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/)
  5. /Validation status



# Validation status

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRefresh validation

When you [validate a custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/), that hostname can be in several different statuses.

Status | Description  
---|---  
Pending | Custom hostname is pending hostname validation.  
Active | Custom hostname has completed hostname validation and is active.  
Active re-deploying | Customer hostname is active and the changes have been processed.  
Blocked | Custom hostname cannot be added to Cloudflare at this time. Custom hostname was likely associated with Cloudflare previously and flagged for abuse.  
  
If you are an Enterprise customer, contact your account team. Otherwise, email `abusereply@cloudflare.com` with the name of the web property and a detailed explanation of your association with this web property.  
Moved | Custom hostname is not active after **Pending** for the entirety of the [Validation Backoff Schedule](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/) or it no longer points to the fallback origin.  
Deleted | Custom hostname was deleted from the zone. Occurs when status is **Moved** for more than seven days.  
  
The custom hostname validation status is separate from the certificate status. In the [Custom hostname details endpoint](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/get/) response, `result.status` tracks hostname activation and `result.ssl.status` tracks certificate issuance and deployment.

A custom hostname is ready for production traffic when `result.status` is `active`, `result.ssl.status` is `active`, and DNS points to your SaaS target. If `result.status` is `active` but `result.ssl.status` is not `active`, Cloudflare has validated the hostname, but the certificate has not completed issuance and deployment.

## Refresh validation

To run the custom hostname validation check again, select **Refresh** on the dashboard or send a `PATCH` request to the [Edit custom hostname endpoint](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/). If using the API, make sure that the `--data` field contains an `ssl` object with the same `method` and `type` as the original request.

If the hostname is in a **Moved** or **Deleted** state, the refresh will set the custom hostname back to **Pending validation**.

[PreviousBackoff schedule](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/)[NextError codes](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
