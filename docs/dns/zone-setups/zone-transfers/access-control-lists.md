---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/
title: Access Control Lists (ACLs) \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.445656+00:00
---

# Access Control Lists (ACLs) · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)
  5. /Access Control Lists (ACLs)



# Access Control Lists (ACLs)

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Access Control Lists (ACLs) define allowed source IP addresses from where servers accept incoming data or control messages.

When setting up new DNS zone transfers ([incoming](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/) or [outgoing](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/)), you will need to update the ACL at your other DNS provider(s) to allow Cloudflare to communicate with their server(s). You can find the Cloudflare IP addresses you need to allow at your other DNS provider(s) at [Cloudflare IP addresses](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/).

For your Cloudflare account, you only need to [create a new ACL](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/create-new-list/) if you want to specify additional NOTIFY IPs that Cloudflare should listen to.

[PreviousAlerts](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/)[NextCloudflare IP addresses](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/access-control-lists/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
