---
url: https://developers.cloudflare.com/changelog/post/2026-10-01-infrastructure-target-tag-permissions/
title: Simplified permissions for tagging targets with Access for Infrastructure \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:18.389907+00:00
---

# Simplified permissions for tagging targets with Access for Infrastructure · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-01-infrastructure-target-tag-permissions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2026

## Simplified permissions for tagging targets with Access for Infrastructure

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-infrastructure-target-tag-permissions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now tag [targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets) using only the `Zero Trust Write` API token permission. Previously, tagging targets through the API required both `Zero Trust Write` and `Tag Write` permissions on the API token.

This change applies to inline target tagging through the [Infrastructure Access Targets API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/). Tagging resources through the general [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/) still requires the `Tag Admin`, `Tag Write`, or equivalent role.

For more information, refer to [Tag targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets).
