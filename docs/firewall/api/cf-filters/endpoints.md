---
url: https://developers.cloudflare.com/firewall/api/cf-filters/endpoints/
title: Endpoints - Filters \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.821877+00:00
---

# Endpoints - Filters · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-filters/endpoints/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/)
  5. /Endpoints



# Endpoints

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/endpoints/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To invoke a Cloudflare Filters API operation, append the endpoint to the Cloudflare API base URL:
    
    
    https://api.cloudflare.com/client/v4/

For authentication instructions, refer to [Getting Started: Requests](https://developers.cloudflare.com/fundamentals/api/) in the Cloudflare API documentation.

For help with endpoints and pagination, refer to [Getting Started: Endpoints](https://developers.cloudflare.com/fundamentals/api/).

Note

The Filters API endpoints require a value for `<ZONE_ID>`.

To retrieve a list of zones associated with your account, use the [List Zones](https://developers.cloudflare.com/api/resources/zones/methods/list/) operation and note the Zone ID associated with the domain for which you want to manage filters.

The Cloudflare Filters API supports the operations outlined below. Visit the pages in this section for examples.

Operation| Method & Endpoint| Notes  
---|---|---  
[Create filters](https://developers.cloudflare.com/api/resources/filters/methods/create/)| `POST zones/<ZONE_ID>/filters`| Handled as a single transaction. If there is an error, the entire operation fails.  
[Get filters](https://developers.cloudflare.com/api/resources/filters/methods/list/)| `GET zones/<ZONE_ID>/filters`| Lists all current filters. Results return paginated with 25 items per page by default. Use optional parameters to narrow results.  
[Get a filter](https://developers.cloudflare.com/api/resources/filters/methods/get/)| `GET zones/<ZONE_ID>/filters/<FILTER_ID>`| Retrieve a single filter by ID.  
[Update filters](https://developers.cloudflare.com/api/resources/filters/methods/bulk_update/)| `PUT zones/<ZONE_ID>/filters`| Handled as a single transaction. All filters must exist for operation to succeed. If there is an error, the entire operation fails.  
[Update a filter](https://developers.cloudflare.com/api/resources/filters/methods/update/)| `PUT zones/<ZONE_ID>/filters/<FILTER_ID>`| Update a single filter by ID.  
[Delete filters](https://developers.cloudflare.com/api/resources/filters/methods/bulk_delete/)| `DELETE zones/<ZONE_ID>/filters`| Delete existing filters. Must specify list of filter IDs.Empty requests result in no deletion. Returns HTTP status code 200 if a specified filter does not exist.  
[Delete a filter](https://developers.cloudflare.com/api/resources/filters/methods/delete/)| `DELETE zones/<ZONE_ID>/filters/<FILTER_ID>`| Delete a filter by ID.  
  
[PreviousJSON object](https://developers.cloudflare.com/firewall/api/cf-filters/json-object/)[NextPOST example](https://developers.cloudflare.com/firewall/api/cf-filters/post/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-filters/endpoints.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
