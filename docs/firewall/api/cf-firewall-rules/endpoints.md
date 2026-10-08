---
url: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/
title: Endpoints - Firewall rules \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:16.309833+00:00
---

# Endpoints - Firewall rules · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Firewall Rules API](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/)
  5. /Endpoints



# Endpoints

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To invoke a Cloudflare Firewall Rules API operation, append the endpoint to the Cloudflare API base URL:
    
    
    https://api.cloudflare.com/client/v4/

For authentication instructions, refer to [Getting Started: Requests](https://developers.cloudflare.com/fundamentals/api/) in the Cloudflare API documentation.

For help with endpoints and pagination, refer to [Getting Started: Endpoints](https://developers.cloudflare.com/fundamentals/api/).

Note

The Firewall Rules API endpoints require a value for `<ZONE_ID>`.

To retrieve a list of zones associated with your account, use the [List Zones](https://developers.cloudflare.com/api/resources/zones/methods/list/) operation and note the zone ID associated with the domain whose firewall rules you want to manage.

The Cloudflare Firewall Rules API supports the operations outlined below. Visit the pages in this section for examples.

Operation| Method & Endpoint| Notes  
---|---|---  
[Create firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/create/)| `POST zones/<ZONE_ID>/firewall/rules`| Handled as a single transaction. If there is an error, the entire operation fails.  
[List firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/list/)| `GET zones/<ZONE_ID>/firewall/rules`| Lists all current firewall rules. Results return paginated with 25 items per page by default. Use optional parameters to narrow results.  
[Get a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/get/)| `GET zones/<ZONE_ID>/firewall/rules/<RULE_ID>`| Retrieve a single firewall rule by ID.  
[Update firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/bulk_update/)| `PUT zones/<ZONE_ID>/firewall/rules`| Handled as a single transaction. All rules must exist for operation to succeed. If there is an error, the entire operation fails.  
[Update a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/update/)| `PUT zones/<ZONE_ID>/firewall/rules/<RULE_ID>`| Update a single firewall rule by ID.  
[Delete firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/bulk_delete/)| `DELETE zones/<ZONE_ID>/firewall/rules`| Delete existing firewall rules. Must specify list of firewall rule IDs.Empty requests result in no deletion. Returns HTTP status code 200 if a specified rule does not exist.  
[Delete a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/delete/)| `DELETE zones/<ZONE_ID>/firewall/rules/<RULE_ID>`| Delete a firewall rule by ID.  
  
[PreviousJSON object](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/json-object/)[NextPOST example](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/post/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-firewall-rules/endpoints.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
