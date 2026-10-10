---
url: https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/
title: Access resource lists now support resource-scoped roles \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.742402+00:00
---

# Access resource lists now support resource-scoped roles · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2026

## Access resource lists now support resource-scoped roles

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.

The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned `403` responses.

For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.

For role definitions and assignment details, refer to [Resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) and [Role scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/).
