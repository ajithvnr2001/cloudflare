---
url: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/create-local-tunnel/
title: Create a locally-managed tunnel \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:03.615297+00:00
---

# Create a locally-managed tunnel · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/create-local-tunnel/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /…

Features

  4. /[Locally-managed tunnels](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/)
  5. /Create a locally-managed tunnel



# Create a locally-managed tunnel

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/create-local-tunnel/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Download and install cloudflared2\. Authenticate cloudflared3\. Create a tunnel and give it a name4\. Create a configuration file5\. Start routing traffic6\. Run the tunnel7\. Check the tunnel

Follow this step-by-step guide to get your first tunnel up and running using the CLI.

## Prerequisites

Before you start, make sure you:

  * [Add a website to Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/).
  * [Change your domain nameservers to Cloudflare](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/).



## 1\. Download and install `cloudflared`

  1. Download `cloudflared` on your machine. Visit the [downloads](https://developers.cloudflare.com/tunnel/downloads/) page to find the right package for your OS.

  2. Rename the executable to `cloudflared.exe`

  3. In PowerShell, change directory to your Downloads folder and run `.\cloudflared.exe --version`. It should output the version of `cloudflared`. Note that `cloudflared.exe` could be `cloudflared-windows-amd64.exe` or `cloudflared-windows-386.exe` if you have not renamed it.
         
         PS C:\Users\Administrator\Downloads\cloudflared-stable-windows-amd64> .\cloudflared.exe --version




To download and install `cloudflared`:
    
    
    brew install cloudflared

Alternatively, you can [download the latest Darwin amd64 release](https://developers.cloudflare.com/tunnel/downloads/) directly.

**Debian and Ubuntu APT**

Use the apt package manager to install `cloudflared` on compatible machines.

  1. Add Cloudflare's package signing key:


    
    
    sudo mkdir -p --mode=0755 /usr/share/keyrings
    curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null

  2. Add Cloudflare's apt repo to your apt repositories:


    
    
    echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared any main" | sudo tee /etc/apt/sources.list.d/cloudflared.list

  3. Update repositories and install cloudflared:


    
    
    sudo apt-get update && sudo apt-get install cloudflared

**RHEL RPM**

Use the rpm package manager to install `cloudflared` on compatible machines.

  1. Add Cloudflare's repository:
         
         curl -fsSl https://pkg.cloudflare.com/cloudflared.repo | sudo tee /etc/yum.repos.d/cloudflared.repo

  2. Update repositories and install cloudflared:
         
         sudo yum update && sudo yum install cloudflared




**Arch Linux**

`cloudflared` is in the Arch Linux [`community` repository ↗︎](https://wiki.archlinux.org/title/official_repositories#community). Use `pacman` to install `cloudflared` on compatible machines.
    
    
    pacman -Syu cloudflared

**Other**

Alternatively you can download the `cloudflared` binary or the linux packages to your machine and install manually. Visit the [downloads](https://developers.cloudflare.com/tunnel/downloads/) page to find the right package for your OS.

To build the latest version of `cloudflared` from source:
    
    
    git clone https://github.com/cloudflare/cloudflared.git
    cd cloudflared
    make cloudflared
    go install github.com/cloudflare/cloudflared/cmd/cloudflared

Depending on where you installed `cloudflared`, you can move it to a known path as well.
    
    
    mv /root/cloudflared/cloudflared /usr/bin/cloudflared

## 2\. Authenticate `cloudflared`
    
    
    cloudflared tunnel login

Running this command will:

  * Open a browser window and prompt you to log in to your Cloudflare account. After logging in to your account, select your hostname.
  * Generate an account certificate, the [cert.pem file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/local-tunnel-terms/#certpem), in the [default `cloudflared` directory](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/local-tunnel-terms/#default-cloudflared-directory).



## 3\. Create a tunnel and give it a name
    
    
    cloudflared tunnel create <NAME>

Running this command will:

  * Create a tunnel by establishing a persistent relationship between the name you provide and a UUID for your tunnel. At this point, no connection is active within the tunnel yet.
  * Generate a [tunnel credentials file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/local-tunnel-terms/#credentials-file) in the [default `cloudflared` directory](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/local-tunnel-terms/#default-cloudflared-directory).
  * Create a subdomain of `.cfargotunnel.com`.



From the output of the command, take note of the tunnel's UUID and the path to your tunnel's credentials file.

Confirm that the tunnel has been successfully created by running:
    
    
    cloudflared tunnel list

## 4\. Create a configuration file

  1. In your `.cloudflared` directory, create a [`config.yml` file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/) using any text editor. This file will configure the tunnel to route traffic from a given origin to the hostname of your choice.

  2. Add the following fields to the file:
         
         url: http://localhost:8000
         tunnel: <Tunnel-UUID>
         credentials-file: /root/.cloudflared/<Tunnel-UUID>.json

  3. Confirm that the configuration file has been successfully created by running:
         
         cat config.yml




## 5\. Start routing traffic

To route a [published application](https://developers.cloudflare.com/tunnel/concepts/routing/) through the tunnel:
    
    
    cloudflared tunnel route dns <UUID or NAME> <hostname>

This command will create a `CNAME` record pointing to `<UUID>.cfargotunnel.com`.

## 6\. Run the tunnel

Run the tunnel to proxy incoming traffic from the tunnel to any number of services running locally on your origin.
    
    
    cloudflared tunnel run <UUID or NAME>

If your configuration file has a custom name or is not in the `.cloudflared` directory, add the `--config` flag and specify the path.
    
    
    cloudflared tunnel --config /path/your-config-file.yml run <UUID or NAME>

Note

Cloudflare Tunnel can install itself as a system service on Linux and Windows and as a launch agent on macOS. For more information, refer to [run as a service](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/).

## 7\. Check the tunnel

To get information on the tunnel you just created, run:
    
    
    cloudflared tunnel info <UUID or NAME>

Looking for private network routing?

For Cloudflare One Client private network access, refer to the [Cloudflare One Tunnel documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/#file-structure-for-private-networks).

[PreviousOverview](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/)[NextConfiguration file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/features/locally-managed-tunnels/create-local-tunnel.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
