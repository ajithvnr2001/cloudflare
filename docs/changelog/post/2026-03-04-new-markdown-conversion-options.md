---
url: https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/
title: New conversion options for Markdown Conversion \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.786680+00:00
---

# New conversion options for Markdown Conversion · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 4, 2026

## New conversion options for Markdown Conversion

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now customize how the [Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) service processes different file types by passing a `conversionOptions` object.

Available options:

  * **Images** : Set the language for AI-generated image descriptions
  * **HTML** : Use CSS selectors to extract specific content, or provide a hostname to resolve relative links
  * **PDF** : Exclude metadata from the output



Use the [`env.AI`](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/) binding:
    
    
    await env.AI.toMarkdown(
    	{ name: "page.html", blob: new Blob([html]) },
    	{
    		conversionOptions: {
    			html: { cssSelector: "article.content" },
    			image: { descriptionLanguage: "es" },
    		},
    	},
    );
    
    
    await env.AI.toMarkdown(
    	{ name: "page.html", blob: new Blob([html]) },
    	{
    		conversionOptions: {
    			html: { cssSelector: "article.content" },
    			image: { descriptionLanguage: "es" },
    		},
    	},
    );

Or call the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \
      -H 'Authorization: Bearer {API_TOKEN}' \
      -F 'files=@index.html' \
      -F 'conversionOptions={"html": {"cssSelector": "article.content"}}'

For more details, refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/).
