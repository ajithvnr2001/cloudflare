---
url: https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/
title: Identity-aware controls are now available in AI Gateway \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.872713+00:00
---

# Identity-aware controls are now available in AI Gateway · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 5, 2026

## Identity-aware controls are now available in AI Gateway

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:

  * **Protect your gateway endpoint.** Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.
  * **Identity-aware controls.** When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.



With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as `cf.user_id`.

For setup instructions, refer to [Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access/).
