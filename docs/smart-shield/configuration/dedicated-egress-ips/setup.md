---
url: https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/
title: Set up Dedicated CDN Egress IPs \u00b7 Cloudflare Smart Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:31.844579+00:00
---

# Set up Dedicated CDN Egress IPs · Cloudflare Smart Shield docs

> Source: https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Smart Shield](https://developers.cloudflare.com/smart-shield/)
  3. /…

Configuration

  4. /[Dedicated Egress IPs](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/)
  5. /Setup



# Setup

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequirementsTurn on DCEI for a zoneCheck DCEI status for a zoneTurn off DCEI for a zoneCheck your IPs

You can use the [Edit Zone Settings API endpoint](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) to set up Dedicated CDN Egress IPs (formerly known as Aegis). If you are not familiar with how Cloudflare API works, refer to [Fundamentals](https://developers.cloudflare.com/fundamentals/api/).

Enterprise-only

Dedicated CDN Egress IPs (DCEI) are currently available to Enterprise customers. Contact your account team to request access.

## Requirements

  * The Dedicated CDN Egress IPs (DCEI) zone setting is only available within Cloudflare accounts that own leased IPs, or accounts to which a [BYOIP prefix](https://developers.cloudflare.com/byoip/) has been delegated. If you wish to use Dedicated CDN Egress IPs for zones that do not meet this criteria, contact your account team.
  * Each dedicated egress pool can consist of either IPs from a [BYOIP prefix](https://developers.cloudflare.com/byoip/) or Cloudflare-leased IPs. A single dedicated egress pool cannot contain both BYOIPs and leased IPs. Also, a single BYOIP prefix can be used for either CDN ingress or CDN egress, but not both.




Caution

You must allowlist the IP addresses from this pool in your infrastructure before linking it to a zone. If you skip this step, traffic will not reach your origin, causing errors.

## Turn on DCEI for a zone

  1. Contact your account team to get the ID for your dedicated egress pool.
  2. Make a `PATCH` request to the [Edit Zone Setting](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) endpoint:


  * Specify `aegis` as the setting ID in the URL.
  * In the request body, set `enabled` to `true` and use the ID from the previous step as the `pool_id` value.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone Settings Write`

Edit zone settingbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/aegis" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"id": "aegis",
    		"value": {
    				"enabled": true,
    				"pool_id": "<EGRESS_POOL_ID>"
    		}
    	}'

## Check DCEI status for a zone

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone Settings Write`
  * `Zone Settings Read`

Get zone settingbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/aegis" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Turn off DCEI for a zone

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone Settings Write`

Edit zone settingbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/aegis" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"id": "aegis",
    		"value": {
    				"enabled": false
    		}
    	}'

## Check your IPs

You can find your leased dedicated IPs for CDN egress on the dashboard under [**Address space** > **Leased IPs** ↗︎](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space).

If you are using BYOIP, refer to **BYOIP prefixes** instead.

[PreviousConnection forwarding](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/how-it-works/connection-forwarding/)[NextIPs utilization](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ips-utilization/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/smart-shield/configuration/dedicated-egress-ips/setup.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
