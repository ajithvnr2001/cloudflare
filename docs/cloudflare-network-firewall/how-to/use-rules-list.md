---
url: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-rules-list/
title: Define an IP list \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:07.723500+00:00
---

# Define an IP list · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-rules-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /How to
  4. /Use IP lists



# Use IP lists

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-rules-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Create a new IP list.2\. Add IPs to the list3\. Use the list in a ruleManaged lists

[IP lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#ip-lists) are a part of Cloudflare's custom lists. Custom lists contain one or more items of the same type — IP addresses, hostnames or ASNs — that you can reference in rule expressions.

IP lists are defined at the account level and can be used to match against `ip.src` and `ip.dst` fields. Currently, Cloudflare Network Firewall (formerly Magic Firewall) only supports IPv4 addresses in these lists, not IPv6.

To use this feature:

## 1\. Create a [new IP list](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/create/).

For example:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rules/lists \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      "name": "iplist",
      "description": "This contains IPs that should be allowed.",
      "kind": "ip"
    }'

## 2\. Add IPs to the list

Next, [create list items](https://developers.cloudflare.com/api/resources/rules/subresources/lists/subresources/items/methods/create/). This will add elements to the current list.
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rules/lists/{list_id}/items \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '[
      {"ip":"10.0.0.1"},
      {"ip":"10.10.0.0/24"}
    ]'

## 3\. Use the list in a rule

Finally, add a Network Firewall rule referencing the list into an existing ruleset:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/rules \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "action": "skip",
      "action_parameters": {
        "ruleset": "current"
      },
      "expression": "ip.src in $iplist",
      "description": "Allowed IPs from iplist",
      "enabled": true
    }'

## Managed lists

Note

Available for customers with a Cloudflare Network Firewall Advanced plan.

You can create rules with managed lists. Managed IP Lists are [lists of IP addresses](https://developers.cloudflare.com/waf/tools/lists/managed-lists/#managed-ip-lists) maintained by Cloudflare and updated frequently.

You can access these managed lists when you create rules with either _IP destination address_ or _IP source address_ in the **Field** dropdown, and _is in list_ or _is not in list_ in the **Operator** dropdown.

For example:

Field | Operator | Value  
---|---|---  
_IP destination address_ | _is in list_ | _Anonymizers_  
  
[PreviousForm expressions](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/form-expressions/)[NextAdd custom policies](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/how-to/use-rules-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
