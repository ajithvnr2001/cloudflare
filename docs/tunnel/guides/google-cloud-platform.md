---
url: https://developers.cloudflare.com/tunnel/guides/google-cloud-platform/
title: GCP \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:04.509360+00:00
---

# GCP · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/guides/google-cloud-platform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /[Guides](https://developers.cloudflare.com/tunnel/guides/)
  4. /GCP



# GCP

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/guides/google-cloud-platform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Prerequisites1\. Create a VM instance2\. Create a tunnel3\. Publish an applicationFirewall configuration

This guide covers how to connect a Google Cloud Platform (GCP) virtual machine to Cloudflare using `cloudflared` and publish a web application through a Cloudflare Tunnel.

### Prerequisites

  * [A Google Cloud Project ↗︎](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project)
  * [A zone on Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/)



## 1\. Create a VM instance

  1. In your [Google Cloud Console ↗︎](https://console.cloud.google.com/), [create a new project ↗︎](https://developers.google.com/workspace/guides/create-project).

  2. Go to **Compute Engine** > **VM instances**.

  3. Select **Create instance**.

  4. Name your VM instance. In this example we will name it `http-test-server`.

  5. Choose your desired operating system and specifications. For this example, you can use the following settings:

     * **Machine family:** General Purpose
     * **Series:** E2
     * **Machine type:** e2-micro
     * **Boot disk image:** Debian GNU/Linux 12
     * **Firewalls** : Allow HTTP and HTTPS traffic
  6. Under **Advanced options** > **Management** > **Automation** , add the following startup script. This example deploys a basic Apache web server on port `80`.
         
         #!/bin/bash
         apt update
         apt -y install apache2
         cat <<EOF > /var/www/html/index.html
         <html><body><h1>Hello Cloudflare!</h1>
         <p>This page was created for a Cloudflare demo.</p>
         </body></html>
         EOF

  7. Select **Create**.

  8. The operating system automatically starts the Apache HTTP server. To verify that the server is running:

     1. Copy the **External IP** for the VM instance.
     2. Open a browser and go to `http://<EXTERNAL IP>`. You should see the **Hello Cloudflare!** test page.
  9. To login to the VM instance, open the dropdown next to **SSH** and select _Open in browser window_.




## 2\. Create a tunnel

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Networking** > **Tunnels**.
  2. Select **Create Tunnel** and enter a name (for example, `gcp-tunnel`).
  3. Select **Create Tunnel**.
  4. Under **Setup Environment** , select **Debian 64-bit**.
  5. SSH into your VM and run the install commands shown in the dashboard.
  6. Once the tunnel connects, select **Continue**.



## 3\. Publish an application

  1. Under **Routes** , select **Add route** > **Published application**.
  2. Enter a hostname (for example, `hellocloudflare.<your-domain>.com`).
  3. Under **Service** , enter `http://localhost:80`.
  4. Select **Add route**.



To test, open a browser and go to the hostname you configured.

You can optionally add [Cloudflare Access](https://developers.cloudflare.com/tunnel/integrations/#cloudflare-access) to control who can reach the service.

Looking for private network access?

To connect to your VM via private IP using the Cloudflare One Client, refer to the [Cloudflare One Tunnel documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/).

## Firewall configuration

To secure your VM instance, you can [configure your VPC firewall rules ↗︎](https://cloud.google.com/firewall/docs/using-firewalls) to deny all ingress traffic and allow only egress traffic to the [Cloudflare Tunnel IP addresses](https://developers.cloudflare.com/tunnel/configuration/#required-ports). Since GCP denies ingress traffic by [default ↗︎](https://cloud.google.com/firewall/docs/firewalls#default_firewall_rules), you can delete all ingress rules and leave only the relevant egress rules.

Note

If you delete the default `allow-ssh` rule, you will be unable to SSH back into the VM.

After configuring your VPC firewall rules, verify that you can still access the service through Cloudflare Tunnel via its public hostname. The service should no longer be accessible from outside Cloudflare Tunnel -- for example, if you go to `http://<EXTERNAL IP>` the test page should no longer load.

[PreviousAzure](https://developers.cloudflare.com/tunnel/guides/azure/)[NextKubernetes](https://developers.cloudflare.com/tunnel/guides/kubernetes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/guides/google-cloud-platform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
