---
url: https://developers.cloudflare.com/changelog/post/2026-08-19-warp-windows-ga/
title: Cloudflare One Client for Windows (version 2026.7.1343.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:09.488818+00:00
---

# Cloudflare One Client for Windows (version 2026.7.1343.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-19-warp-windows-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2026

## Cloudflare One Client for Windows (version 2026.7.1343.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-19-warp-windows-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

  * When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
  * When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.



**Additional changes and improvements**

  * Fixed a process leak in the Windows GUI that could exhaust system resources during IPC client-creation failures.
  * Fixed being unable to switch organizations when the client was stuck in the "Device not in organization" state.
  * Fixed an issue where Microsoft Defender would falsely flag the Cloudflare One Client installation as malicious when installing with Intune.
  * Made the Windows domain-joined posture check more reliable.
  * A DNS search domain parsing failure no longer prevents connection.
  * Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
  * Fixed missing certificate error display due to a race condition.
  * Fixed empty black window after transitioning from docked dual displays to undocked/internal display.



**Known issues**

  * If a user upgrades to version 2026.7.1343.0, downgrades to an earlier version, re-registers, and then upgrades back to 2026.7.1343.0, the client might fail to connect or switch organizations. To resolve this issue, run `warp-cli registration delete` or `warp-cli registration delete-all`.


