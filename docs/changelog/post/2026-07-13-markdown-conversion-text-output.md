---
url: https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/
title: Plain text output for Markdown Conversion \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:02.774835+00:00
---

# Plain text output for Markdown Conversion · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 10, 2026

## Plain text output for Markdown Conversion

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) service now supports a new `output` conversion option that controls the format of the converted content.

Set `output.format` to `text` to receive plain text with Markdown syntax removed. The default value is `markdown`, so existing conversions are unchanged.

Use the [`env.AI`](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/) binding:
    
    
    await env.AI.toMarkdown(
    	{ name: "page.html", blob: new Blob([html]) },
    	{
    		conversionOptions: {
    			output: { format: "text" },
    		},
    	},
    );
    
    
    await env.AI.toMarkdown(
    	{ name: "page.html", blob: new Blob([html]) },
    	{
    		conversionOptions: {
    			output: { format: "text" },
    		},
    	},
    );

Or call the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \
      -H 'Authorization: Bearer {API_TOKEN}' \
      -F 'files=@index.html' \
      -F 'conversionOptions={"output": {"format": "text"}}'

When you request text output, the `format` field of each result is set to `text`. For more details, refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/#output).
