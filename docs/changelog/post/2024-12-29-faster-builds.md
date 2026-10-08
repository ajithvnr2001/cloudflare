---
url: https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/
title: Faster Workers Builds with Build Caching and Watch Paths \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:00.293943+00:00
---

# Faster Workers Builds with Build Caching and Watch Paths · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 29, 2024

## Faster Workers Builds with Build Caching and Watch Paths

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2024-12-29-faster-builds/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

![Build caching settings](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1494,height=140,format=webp/_astro/workers-build-caching.DWEh3Tj1.png)![Build watch path settings](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1494,height=190,format=webp/_astro/workers-build-watch-paths.ClqD-iNq.png)

[**Workers Builds**](https://developers.cloudflare.com/workers/ci-cd/builds/), the integrated CI/CD system for Workers (currently in beta), now lets you cache artifacts across builds, speeding up build jobs by eliminating repeated work, such as downloading dependencies at the start of each build.

  * **[Build Caching](https://developers.cloudflare.com/workers/ci-cd/builds/build-caching/)** : Cache dependencies and build outputs between builds with a shared project-wide cache, ensuring faster builds for the entire team.

  * **[Build Watch Paths](https://developers.cloudflare.com/workers/ci-cd/builds/build-watch-paths/)** : Define paths to include or exclude from the build process, ideal for [monorepos](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#monorepos) to target only the files that need to be rebuilt per Workers project.




To get started, select your Worker on the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) then go to **Settings** > **Builds** , and connect a GitHub or GitLab repository. Once connected, you'll see options to configure Build Caching and Build Watch Paths.
