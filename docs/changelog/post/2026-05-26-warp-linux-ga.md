---
url: https://developers.cloudflare.com/changelog/post/2026-05-26-warp-linux-ga/
title: Cloudflare One Client for Linux (version 2026.4.1390.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:54.573629+00:00
---

# Cloudflare One Client for Linux (version 2026.4.1390.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-26-warp-linux-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 26, 2026

## Cloudflare One Client for Linux (version 2026.4.1390.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-26-warp-linux-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces the new Cloudflare One Client UI for Linux! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:

  * Right click context menu to access the most common client actions quickly
  * Built-in captive portal login experience



**Changes and improvements**

  * Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.
  * Official support for RHEL 9 has been added for Cloudflare Mesh nodes. To install the RHEL 9 package, the Extra Packages for Enterprise Linux (EPEL) repository must be active, as it contains dependencies required for the tray icon and captive portal webview.
  * Fixed a proxy mode connection stall issue.



**Known issues**

  * Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
  * Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via `warp-cli tunnel ip` and `warp-cli tunnel host`. UI support will be added in a future release.


