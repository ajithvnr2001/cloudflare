---
url: https://developers.cloudflare.com/cloudflare-one/reusable-components/use-rules-list/
title: Define an IP list \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:51.244407+00:00
---

# Define an IP list · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/reusable-components/use-rules-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /Reusable components
  4. /Use IP lists



# Use IP lists

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/reusable-components/use-rules-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Create a new IP list.2\. Add IPs to the list3\. Use the list in a ruleManaged listsList types Threat intelligence IP lists Geo-blocking

[IP lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#ip-lists) are a part of Cloudflare's custom lists. Custom lists contain one or more items of the same type — IP addresses, hostnames or ASNs — that you can reference in rule expressions.

IP lists are defined at the account level and can be used to match against `ip.src` and `ip.dst` fields. Currently, Cloudflare Network Firewall only supports IPv4 addresses in these lists, not IPv6.

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

Finally, add a Cloudflare Network Firewall rule referencing the list into an existing ruleset:
    
    
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
  
## List types

### Threat intelligence

Cloudflare handles millions of HTTP requests each second and blocks billions of cyber threats each day. Cloudflare uses that data to detect malicious actors on the Internet and turns that information into a list of known malicious IP addresses. Cloudflare also integrates with a number of third-party vendors to augment the coverage.

The threat intelligence feed categories are described in [Managed IP Lists](https://developers.cloudflare.com/waf/tools/lists/managed-lists/#managed-ip-lists). All of these lists are compatible with Cloudflare Network Firewall.

### IP lists

Use [IP lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#ip-lists) to group services in networks, like web servers, or for lists of known bad IP addresses to make managing good network endpoints easier. IP lists are helpful for users with very expansive firewall rules with many IP lists. By default, you can add up to 10,000 IPs across all lists. Refer to [Use an IP list](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/add-policies/#use-an-ip-list) to check an example of how to use an IP list.

### Geo-blocking

Geo-blocking enables you to selectively allow or block traffic to any country. Refer to [Block a country](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/add-policies/#block-a-country) to check an example of how to block a country.

[PreviousTags](https://developers.cloudflare.com/cloudflare-one/reusable-components/tags/)[NextBlock page](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/gateway-block-page/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/reusable-components/use-rules-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
