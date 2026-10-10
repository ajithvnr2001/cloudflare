---
url: https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/
title: Access for Infrastructure now supports tagged targets and tag-based target criteria \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.200213+00:00
---

# Access for Infrastructure now supports tagged targets and tag-based target criteria · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 15, 2026

## Access for Infrastructure now supports tagged targets and tag-based target criteria

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now integrates with [Resource Tagging](https://developers.cloudflare.com/resource-tagging/). You can attach key-value tags to [infrastructure targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target) and use them in access policies.

You can manage tags on targets inline when you create or edit a target or through the central [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/). Cloudflare keeps tags in sync across both methods.

Infrastructure applications also support a target criteria model with `include`, `require`, and `exclude` operators. Each operator can match targets by hostname, tag, or both.

  * **Include** matches targets that have any of the specified values.
  * **Require** matches targets that have all of the specified values.
  * **Exclude** rejects targets that have any of the specified values.

![Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2372,height=1616,format=webp/_astro/tags-in-infra-app.ja2Tp-Gq.png)

For more information, refer to [Add an infrastructure application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/).
