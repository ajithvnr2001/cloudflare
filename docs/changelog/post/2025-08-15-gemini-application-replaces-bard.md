---
url: https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/
title: Google Bard Application replaced by Gemini \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.036528+00:00
---

# Google Bard Application replaced by Gemini · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-15-gemini-application-replaces-bard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 22, 2025

## Google Bard Application replaced by Gemini

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The **Google Bard** application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the **Gemini** application (ID: 1340). Any existing Gateway policies that reference the old Google Bard application will no longer function. To ensure your policies continue to work as intended, you should update them to use the new Gemini application. We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies. For more information about application policies, please see the [Cloudflare Gateway documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).
