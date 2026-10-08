---
url: https://developers.cloudflare.com/changelog/post/2026-05-26-warp-windows-ga/
title: Cloudflare One Client for Windows (version 2026.4.1390.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:54.611101+00:00
---

# Cloudflare One Client for Windows (version 2026.4.1390.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-26-warp-windows-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 26, 2026

## Cloudflare One Client for Windows (version 2026.4.1390.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-26-warp-windows-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:

  * Right click context menu to access the most common client actions quickly
  * Built-in captive portal login experience



**Additional Changes and improvements**

  * Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.
  * Fixed a proxy mode connection stall issue.



**Known issues**

  * Registration authentication for devices via the integrated WebView2 browser is unavailable in this version as a temporary measure. As a result, the client will utilize the default browser on the device to complete the authentication process.
  * An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.
  * Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
  * Split tunnel list configuration is not available in the new UI. Management of Split Tunnel entries is currently only possible via `warp-cli tunnel ip` and `warp-cli tunnel host`. UI support will be added in a future release.
  * Windows ARM may prompt the user to close running applications while trying to install this version. Simply click “Ok” with the default highlighted option.
  * DNS resolution may be broken when the following conditions are all true: 
    * The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
    * A custom DNS server address is configured on the primary network adapter.
    * The custom DNS server address on the primary network adapter is changed while the client is connected.  
To work around this issue, please reconnect the client by selecting "disconnect" and then "connect" in the client user interface.


