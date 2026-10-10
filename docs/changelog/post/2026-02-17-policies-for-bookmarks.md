---
url: https://developers.cloudflare.com/changelog/post/2026-02-17-policies-for-bookmarks/
title: Policies for bookmark applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.573255+00:00
---

# Policies for bookmark applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-17-policies-for-bookmarks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 17, 2026

## Policies for bookmark applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now assign [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) to [bookmark applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/bookmarks/). This lets you control which users see a bookmark in the [App Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/) based on identity, device posture, and other policy rules.

Previously, bookmark applications were visible to all users in your organization. With policy support, you can now:

  * **Tailor the App Launcher to each user** — Users only see the applications they have access to, reducing clutter and preventing accidental clicks on irrelevant resources.
  * **Restrict visibility of sensitive bookmarks** — Limit who can view bookmarks to internal tools or partner resources based on group membership, identity provider, or device posture.



Bookmarks support all [Access policy configurations](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) except purpose justification, temporary authentication, and application isolation. If no policy is assigned, the bookmark remains visible to all users (maintaining backwards compatibility).

For more information, refer to [Add bookmarks](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/bookmarks/).
