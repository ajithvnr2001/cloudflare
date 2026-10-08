---
url: https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/
title: Reference zones \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:58.541856+00:00
---

# Reference zones · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[Internal DNS](https://developers.cloudflare.com/dns/internal-dns/)

  4. /[Internal zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/)
  5. /Reference zones



# Reference zones

Last updated Jul 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfiguration conditionsSet up

During an [internal DNS query resolution](https://developers.cloudflare.com/dns/internal-dns/#architecture-overview), if no internal record is found within a matching internal zone, Cloudflare will check if the matching internal zone is referencing another internal zone. Successive references can be followed with a maximum of five references in a chain.

Note

A wildcard record (`*.example.local`) in the matching internal zone will take precedence over an exact match in a reference zone.

## Configuration conditions

  * Each internal zone can only reference one other zone.
  * The same zone can be referenced by multiple internal zones.
  * Public zones cannot be used as reference zones.
  * Reference zones do not have to be linked to the same [DNS view](https://developers.cloudflare.com/dns/internal-dns/dns-views/) as the zone referencing them. They may also not be linked to any view at all.



## Set up

  1. In the Cloudflare dashboard, go to the **Internal DNS** page.

[ Go to **Internal DNS** ↗ ](https://dash.cloudflare.com/?to=/:account/internal-dns)
  2. Select a zone.

  3. Within the selected zone, go to **Reference zone**.

  4. Select **Add reference zone**. If your zone already has a reference zone set up, you must first remove it. As explained in the configuration conditions, each internal zone can only reference one other zone at a time.

  5. Find the zone you want to use as reference and choose **Select** in the respective row.




Use the [Update DNS settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/zone/methods/edit/) endpoint. In `--json`, specify the `internal_dns` object with the parameter `reference_zone_id`.

Note

If your API token is scoped to specific zones, make sure it includes both the zone you are updating and the zone you are referencing.

In the following example, internal zone A (ID `8a904aeb565c42cfa207d98f6edea2f3`) is referencing internal zone B (ID `8e64c6fb4b514f3faf64de81efc11e51`).

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone DNS Settings Write`
  * `DNS Write`

Update DNS Settingsbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/8a904aeb565c42cfa207d98f6edea2f3/dns_settings" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"internal_dns": {
    				"reference_zone_id": "8e64c6fb4b514f3faf64de81efc11e51"
    		}
    	}'

A third zone (C) could also point to zone B as a reference, but zone A cannot add another zone as a reference while also having zone B configured as its reference zone.

[PreviousInternal DNS records](https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/)[NextViews](https://developers.cloudflare.com/dns/internal-dns/dns-views/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/internal-dns/internal-zones/reference-zones.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
