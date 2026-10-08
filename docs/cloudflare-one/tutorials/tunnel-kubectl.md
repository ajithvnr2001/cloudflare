---
url: https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/
title: Use Cloudflare Tunnels with Kubernetes client-go credential plugins \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:24.235567+00:00
---

# Use Cloudflare Tunnels with Kubernetes client-go credential plugins · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Tutorials](https://developers.cloudflare.com/cloudflare-one/tutorials/)
  4. /Tunnel Kubectl



# Use Cloudflare Tunnels with Kubernetes client-go credential plugins

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/tutorials/tunnel-kubectl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Set up a Cloudflare Tunnel2\. Configure the Kubernetes API server3\. Set up client-go credential plugin4\. Use kubectl with Cloudflare TunnelTroubleshooting

This tutorial explains how to use Cloudflare Tunnels with Kubernetes client-go credential plugins for authentication. By following these steps, you can securely access your Kubernetes cluster through a Cloudflare Tunnel using the `kubectl` command-line tool.

## Prerequisites

  * A Cloudflare account
  * The Cloudflare Tunnel client (`cloudflared`) installed on your machine
  * Access to a Kubernetes cluster
  * `kubectl` installed on your machine



## 1\. Set up a Cloudflare Tunnel

  1. Authenticate `cloudflared` with your Cloudflare account:
         
         cloudflared tunnel login

  2. Create a new tunnel:
         
         cloudflared tunnel create k8s-tunnel

  3. Configure your tunnel by creating a configuration file named `config.yml`:
         
         tunnel: <TUNNEL_ID>
         credentials-file: /path/to/credentials.json
         ingress:
           - hostname: k8s.example.com
             service: tcp://kubernetes.default.svc.cluster.local:443
           - service: http_status:404

Replace `<TUNNEL_ID>` with your tunnel ID and adjust the hostname as needed.

  4. Start the tunnel:
         
         cloudflared tunnel run k8s-tunnel




## 2\. Configure the Kubernetes API server

Ensure your Kubernetes API server is configured to accept authentication from Cloudflare Tunnels. This may involve setting up an authentication webhook or configuring the API server to trust the Cloudflare Tunnel's client certificates.

## 3\. Set up client-go credential plugin

  1. Create a script named `cloudflare-k8s-auth.sh` with the following content:
         
         #!/bin/bash
         
         echo '{
           "apiVersion": "client.authentication.k8s.io/v1beta1",
           "kind": "ExecCredential",
           "status": {
             "token": "'"$(cloudflared access token -app=https://k8s.example.com)"'"
           }
         }'

Make the script executable:
         
         chmod +x cloudflare-k8s-auth.sh

  2. Update your `~/.kube/config` file to use the credential plugin:
         
         apiVersion: v1
         kind: Config
         clusters:
           - cluster:
               server: https://k8s.example.com
             name: cloudflare-k8s
         users:
           - name: cloudflare-user
             user:
               exec:
                 apiVersion: client.authentication.k8s.io/v1beta1
                 command: /path/to/cloudflare-k8s-auth.sh
                 interactiveMode: Never
         contexts:
           - context:
               cluster: cloudflare-k8s
               user: cloudflare-user
             name: cloudflare-k8s-context
         current-context: cloudflare-k8s-context




## 4\. Use kubectl with Cloudflare Tunnel

Now you can use `kubectl` commands as usual. The client-go credential plugin will automatically handle authentication through the Cloudflare Tunnel:
    
    
    kubectl get pods

## Troubleshooting

If you encounter issues:

  * Ensure `cloudflared` is running and the tunnel is active
  * Check that your `~/.kube/config` file is correctly configured
  * Verify that the Kubernetes API server is properly set up to accept authentication from Cloudflare Tunnels
  * Review the Cloudflare Tunnel logs for any error messages



For more information, refer to the [Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) and the [Kubernetes client-go credential plugins documentation ↗︎](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins).

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/tutorials/tunnel-kubectl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
