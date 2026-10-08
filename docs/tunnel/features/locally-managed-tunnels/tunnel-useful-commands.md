---
url: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/
title: Useful commands \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:04.006749+00:00
---

# Useful commands · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /…

Features

  4. /[Locally-managed tunnels](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/)
  5. /Useful commands



# Useful commands

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-useful-commands/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManage cloudflaredManage tunnelsManage published applications

This page lists the most commonly used commands for managing local tunnels.

To view all CLI commands, refer to the CLI help text in your terminal. For example, to view all options for the `cloudflared tunnel` subcommand, type `cloudflared tunnel help`.

## Manage `cloudflared`

Command | Description  
---|---  
`cloudflared update` | Looks for a new version on the official download server. If a new version exists, it updates the agent binary and quits. Otherwise, no action is performed. This command only works if `cloudflared` was installed from GitHub binaries or from source. For more information, refer to the [update instructions](https://developers.cloudflare.com/tunnel/guides/update-cloudflared/).  
`cloudflared version` | Prints the `cloudflared` version number and build date.  
`cloudflared help` | Shows a list of all top-level commands for `cloudflared`.  
  
## Manage tunnels

Command | Description  
---|---  
`cloudflared tunnel login` | Prompts a browser window where you can authenticate your tunnel to your Cloudflare account.  
`cloudflared tunnel list` | Displays all active tunnels, their creation time, and associated connections. Use the `-d` flag to include deleted tunnels.  
`cloudflared tunnel create <NAME or UUID>` | Creates a tunnel, registers it with the Cloudflare edge and generates a credential file to run this tunnel.  
`cloudflared tunnel --config path/config.yaml run <NAME or UUID>` | Runs a tunnel, creating highly available connections between your server and the Cloudflare edge. You can provide name or UUID of the tunnel to run either as the last command line argument or in the configuration file using `tunnel: <NAME>`.  
`cloudflared tunnel info <NAME or UUID>` | Displays details about the active connectors for a given tunnel identified by name of UUID.  
`cloudflared tunnel cleanup <NAME or UUID>` | Deletes connections for tunnels with the given UUIDs or names. This is useful if you get an error trying to delete or run a tunnel after `cloudflared` is not shut down gracefully (for example, if a `kill` command is issued).  
`cloudflared tunnel cleanup --connector-id <CONNECTOR-ID> <NAME or UUID>` | Disconnects and deletes a [`cloudflared` replica](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability) with the given connector ID. You can view all replicas for a tunnel by running `cloudflared tunnel info <NAME or UUID>`.  
`cloudflared tunnel delete <NAME or UUID>` | Deletes tunnels with the given name or UUID. A tunnel cannot be deleted if it has active connections. To delete the tunnel unconditionally, use the `-f` flag.  
`cloudflared tail <UUID>` | Start a session to livestream logs from a specific tunnel. For more information, refer to [Tunnel logs](https://developers.cloudflare.com/tunnel/observability/#logs).  
  
## Manage published applications

Command | Description  
---|---  
`cloudflared tunnel route dns` | Creates a DNS CNAME record hostname that points to the tunnel.  
`cloudflared tunnel route lb <NAME or UUID> <hostname> <load balancer pool>` | Adds a tunnel as an endpoint in a [load balancer pool](https://developers.cloudflare.com/tunnel/concepts/routing/#add-a-tunnel-to-a-load-balancer-pool). A new load balancer and pool will be created if necessary. 

  * `<hostname>`: the public-facing hostname of the load balancer, for example `lb.example.com`
  * `<load balancer pool>`: the name of the [pool](https://developers.cloudflare.com/load-balancing/pools/create-pool/#create-a-pool) that will contain the tunnel endpoint 

To load balance traffic to a [published application](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/#file-structure-for-published-applications), you will also need to specify the application hostname in the [endpoint host header](https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/) using the dashboard or API.  
  
[PreviousWindows](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/windows/)[NextTunnel permissions](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/tunnel-permissions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/features/locally-managed-tunnels/tunnel-useful-commands.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
