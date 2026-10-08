---
url: https://developers.cloudflare.com/changelog/post/2026-04-02-warp-linux-ga/
title: Cloudflare One Client for Linux (version 2026.3.846.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:45.074350+00:00
---

# Cloudflare One Client for Linux (version 2026.3.846.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-02-warp-linux-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 2, 2026

## Cloudflare One Client for Linux (version 2026.3.846.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-02-warp-linux-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes and improvements.

The next stable release for Linux will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.

**Changes and improvements**

  * Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
  * Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.
  * Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.
  * Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
  * Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
  * Added monitoring for tunnel statistics collection timeouts.
  * Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.
  * Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.


