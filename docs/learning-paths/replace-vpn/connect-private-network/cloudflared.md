---
url: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/
title: Connect with Cloudflare Tunnel \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:55.418573+00:00
---

# Connect with Cloudflare Tunnel · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Replace Vpn

  4. /[Connect your private network](https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/)
  5. /Connect with Cloudflare Tunnel



# Connect with Cloudflare Tunnel

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflared/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a tunnelBest practices

Cloudflare Tunnel is an outbound-only daemon service that can run on nearly any host machine and proxies local traffic once validated from the Cloudflare network. User traffic initiated from the Cloudflare One Client onramps to Cloudflare, passes down your Cloudflare Tunnel connections, and terminates automatically in your local network. Traffic reaching your internal applications or services will carry the local source IP address of the host machine running the `cloudflared` daemon.

## Create a tunnel

To connect your private network:

  1. Log in to the Cloudflare dashboard and go to **Networking** > **Tunnels**.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Select **Create a tunnel**.

  3. Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, `enterprise-VPC-01`).

  4. Select **Create Tunnel**.

  5. Choose your operating system, then copy the installation command and run it in a terminal on your origin server.

  6. Wait for the tunnel to connect. Once the connection is established, select **Continue**.



  9. In the **CIDR** tab, enter the CIDR of your private network (for example, `10.0.0.0/8`).

  10. Select **Save tunnel**.




  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Cloudflare Tunnel Write`
  2. Create a tunnel using the [`cloudflare_zero_trust_tunnel_cloudflare` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared) resource.
         
         resource "cloudflare_zero_trust_tunnel_cloudflared" "example_tunnel" {
         	account_id = var.cloudflare_account_id
         	name       = "Example tunnel"
         	config_src = "cloudflare"
         }

  3. Route the CIDR of your private network through the tunnel using the [`cloudflare_zero_trust_tunnel_cloudflared_route` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route) resource:
         
         resource "cloudflare_zero_trust_tunnel_cloudflared_route" "example_tunnel_route" {
         	account_id         = var.cloudflare_account_id
         	tunnel_id          = cloudflare_zero_trust_tunnel_cloudflared.example_tunnel.id
         	network            = "10.0.0.0/8"
         	comment            = "Example tunnel route"
         }

  4. Get the [token](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/) used to run the tunnel:
         
         data "cloudflare_zero_trust_tunnel_cloudflared_token" "tunnel_token" {
         	account_id = var.cloudflare_account_id
         	tunnel_id = cloudflare_zero_trust_tunnel_cloudflared.example_tunnel.id
         }

If your host machine is not managed in Terraform or you want to install the tunnel manually, you can output the token value to the CLI.

Example: Output to CLI

     1. Output the tunnel token to the Terraform state file: 
            
            output "tunnel_token" {
            	value       = data.cloudflare_zero_trust_tunnel_cloudflared_token.tunnel_token.token
            	sensitive   = true
            }

     2. Apply the configuration: 
            
            terraform apply

     3. Read the tunnel token: 
            
            terraform output -raw tunnel_token
            
            eyJhIj...

Alternatively, pass `data.cloudflare_zero_trust_tunnel_cloudflared_token.tunnel_token.token` directly into your host's Terraform configuration or store the token in your secret management tool.

Example: Store in HashiCorp Vault
    
    resource "vault_generic_secret" "tunnel_token" {
    	path         = "kv/cloudflare/tunnel_token"
    
    	data_json = jsonencode({
    		"TUNNEL_TOKEN" = data.cloudflare_zero_trust_tunnel_cloudflared_token.tunnel_token.token
    	})
    }

  5. Install `cloudflared` on a host machine in your private network and run the tunnel:

     1. [Download and install ↗︎](https://pkg.cloudflare.com/index.html) `cloudflared`.

     2. Run the following command:
            
            sudo cloudflared service install <TUNNEL_TOKEN>

     1. [Download and install](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#windows) `cloudflared`.

     2. Open Command Prompt as administrator.

     3. Run the following command:
            
            cloudflared.exe service install <TUNNEL_TOKEN>

     1. [Download and install](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#macos) `cloudflared`.

     2. Open a terminal window and run the following command:
            
            sudo cloudflared service install <TUNNEL_TOKEN>

     1. Open a terminal window.

     2. Run the following command:
            
            docker run cloudflare/cloudflared:latest tunnel --no-autoupdate run --token <TUNNEL_TOKEN>




All internal applications and services in this IP range are now connected to Cloudflare.

Note

If the tunnel is disconnected:

  * Ensure that your on-premise or cloud firewall allows egress traffic on the [required ports](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/#required-for-tunnel-operation).
  * Ensure that the `cloudflared` host machine can connect to your internal applications and services. Verify that the host has the proper security group memberships and that no firewalls will block traffic between the host and the target services.



## Best practices

  * Segregate production and staging traffic among different Cloudflare tunnels.
  * Add a [`cloudflared` replica](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) to another host machine for an additional point of availability.
  * Distribute access to critical services (for example, private DNS, Active Directory, and other critical systems) across different tunnels for blast-radius reduction in the event of a server-side outage.
  * [Enable notifications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/) in the Cloudflare dashboard to monitor tunnel health.
  * [Monitor performance metrics](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/) to identify potential bottlenecks.
  * [Update `cloudflared`](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/) regularly.



[PreviousConnect with Cloudflare Mesh](https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/)[NextTunnel capacity for cloudflared](https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/tunnel-capacity/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/replace-vpn/connect-private-network/cloudflared.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
