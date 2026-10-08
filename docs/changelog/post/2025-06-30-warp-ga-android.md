---
url: https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-android/
title: Cloudflare One Agent for Android (version 2.4.2) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:15.529110+00:00
---

# Cloudflare One Agent for Android (version 2.4.2) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-android/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 30, 2025

## Cloudflare One Agent for Android (version 2.4.2)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-android/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Android Cloudflare One Agent is now available in the [Google Play Store ↗︎](https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent). This release contains improvements and new exciting features, including [post-quantum cryptography](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum). By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate [protection of post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) without needing to upgrade any of your individual corporate applications or systems.

**Changes and improvements**

  * QLogs are now disabled by default and can be enabled in the app by turning on **Enable qlogs** under **Settings** > **Advanced** > **Diagnostics** > **Debug Logs**. The QLog setting from previous releases will no longer be respected.
  * DNS over HTTPS traffic is now included in the WARP tunnel by default.
  * The WARP client now applies [post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by [MDM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum).
  * Fixed an issue that caused WARP connection failures on ChromeOS devices.


