---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/
title: Configure Programmable Flow Protection via API \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:44.660492+00:00
---

# Configure Programmable Flow Protection via API · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systems

  4. /API configuration
  5. /Programmable Flow Protection



# Programmable Flow Protection

Last updated Jun 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpoints Program operations Rule operations Debug operationsPagination

Use the [Cloudflare API](https://developers.cloudflare.com/api/) to configure Programmable Flow Protection.

For examples of API calls, refer to [Common API calls](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples/).

## Endpoints

To obtain the complete endpoint, append the Programmable Flow Protection API endpoints listed below to the Cloudflare API base URL:
    
    
    https://api.cloudflare.com/client/v4

The `{account_id}` argument is the [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) (a hexadecimal string). You can find this value in the Cloudflare dashboard.

The tables in the following sections summarize the available operations.

### Program operations

Operation | Method and endpoint / Description  
---|---  
List programs | `GET accounts/{account_id}/magic/programmable_flow_protection/configs/programs`Fetches all Programmable Flow Protection programs in the account.  
Upload a program | `POST accounts/{account_id}/magic/programmable_flow_protection/configs/programs`Uploads a new program to the account. Include the optional `X-Program-Name` header to specify a human-readable program name. If omitted, the API generates a UUID as the program name.  
Get a program | `GET accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}`Fetches the details of an existing program.  
Update a program | `PATCH accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}`Updates an existing program.  
Delete a program | `DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}`Deletes an existing program from the account.  
Delete all programs | `DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/programs`Deletes all existing programs from the account.  
  
### Rule operations

Operation | Method and endpoint / Description  
---|---  
List rules | `GET accounts/{account_id}/magic/programmable_flow_protection/configs/rules`Fetches all Programmable Flow Protection rules in the account.  
Create a rule | `POST accounts/{account_id}/magic/programmable_flow_protection/configs/rules`Creates a new rule in the account.  
Get a rule | `GET accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}`Fetches the details of an existing rule.  
Update a rule | `PATCH accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}`Updates an existing rule in the account.  
Delete a rule | `DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}`Deletes an existing rule from the account.  
Delete all rules | `DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/rules`Deletes all existing rules from the account.  
  
### Debug operations

Operation | Method and endpoint / Description  
---|---  
Debug with PCAP | `POST accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}/pcap`Runs a program against a PCAP file and returns an annotated PCAP with program verdicts.  
  
## Pagination

The API operations that return a list of items use pagination. For more information on the available pagination query parameters, refer to [Pagination](https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/#pagination).

[PreviousJSON objects](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/tcp-protection/json-objects/)[NextCommon API calls](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
