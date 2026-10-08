---
url: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/
title: Run as a service on macOS \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:03.021755+00:00
---

# Run as a service on macOS · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /…

Features[Locally-managed tunnels](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/)

  4. /[Run as a service](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/)
  5. /macOS



# macOS

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/macos/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Configure cloudflared as a service2\. Run cloudflared as a service Run at login Run at boot3\. Manually start the serviceNext steps

You can install `cloudflared` as a system service on macOS.

## Prerequisites

Before you install Cloudflare Tunnel as a service on your OS, follow Steps 1 through 4 of the [Tunnel CLI setup guide](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/create-local-tunnel/). At this point you should have a named tunnel and a `config.yml` file in your `$HOME/.cloudflared` directory.

## 1\. Configure `cloudflared` as a service

By default, Cloudflare Tunnel expects all of the configuration to exist in the `$HOME/.cloudflared/config.yml` [configuration file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/). At a minimum you must specify the following arguments to run as a service:

Argument | Description  
---|---  
`tunnel` | The UUID of your tunnel  
`credentials-file` | The location of the credentials file for your tunnel  
  
## 2\. Run `cloudflared` as a service

You can install the service to either run at login or at boot.

### Run at login

Open a terminal window and run the following command:
    
    
    cloudflared service install

Cloudflare Tunnel will be installed as a launch agent and start whenever you log in, using your local user configuration found in `~/.cloudflared/`.

### Run at boot

Open a terminal window and run the following command:
    
    
    sudo cloudflared service install

Cloudflare Tunnel will be installed as a launch daemon and start whenever your system boots, using your configuration found in `/etc/cloudflared`.

## 3\. Manually start the service

Run the following command:
    
    
    sudo launchctl start com.cloudflare.cloudflared

The output will be logged to `/Library/Logs/com.cloudflare.cloudflared.err.log` and `/Library/Logs/com.cloudflare.cloudflared.out.log`.

## Next steps

You can now [route traffic through your tunnel](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/create-local-tunnel/#5-start-routing-traffic). If you add IP routes or otherwise change the configuration, restart the service to load the new configuration:
    
    
    sudo launchctl stop com.cloudflare.cloudflared
    sudo launchctl start com.cloudflare.cloudflared

[PreviousLinux](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/linux/)[NextWindows](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/as-a-service/windows/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/features/locally-managed-tunnels/as-a-service/macos.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
