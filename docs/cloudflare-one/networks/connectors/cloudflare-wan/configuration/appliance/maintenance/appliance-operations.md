---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/
title: Appliance operations \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:26.160339+00:00
---

# Appliance operations · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)Configuration[Configure with Connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/)

  4. /Maintenance
  5. /Appliance operations



# Appliance operations

Last updated Jul 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can restart, reboot, or shut down a Cloudflare One Appliance (formerly Magic WAN Connector) from the dashboard or via API. Operations are asynchronous — the appliance executes them the next time it checks in.

Operation | Effect  
---|---  
**Restart** | Restart managed services. Purges temporary and (optionally) persistent state.  
**Reboot** | Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.  
**Shutdown** | Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.  
  
Caution

Operations may disrupt service. Only one operation can be pending at a time.

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)

  2. Go to the **Appliances** tab > **Appliances**.
  3. Find the Cloudflare One Appliance you want to manage > **Edit**.
  4. Scroll down to the **Operations** section.
  5. Select **Restart** , **Reboot** , or **Shutdown**.
  6. In the confirmation dialog: 
     * Check **I understand this operation may disrupt service** (required).
     * Optionally, check **Purge persistent state** to clear persistent data in addition to temporary state.
  7. Select **Confirm**.



The operation is submitted and runs when the appliance next checks in. A banner shows the pending operation status until the appliance executes it.

Send a `POST` request to the interrupts endpoint with one of the following actions:

**Restart managed services:**
    
    
     curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/connectors/{connector_id}/interrupts" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{"restart": {"purge": false}}'

**Reboot (power cycle):**
    
    
     curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/connectors/{connector_id}/interrupts" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{"reboot": {"purge": false}}'

**Shut down:**
    
    
     curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/connectors/{connector_id}/interrupts" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{"shutdown": {"purge": false}}'

Set `"purge": true` to also purge persistent state.

The response includes a `submitted_at` timestamp. To check whether the appliance has executed the operation, poll the list endpoint:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/connectors/{connector_id}/interrupts" \
    --header "Authorization: Bearer <API_TOKEN>"

When `triggered_at` is populated in the response, the appliance has executed the operation.

Note

Only one operation can be pending at a time. If an operation is already pending, the API returns a `409 Conflict` response.

[PreviousInterrupt window](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/)[NextDevice metrics](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/device-metrics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/appliance-operations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
