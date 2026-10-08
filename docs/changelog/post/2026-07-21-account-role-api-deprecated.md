---
url: https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/
title: Account Role API deprecated \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:03.959058+00:00
---

# Account Role API deprecated · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 21, 2026

## Account Role API deprecated

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Account Roles API](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/) is deprecated and is being replaced by the [Permission Groups API](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/). An end of life date has not yet been established.

#### What you need to do

Review the [Permission Groups API](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/) documentation; the response schema differs from the legacy Roles response.

#### Highlights

  * Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.
  * The legacy `Role` response includes a top-level `description` and a `permissions` object keyed by resource type with edit/read flags.
  * The `PermissionGroup` response replaces those with a `meta` object containing `label` and `scopes`. Individual permissions are not returned as part of the permission group.
  * The new API supports the [API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) authorization scheme. The legacy Email + API Key authorization schema is provided for backwards compatibility.



For more information, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).
