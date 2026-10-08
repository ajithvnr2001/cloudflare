---
url: https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/
title: Source Maps are Generally Available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:07.576897+00:00
---

# Source Maps are Generally Available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 25, 2025

## Source Maps are Generally Available

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-25-gzip-source-maps/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Source maps are now Generally Available (GA). You can now be uploaded with a maximum gzipped size of 15 MB. Previously, the maximum size limit was 15 MB uncompressed.

Source maps help map between the original source code and the transformed/minified code that gets deployed to production. By uploading your source map, you allow Cloudflare to map the stack trace from exceptions onto the original source code making it easier to debug.

![Stack Trace without Source Map remapping](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1908,height=198,format=webp/_astro/without-source-map.ByYR83oU.png)

With **no source maps uploaded** : notice how all the Javascript has been minified to one file, so the stack trace is missing information on file name, shows incorrect line numbers, and incorrectly references `js` instead of `ts`.

![Stack Trace with Source Map remapping](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1850,height=238,format=webp/_astro/with-source-map.PipytmVe.png)

With **source maps uploaded** : all methods reference the correct files and line numbers.

Uploading source maps and stack trace remapping happens out of band from the Worker execution, so source maps do not affect upload speed, bundle size, or cold starts. The remapped stack traces are accessible through Tail Workers, Workers Logs, and Workers Logpush.

To enable source maps, add the following to your [Pages Function's](https://developers.cloudflare.com/pages/functions/source-maps/) or [Worker's](https://developers.cloudflare.com/workers/observability/source-maps/) wrangler configuration:
    
    
    {
    	"upload_source_maps": true
    }
    
    
    upload_source_maps = true
