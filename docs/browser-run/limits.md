---
url: https://developers.cloudflare.com/browser-run/limits/
title: Limits \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:38.286895+00:00
---

# Limits · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Limits



# Limits

Last updated Sep 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWorkers Free /crawl endpoint limitsWorkers PaidFAQ How can I manage concurrency and session isolation with Browser Run? Can I increase the browser timeout? Is there a maximum session duration? I upgraded from the Workers Free plan, but I'm still hitting the 10-minute per day limit. What should I do? Why is my browser usage higher than expected?Troubleshooting Error: 429 Too many requests Error: 429 Browser time limit exceeded for today

Browser Run limits are based on your [Cloudflare Workers plan](https://developers.cloudflare.com/workers/platform/pricing/).

For pricing information, refer to [Browser Run pricing](https://developers.cloudflare.com/browser-run/pricing/).

## Workers Free

Need higher limits?

If you are on a Workers Free plan and you want to increase your limits, upgrade to a Workers Paid plan in the **Workers plans** page of the Cloudflare dashboard:

[ Go to **Workers plans** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/plans)

Feature | Limit  
---|---  
Browser hours | 10 minutes per day  
Concurrent browsers per account (Browser Sessions only) 1 | 3 per account  
New browser instances (Browser Sessions only) | 1 every 20 seconds  
Browser timeout | 60 seconds 2  
Total requests (Quick Actions only) 3 | 1 every 10 seconds  
  
### `/crawl` endpoint limits

The [`/crawl` endpoint](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) has additional limits for Workers Free plan users:

Feature | Limit  
---|---  
Crawl jobs per day | 5 per day  
Maximum pages per crawl | 100 pages  
  
## Workers Paid

Need higher limits?

The limits below are defaults for Workers Paid users. If you need to scale beyond them, Cloudflare can increase your account limits. [Request higher limits ↗︎](https://forms.gle/CdueDKvb26mTaepa9).

Feature | Limit  
---|---  
Browser hours | No limit ([See pricing](https://developers.cloudflare.com/browser-run/pricing/))  
Concurrent browsers per account (Browser Sessions only) 1 | 200 per account ([See pricing](https://developers.cloudflare.com/browser-run/pricing/))  
New browser instances per second (Browser Sessions only) | 3 per second  
Browser timeout | 60 seconds 2  
Total requests per second (Quick Actions only) 3 | 30 per second  
  
## FAQ

### How can I manage concurrency and session isolation with Browser Run?

If you are hitting concurrency [limits](https://developers.cloudflare.com/browser-run/limits/#workers-paid), or want to optimize concurrent browser usage, here are a few tips:

  * Optimize with tabs or shared browsers: Instead of launching a new browser for each task, consider opening multiple tabs or running multiple actions within the same browser instance.
  * [Reuse sessions](https://developers.cloudflare.com/browser-run/features/reuse-sessions/): You can optimize your setup and decrease startup time by reusing sessions instead of launching a new browser every time. If you are concerned about maintaining test isolation (for example, for tests that depend on a clean environment), we recommend using [incognito browser contexts ↗︎](https://pptr.dev/api/puppeteer.browser.createbrowsercontext), which isolate cookies and cache with other sessions.



If you are still running into concurrency limits you can [request a higher limit ↗︎](https://forms.gle/CdueDKvb26mTaepa9).

### Can I increase the browser timeout?

By default, a browser instance will time out after 60 seconds of inactivity. If you want to keep the browser open longer, you can use the [`keep_alive` option](https://developers.cloudflare.com/browser-run/puppeteer/#keep-alive), which allows you to extend the timeout to up to 10 minutes.

### Is there a maximum session duration?

There is no fixed maximum lifetime for a browser session as long as it remains active. By default, Browser Run closes sessions after one minute of inactivity to prevent unintended usage. You can [increase this inactivity timeout](https://developers.cloudflare.com/browser-run/puppeteer/#keep-alive) to up to 10 minutes.

If you need sessions to remain open longer, keep them active by sending a command at least once within your configured inactivity window (for example, every 10 minutes). Sessions also close when Browser Run rolls out a new release.

### I upgraded from the Workers Free plan, but I'm still hitting the 10-minute per day limit. What should I do?

If you recently upgraded to the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/) but still encounter the 10-minute per day limit, redeploy your Worker to ensure your usage is correctly associated with the new plan.

### Why is my browser usage higher than expected?

If you are hitting the daily limit or seeing higher usage than expected, the most common cause is browser sessions that are not being closed properly. When a browser session is not explicitly closed with `browser.close()`, it remains open and continues to consume browser time until it times out (60 seconds by default, or up to 10 minutes if you use the `keep_alive` option).

To minimize usage:

  * Always call `browser.close()` when you are finished with a browser session.
  * Wrap your browser code in a `try/finally` block to ensure `browser.close()` is called even if an error occurs.
  * Use [`puppeteer.history()`](https://developers.cloudflare.com/browser-run/puppeteer/#list-recent-sessions) or [`playwright.history()`](https://developers.cloudflare.com/browser-run/playwright/#list-recent-sessions) to review recent sessions and identify any that closed due to `BrowserIdle` instead of `NormalClosure`. Sessions that close due to idle timeout indicate the browser was not closed explicitly.



You can monitor your usage and view session close reasons in the Cloudflare dashboard on the **Browser Run** page:

[ Go to **Browser Run** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/browser-run)

Refer to [Browser close reasons](https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/) for more information.

## Troubleshooting

### Error: `429 Too many requests`

When you make too many requests in a short period of time, Browser Run will respond with HTTP status code `429 Too many requests`. You can view your account's rate limits in the Workers Free and Workers Paid sections above.

The example below demonstrates how to handle rate limiting gracefully by reading the `Retry-After` value and retrying the request after that delay.
    
    
    const response = await fetch('https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-run/content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer <your-token>',
        },
        body: JSON.stringify({ url: 'https://example.com' })
    });
    
    if (response.status === 429) {
    const retryAfter = response.headers.get('Retry-After');
    console.log(`Rate limited. Waiting ${retryAfter} seconds...`);
    await new Promise(resolve => setTimeout(resolve, retryAfter \* 1000));
    
        // Retry the request
        const retryResponse = await fetch(/* same request as above */);
    
    }
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    try {
    	const browser = await puppeteer.launch(env.MYBROWSER);
    
    	const page = await browser.newPage();
    	await page.goto("https://example.com");
    	const content = await page.content();
    
    	await browser.close();
    } catch (error) {
    	if (error.status === 429) {
    		const retryAfter = error.headers.get("Retry-After");
    		console.log(
    			`Browser instance limit reached. Waiting ${retryAfter} seconds...`,
    		);
    		await new Promise((resolve) => setTimeout(resolve, retryAfter * 1000));
    
    		// Retry launching browser
    		const browser = await puppeteer.launch(env.MYBROWSER);
    	}
    }

### Error: `429 Browser time limit exceeded for today`

This `Error processing the request: Unable to create new browser: code: 429: message: Browser time limit exceeded for today` error indicates you have hit the daily browser limit on the Workers Free plan. Workers Free plan accounts are limited to 10 minutes of Browser Run usage per day. If you exceed that limit, you will receive a `429` error until the next UTC day.

You can increase your limits by upgrading to a Workers Paid plan on the **Workers plans** page of the Cloudflare dashboard:

[ Go to **Workers plans** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/plans)

If you recently upgraded but still encounter the 10-minute per day limit, redeploy your Worker to ensure your usage is correctly associated with the new plan.

## Footnotes

  1. Browsers close upon task completion or sixty seconds of inactivity (if you do not extend your browser timeout). Therefore, in practice, many workflows do not require a high number of concurrent browsers. ↩ ↩2

  2. By default, a browser will time out after 60 seconds of inactivity. You can extend this to up to 10 minutes using the [`keep_alive` option](https://developers.cloudflare.com/browser-run/puppeteer/#keep-alive). Call `browser.close()` to release the browser instance immediately. ↩ ↩2

  3. If you exceed the per-second rate limit, you will receive a `429` response. Refer to troubleshooting the `429 Too many requests` error. ↩ ↩2




[PreviousFAQ](https://developers.cloudflare.com/browser-run/faq/)[NextPricing](https://developers.cloudflare.com/browser-run/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
