---
url: https://developers.cloudflare.com/changelog/post/2026-10-07-warp-linux-ga/
title: Cloudflare One Client for Linux (version 2026.8.2100.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.216352+00:00
---

# Cloudflare One Client for Linux (version 2026.8.2100.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-07-warp-linux-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 7, 2026

## Cloudflare One Client for Linux (version 2026.8.2100.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client window not appearing on first launch after a fresh install on RHEL 10.
  * Fixed duplicate WARP routing policy rules accumulating on reconnect.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.


