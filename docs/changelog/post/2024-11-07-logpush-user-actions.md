---
url: https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/
title: Use Logpush for Email security user actions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:59.704365+00:00
---

# Use Logpush for Email security user actions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 7, 2024

## Use Logpush for Email security user actions

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.

Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.

When creating a new Logpush job, remember to select **Audit logs** as the dataset and filter by:

  * **Field** : `"ResourceType"`
  * **Operator** : `"starts with"`
  * **Value** : `"email_security"`.

![Logpush-user-actions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=829,height=454,format=webp/_astro/Logpush-User-Actions.D14fWgmq.png)

For more information, refer to [Enable user action logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs).

This feature is available across all Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**


