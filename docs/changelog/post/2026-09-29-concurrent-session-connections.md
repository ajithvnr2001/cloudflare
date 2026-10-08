---
url: https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/
title: Connect multiple clients to one Browser Run session \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:16.823789+00:00
---

# Connect multiple clients to one Browser Run session · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 29, 2026

## Connect multiple clients to one Browser Run session

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) sessions now accept multiple concurrent connections. Before, a session accepted only one connection at a time, and other Workers had to wait until that connection closed. Now multiple Workers can connect to the same browser at the same time.

Each `puppeteer.connect()` call opens its own Chrome DevTools Protocol (CDP) connection. Create a separate browser context for each request to keep its pages, cookies, and storage apart from other clients.
    
    
    const browser = await puppeteer.connect(env.MYBROWSER, sessionId);
    const context = await browser.createBrowserContext();
    
    try {
    	const page = await context.newPage();
    	await page.goto("https://example.com");
    	// ...
    } finally {
    	await context.close();
    	await browser.disconnect(); // keep the shared browser running
    }
    
    
    const browser = await puppeteer.connect(env.MYBROWSER, sessionId);
    const context = await browser.createBrowserContext();
    
    try {
    	const page = await context.newPage();
    	await page.goto("https://example.com");
    	// ...
    } finally {
    	await context.close();
    	await browser.disconnect(); // keep the shared browser running
    }

Sharing sessions means fewer new browsers to launch, less cold-start time, and fewer [concurrent browsers](https://developers.cloudflare.com/browser-run/limits/) counted against your limits.

Concurrent connections require `@cloudflare/puppeteer` version 1.1.0 or later.

Refer to [Reuse sessions](https://developers.cloudflare.com/browser-run/features/reuse-sessions/) for a full example.
