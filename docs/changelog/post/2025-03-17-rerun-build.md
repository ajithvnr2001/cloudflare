---
url: https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/
title: Retry Pages & Workers Builds Directly from GitHub \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:06.492249+00:00
---

# Retry Pages & Workers Builds Directly from GitHub · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 17, 2025

## Retry Pages & Workers Builds Directly from GitHub

[Workers](https://developers.cloudflare.com/workers/)[Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now retry your Cloudflare Pages and Workers builds directly from GitHub. No need to switch to the Cloudflare Dashboard for a simple retry!

Let\u2019s say you push a commit, but your build fails due to a spurious error like a network timeout. Instead of going to the Cloudflare Dashboard to manually retry, you can now rerun the build with just a few clicks inside GitHub, keeping you inside your workflow.

For Pages and Workers projects connected to a GitHub repository:

  1. When a build fails, go to your GitHub repository or pull request
  2. Select the failed Check Run for the build
  3. Select "Details" on the Check Run
  4. Select "Rerun" to trigger a retry build for that commit



Learn more about [Pages Builds](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/) and [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/).
