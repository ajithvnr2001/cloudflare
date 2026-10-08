---
url: https://developers.cloudflare.com/dns/internal-dns/dns-views/
title: Manage DNS views \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:57.672205+00:00
---

# Manage DNS views · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/internal-dns/dns-views/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Internal DNS](https://developers.cloudflare.com/dns/internal-dns/)
  4. /Views



# Manage DNS views

Last updated Jul 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/internal-dns/dns-views/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfiguration conditionsCreate a viewDelete a viewOther API actions

Internal DNS views are logical groupings of [internal DNS zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/). As explained in the [architecture overview](https://developers.cloudflare.com/dns/internal-dns/#architecture-overview), DNS views are referenced by [Gateway resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) to define how a specific query should be resolved.

Refer to the sections below for details on how to manage your DNS views, or consider the [get started](https://developers.cloudflare.com/dns/internal-dns/get-started/) for a complete workflow.

## Configuration conditions

When setting up DNS views, observe the following conditions:

  * DNS views can be empty, with no [internal zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/) linked to them.
  * A DNS view cannot contain public DNS zones.1
  * Each internal DNS zone name must be unique within a given DNS view.
  * Each DNS view name must be unique within a given Cloudflare account.



1 DNS zones that contain public DNS records and are accessible by public resolvers.

## Create a view

  1. In the Cloudflare dashboard, go to the **Internal DNS** page.

[ Go to **Internal DNS** ↗ ](https://dash.cloudflare.com/?to=/:account/internal-dns)
  2. Go to **Internal DNS Views**.

  3. Select **Create a view**.

  4. Give your view a descriptive name.

  5. Select **Manage zones** to add zones to your view. Select the internal zones that should be used to resolve queries sent by Gateway resolver to this view.

  6. Choose **Save** to confirm.




Use the [Create Internal DNS View](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/create/) endpoint. For each view you create, list all the internal zones that should be grouped under that view.

Note

DNS views are managed at the account level. Make sure your API token includes **Account** > **DNS Views** > **Edit** permission.

## Delete a view

DNS views can be deleted even if they still have internal zones linked to them. The internal DNS zones will continue to exist but will be unlinked once the view is deleted.

It is also possible to delete a DNS view that is being referenced by a Gateway resolver policy. In this case, queries matching the policy will return SERVFAIL.

  1. In the Cloudflare dashboard, go to the **Internal DNS** page.

[ Go to **Internal DNS** ↗ ](https://dash.cloudflare.com/?to=/:account/internal-dns)
  2. Go to **Internal DNS Views**.

  3. Find the view you want to delete.

  4. Select the three dots in the corresponding row and choose _Delete_.

  5. In the confirmation dialog, select **Delete** again to proceed.




Use the [Delete Internal DNS View](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/delete/) endpoint.

## Other API actions

  * [Update a DNS view](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/edit/) (`PATCH`)
  * [Get view details](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/get/) (`GET`)
  * [List DNS views](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/list/) (`GET`)



[PreviousReference zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/)[NextConnectivity](https://developers.cloudflare.com/dns/internal-dns/connectivity/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/internal-dns/dns-views.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
