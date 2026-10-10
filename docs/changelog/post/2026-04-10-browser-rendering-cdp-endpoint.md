---
url: https://developers.cloudflare.com/changelog/post/2026-04-10-browser-rendering-cdp-endpoint/
title: Browser Rendering adds Chrome DevTools Protocol (CDP) and MCP client support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.774503+00:00
---

# Browser Rendering adds Chrome DevTools Protocol (CDP) and MCP client support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-10-browser-rendering-cdp-endpoint/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 10, 2026

## Browser Rendering adds Chrome DevTools Protocol (CDP) and MCP client support

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Rendering](https://developers.cloudflare.com/browser-run/) now exposes the [Chrome DevTools Protocol (CDP)](https://developers.cloudflare.com/browser-run/cdp/), the low-level protocol that powers browser automation. The growing ecosystem of CDP-based agent tools, along with existing CDP automation scripts, can now use Browser Rendering directly.

Any CDP-compatible client, including [Puppeteer](https://developers.cloudflare.com/browser-run/cdp/puppeteer/) and [Playwright](https://developers.cloudflare.com/browser-run/cdp/playwright/), can connect from any environment, whether that is [Cloudflare Workers](https://developers.cloudflare.com/workers/), your local machine, or a cloud environment. All you need is your Cloudflare API key.

For any existing CDP script, switching to Browser Rendering is a one-line change:
    
    
    const puppeteer = require("puppeteer-core");
    
    const browser = await puppeteer.connect({
    	browserWSEndpoint: `wss://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/browser-rendering/devtools/browser?keep_alive=600000`,
    	headers: { Authorization: `Bearer ${API_TOKEN}` },
    });
    
    const page = await browser.newPage();
    await page.goto("https://example.com");
    console.log(await page.title());
    await browser.close();

Additionally, MCP clients like Claude Desktop, Claude Code, Cursor, and OpenCode can now use Browser Rendering as their remote browser via the [chrome-devtools-mcp ↗︎](https://github.com/ChromeDevTools/chrome-devtools-mcp) package.

Here is an example of how to configure Browser Rendering for Claude Desktop:
    
    
    {
    	"mcpServers": {
    		"browser-rendering": {
    			"command": "npx",
    			"args": [
    				"-y",
    				"chrome-devtools-mcp@latest",
    				"--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/browser-rendering/devtools/browser?keep_alive=600000",
    				"--wsHeaders={\"Authorization\":\"Bearer <API_TOKEN>\"}"
    			]
    		}
    	}
    }

To get started, refer to the [CDP documentation](https://developers.cloudflare.com/browser-run/cdp/).
