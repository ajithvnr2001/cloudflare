---
url: https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/
title: AI Search path filtering for website and R2 data sources \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.925947+00:00
---

# AI Search path filtering for website and R2 data sources · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-path-filtering/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 20, 2026

## AI Search path filtering for website and R2 data sources

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now includes [path filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/path-filtering/) for both [website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/#path-filtering) and [R2](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/#path-filtering) data sources. You can now control which content gets indexed by defining include and exclude rules for paths.

By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.

![Path filtering configuration in AI Search](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2346,height=1360,format=webp/_astro/path-filtering.BCH7HN-Q.png)

Path filtering uses [micromatch ↗︎](https://github.com/micromatch/micromatch) patterns, so you can use `*` to match within a directory and `**` to match across directories.

Use case | Include | Exclude  
---|---|---  
Index docs but skip drafts | `**/docs/**` | `**/docs/drafts/**`  
Keep admin pages out of results | — | `**/admin/**`  
Index only English content | `**/en/**` | —  
  
Configure path filters when creating a new instance or update them anytime from **Settings**. Check out [path filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/path-filtering/) to learn more.
