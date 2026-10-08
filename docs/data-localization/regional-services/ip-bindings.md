---
url: https://developers.cloudflare.com/data-localization/regional-services/ip-bindings/
title: Regionalized IP Bindings \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:43.943660+00:00
---

# Regionalized IP Bindings · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/regional-services/ip-bindings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /[Regional Services](https://developers.cloudflare.com/data-localization/regional-services/)
  4. /Regionalized IP Bindings



# Regionalized IP Bindings

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/regional-services/ip-bindings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksChoose which CIDR to bindPrerequisitesRequired API token permissionsList available regionsCreate a prefix binding Check binding status Handle a conflict errorList prefix bindingsUpdate the region for a bindingDelete a bindingRelated resources

Note

Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.

Regionalized IP Bindings let you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through [Bring Your Own IP (BYOIP)](https://developers.cloudflare.com/byoip/). You bind a CIDR from one of your prefixes to a region, and Cloudflare processes traffic destined for those IP addresses only within the data centers in that region.

This complements the other ways to use [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/): where [Regional Hostnames](https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/) regionalize traffic by hostname, Regionalized IP Bindings regionalize traffic by IP prefix — ideal for address-map deployments and any service you address by IP rather than hostname. Because bindings are managed entirely through the API, you can regionalize broad configurations yourself once your entitlements are enabled, without per-zone setup from your account team.

## How it works

A prefix binding maps a CIDR (within a BYOIP prefix you own) to a region key (for example, `us` or `eu`). After Cloudflare provisions the binding, traffic to addresses in that CIDR terminates TLS and is processed only inside the configured region, following the same in-region processing model described in [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/).

Bindings are managed through the Data Localization Suite API under `/accounts/{account_id}/dls/`.

## Choose which CIDR to bind

A binding covers a range of addresses within a prefix, not just a single address — you do **not** need to create one binding per IP address. The `cidr` you bind must:

  * Fall within the prefix identified by `prefix_id`.
  * Contain only unused IP addresses. Binding IP addresses that are already in use interrupts their traffic while the change propagates.
  * Be **more specific than the prefix itself** — a sub-range within it. For example, within a `/24` prefix you can bind any range from a `/25` down to a single address (a `/32` for IPv4, or a `/128` for IPv6). Binding the entire prefix (the full `/24`) is rejected with a conflict error, because the whole prefix range is already in use once Cloudflare advertises it.



How you choose the CIDR depends on how you want to split the prefix across regions:

  * **One region for the whole prefix** — cover the prefix with sub-ranges that all point to the same region. For example, bind both `203.0.113.0/25` and `203.0.113.128/25` to `eu` to regionalize every address in a `/24`.
  * **Different regions for different addresses** — bind each range to the region you want (for example, `203.0.113.0/25` to `eu` and `203.0.113.128/25` to `us`). Cloudflare applies the most specific binding that matches a given address, so a narrower binding takes precedence over a broader one that overlaps it.



A conflict occurs only when you try to create two bindings for the exact same CIDR. Bindings with overlapping but different CIDRs can coexist, and Cloudflare applies the most specific matching binding. To change the region for an existing CIDR, update its binding instead of creating another one.

## Prerequisites

Before you create a binding, make sure that:

  * Your account has both the **Regional Services** and **Regional Services for BYOIP** entitlements enabled. Contact your account team to enable them.
  * You have [onboarded a BYOIP prefix](https://developers.cloudflare.com/byoip/) to Cloudflare and know its prefix ID.
  * The region you want to use exists for your account. Refer to List available regions.
  * Your [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) has the required permissions. Refer to Required API token permissions.



## Required API token permissions

These endpoints are authorized at the account level. The permissions you need depend on the operation:

Operation | Required token permissions  
---|---  
List regions, get a region, list or get bindings | **DLS: Read**  
Create, update, or delete a prefix binding | **DLS: Write** _and_ **IP Prefixes: Write**  
  
Write operations require **IP Prefixes: Write** in addition to **DLS: Write** because the binding is created against a BYOIP prefix that you own in [Addressing](https://developers.cloudflare.com/byoip/) — Cloudflare verifies that you have permission to modify that prefix. A token with only **DLS: Write** can read regions and bindings but will be rejected when it tries to create or change a binding.

The **Super Administrator** and **Administrator** roles include all of these permissions. A custom role works as long as it includes the permission groups above.

## List available regions

Each binding references a region by its `region_key` (for example, `us` or `eu`). List the regions available to your account to find a valid key.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/dls/regions" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Responsejson
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": [
    		{
    			"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    			"name": "Europe",
    			"region_key": "eu",
    			"created_on": "2026-01-13T23:59:45.276558Z",
    			"modified_on": "2026-01-13T23:59:45.276558Z",
    			"version": 1,
    			"version_created_on": "2026-01-13T23:59:45.276558Z"
    		}
    	],
    	"result_info": {
    		"count": 1,
    		"per_page": 25,
    		"cursor": ""
    	}
    }

Use the `type` query parameter (`managed` or `custom`) to filter the results by [region type](https://developers.cloudflare.com/data-localization/region-support/#region-types). Results are paginated — pass the `cursor` value from a response to fetch the next page.

Get a single region

Retrieve a region by its `region_key` or ID.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/dls/regions/eu" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Create a prefix binding

Bind a CIDR from one of your BYOIP prefixes to a region. The `cidr` must fall within the prefix identified by `prefix_id` and be more specific than the prefix itself.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/dls/regional_services/prefix_bindings" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"prefix_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    		"cidr": "203.0.113.0/25",
    		"region_key": "eu"
    	}'

Responsejson
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"id": "f0e1d2c3-b4a5-6789-0abc-def123456789",
    		"prefix_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    		"cidr": "203.0.113.0/25",
    		"region_key": "eu"
    	}
    }

Always bind unused IP addresses

Creating or changing a binding can take four to six hours to propagate across Cloudflare's network. If the affected IP addresses are already in use, this process interrupts their traffic and clients receive TCP resets.

Always bind unused IP addresses. Wait for the binding to become **active** before you direct production traffic to the addresses or add them to an [address map](https://developers.cloudflare.com/byoip/address-maps/).

### Check binding status

Use the binding ID returned by the create request to call the [Get service binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/get/) endpoint. The Regionalized IP Bindings API and Service Bindings API use the same binding ID.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/addressing/prefixes/%7Bprefix_id%7D/bindings/%7Bbinding_id%7D" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

The binding is ready when `result.provisioning.state` is `active`:

Responsejson
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"id": "f0e1d2c3-b4a5-6789-0abc-def123456789",
    		"cidr": "203.0.113.0/25",
    		"provisioning": {
    			"state": "active"
    		}
    	}
    }

### Handle a conflict error

Because each CIDR can have only one binding, a create request for a CIDR that is already bound fails with an HTTP `409` conflict:

Responsejson
    
    
    {
    	"result": null,
    	"success": false,
    	"errors": [
    		{
    			"code": 1108,
    			"message": "conflict: binding already exists for CIDR 203.0.113.0/24"
    		}
    	],
    	"messages": []
    }

You get this error in two cases:

  * **You tried to bind the entire prefix.** The full prefix range (for example, the whole `/24`) is already in use once Cloudflare advertises your prefix, so it cannot be bound to a region directly. Bind a more specific range within the prefix instead — a `/25` down to a single `/32` — and cover the prefix with several sub-ranges if you need to regionalize all of its addresses.
  * **The CIDR is already bound.** A binding for that exact range already exists, for example from an earlier request that succeeded.



To resolve it:

  * List your existing bindings to see what is already configured.
  * To move an existing binding to a different region, update it rather than creating a new one.
  * To bind a different range, choose a CIDR that is not already bound. To replace an existing binding with a different CIDR, delete it first, then create the new one.



## List prefix bindings
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/dls/regional_services/prefix_bindings" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Responsejson
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": [
    		{
    			"id": "f0e1d2c3-b4a5-6789-0abc-def123456789",
    			"prefix_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    			"cidr": "203.0.113.0/25",
    			"region_key": "eu"
    		}
    	],
    	"result_info": {
    		"count": 1,
    		"per_page": 25,
    		"cursor": ""
    	}
    }

Get a single binding
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/dls/regional_services/prefix_bindings/%7Bbinding_id%7D" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Update the region for a binding

Change the region a binding points to. Only the `region_key` can be updated. To change the CIDR, delete the binding and create a new one.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/dls/regional_services/prefix_bindings/%7Bbinding_id%7D" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"region_key": "us"
    	}'

Responsejson
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"id": "f0e1d2c3-b4a5-6789-0abc-def123456789",
    		"prefix_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    		"cidr": "203.0.113.0/25",
    		"region_key": "us"
    	}
    }

## Delete a binding

Remove a binding to stop regionalizing traffic for its CIDR.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/dls/regional_services/prefix_bindings/%7Bbinding_id%7D" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Responsejson
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": null
    }

## Related resources

  * [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/) — overview and in-region processing model.
  * [Available regions and product support](https://developers.cloudflare.com/data-localization/region-support/) — the full list of regions and their definitions.
  * [Bring Your Own IP (BYOIP)](https://developers.cloudflare.com/byoip/) — onboard your own IP prefixes to Cloudflare.



[PreviousRegionalized Spectrum Applications](https://developers.cloudflare.com/data-localization/regional-services/spectrum-applications/)[NextOverview](https://developers.cloudflare.com/data-localization/how-to/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/regional-services/ip-bindings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
