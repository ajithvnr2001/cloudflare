---
url: https://developers.cloudflare.com/changelog/post/2025-05-15-open-links-browser-isolation/
title: Open email links with Browser Isolation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:12.297412+00:00
---

# Open email links with Browser Isolation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-15-open-links-browser-isolation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 8, 2025

## Open email links with Browser Isolation

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-15-open-links-browser-isolation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now safely open links in emails to view and investigate them.

![Open links with Browser Isolation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=558,height=204,format=webp/_astro/investigate-links.pYbpGkt5.jpg)

From **Investigation** , go to **View details** , and look for the **Links identified** section. Next to each link, the Cloudflare dashboard will display an **Open in Browser Isolation** icon which allows your team to safely open the link in a clientless, isolated browser with no risk to the analyst or your environment. Refer to [Open links](https://developers.cloudflare.com/cloudflare-one/email-security/investigation/search-email/#open-links) to learn more about this feature.

To use this feature, you must:

  * Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
  * Have **Browser Isolation (RBI)** seats assigned.



For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**


