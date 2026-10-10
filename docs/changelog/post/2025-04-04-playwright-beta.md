---
url: https://developers.cloudflare.com/changelog/post/2025-04-04-playwright-beta/
title: Playwright for Browser Rendering now available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.482958+00:00
---

# Playwright for Browser Rendering now available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-04-playwright-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 4, 2025

## Playwright for Browser Rendering now available

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to share that you can now use Playwright's browser automation [capabilities ↗︎](https://playwright.dev/docs/api/class-playwright) from Cloudflare [Workers](https://developers.cloudflare.com/workers/).

[Playwright ↗︎](https://playwright.dev/) is an open-source package developed by Microsoft that can do browser automation tasks; it's commonly used to write software tests, debug applications, create screenshots, and crawl pages. Like [Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/), we [forked ↗︎](https://github.com/cloudflare/playwright) Playwright and modified it to be compatible with Cloudflare Workers and [Browser Rendering](https://developers.cloudflare.com/browser-run/).

Below is an example of how to use Playwright with Browser Rendering to test a TODO application using assertions:

Assertion examplets
    
    
    import { launch, type BrowserWorker } from "@cloudflare/playwright";
    import { expect } from "@cloudflare/playwright/test";
    
    interface Env {
    	MYBROWSER: BrowserWorker;
    }
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const browser = await launch(env.MYBROWSER);
    		const page = await browser.newPage();
    
    		await page.goto("https://demo.playwright.dev/todomvc");
    
    		const TODO_ITEMS = [
    			"buy some cheese",
    			"feed the cat",
    			"book a doctors appointment",
    		];
    
    		const newTodo = page.getByPlaceholder("What needs to be done?");
    		for (const item of TODO_ITEMS) {
    			await newTodo.fill(item);
    			await newTodo.press("Enter");
    		}
    
    		await expect(page.getByTestId("todo-title")).toHaveCount(TODO_ITEMS.length);
    
    		await Promise.all(
    			TODO_ITEMS.map((value, index) =>
    				expect(page.getByTestId("todo-title").nth(index)).toHaveText(value),
    			),
    		);
    	},
    };

Playwright is available as an npm package at [`@cloudflare/playwright` ↗︎](https://www.npmjs.com/package/@cloudflare/playwright) and the code is at [GitHub ↗︎](https://github.com/cloudflare/playwright).

Learn more in our [documentation](https://developers.cloudflare.com/browser-run/playwright/).
