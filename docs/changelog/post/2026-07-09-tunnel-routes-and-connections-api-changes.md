---
url: https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/
title: Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:02.653757+00:00
---

# Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 9, 2026

## Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

On **October 5, 2026** , two changes take effect across the [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) and [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/): the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the `connections` field. If you manage private network routes or read tunnel connection details through the API, `cloudflared`, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.

#### Route endpoints

The CIDR-encoded route endpoints are deprecated in favor of the standard, `route_id`-based endpoints that already exist today. Both sets of endpoints route a private network through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) or [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) (the API still refers to Mesh nodes as `warp_connector`) — only the request shape changes.

**Deprecated endpoints (removed October 5, 2026):**

  * Create a tunnel route (CIDR Endpoint): [`POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create/)
  * Update a tunnel route (CIDR Endpoint): [`PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit/)
  * Delete a tunnel route (CIDR Endpoint): [`DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete/)



**Replacement endpoints:**

  * Create a tunnel route: [`POST /accounts/{account_id}/teamnet/routes`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/)
  * Update a tunnel route: [`PATCH /accounts/{account_id}/teamnet/routes/{route_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit/)
  * Delete a tunnel route: [`DELETE /accounts/{account_id}/teamnet/routes/{route_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete/)



#### What is changing

| Deprecated (CIDR-encoded path) | Replacement  
---|---|---  
Route identifier | URL-encoded CIDR in the path (`/network/{ip_network_encoded}`) | `route_id` in the path (`network` moves to the request body on create)  
Create | `POST .../teamnet/routes/network/{ip_network_encoded}` | `POST .../teamnet/routes` with `network` and `tunnel_id` in the body  
Update | `PATCH .../teamnet/routes/network/{ip_network_encoded}` | `PATCH .../teamnet/routes/{route_id}`  
Delete | `DELETE .../teamnet/routes/network/{ip_network_encoded}` | `DELETE .../teamnet/routes/{route_id}`  
  
#### Action required

  1. Capture each route's `route_id` by calling [List tunnel routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/), or read it from the response the first time you create a route with the replacement endpoint.
  2. Update any scripts, backend services, or CI/CD pipelines that call the CIDR-encoded endpoints directly.
  3. If you manage routes with the `cloudflared tunnel route ip add | delete` commands, upgrade `cloudflared` to the [latest version ↗︎](https://github.com/cloudflare/cloudflared/releases).
  4. If you manage routes with Terraform, make sure you are on a current version of the [`cloudflare_zero_trust_tunnel_cloudflared_route` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route) resource and the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).


    
    
    # Before: create a route by URL-encoding the CIDR into the path
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \
         -H 'Content-Type: application/json' \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
         -d '{"tunnel_id": "'$TUNNEL_ID'", "comment": "Example comment for this route."}'
    
    # After: create a route with the network in the request body
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \
         -H 'Content-Type: application/json' \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
         -d '{"network": "172.16.0.0/16", "tunnel_id": "'$TUNNEL_ID'", "comment": "Example comment for this route."}'
    
    # After: update or delete a route using its route_id
    curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \
         -H 'Content-Type: application/json' \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
         -d '{"comment": "Updated comment for this route."}'
    
    curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

#### Cloudflare Tunnel and Cloudflare Mesh connections

Starting the same day, the `connections` array is removed from list and get responses for [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes (the `cfd_tunnel` and `warp_connector` API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.

This affects:

  * [`GET /accounts/{account_id}/cfd_tunnel`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/) — `connections` removed from each item in `result`
  * [`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/) — `connections` removed from `result`
  * [`GET /accounts/{account_id}/warp_connector`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/) — `connections` removed from each item in `result`
  * [`GET /accounts/{account_id}/warp_connector/{tunnel_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get/) — `connections` removed from `result`



#### Action required

Fetch connection details from the tunnel-specific connections endpoint instead of parsing it off the list or get response. For Cloudflare Tunnel, call [`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/). For Cloudflare Mesh, call [`GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get/).
    
    
    # Before: read connections off the tunnel object
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    # After: query connections directly
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Update any dashboards, monitoring scripts, or automation that parses `connections` from the tunnel list or get response. `cloudflared` and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.

#### Why we are making these changes

  * **Smaller, faster responses.** Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.
  * **A single way to identify a route.** Consolidating on `route_id` removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.
  * **Consistency across the API.** Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.



To learn more, refer to the [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/), the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/), and [Routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/) documentation.
