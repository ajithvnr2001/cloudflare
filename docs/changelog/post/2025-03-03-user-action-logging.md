---
url: https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/
title: Gain visibility into user actions in Zero Trust Browser Isolation sessions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.318111+00:00
---

# Gain visibility into user actions in Zero Trust Browser Isolation sessions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 4, 2025

## Gain visibility into user actions in Zero Trust Browser Isolation sessions

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to announce that new logging capabilities for [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) through [Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) are available in Beta starting today!

With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.
    
    
    {
    	"AccountID": "$ACCOUNT_ID",
    	"Decision": "block",
    	"DomainName": "www.example.com",
    	"Timestamp": "2025-02-27T23:15:06Z",
    	"Type": "copy",
    	"UserID": "$USER_ID"
    }

User Actions available:

  * **Copy & Paste**
  * **Downloads & Uploads**
  * **Printing**



Learn more about how to get started with Logpush in our [documentation](https://developers.cloudflare.com/logs/logpush/).
