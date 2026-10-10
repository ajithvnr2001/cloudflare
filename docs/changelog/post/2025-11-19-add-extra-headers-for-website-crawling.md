---
url: https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/
title: AI Search support for crawling login protected website content \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.557405+00:00
---

# AI Search support for crawling login protected website content · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2025

## AI Search support for crawling login protected website content

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports [custom HTTP headers](https://developers.cloudflare.com/ai-search/configuration/data-source/website/authentication-headers/) for website crawling, solving a common problem where valuable content behind authentication or access controls could not be indexed.

Previously, AI Search could only crawl publicly accessible pages, leaving knowledge bases, documentation, and other protected content out of your search results. With custom headers support, you can now include authentication credentials that allow the crawler to access this protected content.

This is particularly useful for indexing content like:

  * **Internal documentation** behind corporate login systems
  * **Premium content** that requires users to provide access to unlock
  * **Sites protected by Cloudflare Access** using service tokens



To add custom headers when creating an AI Search instance, select **Parse options**. In the **Extra headers** section, you can add up to five custom headers per Website data source.

![Custom headers configuration in AI Search](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1098,height=287,format=webp/_astro/ai-search-extra-headers.B7A2spby.png)

For example, to crawl a site protected by [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/), you can add service token credentials as custom headers:
    
    
    CF-Access-Client-Id: your-token-id.access
    CF-Access-Client-Secret: your-token-secret

The crawler will automatically include these headers in all requests, allowing it to access protected pages that would otherwise be blocked.

Learn more about [configuring custom headers for website crawling](https://developers.cloudflare.com/ai-search/configuration/data-source/website/authentication-headers/) in AI Search.
