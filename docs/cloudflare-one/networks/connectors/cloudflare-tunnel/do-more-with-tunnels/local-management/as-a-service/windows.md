---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/
title: Run as a service on Windows \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:14.579050+00:00
---

# Run as a service on Windows · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Other tunnel types](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/)[Locally-managed tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/)

  4. /[Run as a service](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/)
  5. /Windows



# Windows

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure cloudflared as a serviceRun cloudflared as a serviceNext steps

You can install `cloudflared` as a system service on Windows.

## Configure `cloudflared` as a service

By default, Cloudflare Tunnel expects all of the configuration to exist in the `%USERPROFILE%\.cloudflared\config.yml` [configuration file](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/). At a minimum you must specify the following arguments to run as a service:

Argument | Description  
---|---  
`tunnel` | The UUID of your tunnel  
`credentials-file` | The location of the credentials file for your tunnel  
  
## Run `cloudflared` as a service

  1. [Download](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/) the latest `cloudflared` version.

  2. Create a new directory:
         
         C:\Cloudflared\bin

  3. Copy the `.exe` file you downloaded in step 1 to the new directory and rename it to `cloudflared.exe`.

  4. Open CMD as an administrator and go to `C:\Cloudflared\bin`.

  5. Run this command to install `cloudflared`:
         
         cloudflared.exe service install

  6. Next, run this command to create another directory:
         
         mkdir C:\Windows\System32\config\systemprofile\.cloudflared

  7. Log in and authenticate `cloudflared`:
         
         cloudflared.exe login

  8. The login command will generate a `cert.pem` file and save it to your user profile by default. Copy the file to the `.cloudflared` folder created in step 5 using this command:
         
         copy C:\Users\%USERNAME%\.cloudflared\cert.pem C:\Windows\System32\config\systemprofile\.cloudflared\cert.pem

  9. Next, create a tunnel:
         
         cloudflared.exe tunnel create <Tunnel Name>

This will generate a [credentials file](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/#credentials-file) in `.json` format.

  10. [Create a configuration file](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/#4-create-a-configuration-file) with the following content:
         
         tunnel: <Tunnel ID>
         credentials-file: C:\Windows\System32\config\systemprofile\.cloudflared\<Tunnel-ID>.json
         # Uncomment the following two lines if you are using self-signed certificates in your origin server
         # originRequest:
         #   noTLSVerify: true
         
         ingress:
           - hostname: app.mydomain.com
             service: https://internal.mydomain.com
           - service: http_status:404
         logfile:  C:\Cloudflared\cloudflared.log

  11. Copy the credentials file to the folder created in step 6:
         
         copy C:\Users\%USERNAME%\.cloudflared\<Tunnel-ID>.json C:\Windows\System32\config\systemprofile\.cloudflared\<Tunnel-ID>.json

  12. Validate the ingress rule entries in your configuration file using the command:
         
         cloudflared.exe tunnel ingress validate

  13. In the Registry Editor, go to `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Cloudflared`.

  14. In the Cloudflared registry entry, modify `ImagePath` to point to the `cloudflared.exe` and `config.yml` files. Make sure that there are no extra spaces or characters while you modify the registry entry, as this could cause problems with starting the service.
         
         C:\Cloudflared\bin\cloudflared.exe --config=C:\Windows\System32\config\systemprofile\.cloudflared\config.yml tunnel run

  15. If the service does not start, run the following command from `C:\Cloudflared\bin`:
         
         sc start cloudflared

You will see the output below:
         
         SERVICE_NAME: cloudflared
                 TYPE               : 10  WIN32_OWN_PROCESS
                 STATE              : 2  START_PENDING
                                         (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
                 WIN32_EXIT_CODE    : 0  (0x0)
                 SERVICE_EXIT_CODE  : 0  (0x0)
                 CHECKPOINT         : 0x0
                 WAIT_HINT          : 0x7d0
                 PID                : 3548
                 FLAGS              :




## Next steps

You can now [route traffic through your tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/#5-start-routing-traffic). If you add IP routes or otherwise change the configuration, restart the service to load the new configuration:
    
    
    sc stop cloudflared
    sc start cloudflared

[PreviousmacOS](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/macos/)[NextUseful commands](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/tunnel-useful-commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
