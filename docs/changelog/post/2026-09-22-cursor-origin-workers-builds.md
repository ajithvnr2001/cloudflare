---
url: https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/
title: Workers Builds now supports Cursor Origin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.837786+00:00
---

# Workers Builds now supports Cursor Origin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 22, 2026

## Workers Builds now supports Cursor Origin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers Builds now supports repositories hosted in Cursor Origin. Connect a Cursor Origin repository to automatically build and deploy production changes, preview non-production branches, and see build status in pull requests.

Pushes to your production branch automatically build and deploy your Worker. When you enable [non-production branch builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds), each branch receives a version-specific preview URL and a stable preview URL that follows the latest build.

Cloudflare posts build status and preview links to the Cursor Origin pull request and creates a check run for each triggered build.

To get started, install the [Cloudflare app in Cursor ↗︎](https://cursor.com/codebase/settings/apps/public/cloudflare), choose the Cursor Origin repositories Cloudflare can access, and follow the prompts to configure your Worker build. For details, refer to the [Cursor Origin integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/cursor-origin-integration/).
