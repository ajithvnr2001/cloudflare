---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/create-new-list/
title: Create a new Access Control List \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.509628+00:00
---

# Create a new Access Control List · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/create-new-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)

  4. /[Access Control Lists (ACLs)](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/)
  5. /Create ACL



# Create ACL

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/create-new-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You need to create an Access Control List (ACL) if Cloudflare is your [secondary DNS provider](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/). The ACL will specify additional NOTIFY IPs that Cloudflare should listen to.

An ACL is configured at the account level, which means that it will apply to every primary and secondary zone in your account.

To create a new ACL using the dashboard:

  1. In the Cloudflare dashboard, go to the account **Settings** page.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
  2. Go to **DNS Settings**.

  3. Under **DNS Zone Transfers** , for **ACL** , select **Create**.

  4. Enter the following information:

     * **ACL name** : Provide a descriptive name.
     * **IP range** : Enter a range of IPv4 or IPv6 addresses (limited to a maximum of /24 for IPv4 and /64 for IPv6).
  5. Select **Create**.




To create a new ACL using the API, send a [POST](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/acls/methods/create/) request.

[PreviousCloudflare IP addresses](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/)[NextTroubleshooting](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/access-control-lists/create-new-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
