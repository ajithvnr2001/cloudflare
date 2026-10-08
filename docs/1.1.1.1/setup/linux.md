---
url: https://developers.cloudflare.com/1.1.1.1/setup/linux/
title: Set up 1.1.1.1 on Linux \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:04.410645+00:00
---

# Set up 1.1.1.1 on Linux · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/setup/linux/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /[Set up](https://developers.cloudflare.com/1.1.1.1/setup/)
  4. /Linux



# Linux

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/setup/linux/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse command line interface (CLI) resolv.conf systemd-resolvedUse graphical user interface (GUI) GNOME KDE Plasma

Before you begin, take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.

You can configure 1.1.1.1 using the command line or a graphical interface.

## Use command line interface (CLI)

If you want to use 1.1.1.1 for Families instead of the standard resolver, replace `1.1.1.1` in the examples below with the corresponding [IPv4 or IPv6 address](https://developers.cloudflare.com/1.1.1.1/ip-addresses/).

### `resolv.conf`

On most Linux distributions, `/etc/resolv.conf` controls which DNS resolver the system uses.

To set `1.1.1.1` as your DNS resolver with `1.0.0.1` as a backup:
    
    
    echo -e "nameserver 1.1.1.1\nnameserver 1.0.0.1" | sudo tee /etc/resolv.conf

Caution

Some services — such as DHCP clients or `NetworkManager` — automatically overwrite `/etc/resolv.conf` when your network connection changes. If your DNS settings revert after a reboot or reconnection, configure 1.1.1.1 in your network manager or DHCP client instead.

You can also edit `/etc/resolv.conf` manually with a text editor like `nano` or `vim`.

### `systemd-resolved`

If your system uses `systemd-resolved` to manage DNS, edit the configuration file at `/etc/systemd/resolved.conf`:

  1. Run the following command, replacing `<EDITOR>` with your preferred editor.


    
    
    sudo <EDITOR> /etc/systemd/resolved.conf

  2. In the editor, add or edit the following lines:


    
    
    [Resolve]
    DNS=1.1.1.1

To use DNS over TLS, append `#one.one.one.one` after the IP address (this tells `systemd-resolved` which hostname to use for TLS verification) and set `DNSOverTLS` to `yes`:
    
    
    [Resolve]
    DNS=1.1.1.1#one.one.one.one
    DNSOverTLS=yes

## Use graphical user interface (GUI)

### GNOME

  1. Go to **Show Applications** > **Settings** > **Network**.
  2. Select the adapter you want to configure — such as your Ethernet adapter or Wi-Fi card — and select the **Settings** button.
  3. On the **IPv4** tab > **DNS** section, disable the **Automatic** toggle.
  4. Depending on what you want to configure, choose one of the following DNS addresses for IPv4:

Use 1.1.1.1 resolver
         
         1.1.1.1
         1.0.0.1

Block malware with 1.1.1.1 for Families
         
         1.1.1.2
         1.0.0.2

Block malware and adult content with 1.1.1.1 for Families
         
         1.1.1.3
         1.0.0.3

  5. Go to **IPv6**.
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

  7. Select **Apply**.



### KDE Plasma

  1. Go to **System Settings** > **Wi-Fi & Internet** > **Wi-Fi & Networking**. (or **Connections** , if on Plasma 5)
  2. Select the connection you want to configure - like your current connected network.
  3. On the **IPv4** tab, select the **Method** drop-down menu > _Automatic (Only addresses)_.
  4. Select the text box next to **DNS servers**.
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

  6. On the **IPv6** tab, select the **Method** drop-down menu > _Automatic (Only addresses)_.
  7. Select the text box next to **DNS servers**.
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

  9. Select **Apply**.



Note

Setting up a static IP address to configure a DNS server may prevent you from connecting to some public Wi-Fi networks that use captive portals — these are the web pages some wireless networks employ to let users log in and use their services.

If you are experiencing connectivity issues related to captive portals:

  1. Remove the static IP addresses from the device or disable the 1.1.1.1 app.
  2. Connect to the Wi-Fi network.
  3. Once the connection has been established, re-add the static IP addresses or enable the 1.1.1.1 app.



[PreviousiOS](https://developers.cloudflare.com/1.1.1.1/setup/ios/)[NextmacOS](https://developers.cloudflare.com/1.1.1.1/setup/macos/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/setup/linux.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
