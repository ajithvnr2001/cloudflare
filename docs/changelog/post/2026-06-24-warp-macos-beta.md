---
url: https://developers.cloudflare.com/changelog/post/2026-06-24-warp-macos-beta/
title: Cloudflare One Client for macOS (version 2026.6.782.1) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:59.562298+00:00
---

# Cloudflare One Client for macOS (version 2026.6.782.1) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-24-warp-macos-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 24, 2026

## Cloudflare One Client for macOS (version 2026.6.782.1)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-24-warp-macos-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release introduces upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation.

**Additional changes and improvements**

This release also introduces multiple fixes and improvements including:

  * Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.
  * Path MTU Discovery (PMTUD) is now enabled by default.
  * Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.
  * Users can now register with team names in any case format without errors.
  * New UI fixes 
    * Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.
    * Added a re-auth button and banner to the home screen so users don't miss it when their session expires.
    * Added clear error messaging when the Cloudflare certificate needs to be installed.
    * Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.
    * New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.
    * Added ability to configure proxy mode for consumer users.
    * Added back the option to quit for consumer users.



**Known issues**

  * Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.


