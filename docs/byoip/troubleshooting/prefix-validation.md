---
url: https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/
title: Troubleshoot prefix validation \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:40.339472+00:00
---

# Troubleshoot prefix validation · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /[Troubleshooting](https://developers.cloudflare.com/byoip/troubleshooting/)
  4. /Prefix validation checks



# Troubleshoot prefix validation

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

  1. Use the [Prefix Details endpoint](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/get/) to check if any issues were found during validation.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Magic Transit Read`
     * `Magic Transit Write`
     * `IP Prefixes: Write`
     * `IP Prefixes: Read`
     * `IP Prefixes: BGP On Demand Write`
     * `IP Prefixes: BGP On Demand Read`
Prefix Detailsbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/prefixes/$PREFIX_ID" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Responsejson
    
     "result": {
        "id": "72823e95d6c64d48a8111fec81179816",
        "created_at": "2025-02-25T00:34:11.423722Z",
        "modified_at": "2025-02-25T00:34:11.423722Z",
        "cidr": "203.0.113.0/24",
        "account_id": "654c5f71c324478cc9f68d60065d4620",
        "description": "",
        "approved": "P",
        "on_demand_enabled": false,
        "on_demand_locked": false,
        "advertised": null,
        "advertised_modified_at": null,
        "loa_document_id": "b9ff4afe312246a8b2e7324d98f40b23",
        "asn": 13335,
        "ownership_validation_token": "<OWNERSHIP_VALIDATION_TOKEN>",
        "delegate_loa_creation" : true,
        "irr_validation_state": "valid",
        "rpki_validation_state": "valid",
        "ownership_validation_state": "missing",
      }

  2. Consider the states returned in the API response (for example, `missing`, `invalid`, `mismatch_asn`) and review your IRR record, ROA, and ownership validation method accordingly.

     * Information in the IRR and ROA records should meet the [onboarding prerequisites](https://developers.cloudflare.com/byoip/get-started/#before-you-begin).

     * [Ownership validation](https://developers.cloudflare.com/byoip/get-started/#validate-prefix-ownership) requires a matching ROA and the correct validation token found in all DNS TXT records or in the IRR record.

  3. After applying the necessary changes, use the Validate Prefix endpoint to trigger the validation checks.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Magic Transit Write`
     * `IP Prefixes: Write`
Validate Prefixbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/prefixes/$PREFIX_ID/validate" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"




[PreviousGeneral](https://developers.cloudflare.com/byoip/troubleshooting/)[NextGlossary](https://developers.cloudflare.com/byoip/glossary/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/troubleshooting/prefix-validation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
