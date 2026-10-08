---
url: https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/
title: Workers AI Markdown Conversion: New endpoint to list supported formats \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:26.852661+00:00
---

# Workers AI Markdown Conversion: New endpoint to list supported formats · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 23, 2025

## Workers AI Markdown Conversion: New endpoint to list supported formats

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-23-new-markdown-conversion-endpoint/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Developers can now programmatically retrieve a list of all file formats supported by the [Markdown Conversion utility](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) in Workers AI.

You can use the [`env.AI`](https://developers.cloudflare.com/workers-ai/configuration/bindings/) binding:
    
    
    await env.AI.toMarkdown().supported()

Or call the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \
      -H 'Authorization: Bearer {API_TOKEN}'

Both return a list of file formats that users can convert into Markdown:
    
    
    [
    	{
    		"extension": ".pdf",
    		"mimeType": "application/pdf",
    	},
    	{
    		"extension": ".jpeg",
    		"mimeType": "image/jpeg",
    	},
    	...
    ]

Learn more about our [Markdown Conversion utility](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/).
