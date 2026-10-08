---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/
title: Move hostnames between zones \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:00.267719+00:00
---

# Move hostnames between zones · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /[Custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/)
  5. /Move hostnames



# Move hostnames

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCNAMEA recordWildcard certificate

As a SaaS provider, you may want, or have, multiple zones to manage hostnames. Each zone can have different configurations or origins, as well as correlate to varying products. You might shift custom hostnames between zones to enable or disable certain features. Cloudflare allows migration within the same account through the steps below:

* * *

## CNAME

If your custom hostname uses a CNAME record, add the custom hostname to the new zone and [update your DNS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records) to point to the new zone.

Note

If you would like to migrate the custom hostname without end customers changing the DNS target, use [apex proxying](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/).

  1. [Add custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/) to your new zone.

  2. Direct your customer to [change the DNS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records) so that it points to the new zone.

  3. Confirm that the custom hostname has validated in the new zone.

  4. Wait for the certificate to validate automatically through Cloudflare or [validate it using Domain Control Validation (DCV)](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/#perform-dcv).

  5. Remove custom hostname from the old zone.




Once these steps are complete, the custom hostname's traffic will route to the second SaaS zone and will use its configuration.

## A record

Through [Apex Proxying](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/) or [BYOIP](https://developers.cloudflare.com/byoip/), you can migrate the custom hostname without action from your end customer.

  1. Verify with the account team that your apex proxying IPs have been assigned to both SaaS zones.

  2. [Add custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/) to the new zone.

  3. Confirm that the custom hostname has validated in the new zone.

  4. Wait for the certificate to validate automatically through Cloudflare or [validate it using DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/#perform-dcv).

  5. Remove custom hostname from the old zone.




Note

The most recently edited custom hostname will be active. For instance, `example.com` exists on `SaaS Zone 1`. It is added to `SaaS Zone 2`. Because it was activated more recently on `SaaS Zone 2`, that is where it will be active. However, if edits are made to example.com on `SaaS Zone 1`, it will reactivate on that zone instead of `SaaS Zone 2`.

## Wildcard certificate

If you are migrating custom hostnames that rely on a Wildcard certificate, Cloudflare cannot automatically complete Domain Control Validation (DCV).

  1. [Add custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/) to the new zone.

  2. Direct your customer to [change the DNS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records) so that it points to the new zone.

  3. [Validate the certificate](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/#perform-dcv) on the new zone through DCV.




The custom hostname can activate on the new zone even if the certificate is still active on the old zone. This ensures a valid certificate exists during migration. However, it is important to validate the certificate on the new zone as soon as possible.

Note

Verify that the custom hostname successfully activated after the migration on the [**Custom Hostnames** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/custom-hostnames) page.

[PreviousError codes](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/)[NextRemove custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
