---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/
title: Set up multi-signer DNSSEC with outgoing zone transfers \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.662000+00:00
---

# Set up multi-signer DNSSEC with outgoing zone transfers · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)

  4. /[Cloudflare as Primary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/)
  5. /DNSSEC options



# Set up DNSSEC with Cloudflare as Primary

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you beginSteps

With [outgoing zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/), you keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance.

If you want to use DNSSEC with outgoing zone transfers, you should configure [multi-signer DNSSEC](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/). After setting up [Cloudflare as primary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/setup/), follow the steps below to enable DNSSEC.

## Before you begin

Note that:

  * This process requires that your other DNS provider(s) also support multi-signer DNSSEC.
  * Although you can complete a few steps via the dashboard, currently the whole process can only be completed using the API.
  * Enabling **DNSSEC** and **Multi-signer DNSSEC** in [**DNS Settings** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings) only replaces the first step below. You still have to follow the rest of this tutorial to complete the setup.



## Steps

  1. Use the [Edit DNSSEC Status endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/edit/) to enable DNSSEC and activate multi-signer DNSSEC for your zone. This is done by setting `status` to `active` and `dnssec_multi_signer` to `true`, as in the following example.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Write`

Edit DNSSEC Statusbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dnssec" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"status": "active",
    		"dnssec_multi_signer": true
    	}'

  2. Add the ZSK(s) of your external provider(s) to Cloudflare by creating a DNSKEY record on your zone.


    
    
    curl 'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records' \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      "type": "DNSKEY",
      "name": "<ZONE_NAME>",
      "data": {
        "flags": 256,
        "protocol": 3,
        "algorithm": 13,
        "public_key": "<PUBLIC_KEY>"
      },
      "ttl": 3600
    }'

  3. Once the DNSKEY record is transferred out from Cloudflare to your secondary provider, get Cloudflare's ZSK and manually add it to the DNSKEY record.

Currently, the ZSK is not automatically transferred out. You can use either the API or a query from one of the assigned Cloudflare nameservers to obtain it.




API example:
    
    
    curl 'https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec/zsk' \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Command line query example:
    
    
    $ dig <ZONE_NAME> dnskey @<CLOUDFLARE_NAMESERVER> +noall +answer | grep 256

  4. Add DS records to your registrar, one for each provider. You can see your Cloudflare DS record on the [**DNS Settings** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings) page, under **DS Record**.



The nameserver settings at your registrar should include the nameservers of all providers you will be using for your multi-signer DNSSEC setup.

[PreviousSetup](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/setup/)[NextRecords transfer](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
