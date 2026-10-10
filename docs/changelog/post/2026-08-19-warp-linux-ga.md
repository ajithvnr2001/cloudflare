---
url: https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/
title: Cloudflare One Client for Linux (version 2026.7.1343.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.635220+00:00
---

# Cloudflare One Client for Linux (version 2026.7.1343.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2026

## Cloudflare One Client for Linux (version 2026.7.1343.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

  * When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
  * When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.



**Additional changes and improvements**

  * Fixed the client not allowing login to another organization when currently showing "Device not in organization."
  * A DNS search domain parsing failure no longer prevents connection.
  * Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
  * Fixed missing certificate error display due to a race condition.
  * Fixed empty black window after transitioning from docked dual displays to undocked/internal display.
  * Fixed hostname routes not working for Cloudflare Mesh when the IP addresses of the hostnames are local addresses.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.


