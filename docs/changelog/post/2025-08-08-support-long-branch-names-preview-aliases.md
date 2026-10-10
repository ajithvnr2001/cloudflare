---
url: https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/
title: Workers per-branch preview URLs now support long branch names \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.220695+00:00
---

# Workers per-branch preview URLs now support long branch names · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 14, 2025

## Workers per-branch preview URLs now support long branch names

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've updated [preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) for Cloudflare Workers to support long branch names.

Previously, branch and Worker names exceeding the 63-character DNS limit would cause alias generation to fail, leaving pull requests without aliased preview URLs. This particularly impacted teams relying on descriptive branch naming.

Now, Cloudflare automatically truncates long branch names and appends a unique hash, ensuring every pull request gets a working preview link.

#### How it works

  * **63 characters or less** : `<branch-name>-<worker-name>` → Uses actual branch name as is
  * **64 characters or more** : `<truncated-branch-name>--<hash>-<worker-name>` → Uses truncated name with 4-character hash
  * **Hash generation** : The hash is derived from the full branch name to ensure uniqueness
  * **Stable URLs** : The same branch always generates the same hash across all commits



#### Requirements and compatibility

  * **Wrangler 4.30.0 or later** : This feature requires updating to wrangler@4.30.0+
  * **No configuration needed** : Works automatically with existing preview URL setups


