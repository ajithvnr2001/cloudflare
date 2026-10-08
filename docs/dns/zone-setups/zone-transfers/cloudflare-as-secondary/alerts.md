---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/
title: Alerts for Secondary DNS \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.915617+00:00
---

# Alerts for Secondary DNS · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)

  4. /[Cloudflare as Secondary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/)
  5. /Alerts



# Alerts

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can configure alerts to receive notifications for changes in your secondary DNS.

Secondary DNS all Primaries Failing

**Who is it for?**

Enterprise customers who have at least one secondary zone in their account and want to receive a notification if all of their primary nameservers are failing.

**Other options / filters**

None.

**Included with**

Purchase of Secondary DNS

**What should you do if you receive one?**

  1. Confirm that your primary nameservers are up and running.
  2. Confirm that the [Access Control Lists (ACLs)](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/) on your primary nameservers are configured correctly.
  3. Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).



Secondary DNS Primaries Failing

**Who is it for?**

Enterprise customers who have at least one secondary zone and want to receive a notification if at least one of their primary nameservers is failing while transfers from at least one other primary are still successful.

**Other options / filters**

None.

**Included with**

Purchase of Secondary DNS.

**What should you do if you receive one?**

  1. Confirm that your primary nameservers are up and running.
  2. Confirm that the [Access Control Lists (ACLs)](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/) on your primary nameservers are configured correctly.
  3. Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).



Secondary DNS Successfully Updated

**Who is it for?**

Enterprise customers who have at least one secondary zone in their account and want to receive a notification on successful zone transfers.

**Other options / filters**

None.

**Included with**

Purchase of Secondary DNS.

**What should you do if you receive one?**

No action needed. Everything is working correctly.

Secondary DNS Warning

**Who is it for?**

Customers who are using Cloudflare for Secondary DNS and want to receive notifications about warnings issued by the transferred zone.

**Other options / filters**

None.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

Actions for failure notifications will depend on the type of failure.

Refer to [Cloudflare Notifications](https://developers.cloudflare.com/notifications/get-started/) for more information on how to set up an alert.

[PreviousDNSSEC options](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/)[NextAbout](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
