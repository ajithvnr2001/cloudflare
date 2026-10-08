---
url: https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/
title: Tunnel tokens \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:05.835664+00:00
---

# Tunnel tokens · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /Reference
  4. /Tunnel tokens



# Tunnel tokens

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet the tokenRotate a token

A remotely-managed tunnel only requires a token to run. Anyone with the token can run the tunnel.

## Get the token

To get the token for a remotely-managed tunnel:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Networking** > **Tunnels**.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Select your tunnel.

  3. Select **Add a replica**.

  4. Copy the `cloudflared` installation command into a text editor (do not run the command). The token is the `eyJ...` string.




Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Cloudflare One Connectors Write`
  * `Cloudflare One Connector: cloudflared Write`
  * `Cloudflare Tunnel Write`

Get a Cloudflare Tunnel tokenbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/token" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Rotate a token

Rotate tokens regularly to reduce the risk of compromise. For tunnels with multiple [replicas](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability), rotate outside working hours and update replicas in batches.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Networking** > **Tunnels**.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Select your tunnel.

  3. Select **Rotate token**. After rotating the token, `cloudflared` cannot establish new connections with the old token. Existing connectors remain active until restarted.

  4. Select **Add replica** and copy the new `cloudflared` installation command.

  5. On each replica, reinstall the `cloudflared` service using the new token:
         
         sudo cloudflared service uninstall
         sudo cloudflared service install <NEW_TOKEN>




Rotate a compromised token

If your tunnel token is compromised, immediately rotate the token, then force-disconnect all existing connections:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Cloudflare One Connectors Write`
  * `Cloudflare One Connector: cloudflared Write`
  * `Cloudflare Tunnel Write`

Clean up Cloudflare Tunnel connectionsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Then reinstall the `cloudflared` service on all replicas using the new token.

[PreviousOrigin parameters](https://developers.cloudflare.com/tunnel/reference/origin-parameters/)[NextObservability](https://developers.cloudflare.com/tunnel/observability/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/reference/tunnel-tokens.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
