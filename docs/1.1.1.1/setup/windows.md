---
url: https://developers.cloudflare.com/1.1.1.1/setup/windows/
title: Set up 1.1.1.1 on Windows \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:04.847541+00:00
---

# Set up 1.1.1.1 on Windows · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/setup/windows/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /[Set up](https://developers.cloudflare.com/1.1.1.1/setup/)
  4. /Windows



# Windows

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/setup/windows/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWindows 10Windows 11Encrypt your DNS queries

## Windows 10

Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.

  1. Select the **Start menu** > **Settings**.
  2. On **Network and Internet** , select **Change Adapter Options**.
  3. Right-click on the Ethernet or Wi-Fi network you are connected to and select **Properties**.
  4. Select **Internet Protocol Version 4**.
  5. Select **Properties** > **Use the following DNS server addresses**.
  6. Depending on what you want to configure, choose one of the following DNS addresses for IPv4:

Use 1.1.1.1 resolver
         
         1.1.1.1
         1.0.0.1

Block malware with 1.1.1.1 for Families
         
         1.1.1.2
         1.0.0.2

Block malware and adult content with 1.1.1.1 for Families
         
         1.1.1.3
         1.0.0.3

  7. Select **OK**.
  8. Select **Internet Protocol Version 6**.
  9. Select **Properties** > **Use the following DNS server addresses**.
  10. Depending on what you want to configure, choose one of the following DNS addresses for IPv6:

Use 1.1.1.1 resolver
         
         2606:4700:4700::1111
         2606:4700:4700::1001

Block malware with 1.1.1.1 for Families
         
         2606:4700:4700::1112
         2606:4700:4700::1002

Block malware and adult content with 1.1.1.1 for Families
         
         2606:4700:4700::1113
         2606:4700:4700::1003

  11. Select **OK**.



## Windows 11

Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.

  1. Select the **Start menu** > **Settings**.
  2. On **Network and Internet** , select the adapter you want to configure — such as your Ethernet adapter or Wi-Fi card.
  3. Scroll to **DNS server assignment** and select **Edit**.
  4. Select the **Automatic (DHCP)** drop-down menu > **Manual**.
  5. Select the **IPv4** toggle to turn it on.
  6. Depending on what you want to configure, choose one of the following DNS addresses for IPv4:

Use 1.1.1.1 resolver
         
         1.1.1.1
         1.0.0.1

Block malware with 1.1.1.1 for Families
         
         1.1.1.2
         1.0.0.2

Block malware and adult content with 1.1.1.1 for Families
         
         1.1.1.3
         1.0.0.3

  7. Select the **IPv6** toggle.
  8. Depending on what you want to configure, choose one of the following DNS addresses for IPv6:

Use 1.1.1.1 resolver
         
         2606:4700:4700::1111
         2606:4700:4700::1001

Block malware with 1.1.1.1 for Families
         
         2606:4700:4700::1112
         2606:4700:4700::1002

Block malware and adult content with 1.1.1.1 for Families
         
         2606:4700:4700::1113
         2606:4700:4700::1003

  9. Select **Save**.



Note

Setting up a static IP address to configure a DNS server may prevent you from connecting to some public Wi-Fi networks that use captive portals — these are the web pages some wireless networks employ to let users log in and use their services.

If you are experiencing connectivity issues related to captive portals:

  1. Remove the static IP addresses from the device or disable the 1.1.1.1 app.
  2. Connect to the Wi-Fi network.
  3. Once the connection has been established, re-add the static IP addresses or enable the 1.1.1.1 app.



## Encrypt your DNS queries

1.1.1.1 supports DNS over TLS (DoT) and DNS over HTTPS (DoH), two standards developed for encrypting plaintext DNS traffic. This prevents untrustworthy entities from interpreting and manipulating your queries. For more information on how to encrypt your DNS queries, please refer to the [Encrypted DNS documentation](https://developers.cloudflare.com/1.1.1.1/encryption/).

[PreviousRouter](https://developers.cloudflare.com/1.1.1.1/setup/router/)[NextOverview](https://developers.cloudflare.com/1.1.1.1/encryption/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/setup/windows.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
