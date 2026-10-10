---
url: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/
title: AI Search UI snippets and MCP support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.858733+00:00
---

# AI Search UI snippets and MCP support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 23, 2026

## AI Search UI snippets and MCP support

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports public endpoints, UI snippets, and MCP, making it easy to add search to your website or connect AI agents.

Public endpoints allow you to expose AI Search capabilities without requiring API authentication. To enable public endpoints:

  1. Go to **AI Search** in the Cloudflare dashboard. [ Go to **AI Search** ↗ ](https://dash.cloudflare.com/?to=/:account/ai/ai-search)
  2. Select your instance, and turn on **Public Endpoint** in **Settings**. For more details, refer to [Public endpoint configuration](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/).



#### UI snippets

UI snippets are pre-built search and chat components you can embed in your website. Visit [search.ai.cloudflare.com ↗︎](https://search.ai.cloudflare.com/) to configure and preview components for your AI Search instance.

![Example of the search-modal-snippet component](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1842,height=806,format=webp/_astro/ui-snippet-search-modal.nSXbvcsi.png)

To add a search modal to your page:
    
    
    <script
    	type="module"
    	src="https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js"
    ></script>
    
    <search-modal-snippet
    	api-url="https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/"
    	placeholder="Search..."
    >
    </search-modal-snippet>

For more details, refer to the [UI snippets documentation](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/).

#### MCP

The MCP endpoint allows AI agents to search your content via the Model Context Protocol. Connect your MCP client to:
    
    
    https://<PUBLIC_ENDPOINT_ID>.search.ai.cloudflare.com/mcp

For more details, refer to the [MCP documentation](https://developers.cloudflare.com/ai-search/api/search/mcp/).
