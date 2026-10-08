---
url: https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/
title: Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:21.350571+00:00
---

# Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 2, 2025

## Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting **December 1, 2025** , list endpoints for the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/) and [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.

No action is required if you already explicitly set `is_deleted=false` or if you only need to list active resources.

This change affects the following API endpoints:

  * List all tunnels: [`GET /accounts/{account_id}/tunnels`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/methods/list/)
  * List [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/): [`GET /accounts/{account_id}/cfd_tunnel`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/)
  * List [WARP Connector](https://developers.cloudflare.com/mesh/) tunnels: [`GET /accounts/{account_id}/warp_connector`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/)
  * List tunnel routes: [`GET /accounts/{account_id}/teamnet/routes`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/)
  * List subnets: [`GET /accounts/{account_id}/zerotrust/subnets`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/)
  * List virtual networks: [`GET /accounts/{account_id}/teamnet/virtual_networks`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/)



#### What is changing?

The default behavior of the `is_deleted` query parameter will be updated.

Scenario | Previous behavior (before December 1, 2025) | New behavior (from December 1, 2025)  
---|---|---  
`is_deleted` parameter is omitted | Returns **active & deleted** tunnels, routes, subnets and virtual networks | Returns **only active** tunnels, routes, subnets and virtual networks  
  
#### Action required

If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the `is_deleted` parameter before **December 1, 2025**.

To get a list of only deleted resources, you must now explicitly add the `is_deleted=true` query parameter to your request:
    
    
    # Example: Get ONLY deleted Tunnels
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true" \
         -H "Authorization: Bearer $API_TOKEN"
    
    # Example: Get ONLY deleted Virtual Networks
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true" \
         -H "Authorization: Bearer $API_TOKEN"

Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using `is_deleted=false`) and one to get deleted items (`is_deleted=true`).

#### Why we’re making this change

This update is based on user feedback and aims to:

  * **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
  * **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
  * **Improve performance:** For most users, the default query result will now be smaller and more relevant.



To learn more, please visit the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/) and [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) documentation.
