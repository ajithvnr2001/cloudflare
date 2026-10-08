---
url: https://developers.cloudflare.com/time-services/ntp/usage/
title: Using Cloudflare's Time Service \u00b7 Cloudflare Time Services docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:02.037323+00:00
---

# Using Cloudflare's Time Service · Cloudflare Time Services docs

> Source: https://developers.cloudflare.com/time-services/ntp/usage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Time Services](https://developers.cloudflare.com/time-services/)
  3. /[Network Time Protocol](https://developers.cloudflare.com/time-services/ntp/)
  4. /User Guide



# User Guide

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/time-services/ntp/usage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewmacOSWindowsLinux chrony ↗︎ systemd-timesyncd ↗︎ ntpd ↗︎

[Network Time Protocol ↗︎](https://tools.ietf.org/html/rfc1305) (NTP) is an Internet protocol designed to synchronize time between computer systems communicating over unreliable and variable-latency network paths. Cloudflare offers its version of NTP for free so you can use our [global anycast network ↗︎](https://www.cloudflare.com/network/) to synchronize time from our closest server.

To use our NTP server, change the time configuration in your device to point to `time.cloudflare.com`.

## macOS

To have your Mac to synchronize time from `time.cloudflare.com`:

  1. Go to **System Settings**.
  2. Go to **General** > **Date & Time**.
  3. Enable **Set date and time automatically**.
  4. For **Source** , select **Set...** and enter `time.cloudflare.com` in the text field that appears.

![Screenshot of updating the Date & Time settings on machine running macOS](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1311,height=1038,format=webp/_astro/mactime.DBCp2s9r.png)

## Windows

To have your Windows machine synchronize time from `time.cloudflare.com`:

  1. Go to **Control Panel**.
  2. Go to **Clock and Region**.
  3. Click **Date and Time**.
  4. Go to the **Internet Time** tab.
  5. Click **Change settings..**
  6. For **Server:** , type `time.cloudflare.com` and click **Update now**.
  7. Click **OK**.

![Screenshot of updating the Date and Time settings on machine running Windows](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=510,height=346,format=webp/_astro/window.g3wVkbhY.png)

## Linux

Cloudflare's time servers are included in [pool.ntp.org ↗︎](https://www.ntppool.org/en/) which is the default time service for many Linux distributions and network appliances. If your NTP client is synchronizing from one of the below servers, you are already using Cloudflare's time services.

  * [162.159.200.1 ↗︎](https://www.ntppool.org/scores/162.159.200.1)
  * [162.159.200.123 ↗︎](https://www.ntppool.org/scores/162.159.200.123)
  * [2606:4700:f1::1 ↗︎](https://www.ntppool.org/scores/2606:4700:f1::1)
  * [2606:4700:f1::123 ↗︎](https://www.ntppool.org/scores/2606:4700:f1::123)



To manually configure your NTP client to use our time service, please first refer to the documentation for your Linux distribution to determine which NTP client you are using and where the configuration files are stored.

For example:

  * [Ubuntu ↗︎](https://ubuntu.com/server/docs/about-time-synchronisation)
  * [Debian ↗︎](https://wiki.debian.org/NTP)
  * [RHEL ↗︎](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-configuring_ntp_using_the_chrony_suite)



Exact configuration will vary by Linux distribution, but below are some example configurations for popular clients:

### [chrony ↗︎](https://chrony-project.org)

  1. Add `time.cloudflare.com` as a server in the configuration file on your system (e.g., `/etc/chrony/chrony.conf`)
         
         server time.cloudflare.com iburst

  2. Restart the chronyd service.
         
         systemctl restart chronyd




### [systemd-timesyncd ↗︎](https://man7.org/linux/man-pages/man5/timesyncd.conf.5.html)

  1. Add `time.cloudflare.com` to the `[Time]` section of the configuration file on your system (e.g., `/etc/systemd/timesyncd.conf`)
         
         [Time]
         NTP=time.cloudflare.com

  2. Restart the systemd-timesyncd service.
         
         systemctl restart systemd-timesyncd




### [ntpd ↗︎](https://linux.die.net/man/5/ntp.conf)

  1. Add `time.cloudflare.com` as a server in the configuration file on your system (e.g., `/etc/ntp.conf`)
         
         server time.cloudflare.com iburst

  2. Restart the ntpd service.
         
         systemctl restart ntpd




[PreviousOverview](https://developers.cloudflare.com/time-services/ntp/)[NextNetwork Time Security](https://developers.cloudflare.com/time-services/nts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/time-services/ntp/usage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
