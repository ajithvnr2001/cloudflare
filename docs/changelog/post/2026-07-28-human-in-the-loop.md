---
url: https://developers.cloudflare.com/changelog/post/2026-07-28-human-in-the-loop/
title: Browser Run adds structured handoff for Human in the Loop \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.244327+00:00
---

# Browser Run adds structured handoff for Human in the Loop · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-28-human-in-the-loop/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 28, 2026

## Browser Run adds structured handoff for Human in the Loop

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) now supports structured handoff for [Human in the Loop](https://developers.cloudflare.com/browser-run/features/human-in-the-loop/) workflows. Using Cloudflare-specific [CDP commands](https://developers.cloudflare.com/browser-run/features/human-in-the-loop/#cloudflare-cdp-commands), your agent can signal that it needs help, a human steps in through [Live View](https://developers.cloudflare.com/browser-run/features/live-view/) to handle the task, and the agent resumes once the work is done.

For agents running multi-step browser workflows, a single login wall or unexpected prompt can fail the entire run. Previously, scripts had to manage human intervention manually by sharing a Live View URL and polling for completion. Structured handoff replaces this with a formal pause-and-resume flow.

The following example requests human intervention for a login page and waits for the human to finish before continuing:
    
    
    const cdp = await page.createCDPSession();
    
    // Get Live View URL for the human operator
    const { devtoolsFrontendUrl } = await cdp.send("Cloudflare.getLiveView", {
    	mode: "tab",
    });
    console.log(`Human input needed: ${devtoolsFrontendUrl}`);
    
    // Request human intervention and wait for completion
    const handoffComplete = new Promise((resolve) => {
    	cdp.once("Cloudflare.handoffComplete", resolve);
    });
    
    await cdp.send("Cloudflare.handoff", {
    	instructions: "Please log in with your credentials",
    	timeout: 600000,
    });
    
    const result = await handoffComplete;
    console.log(result.success ? "Handoff complete" : `Failed: ${result.reason}`);

Refer to the [Human in the Loop documentation](https://developers.cloudflare.com/browser-run/features/human-in-the-loop/) for the full API reference, examples, and best practices.
