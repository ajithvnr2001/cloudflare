---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames/
title: Remove custom hostnames \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:00.304614+00:00
---

# Remove custom hostnames · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /[Custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/)
  5. /Remove custom hostnames



# Remove custom hostnames

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDomains using CloudflareDomains not using CloudflareFor end customers

As a SaaS provider, your customers may decide to no longer participate in your service offering. If that happens, you need to stop routing traffic through those custom hostnames.

## Domains using Cloudflare

If your customer's domain is also using Cloudflare, they can stop routing their traffic through your custom hostname by updating their Cloudflare DNS.

If they update their [`CNAME` record](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record) so that it no longer points to your `CNAME` target:

  * The domain's traffic will not route through your custom hostname.
  * The custom hostname will enter into a **Moved** state.



If the custom hostname is in a **Moved** state for seven days, it will transition into a **Deleted** state.

You should remove a customer's custom hostname from your zone if they decide to churn. This is especially important if your end customers are using Cloudflare because if the churned customer changes the DNS target to point away from your SaaS zone but you have not removed it, the custom hostname will continue to route to your service. This is a result of the [custom hostname priority logic](https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/#hostname-priority).

## Domains not using Cloudflare

If your customer's domain is not using Cloudflare, you must remove a customer's custom hostname from your zone if they decide to churn.

  1. In the Cloudflare dashboard, go to the **Custom Hostnames** page.

[ Go to **Custom Hostnames** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/custom-hostnames)
  2. Select the custom hostname and select **Delete**.

  3. A confirmation window will appear. Acknowledge the warning and select **Delete** again.




To delete a custom hostname and any issued certificates using the API, send a [`DELETE` request](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/delete/).

## For end customers

If your SaaS domain is also a [domain using Cloudflare](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/), you can use your Cloudflare DNS to remove your domain from your SaaS provider.

This means that - if you [remove the DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#delete-dns-records) pointing to your SaaS provider - Cloudflare will stop routing domain traffic through your SaaS provider and the associated custom hostname will enter a **Moved** state.

This also means that you need to keep DNS records pointing to your SaaS provider for as long as you are a customer. Otherwise, you could accidentally remove your domain from their services.

[PreviousMove hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/)[NextCustom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
