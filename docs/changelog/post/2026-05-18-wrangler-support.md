---
url: https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/
title: Manage Artifacts namespaces and repos with Wrangler CLI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:53.643788+00:00
---

# Manage Artifacts namespaces and repos with Wrangler CLI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 18, 2026

## Manage Artifacts namespaces and repos with Wrangler CLI

[Artifacts](https://developers.cloudflare.com/artifacts/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now manage [Artifacts](https://developers.cloudflare.com/artifacts/) namespaces, repos, and repo-scoped tokens directly from Wrangler CLI.

Available commands:

  * `wrangler artifacts namespaces list` — List Artifacts namespaces in your account.
  * `wrangler artifacts namespaces get` — Get metadata for a namespace.
  * `wrangler artifacts repos create` — Create a repo in a namespace.
  * `wrangler artifacts repos list` — List repos in a namespace.
  * `wrangler artifacts repos get` — Get metadata for a repo.
  * `wrangler artifacts repos delete` — Delete a repo.
  * `wrangler artifacts repos issue-token` — Issue a repo-scoped token for Git access.



To get started, refer to the [Wrangler Artifacts commands documentation](https://developers.cloudflare.com/workers/wrangler/commands/artifacts/).
