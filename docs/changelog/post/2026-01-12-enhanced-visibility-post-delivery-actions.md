---
url: https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/
title: Enhanced visibility for post-delivery actions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:33.502456+00:00
---

# Enhanced visibility for post-delivery actions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 12, 2026

## Enhanced visibility for post-delivery actions

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Action Log now provides enriched data for post-delivery actions to improve troubleshooting. In addition to success confirmations, failed actions now display the targeted Destination folder and a specific failure reason within the Activity field.

Note

Error messages will vary depending on whether you are using Google Workspace or Microsoft 365.

![failure-log-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2348,height=1692,format=webp/_astro/enhanced-visibility-post-delivery-actions.BNiyPtJU.png)

This update allows you to see the full lifecycle of a failed action. For instance, if an administrator tries to move an email that has already been deleted or moved manually, the log will now show the multiple retry attempts and the specific destination error.

This applies to all Email Security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**


