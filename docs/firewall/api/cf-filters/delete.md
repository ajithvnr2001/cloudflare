---
url: https://developers.cloudflare.com/firewall/api/cf-filters/delete/
title: DELETE examples - Filters \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.799052+00:00
---

# DELETE examples - Filters · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-filters/delete/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/)
  5. /DELETE examples



# DELETE examples

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/delete/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDelete multiple filtersDelete a single filter

## Delete multiple filters

This example deletes filters with IDs `{filter_id_1}` and `{filter_id_2}`.

Requestbash
    
    
    curl --request DELETE \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters?id={filter_id_1}&id={filter_id_2}" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
      "result": [
        {
          "id": "<FILTER_ID_1>"
        },
        {
          "id": "<FILTER_ID_2>"
        }
      ],
      "success": true,
      "errors": [],
      "messages": []
    }

## Delete a single filter

This example deletes a single filter with ID `{filter_id}`.

Requestbash
    
    
    curl --request DELETE \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/filters/{filter_id}" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
      "result": [
        {
          "id": "<FILTER_ID>"
        }
      ],
      "success": true,
      "errors": [],
      "messages": []
    }

[PreviousPUT examples](https://developers.cloudflare.com/firewall/api/cf-filters/put/)[NextExpression validation](https://developers.cloudflare.com/firewall/api/cf-filters/validation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-filters/delete.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
