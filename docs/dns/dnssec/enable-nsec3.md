---
url: https://developers.cloudflare.com/dns/dnssec/enable-nsec3/
title: NSEC3 support \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:56.885489+00:00
---

# NSEC3 support · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/dnssec/enable-nsec3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[DNSSEC](https://developers.cloudflare.com/dns/dnssec/)
  4. /NSEC3 support



# NSEC3 support

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/dnssec/enable-nsec3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable NSEC3 Pre-signed DNSSECVerify NSEC3 is in use Non-existent zone name Non-existent record type at an existing nameAvailability

As explained in [our blog ↗︎](https://blog.cloudflare.com/black-lies/), Cloudflare's implementation of negative answers with NSEC is protected against zone walking1. This implementation, also referred to as Compact Denial of Existence ([RFC 9824 ↗︎](https://www.rfc-editor.org/rfc/rfc9824.html)), removes the need for NSEC3 and is significantly more efficient.

However, if you must use NSEC3 for compliance reasons, you can enable it as explained below.

## Enable NSEC3

Use the [Edit DNSSEC Status endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/edit/), setting `status` to `active` and `dnssec_use_nsec3` to `true`. You should replace the values started by `$` with your zone ID and authentication credentials. To learn more about using the Cloudflare API, refer to [Fundamentals](https://developers.cloudflare.com/fundamentals/api/get-started/).

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Write`

Edit DNSSEC Statusbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dnssec" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"dnssec_use_nsec3": true,
    		"status": "active"
    	}'

### Pre-signed DNSSEC

If you use Cloudflare as a secondary DNS provider with [pre-signed DNSSEC](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/), setting `dnssec_use_nsec3` to `true` means that Cloudflare will use NSEC3 records as transferred in from your primary DNS provider.

Otherwise, NSEC3 records will be generated and signed at request time.

## Verify NSEC3 is in use

To validate that NSEC3 is being used, consider the following scenarios:

### Non-existent zone name

A command like the following would trigger a signed negative response using NSEC3 for proof of non-existence. Look for NSEC3 records under the `Authority Section` of the response.
    
    
    dig +dnssec doesnotexist.example.com

### Non-existent record type at an existing name

If the name `www` exists but the type TXT does not, the example below would trigger a signed NODATA response using NSEC3. Look for NSEC3 records under the `Authority Section` of the response.
    
    
    dig +dnssec www.example.com TXT

## Availability

NSEC3 is only available for zones on the Enterprise plan.

## Footnotes

  1. A method where an attacker exploits NSEC negative answers to obtain all names in a given zone. This is possible when such negative answers provide information on the previous and next names in a chain. ↩




[PreviousMigration tutorial](https://developers.cloudflare.com/dns/dnssec/dnssec-active-migration/)[NextValidation and keys](https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/dnssec/enable-nsec3.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
