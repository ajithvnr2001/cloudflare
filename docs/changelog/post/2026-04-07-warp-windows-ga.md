---
url: https://developers.cloudflare.com/changelog/post/2026-04-07-warp-windows-ga/
title: Cloudflare One Client for Windows (version 2026.3.851.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:45.404701+00:00
---

# Cloudflare One Client for Windows (version 2026.3.851.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-07-warp-windows-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 7, 2026

## Cloudflare One Client for Windows (version 2026.3.851.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-07-warp-windows-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes and improvements.

The next stable release for Windows will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.

**Changes and improvements**

  * Fixed an issue causing Windows client tunnel interface initialization failure which prevented clients from establishing a tunnel for connection.
  * Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
  * Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
  * Added monitoring for tunnel statistics collection timeouts.
  * Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.
  * Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.
  * Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.
  * Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.
  * Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.
  * Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
  * Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.
  * Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.
  * Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.
  * Fixed an issue where degraded Windows Management Instrumentation (WMI) state could put the client in a failed connection state loop during initialization.



**Known issues**

  * For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 version KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution. This warning will be omitted from future release notes. This Windows update was released in July 2025.

  * Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.

  * DNS resolution may be broken when the following conditions are all true:

    * The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
    * A custom DNS server address is configured on the primary network adapter.
    * The custom DNS server address on the primary network adapter is changed while the client is connected.

To work around this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface.



