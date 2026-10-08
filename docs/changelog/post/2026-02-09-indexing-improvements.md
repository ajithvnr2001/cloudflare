---
url: https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/
title: AI Search now with more granular controls over indexing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:36.106517+00:00
---

# AI Search now with more granular controls over indexing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 9, 2026

## AI Search now with more granular controls over indexing

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-09-indexing-improvements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Get your content updates into [AI Search](https://developers.cloudflare.com/ai-search/) faster and avoid a full rescan when you do not need it.

#### Reindex individual files without a full sync

Updated a file or need to retry one that errored? When you know exactly which file changed, you can now [reindex it directly](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/#controls) instead of rescanning your entire data source.

Go to **Overview** > **Indexed Items** and select the sync icon next to any file to reindex it immediately.

![Sync individual files from Indexed Items](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2118,height=782,format=webp/_astro/individual-file-indexing.CQgoIj85.png)

#### Crawl only the sitemap you need

By default, AI Search crawls all sitemaps listed in your `robots.txt`, up to the [maximum files per index limit](https://developers.cloudflare.com/ai-search/platform/limits-pricing/#limits). If your site has multiple sitemaps but you only want to index a specific set, you can now [specify a single sitemap URL](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#specific-sitemap) to limit what the crawler visits.

For example, if your `robots.txt` lists both `blog-sitemap.xml` and `docs-sitemap.xml`, you can specify just `https://example.com/docs-sitemap.xml` to index only your documentation.

Configure your selection anytime in **Settings** > **Parsing options** > **Specific sitemaps** , then trigger a sync to apply the changes.

![Specify a sitemap in Parsinh options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1973,height=387,format=webp/_astro/specify-sitemap.pLCkwmJ-.png)

Learn more about [indexing controls](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/#controls) and [website crawling configuration](https://developers.cloudflare.com/ai-search/configuration/data-source/website/parse-types/#specific-sitemap).
