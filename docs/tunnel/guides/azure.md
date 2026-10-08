---
url: https://developers.cloudflare.com/tunnel/guides/azure/
title: Deploy cloudflared in Azure \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:04.627031+00:00
---

# Deploy cloudflared in Azure · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/guides/azure/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /[Guides](https://developers.cloudflare.com/tunnel/guides/)
  4. /Azure



# Azure

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/guides/azure/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Prerequisites1\. Create a Virtual Machine2\. Create a tunnel3\. Publish an applicationFirewall configuration

This guide covers how to connect an Azure Virtual Machine to Cloudflare using `cloudflared` and publish a web application through a Cloudflare Tunnel.

### Prerequisites

  * [Add a website to Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/)



## 1\. Create a Virtual Machine

  1. In the Azure portal, go to **Virtual Machines** > **Create** > **Azure virtual machine**.

  2. Select a **Resource group** or create a new one.

![Azure group](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1920,height=240,format=webp/_astro/azure-1.f9lJ2gl2.png)
  3. Enter a name for the VM and select a region. For **Image** , select _Ubuntu Server 24.04 LTS_. For **Size** , select an appropriate size (for example, _Standard_B1s_).

  4. Under **Administrator account** , select **SSH public key** and enter your key pair.

![Azure keypair](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1830,height=894,format=webp/_astro/azure-2.TRbZo2Tb.png)
  5. Under **Inbound port rules** , allow SSH (`22`). For testing purposes, also allow HTTP (`80`) and HTTPS (`443`).

![Azure ports](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1788,height=642,format=webp/_astro/azure-3.MZiED3ci.png)
  6. Select **Review + create** , then **Create**.

  7. Once the VM is running, copy its **Public IP address** from the VM overview page.

  8. SSH into the instance:
         
         ssh -i "your-key.pem" azureuser@<PUBLIC_IP>

  9. Run `sudo su` to gain full admin rights to the VM.

  10. For testing purposes, you can deploy a basic Apache web server on port `80`:
         
         apt update
         
         apt -y install apache2
         
         cat <<EOF > /var/www/html/index.html
         <html><body><h1>Hello Cloudflare!</h1>
         <p>This page was created for a Cloudflare demo.</p>
         </body></html>
         EOF

  11. To verify that the Apache server is running, open a browser and go to `http://<PUBLIC_IP>` (make sure to connect over `http`, not `https`). You should see the **Hello Cloudflare!** test page.




## 2\. Create a tunnel

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Networking** > **Tunnels**.
  2. Select **Create Tunnel** and enter a name (for example, `azure-tunnel`).
  3. Select **Create Tunnel**.
  4. Under **Setup Environment** , select **Debian 64-bit**.
  5. Copy the install commands and run them on your Azure VM.
  6. Once the tunnel connects, select **Continue**.



## 3\. Publish an application

  1. Under **Routes** , select **Add route** > **Published application**.
  2. Enter a hostname (for example, `hellocloudflare.<your-domain>.com`).
  3. Under **Service** , enter `http://localhost:80`.
  4. Select **Add route**.



To test, open a browser and go to the hostname you configured. You should see the **Hello Cloudflare!** test page.

Looking for private network access?

To connect to your Azure VM via private IP using the Cloudflare One Client, refer to the [Cloudflare One Tunnel documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/).

## Firewall configuration

To secure your Azure VM, you can configure your [Network Security Group (NSG) ↗︎](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) to deny all inbound traffic and allow only outbound traffic to the [Cloudflare Tunnel IP addresses](https://developers.cloudflare.com/tunnel/configuration/#required-ports). All NSG rules are evaluated by priority; traffic that does not match an allow rule is blocked by the default deny rules. Therefore, you can delete all custom inbound rules and leave only the relevant outbound rules.

Note

If you delete the inbound rule for port `22`, you will be unable to SSH back into the VM.

After configuring your NSG rules, verify that you can still access the service through Cloudflare Tunnel via its public hostname. The service should no longer be accessible from outside Cloudflare Tunnel — for example, direct access to the VM's public IP should no longer work.

[PreviousAWS](https://developers.cloudflare.com/tunnel/guides/aws/)[NextGCP](https://developers.cloudflare.com/tunnel/guides/google-cloud-platform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/guides/azure.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
