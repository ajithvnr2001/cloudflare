---
url: https://developers.cloudflare.com/changelog/post/2025-05-28-playwright-mcp/
title: Playwright MCP server is now compatible with Browser Rendering \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.036149+00:00
---

# Playwright MCP server is now compatible with Browser Rendering · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-28-playwright-mcp/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2025

## Playwright MCP server is now compatible with Browser Rendering

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to share that you can now use the [Playwright MCP ↗︎](https://github.com/cloudflare/playwright-mcp) server with Browser Rendering.

Once you [deploy the server](https://developers.cloudflare.com/browser-run/playwright/playwright-mcp/#deploying), you can use any MCP client with it to interact with Browser Rendering. This allows you to run AI models that can automate browser tasks, such as taking screenshots, filling out forms, or scraping data.

![Access Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1420,height=914,format=webp/_astro/playground-ai-screenshot.v44jFMBu.png)

Playwright MCP is available as an npm package at [`@cloudflare/playwright-mcp` ↗︎](https://www.npmjs.com/package/@cloudflare/playwright-mcp). To install it, type:

npmyarnpnpmbun
    
    
    npm i -D @cloudflare/playwright-mcp
    
    
    yarn add -D @cloudflare/playwright-mcp
    
    
    pnpm add -D @cloudflare/playwright-mcp
    
    
    bun add -d @cloudflare/playwright-mcp

Deploying the server is then as easy as:
    
    
    import { env } from "cloudflare:workers";
    import { createMcpAgent } from "@cloudflare/playwright-mcp";
    
    export const PlaywrightMCP = createMcpAgent(env.BROWSER);
    export default PlaywrightMCP.mount("/sse");

Check out the full code at [GitHub ↗︎](https://github.com/cloudflare/playwright-mcp).

Learn more about Playwright MCP in our [documentation](https://developers.cloudflare.com/browser-run/playwright/playwright-mcp/).
