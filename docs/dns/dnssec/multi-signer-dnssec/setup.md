---
url: https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/
title: Set up multi-signer DNSSEC \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:57.037175+00:00
---

# Set up multi-signer DNSSEC · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNSSEC](https://developers.cloudflare.com/dns/dnssec/)

  4. /Multi-signer DNSSEC
  5. /Setup



# Set up multi-signer DNSSEC

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin1\. Set up Cloudflare zone Cloudflare as Primary (full setup) Cloudflare as Secondary2\. Set up external provider3\. Set up registrar

This page explains how you can enable [multi-signer DNSSEC](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/) with Cloudflare, using the [model 2](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/#model-2) as described in [RFC 8901 ↗︎](https://www.rfc-editor.org/rfc/rfc8901.html).

## Before you begin

Note that:

  * This process requires that your other DNS provider(s) also support multi-signer DNSSEC.
  * Although you can complete a few steps via the dashboard, currently the whole process can only be completed using the API.
  * Enabling **DNSSEC** and **Multi-signer DNSSEC** on the [**DNS Settings** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings) page only replaces the first step in 1\. Set up Cloudflare zone. You still have to follow the rest of this tutorial to complete the setup.



## 1\. Set up Cloudflare zone

### Cloudflare as Primary (full setup)

If you use Cloudflare as a primary DNS provider, meaning that you manage your DNS records in Cloudflare, do the following:

  1. In the Cloudflare dashboard, go to the **DNS Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings)
  2. Select **Enable DNSSEC** and **Confirm**.




Note

For the purpose of this tutorial, you will update your registrar with the DS record later, in [Step 3](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/#3-set-up-registrar).

  3. Also enable **Multi-signer DNSSEC** and **Multi-provider DNS**.
  4. Go to the [**DNS Records** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/records) page and create the following records at your zone apex (meaning you should use `@` in the record **Name** field): 
     * A [DNSKEY record](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/#ds-and-dnskey) with the zone signing key(s) (ZSKs) of your external provider(s).
     * An [NS record](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/#ns) with your external provider nameservers.



  1. Use the [Edit DNSSEC Status endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/edit/) to enable DNSSEC and activate multi-signer DNSSEC for your zone. Set `status` to `active` and `dnssec_multi_signer` to `true`, as in the following example.



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



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Write`

Create DNS Recordbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
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

  3. Add your external provider(s) nameservers as NS records on your zone apex.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Write`

Create DNS Recordbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"type": "NS",
    		"name": "<ZONE_NAME>",
    		"content": "<NS_DOMAIN>",
    		"ttl": 86400
    	}'

  4. Enable the usage of the nameservers you added in the previous step by using the API request below.



Caution

This step is required. Without turning on this setting, Cloudflare will ignore any `NS` records created on the zone apex. This means that responses to DNS queries made to the zone apex and requesting `NS` records will only contain Cloudflare nameservers.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone DNS Settings Write`
  * `DNS Write`

Update DNS Settingsbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_settings" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"multi_provider": true
    	}'

### Cloudflare as Secondary

If you use Cloudflare as a secondary DNS provider, do the following:

  1. In the Cloudflare dashboard, go to the **DNS Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings)
  2. For **DNSSEC with Secondary DNS** select **Live signing**.




Note

For the purpose of this tutorial, you will update your registrar with the DS record later, in [Step 3](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/#3-set-up-registrar).

  3. Also enable **Multi-signer DNSSEC**.
  4. Add the zone signing key(s) (ZSKs) of your external provider(s) to a DNSKEY record at your primary DNS provider. This record should be transferred successfully to Cloudflare.
  5. Add your external provider(s) nameservers as NS records on your zone apex at your primary DNS provider. These records should be transferred successfully to Cloudflare.



  1. Use the [Edit DNSSEC Status endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/edit/) to enable DNSSEC and activate multi-signer DNSSEC for your zone. Set `status` to `active` and `dnssec_multi_signer` to `true`, as in the following example.



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

  2. Add the ZSK(s) of your external provider(s) to a DNSKEY record at your primary DNS provider. This record should be transferred successfully to Cloudflare.

  3. Add your external provider(s) nameservers as NS records on your zone apex at your primary DNS provider. These records should be transferred successfully to Cloudflare.




## 2\. Set up external provider

  1. Get Cloudflare's ZSK using either the API or a query from one of the assigned Cloudflare nameservers.



API example:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec/zsk" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Command line query example:
    
    
    $ dig <ZONE_NAME> dnskey @<CLOUDFLARE_NAMESERVER> +noall +answer | grep 256

  2. Add Cloudflare's ZSK that you fetched in the previous step to the DNSKEY record set of your external provider(s).
  3. Add Cloudflare's nameservers to the NS record set at your external provider(s).



## 3\. Set up registrar

  1. Add DS records to your registrar, one for each provider. You can see your Cloudflare DS record on the [**DNS Settings** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings) page, under **DS Record**.

  2. Update the nameserver settings at your registrar to include the nameservers of all providers you will be using for your multi-signer DNSSEC setup.




[PreviousAbout](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/)[NextDNSSEC states](https://developers.cloudflare.com/dns/dnssec/dnssec-states/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/dnssec/multi-signer-dnssec/setup.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
