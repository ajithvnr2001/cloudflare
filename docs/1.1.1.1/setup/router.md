---
url: https://developers.cloudflare.com/1.1.1.1/setup/router/
title: Set up 1.1.1.1 on a router \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:04.795452+00:00
---

# Set up 1.1.1.1 on a router · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/setup/router/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /[Set up](https://developers.cloudflare.com/1.1.1.1/setup/)
  4. /Router



# Router

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/setup/router/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse DNS over TLS on OpenWrtFRITZ!Box

Configuring 1.1.1.1 on your router applies the DNS setting to every device on your network. You do not need to change DNS settings on individual phones, computers, or other devices.

  1. Go to the **IP address** used to access your router's admin console in your browser.

     * Linksys and Asus routers typically use `http://192.168.1.1` or `http://router.asus.com` (for ASUS).
     * Netgear routers typically use `http://192.168.1.1` or `http://routerlogin.net`.
     * D-Link routers typically use `http://192.168.0.1`.
     * Ubiquiti routers typically use `http://unifi.ubnt.com`.
     * MikroTik routers typically use `http://192.168.88.1`.
  2. Enter the router credentials. For consumer routers, the default credentials for the admin console are often found under or behind the device.

  3. In the admin console, locate the section where **DNS settings** are configured. This may be contained within categories such as **WAN** and **IPv6** (Asus routers), **IP** (MikroTik routers), or **Internet** (Netgear routers). Consult your router's documentation for details.

  4. Take note of any DNS addresses that are currently set and save them in a safe place in case you need to use them later.

  5. Depending on what you want to configure, choose one of the following DNS addresses for IPv4:

Use 1.1.1.1 resolver
         
         1.1.1.1
         1.0.0.1

Block malware with 1.1.1.1 for Families
         
         1.1.1.2
         1.0.0.2

Block malware and adult content with 1.1.1.1 for Families
         
         1.1.1.3
         1.0.0.3

  6. Depending on what you want to configure, choose one of the following DNS addresses for IPv6:

Use 1.1.1.1 resolver
         
         2606:4700:4700::1111
         2606:4700:4700::1001

Block malware with 1.1.1.1 for Families
         
         2606:4700:4700::1112
         2606:4700:4700::1002

Block malware and adult content with 1.1.1.1 for Families
         
         2606:4700:4700::1113
         2606:4700:4700::1003

  7. Save the updated settings.




## Use DNS over TLS on OpenWrt

If your router runs OpenWrt, you can encrypt DNS traffic using DNS over TLS. For setup instructions, refer to [Adding DNS-Over-TLS support to OpenWrt (LEDE) with Unbound ↗︎](https://blog.cloudflare.com/dns-over-tls-for-openwrt/).

## FRITZ!Box

Starting with [FRITZ!OS 7.20 ↗︎](https://en.avm.de/press/press-releases/2020/07/fritzos-720-more-performance-convenience-security/), DNS over TLS is supported. Refer to [Configuring different DNS servers in the FRITZ!Box ↗︎](https://en.avm.de/service/knowledge-base/dok/FRITZ-Box-7590/165_Configuring-different-DNS-servers-in-the-FRITZ-Box/).

[PreviousmacOS](https://developers.cloudflare.com/1.1.1.1/setup/macos/)[NextWindows](https://developers.cloudflare.com/1.1.1.1/setup/windows/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/setup/router.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
