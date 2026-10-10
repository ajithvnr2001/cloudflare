---
url: https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/
title: Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.278718+00:00
---

# Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 8, 2026

## Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion

[Workers AI](https://developers.cloudflare.com/workers-ai/)[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers AI [Markdown conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) (`toMarkdown`) now supports `.gif` and `.bmp` image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.

GIF and BMP files run through the same [image pipeline](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/#images) as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.

[AI Search](https://developers.cloudflare.com/ai-search/) uses `toMarkdown` automatically to process the files it ingests, so any `.gif` and `.bmp` files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.

Learn more about [Markdown conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) and the full list of [AI Search's supported file types](https://developers.cloudflare.com/ai-search/configuration/data-source/#supported-file-types).
