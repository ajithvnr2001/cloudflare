---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/
title: Run as a service on Linux \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:14.458058+00:00
---

# Run as a service on Linux · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Other tunnel types](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/)[Locally-managed tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/)

  4. /[Run as a service](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/)
  5. /Linux



# Linux

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Configure cloudflared as a service2\. Run cloudflared as a serviceNext steps

You can install `cloudflared` as a system service on Linux.

## Prerequisites

Before you install Cloudflare Tunnel as a service on Linux, follow Steps 1 through 4 of the [Tunnel CLI setup guide](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/). At this point you should have a named tunnel and a `config.yml` file in your `.cloudflared` directory.

## 1\. Configure `cloudflared` as a service

By default, Cloudflare Tunnel expects all of the configuration to exist in the `$HOME/.cloudflared/config.yml` [configuration file](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/). At a minimum you must specify the following arguments to run as a service:

Argument | Description  
---|---  
`tunnel` | The UUID of your tunnel  
`credentials-file` | The location of the credentials file for your Tunnel  
  
## 2\. Run `cloudflared` as a service

  1. Install the `cloudflared` service.
         
         cloudflared service install

Note

Installing the `cloudflared` systemd service on Linux typically requires elevated privileges. When the install command is run with `sudo`, `$HOME` points to `/root`, which may prevent `cloudflared` from locating a configuration file created in `/home/<USER>/.cloudflared/config.yml`. In this case, the config path can be passed explicitly:
         
         sudo cloudflared --config /home/<USER>/.cloudflared/config.yml service install

  2. Start the service.
         
         systemctl start cloudflared

  3. (Optional) View the status of the service.
         
         systemctl status cloudflared




## Next steps

You can now [route traffic through your tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/#5-start-routing-traffic). If you add IP routes or otherwise change the configuration, restart the service to load the new configuration:
    
    
    systemctl restart cloudflared

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/)[NextmacOS](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/macos/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/linux.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
