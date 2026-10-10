---
url: https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/
title: New Cloudflare Status page \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.237258+00:00
---

# New Cloudflare Status page · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 11, 2026

## New Cloudflare Status page

[Support](https://developers.cloudflare.com/support/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare Status page at [www.cloudflarestatus.com ↗︎](https://www.cloudflarestatus.com/) has been rebuilt. It is available at the same address, and every previously documented [Status API ↗︎](https://www.cloudflarestatus.com/api) endpoint remains supported, so existing bookmarks, integrations, and monitoring continue to work.

#### Notifications that fire even when Cloudflare is down

The status page now has its own notification system, delivered independently of Cloudflare infrastructure. You can subscribe by email, webhook, Slack, Discord, or Google Chat.

The **Maintenance Notification** and **Incident Alerts** in [Cloudflare Notifications](https://developers.cloudflare.com/notifications/) remain supported, and deliver to the destinations already configured on your account.

#### Markdown for AI agents

Every page on the status page returns Markdown when requested with an `Accept: text/markdown` header, so agents can read the current status without parsing HTML:
    
    
    curl -H "Accept: text/markdown" https://www.cloudflarestatus.com/locations

#### Separate feeds for incidents and maintenance

Incidents and maintenance are published as separate feeds, each available in RSS and Atom, so you can subscribe to one without the other:
    
    
    https://www.cloudflarestatus.com/api/v3/incidents.rss
    https://www.cloudflarestatus.com/api/v3/incidents.atom
    https://www.cloudflarestatus.com/api/v3/maintenance.rss
    https://www.cloudflarestatus.com/api/v3/maintenance.atom

For more information, refer to [Cloudflare Status](https://developers.cloudflare.com/support/cloudflare-status/).
