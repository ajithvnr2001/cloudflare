---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/examples/
title: Common API calls \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:44.504510+00:00
---

# Common API calls · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/examples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systemsAPI configuration

  4. /[Advanced DNS Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/)
  5. /Common API calls



# Common API calls

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/examples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet all DNS protection rules Create DNS protection rule Update DNS protection rule

The following sections contain example requests for common API calls. For a list of available API endpoints, refer to [Endpoints](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/#endpoints).

## Get all DNS protection rules

The following example retrieves the currently configured rules for Advanced DNS Protection.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules" \
    --header "Authorization: Bearer <API_TOKEN>"
    
    
    ---
    {
      "result": [
        {
          "id": "<RULE_ID>",
          "scope": "<SCOPE>",
          "name": "<NAME>",
          "mode": "<MODE>",
          "profile_sensitivity": "<SENSITIVITY>",
          "rate_sensitivity": "<RATE>",
          "burst_sensitivity": "<BURST>",
          "created_on": "2023-10-01T13:10:38.762503+01:00",
          "modified_on": "2023-10-01T13:10:38.762503+01:00",
          }
        ],
      "success": true,
      "errors": [],
      "messages": []
    }

### Create DNS protection rule

The following example creates an Advanced DNS Protection rule with a global scope.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --data '{
      "scope": "global",
      "name": "global",
      "mode": "<MODE>",
      "rate_sensitivity": "<RATE>",
      "burst_sensitivity": "<BURST>",
      "profile_sensitivity": "<SENSITIVITY>"
    }'
    
    
    {
      "result": {
        "id": "<RULE_ID>",
        "scope": "global",
        "name": "global",
        "mode": "<MODE>",
        "rate_sensitivity": "<RATE>",
        "burst_sensitivity": "<BURST>",
        "profile_sensitivity": "<SENSITIVITY>",
        "created_on": "2023-10-01T13:10:38.762503+01:00",
        "modified_on": "2023-10-01T13:10:38.762503+01:00",
      },
      "success": true,
      "errors": [],
      "messages": []
    }

Refer to [JSON objects](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/json-objects/) for more information on the fields in the JSON body.

### Update DNS protection rule

The following example updates an existing DNS protection rule with ID `{rule_id}`.

The request body can contain only the fields you want to update (from `mode`, `profile_sensitivity`, `rate_sensitivity`, and `burst_sensitivity`).

Requestbash
    
    
    curl --request PATCH \
    "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --data '{
      "mode": "<NEW_MODE>",
      "profile_sensitivity": "<NEW_SENSITIVITY>",
      "rate_sensitivity": "<NEW_RATE>",
      "burst_sensitivity": "<NEW_BURST>"
    }'
    
    
    {
      "result": {
        "id": "<RULE_ID>",
        "scope": "<SCOPE>",
        "name": "<NAME>",
        "mode": "<NEW_MODE>",
        "profile_sensitivity": "<NEW_SENSITIVITY>",
        "rate_sensitivity": "<NEW_RATE>",
        "burst_sensitivity": "<NEW_BURST>",
        "created_on": "2023-10-01T13:10:38.762503+01:00",
        "modified_on": "2023-10-01T13:10:38.762503+01:00",
      },
      "success": true,
      "errors": [],
      "messages": []
    }

Refer to [JSON objects](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/json-objects/) for more information on the fields in the JSON body.

[PreviousConfigure via the API](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/)[NextJSON objects](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/json-objects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/api/dns-protection/examples.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
