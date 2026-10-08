---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/
title: Connect to RDP with client-side cloudflared \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:21.419733+00:00
---

# Connect to RDP with client-side cloudflared · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Use cases](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/)

  4. /[RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/)
  5. /RDP with client-side cloudflared



# Connect to RDP with client-side cloudflared

Last updated Jun 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Connect the server to Cloudflare2\. (Recommended) Create an Access application3\. Connect as a user

End users can connect to an RDP server without the Cloudflare One Client by authenticating through `cloudflared` in their native terminal. This method requires having `cloudflared` installed on both the server machine and on the client machine, as well as an active zone on Cloudflare. The traffic is proxied over this connection, and the user logs in to the server with their Cloudflare Access credentials.

Client-side `cloudflared` can be used in conjunction with [the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/) and [Browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/) so that there are multiple ways to connect to the server. You can reuse the same Cloudflare Tunnel when configuring each connection method.

## 1\. Connect the server to Cloudflare

  1. Create a Cloudflare Tunnel by following our [dashboard setup guide](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/).

  2. In the Cloudflare dashboard, go to **Networking** > **Tunnels** and select your tunnel.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  3. On the **Routes** tab, select **Add route** , then select **Published application**.

  4. Choose a domain from the drop-down menu and specify any subdomain (for example, `rdp.example.com`).

  5. For **Service** , select _RDP_ and enter the [RDP listening port ↗︎](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/change-listening-port) of your server (for example, `localhost:3389`). It will likely be port `3389`.

  6. Select **Add route**.




## 2\. (Recommended) Create an Access application

By default, anyone on the Internet can connect to the server using the hostname of the published application. To allow or block specific users, create a [self-hosted application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) in Cloudflare Access.

## 3\. Connect as a user

  1. [Install `cloudflared`](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/) on the client machine.

  2. Run this command to open an RDP listening port:
         
         cloudflared access rdp --hostname rdp.example.com --url rdp://localhost:3389

This process will need to be configured to stay alive and autostart. If the process is killed, users will not be able to connect.




Note

If the client machine is running Windows, port `3389` may already be consumed locally. Select an alternative port to `3389` that is not being used.

  3. While `cloudflared access` is running, connect from an RDP client such as Microsoft Remote Desktop: 
     1. Open Microsoft Remote Desktop and select **Add a PC**.
     2. For **PC name** , enter `localhost:3389`.
     3. For **User account** , enter your RDP server username and password.
     4. Double-click the newly added PC.
     5. When asked if you want to continue, select **Continue**.



When the client launches, a browser window will open and prompt the user to authenticate with Cloudflare Access.

[PreviousRDP with Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/)[NextSMB](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/smb/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
