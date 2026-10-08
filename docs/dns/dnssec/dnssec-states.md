---
url: https://developers.cloudflare.com/dns/dnssec/dnssec-states/
title: DNSSEC states \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:56.793255+00:00
---

# DNSSEC states · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/dnssec/dnssec-states/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[DNSSEC](https://developers.cloudflare.com/dns/dnssec/)
  4. /DNSSEC states



# DNSSEC states

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/dnssec/dnssec-states/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This page describes different DNSSEC states and how they relate to the responses you get from the [DNSSEC details API endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/get/).

State | API response | Description  
---|---|---  
Pending | `"status":"pending"`  
`"modified_on":<TIME_STAMP>` | DNSSEC has been enabled but the Cloudflare DS record has not been added at the registrar.  
Active | `"status":"active"`  
`"modified_on":<TIME_STAMP>` | DNSSEC has been enabled and the Cloudflare DS record is present at the registrar.  
Pending-disabled | `"status":"pending-disabled"`  
`"modified_on":<TIME_STAMP>` | DNSSEC has been disabled but the Cloudflare DS record is still added at the registrar.  
Disabled | `"status":"disabled"`  
`"modified_on":<TIME_STAMP>` | DNSSEC has been disabled and the Cloudflare DS record has been removed from the registrar.  
Deleted | `"status":"disabled"`  
`"modified_on": null` | DNSSEC has never been enabled for the zone or DNSSEC has been disabled and then deleted using the [Delete DNSSEC records endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/delete/).  
  
Caution

Once you have enabled DNSSEC on a zone for the first time, you cannot transition directly from an `active` state to a `deleted` state. You can only [delete DNSSEC records](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/delete/) once your zone DNSSEC is in a `disabled` state. Cloudflare prevents you from deleting DNSSEC records before removing the DS record from the registrar to avoid DNS resolution issues.

In both `pending` and `active` states, Cloudflare signs the zone and responds with RRSIG, NSEC, DNSKEY, CDS, and CDNSKEY record types.

In `pending-disabled` and `disabled` states, Cloudflare still signs the zone and serves RRSIG, NSEC, and DNSKEY record types, but the CDS and CDNSKEY records are set to zero ([RFC 8078 ↗︎](https://www.rfc-editor.org/rfc/rfc8078.html#section-4)), signaling to the registrar that DNSSEC should be disabled.

In `deleted` state, Cloudflare does **not** sign the zone and does **not** respond with RRSIG, NSEC, DNSKEY, CDS, and CDNSKEY record types.

Refer to [How DNSSEC works ↗︎](https://www.cloudflare.com/dns/dnssec/how-dnssec-works/) to learn more about the authentication process and records involved.

[PreviousSetup](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/)[NextMigration tutorial](https://developers.cloudflare.com/dns/dnssec/dnssec-active-migration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/dnssec/dnssec-states.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
