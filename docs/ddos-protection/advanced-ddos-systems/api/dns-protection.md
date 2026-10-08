---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/
title: Configure Advanced DNS Protection via API \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:44.609301+00:00
---

# Configure Advanced DNS Protection via API · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systems

  4. /API configuration
  5. /Advanced DNS Protection



# Advanced DNS Protection

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpoints

Use the [Cloudflare API](https://developers.cloudflare.com/api/) to configure Advanced DNS Protection via API.

For examples of API calls, refer to [Common API calls](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/examples/).

## Endpoints

To obtain the complete endpoint, append the Advanced DNS Protection API endpoints listed below to the Cloudflare API base URL:
    
    
    https://api.cloudflare.com/client/v4

The `{account_id}` argument is the [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) (a hexadecimal string). You can find this value in the Cloudflare dashboard.

The following table summarizes the available operations.

Operation | Verb + Endpoint  
---|---  
List DNS protection rules | `GET accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules`Fetches all DNS protection rules in the account.  
Add a DNS protection rule | `POST accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules`Adds a DNS protection rule to the account.  
Get a DNS protection rule | `GET accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}`Fetches the details of an existing DNS protection rule in the account.  
Update a DNS protection rule | `PATCH accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}`Updates an existing DNS protection rule in the account.  
Delete a DNS protection rule | `DELETE accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}`Deletes an existing DNS protection rule from the account.  
Delete all DNS protection rules | `DELETE accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules`Deletes all existing DNS protection rules from the account.  
  
[PreviousExclude a prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix/)[NextCommon API calls](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/api/dns-protection/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
