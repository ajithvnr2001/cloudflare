---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/
title: Uninstall the Cloudflare One Client \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:04.688787+00:00
---

# Uninstall the Cloudflare One Client · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)

  4. /[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)
  5. /Uninstall



# Uninstall the Cloudflare One Client

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWindowsmacOSLinuxiOS and Android

The following procedures will uninstall the Cloudflare One Client (formerly WARP) from your device. If you used the Cloudflare One Client to deploy a root certificate, the certificate will also be removed.

## Windows

  1. Go to Windows Settings (Windows Key + I).
  2. Select **Apps**.
  3. Select **Installed Apps**.
  4. Scroll to find the Cloudflare One Client application, click the three dots (...), and select **Uninstall**.



## macOS

We include an uninstall script as part of the macOS package that you originally used.

  1. To find and run the uninstall script, run the following commands:


    
    
    cd /Applications/Cloudflare\ WARP.app/Contents/Resources
    ./uninstall.sh

  2. If prompted, enter your admin credentials to proceed with the uninstall.



Note

You can bypass the **Are you sure** prompt by passing `-f` as a parameter to the macOS uninstall command.

## Linux

On CentOS 8, RHEL 8:
    
    
    sudo yum remove cloudflare-warp

On Ubuntu 18.04, Ubuntu 20.04, Ubuntu 22.04, Debian 9, Debian 10, Debian 11:
    
    
    sudo apt remove cloudflare-warp

## iOS and Android

  1. Find the Cloudflare One Agent application (or the legacy 1.1.1.1 application) on the home screen.
  2. Select and hold the application tile, and then select **Remove App**.
  3. Select **Delete App**.



Note

If you [manually deployed a Cloudflare certificate](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/), remember to manually delete the certificate from the device.

[PreviousBusiness Continuity Guide](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/business-continuity/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
