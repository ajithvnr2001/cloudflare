---
url: https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/
title: Convert full setup to secondary setup \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:02.197476+00:00
---

# Convert full setup to secondary setup · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /Setup conversions
  5. /Full to secondary



# Convert full setup to secondary setup

Last updated Jun 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Prepare DNS records2\. Prepare the zone transfers3\. Convert the zone and initiate zone transfers

If you initially configured a [primary setup (full)](https://developers.cloudflare.com/dns/zone-setups/full-setup/), you can later convert your zone to use [incoming zone transfers (Cloudflare as secondary)](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/).

Subdomain setup

If you also use subdomain setup1, consider the [available combinations](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/#available-setups) and whether your zone conversion could have any implications.

## Footnotes

  1. Meaning you have one or more subdomains (`sub.example.com`) added to Cloudflare as their own zone, separate from your apex domain (`example.com`). ↩




Follow the steps below to achieve this conversion.

## 1\. Prepare DNS records

  1. [Export a zone file](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/#export-records).

  2. Import the zone file into your new primary DNS provider.

  3. At your Cloudflare zone, use the [Update DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/zone/methods/edit/) endpoint to enable [secondary DNS overrides](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/). Set the value for `secondary_overrides` to `true`.

Note

Enabling secondary DNS overrides is necessary in case you have DNS records that you wish to keep [proxied](https://developers.cloudflare.com/dns/proxy-status/).




## 2\. Prepare the zone transfers

  1. Make adjustments to DNSSEC according to your option for [DNSSEC with secondary setup](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/).

  2. (Optional) Create a Transaction Signature (TSIG).

A Transaction Signature (TSIG) authenticates communication between a primary and secondary DNS server.

Note

The TSIG names configured at your primary and secondary DNS providers have to be exactly the same. Any differences in TSIG names will cause zone transfers to fail.

While optional, this step is highly recommended.

To create a TSIG using the dashboard:

     1. In the Cloudflare dashboard, go to the account **Settings** page.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
     2. Go to **DNS Settings**.

     3. Under **DNS Zone Transfers** , for **TSIG** , select **Create**.

     4. Enter the following information:

        * **TSIG name** : The name of the TSIG object using domain name syntax (more details in [RFC 8945 section 4.2 ↗︎](https://datatracker.ietf.org/doc/html/rfc8945#section-4.2)).
        * **Secret (optional)** : Get a shared secret to add to your third-party nameservers. If left blank, this field generates a random secret.
        * **Algorithm** : Choose a TSIG signing algorithm.
     5. Select **Create**.

To create a TSIG using the API, send a [POST](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/tsigs/methods/create/) request.

  3. Create a peer server.

To create a peer server using the dashboard:

     1. In the Cloudflare dashboard, go to the account **Settings** page.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
     2. Go to **DNS Settings**.

     3. Under **DNS Zone Transfers** , for **Peer DNS servers** , select **Create**.

     4. Enter the following information, paying particular attention to:

        * **IP** : Specifies where Cloudflare sends transfer requests to.
        * **Port** : Specifies the IP Port for the transfer IP.
        * **Enable incremental (IXFR) zone transfers** : Specifies if Cloudflare sends IXFR requests in addition to the default AXFR requests.
        * **Link an existing TSIG** : If desired, link the TSIG you [previously created](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/#1-create-tsig-optional).
     5. Select **Create**.

To create a peer DNS server using the API, send a [POST request](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/peers/).




## 3\. Convert the zone and initiate zone transfers

  1. Use the [Edit Zone endpoint](https://developers.cloudflare.com/api/resources/zones/methods/edit/) with `type` set to `secondary` to convert the zone type. The existing records will remain in place.

  2. In the Cloudflare dashboard, go to the **DNS Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings)
  3. Select **Manage linked peers** under **DNS Zone Transfers**.

  4. Link the peer server you created in the previous steps and select **Save**.

  5. Back on the [**DNS Settings** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings) page, select **Initiate zone transfer**.

  6. Confirm the DNS records are transferring as expected.

  7. Go to the [**DNS Records** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/records) page and take note of your new **Cloudflare Nameservers**.

  8. At your domain registrar (or parent zone), [update your nameservers](https://developers.cloudflare.com/dns/nameservers/update-nameservers/) to include the `secondary.cloudflare.com` nameservers.




[PreviousFull to partial](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-partial/)[NextPartial to full](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/conversions/convert-full-to-secondary.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
