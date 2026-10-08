---
url: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-permissions/
title: Tunnel permissions \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:03.837575+00:00
---

# Tunnel permissions · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-permissions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /…

Features

  4. /[Locally-managed tunnels](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/)
  5. /Tunnel permissions



# Tunnel permissions

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-permissions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTunnel ownershipRevoke account certificateAccount-scoped roles

Tunnel permissions determine who can run and manage a Cloudflare Tunnel. Two files control permissions for a locally-managed tunnel:

  * **An account certificate** (`cert.pem`) is issued for a Cloudflare account when you login to `cloudflared`. Make sure you are intentional about the locations and machines you store this certificate on, as this certificate allows users to create, delete, and manage all tunnels for the account.
  * **A tunnel credentials file** (`<TUNNEL-UUID>.json`) is issued for a tunnel when you create the tunnel. The credentials file only allows the user to run that specific tunnel, and do nothing else. Hence, as an admin, you can share tunnel credentials with users who will run the tunnel.



Refer to the table below for a comparison between the two files and the purposes for which they are intended.

| Account certificate | Tunnel credential  
---|---|---  
**File name** | `cert.pem` | `<TUNNEL-UUID>.json`  
**Purpose** | Authenticates your instance of `cloudflared` against your Cloudflare account | Authenticates the tunnel it is associated with  
**Scope** | Account-wide | Tunnel-specific  
**File type** | `.pem` | `.json`  
**Stored in** | [Default directory](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/local-tunnel-terms/#default-cloudflared-directory) | [Default directory](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/local-tunnel-terms/#default-cloudflared-directory)  
**Issued when running** | `cloudflared tunnel login` | `cloudflared tunnel create <NAME>`  
**Valid for** | At least 10 years, and the service token it contains is valid until revoked | Does not expire  
**Needed to** | Manage tunnels (for example, create, route, delete and list tunnels) | Run a tunnel. Create a config file.  
  
## Tunnel ownership

Tunnel ownership is bound to the Cloudflare account for which the `cert.pem` file was issued upon authenticating `cloudflared`. If a user in a Cloudflare account creates a tunnel, any other user in the same account who has access to the `cert.pem` file for the account can delete, list, or otherwise manage tunnels within it.

## Revoke account certificate

Your account certificate (`cert.pem`) contains an API token which authorizes `cloudflared` to manage tunnels in your Cloudflare account. To revoke the account certificate, delete the API token associated with your tunnel:

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and go to **My Profile** > **API Tokens**.
  2. Find the **Cloudflare Tunnel API Token** or **Argo Tunnel API Token** for your zone and account.
  3. Select the three dots > **Delete**.



Once this token is deleted, `cloudflared` can no longer use the old `cert.pem` file to read or edit tunnels in your account. To generate a new token and `cert.pem` file, run `cloudflared tunnel login`.

## Account-scoped roles

Minimum permissions needed to create, delete, and configure tunnels for an account:

  * [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/roles-permissions/)



Additional permissions needed to [route traffic to a public hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/) and to be able to perform `cloudflared login`:

  * [DNS](https://developers.cloudflare.com/fundamentals/manage-members/roles/)
  * [Load Balancer](https://developers.cloudflare.com/fundamentals/manage-members/roles/)



[PreviousUseful commands](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/)[NextUseful terms](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/local-tunnel-terms/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/features/locally-managed-tunnels/tunnel-permissions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
