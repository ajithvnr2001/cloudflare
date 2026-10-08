---
url: https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/
title: Expanded Email Link Isolation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:18.674826+00:00
---

# Expanded Email Link Isolation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2025

## Expanded Email Link Isolation

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.

For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.

![Expanded Email Link Isolation Configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=497,format=webp/_astro/expanded-link-actions.DziIg6E8.jpg)

To isolate all links within a message based on the disposition, select **Settings** > **Link Actions** > **View** and select **Configure**. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on [Configure link actions ↗︎](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/).

This feature is available across these Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**


