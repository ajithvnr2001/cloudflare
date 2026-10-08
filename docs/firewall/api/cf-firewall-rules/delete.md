---
url: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/delete/
title: DELETE examples - Firewall rules \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:16.285270+00:00
---

# DELETE examples - Firewall rules · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/delete/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Firewall Rules API](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/)
  5. /DELETE examples



# DELETE examples

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/delete/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDelete multiple rulesDelete a single rule

Note

The `DELETE` operation does not delete any filter related to the firewall rule. To delete the filter, use the [Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/).

## Delete multiple rules

This example deletes firewall rules with IDs `{rule_id_1}` and `{rule_id_2}`.

Requestbash
    
    
    curl --request DELETE \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules?id={rule_id_1}&id={rule_id_2}" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
    	"result": [
    		{
    			"id": "<RULE_ID_1>"
    		},
    		{
    			"id": "<RULE_ID_2>"
    		}
    	],
    	"success": true,
    	"errors": [],
    	"messages": []
    }

## Delete a single rule

This example deletes the rule with ID `{rule_id}`.

Requestbash
    
    
    curl --request DELETE \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules/{rule_id}" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
    	"result": [
    		{
    			"id": "<RULE_ID>"
    		}
    	],
    	"success": true,
    	"errors": [],
    	"messages": []
    }

[PreviousPUT examples](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/put/)[NextOverview](https://developers.cloudflare.com/firewall/api/cf-filters/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-firewall-rules/delete.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
