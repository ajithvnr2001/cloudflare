---
url: https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/
title: New granular API token permissions for Cloudflare Access \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:34.592545+00:00
---

# New granular API token permissions for Cloudflare Access · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 22, 2026

## New granular API token permissions for Cloudflare Access

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Three new API token permissions are available for Cloudflare Access, giving you finer-grained control when building automations and integrations:

  * **Access: Organizations Revoke** — Grants the ability to [revoke user sessions](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions) in a Zero Trust organization. Use this permission when you need a token that can terminate active sessions without broader write access to organization settings.
  * **Access: Population Read** — Grants read access to the [SCIM users and groups](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/) synced from an identity provider to Cloudflare Access. Use this permission for tokens that only need to read synced user and group data.
  * **Access: Population Write** — Grants write access to the [SCIM users and groups](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/) synced from an identity provider to Cloudflare Access. Use this permission for tokens that need to create or modify synced user and group data.



These permissions are scoped at the account level and can be combined with existing Access permissions.

For a full list of available permissions, refer to [API token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/).
