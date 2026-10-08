---
url: https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/
title: Cloudflare One Client for Windows (version 2026.8.1290.1) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:13.272631+00:00
---

# Cloudflare One Client for Windows (version 2026.8.1290.1) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 9, 2026

## Cloudflare One Client for Windows (version 2026.8.1290.1)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None


