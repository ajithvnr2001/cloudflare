---
url: https://developers.cloudflare.com/changelog/post/2025-01-30-browser-rendering-more-instances/
title: Increased Browser Rendering limits! \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.296575+00:00
---

# Increased Browser Rendering limits! · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-30-browser-rendering-more-instances/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 30, 2025

## Increased Browser Rendering limits!

[Workers](https://developers.cloudflare.com/workers/)[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Rendering](https://developers.cloudflare.com/browser-run/) now supports 10 concurrent browser instances per account _and_ 10 new instances per minute, up from the previous limits of 2.

This allows you to launch more browser tasks from [Cloudflare Workers](https://developers.cloudflare.com/workers).

To manage concurrent browser sessions, you can use [Queues](https://developers.cloudflare.com/queues/) or [Workflows](https://developers.cloudflare.com/workflows/):

index.jsjs
    
    
    export default {
    	async queue(batch, env) {
    		for (const message of batch.messages) {
    			const browser = await puppeteer.launch(env.BROWSER);
    			const page = await browser.newPage();
    
    			try {
    				await page.goto(message.url, {
    					waitUntil: message.waitUntil,
    				});
    				// Process page...
    			} finally {
    				await browser.close();
    			}
    		}
    	},
    };

index.tsts
    
    
    interface QueueMessage {
    	url: string;
    	waitUntil: number;
    }
    
    export interface Env {
    	BROWSER_QUEUE: Queue<QueueMessage>;
    	BROWSER: Fetcher;
    }
    
    export default {
    	async queue(batch: MessageBatch<QueueMessage>, env: Env): Promise<void> {
    		for (const message of batch.messages) {
    			const browser = await puppeteer.launch(env.BROWSER);
    			const page = await browser.newPage();
    
    			try {
    				await page.goto(message.url, {
    					waitUntil: message.waitUntil,
    				});
    				// Process page...
    			} finally {
    				await browser.close();
    			}
    		}
    	},
    };
