---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/
title: Custom IKE ID for IPsec \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:27.387573+00:00
---

# Custom IKE ID for IPsec · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration

  4. /[Common settings](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/)
  5. /Custom IKE ID for IPsec



# Custom IKE ID for IPsec

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare WAN (formerly Magic WAN) customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Cloudflare WAN and a VeloCloud SD-WAN device together should utilize this option to create a high availability configuration.

Note

This feature is only available via API. There are no configuration options for a custom IKE ID for an IPsec tunnel in the Cloudflare dashboard.

VeloCloud has a high availability mechanism that allows customers to specify one set of IKE parameters (like IKE ID) and multiple remote IPs. Customers create an IKE ID, and then assign the same custom IKE ID to their primary IPsec tunnel and their backup IPsec tunnel. FQDN is the only supported type for custom IKE IDs.

Cloudflare WAN customers can set a custom IKE ID for an IPsec tunnel using the following API call. Customers will need to fill in the appropriate values for `<account_id>`, `<tunnel_id>`, and the FQDN wildcard before running the API call.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/ipsec_tunnels/TUNNEL_ID" \
    	--request PATCH \
    	--json '{
    		"custom_remote_identities": {
    				"fqdn_id": "<your_custom_label>.<account_id>.custom.ipsec.cloudflare.com"
    		}
    	}'

[PreviousEnable user roles](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/enable-roles/)[NextSecurity filters](https://developers.cloudflare.com/cloudflare-wan/security/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
