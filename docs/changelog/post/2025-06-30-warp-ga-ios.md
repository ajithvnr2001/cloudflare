---
url: https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/
title: Cloudflare One Agent for iOS (version 1.11) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:15.553431+00:00
---

# Cloudflare One Agent for iOS (version 1.11) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 30, 2025

## Cloudflare One Agent for iOS (version 1.11)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-30-warp-ga-ios/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the iOS Cloudflare One Agent is now available in the [iOS App Store ↗︎](https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492). This release contains improvements and new exciting features, including [post-quantum cryptography](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum). By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate [protection of post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) without needing to upgrade any of your individual corporate applications or systems.

**Changes and improvements**

  * QLogs are now disabled by default and can be enabled in the app by turning on **Enable qlogs** under **Settings** > **Advanced** > **Diagnostics** > **Debug Logs**. The QLog setting from previous releases will no longer be respected.
  * DNS over HTTPS traffic is now included in the WARP tunnel by default.
  * The WARP client now applies [post-quantum cryptography ↗︎](https://blog.cloudflare.com/pq-2024/) end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by [MDM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum).


