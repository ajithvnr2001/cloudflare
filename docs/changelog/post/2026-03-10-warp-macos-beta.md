---
url: https://developers.cloudflare.com/changelog/post/2026-03-10-warp-macos-beta/
title: WARP client for macOS (version 2026.3.566.1) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:40.510498+00:00
---

# WARP client for macOS (version 2026.3.566.1) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-10-warp-macos-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 10, 2026

## WARP client for macOS (version 2026.3.566.1)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-10-warp-macos-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new Beta release for the macOS WARP client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the [Cloudflare Community forum](https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362) and let us know.

**Changes and improvements**

  * Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
  * Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.
  * Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.
  * Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
  * Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
  * Added monitoring for tunnel statistics collection timeouts.
  * Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.
  * Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.



**Known issues**

  * The client may become stuck in a `Connecting` state. To resolve this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface. Alternatively, change the client's operation mode.
  * The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.
  * Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.


