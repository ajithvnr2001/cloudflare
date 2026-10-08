---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/
title: DNSSEC for Secondary DNS \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.976345+00:00
---

# DNSSEC for Secondary DNS · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)

  4. /[Cloudflare as Secondary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/)
  5. /DNSSEC options



# DNSSEC options

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up multi-signer DNSSECSet up live signing DNSSECSet up pre-signed DNSSEC Prerequisites StepsTroubleshoot pre-signed DNSSEC Verify that Cloudflare is serving pre-signed records If Cloudflare is live-signing instead of serving pre-signed records

[DNS Security Extensions (DNSSEC) ↗︎](https://www.cloudflare.com/learning/dns/dns-security/) increase security by adding cryptographic signatures to DNS records. When you use multiple providers and Cloudflare is secondary, you have a few options to enable DNSSEC for records served by Cloudflare.

  * **[Multi-signer DNSSEC](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/)** : Both Cloudflare and your primary DNS provider know the signing keys of each other and perform their own live-signing of DNS records, in accordance with [RFC 8901 ↗︎](https://www.rfc-editor.org/rfc/rfc8901.html).
  * **Live signing** : If your domain is not delegated to your primary provider's nameservers and Cloudflare secondary nameservers are the only nameservers authoritatively responding to DNS queries (hidden primary setup), you can choose this option to allow Cloudflare to perform live-signing of your DNS records.
  * **Pre-signed** : Your primary DNS provider signs records and transfers out the signatures. Cloudflare then serves these records and signatures as is, without doing any signing. By default, Cloudflare uses [NSEC records ↗︎](https://www.cloudflare.com/dns/dnssec/how-dnssec-works/) and not NSEC3 - refer to [NSEC3 support](https://developers.cloudflare.com/dns/dnssec/enable-nsec3/) if needed. Also, Pre-signed DNSSEC does not support [Secondary DNS Overrides](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/) nor [Load Balancing](https://developers.cloudflare.com/load-balancing/).



* * *

## Set up multi-signer DNSSEC

Refer to [Set up multi-signer DNSSEC](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/) and follow the instructions, considering the note about Cloudflare as Secondary.

* * *

## Set up live signing DNSSEC

If you use Cloudflare secondary nameservers as the only nameservers authoritatively responding to DNS queries (hidden primary setup), you can enable live signing DNSSEC to have Cloudflare sign the records for your zone.

In this setup, DNSSEC on your primary DNS provider does not need to be enabled.

  1. In the Cloudflare dashboard, go to the **DNS Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings)
  2. Under **DNSSEC with Secondary DNS** select **Live signing**. You will then have access to several necessary values to create a **DS** record at your registrar.

  3. Add the **DS** record to your registrar. If Algorithm 13 - Cloudflare's preferred cipher choice - is not listed by your registrar, it may also be called _ECDSA Curve P-256 with SHA-256_.

Provider-specific DNSSEC instructions

This is not an exhaustive list, but the following links may be helpful:

     * [DNSimple ↗︎](https://support.dnsimple.com/articles/cloudflare-ds-record/)
     * [Domaindiscount24 ↗︎](https://support.domaindiscount24.com/hc/articles/4409759478161)
     * [DreamHost ↗︎](https://help.dreamhost.com/hc/en-us/articles/219539467)
     * [Dynadot ↗︎](https://www.dynadot.com/help/question/set-DNSSEC)
     * [Enom ↗︎](https://support.enom.com/support/solutions/articles/201000065386)
     * [Gandi ↗︎](https://docs.gandi.net/en/domain_names/advanced_users/dnssec.html)
     * [GoDaddy ↗︎](https://www.godaddy.com/help/add-a-ds-record-23865)
     * [Hostinger ↗︎](https://www.hostinger.com/support/3667267-how-to-use-dnssec-records-at-hostinger/)
     * [Hover ↗︎](https://support.hover.com/support/solutions/articles/201000064716)
     * [Infomaniak ↗︎](https://faq.infomaniak.com/2187)
     * [InMotion Hosting ↗︎](https://www.inmotionhosting.com/support/edu/cpanel/enable-dnssec-cloudflare/)
     * [INWX ↗︎](https://kb.inwx.com/en-us/3-nameserver/131)
     * [Joker.com ↗︎](https://joker.com/faq/books/jokercom-faq-en/page/dnssec)
     * [Name.com ↗︎](https://www.name.com/support/articles/205439058-managing-dnssec)
     * [Namecheap ↗︎](https://www.namecheap.com/support/knowledgebase/article.aspx/9722/2232/managing-dnssec-for-domains-pointed-to-custom-dns/)
     * [NameISP ↗︎](https://support.nameisp.com/knowledgebase/dns)
     * [Namesilo ↗︎](https://www.namesilo.com/support/v2/articles/domain-manager/ds-records)
     * [OVH ↗︎](https://help.ovhcloud.com/csm/en-dns-secure-domain-dnssec?id=kb_article_view&sysparm_article=KB0051637)
     * [Squarespace ↗︎](https://support.squarespace.com/hc/articles/4404183898125-Nameservers-and-DNSSEC-for-Squarespace-managed-domains#toc-dnssec)
     * [Registro.br ↗︎](https://registro.br/tecnologia/dnssec/?secao=tutoriais-dns)
     * [Porkbun ↗︎](https://kb.porkbun.com/article/93-how-to-install-dnssec) (do not fill out **keyData**)
     * [TransIP ↗︎](https://www.transip.eu/knowledgebase/150-secure-domains-custom-nameservers-dnssec/)



  1. Use the [Edit DNSSEC Status endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/edit/) and set a `status` of `active` for your zone.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Write`

Edit DNSSEC Statusbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dnssec" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"status": "active"
    	}'

  2. Use the [DNSSEC Details endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/get/) to get the necessary values to create a **DS** record at your registrar.

  3. Add the **DS** record to your registrar. If Algorithm 13 - Cloudflare's preferred cipher choice - is not listed by your registrar, it may also be called _ECDSA Curve P-256 with SHA-256_.

Provider-specific DNSSEC instructions

This is not an exhaustive list, but the following links may be helpful:

     * [DNSimple ↗︎](https://support.dnsimple.com/articles/cloudflare-ds-record/)
     * [Domaindiscount24 ↗︎](https://support.domaindiscount24.com/hc/articles/4409759478161)
     * [DreamHost ↗︎](https://help.dreamhost.com/hc/en-us/articles/219539467)
     * [Dynadot ↗︎](https://www.dynadot.com/help/question/set-DNSSEC)
     * [Enom ↗︎](https://support.enom.com/support/solutions/articles/201000065386)
     * [Gandi ↗︎](https://docs.gandi.net/en/domain_names/advanced_users/dnssec.html)
     * [GoDaddy ↗︎](https://www.godaddy.com/help/add-a-ds-record-23865)
     * [Hostinger ↗︎](https://www.hostinger.com/support/3667267-how-to-use-dnssec-records-at-hostinger/)
     * [Hover ↗︎](https://support.hover.com/support/solutions/articles/201000064716)
     * [Infomaniak ↗︎](https://faq.infomaniak.com/2187)
     * [InMotion Hosting ↗︎](https://www.inmotionhosting.com/support/edu/cpanel/enable-dnssec-cloudflare/)
     * [INWX ↗︎](https://kb.inwx.com/en-us/3-nameserver/131)
     * [Joker.com ↗︎](https://joker.com/faq/books/jokercom-faq-en/page/dnssec)
     * [Name.com ↗︎](https://www.name.com/support/articles/205439058-managing-dnssec)
     * [Namecheap ↗︎](https://www.namecheap.com/support/knowledgebase/article.aspx/9722/2232/managing-dnssec-for-domains-pointed-to-custom-dns/)
     * [NameISP ↗︎](https://support.nameisp.com/knowledgebase/dns)
     * [Namesilo ↗︎](https://www.namesilo.com/support/v2/articles/domain-manager/ds-records)
     * [OVH ↗︎](https://help.ovhcloud.com/csm/en-dns-secure-domain-dnssec?id=kb_article_view&sysparm_article=KB0051637)
     * [Squarespace ↗︎](https://support.squarespace.com/hc/articles/4404183898125-Nameservers-and-DNSSEC-for-Squarespace-managed-domains#toc-dnssec)
     * [Registro.br ↗︎](https://registro.br/tecnologia/dnssec/?secao=tutoriais-dns)
     * [Porkbun ↗︎](https://kb.porkbun.com/article/93-how-to-install-dnssec) (do not fill out **keyData**)
     * [TransIP ↗︎](https://www.transip.eu/knowledgebase/150-secure-domains-custom-nameservers-dnssec/)



* * *

## Set up pre-signed DNSSEC

### Prerequisites

  * Your secondary zone in Cloudflare already exists and zone transfers from your primary DNS provider are working correctly.
  * You have considered whether your primary DNS provider uses NSEC or NSEC3, and have enabled [NSEC3 support](https://developers.cloudflare.com/dns/dnssec/enable-nsec3/) if needed.
  * Your primary DNS provider transfers out DNSSEC related records, such as RRSIG, DNSKEY, and NSEC.



### Steps

  1. Enable DNSSEC at your primary DNS provider.
  2. Enable DNSSEC for your zone at Cloudflare, using either the Dashboard or the API.



Caution

Pre-signed DNSSEC does not support [Secondary DNS Overrides](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/) nor [Load Balancing](https://developers.cloudflare.com/load-balancing/). Once you enable pre-signed DNSSEC, Cloudflare will treat all your DNS records as DNS-only.

  1. In the Cloudflare dashboard, go to the **DNS Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings)
  2. Under **DNSSEC with Secondary DNS** select **Pre-signed**.




Use the [Edit DNSSEC Status endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/edit/) and set the `dnssec_presigned` value to `true`.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Write`

Edit DNSSEC Statusbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dnssec" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"dnssec_presigned": true
    	}'

  3. Make sure Cloudflare nameservers are added at your registrar. You can see your Cloudflare nameservers on the dashboard by going to the [**DNS Records** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/records) page.

  4. Make sure there is a DS record added at your registrar. The DS record is obtained from your primary DNS provider (the signer of the zone) and is what indicates to DNS resolvers that your zone has DNSSEC enabled.




* * *

## Troubleshoot pre-signed DNSSEC

### Verify that Cloudflare is serving pre-signed records

After completing setup, confirm that Cloudflare is serving the pre-signed signatures from your primary rather than signing the zone itself.

Query `DNSKEY` against one of your assigned Cloudflare secondary nameservers:
    
    
    dig DNSKEY example.com @<cloudflare-secondary-ns>

Compare the key tag in the response with the key tag served by your primary nameserver. If the key tags match, Cloudflare is correctly serving the pre-signed records. If the key tags differ, Cloudflare is live-signing the zone with its own keys instead.

### If Cloudflare is live-signing instead of serving pre-signed records

Check each of the following:

  * **`dnssec_presigned` is set to `true`**: Use the [DNSSEC Details endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/get/) to confirm the value in the API response.
  * **Zone transfers include DNSSEC records** : The AXFR from your primary must include `DNSKEY`, `RRSIG`, and `NSEC` (or `NSEC3`) records alongside the regular DNS records. If your primary is configured to transfer only non-DNSSEC records, Cloudflare has no signatures to serve. Confirm by requesting a manual zone transfer from your primary and checking that `DNSKEY` and `RRSIG` records are present in the transferred data.
  * **Zone transfers are completing successfully** : Review your [zone transfer alerts](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/) to confirm that recent transfers from your primary have completed without error.



If all three checks pass but Cloudflare is still live-signing — or if a sibling zone with the same configuration works correctly while this zone does not — [contact Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) and include your zone ID and the output of the [DNSSEC Details endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/get/).

[PreviousProxy traffic](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/)[NextAlerts](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
