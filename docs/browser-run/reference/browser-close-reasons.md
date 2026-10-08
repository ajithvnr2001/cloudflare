---
url: https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/
title: Browser close reasons \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:38.939791+00:00
---

# Browser close reasons · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Reference
  4. /Browser close reasons



# Browser close reasons

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewClose reasonsHandling unexpected closures

A browser session may close for a variety of reasons, including normal completion, inactivity, connection errors, or errors in the headless browser instance. As a best practice, wrap `puppeteer.connect` or `puppeteer.launch` in a [`try...catch` ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) statement to handle unexpected closures gracefully.

To find the reason that a browser closed:

  1. In the Cloudflare dashboard, go to the **Browser Run** page.

[ Go to **Browser Run** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/browser-run)
  2. Select the **Runs** tab.




Browser Run sessions are billed based on [usage](https://developers.cloudflare.com/browser-run/pricing/). We do not charge for sessions that error due to underlying Browser Run infrastructure.

## Close reasons

Reason | Description  
---|---  
**Normal closure** | Your code called `browser.close()` and the session ended normally. No action needed.  
**Browser idle** | The session received no commands for the configured inactivity timeout (60 seconds by default, up to 10 minutes with [`keep_alive`](https://developers.cloudflare.com/browser-run/puppeteer/#keep-alive)). To prevent idle closures, send commands within the inactivity window or increase the `keep_alive` value.  
**Chromium crashed** | The Chromium instance inside the session crashed, often because the page consumed too much memory (large DOMs, heavy JavaScript, or many concurrent pages). Try reducing page complexity, closing unused pages, or breaking work into smaller tasks.  
**Connection error** | The connection between the client and Browser Run was interrupted. This can be caused by network issues, your Worker reaching its CPU time limit, or a WebSocket disconnection. Retry the operation with a `try...catch` block.  
**Session evicted** | Browser Run recycled the session due to infrastructure maintenance or a new release deployment. This is not caused by your code. Retry the operation with a `try...catch` block and reconnection logic.  
  
## Handling unexpected closures

Sessions can close at any time due to infrastructure events, network issues, or browser crashes. Design your code to handle these cases by wrapping browser operations in a `try...catch` block and reconnecting when needed.
    
    
    async function runBrowser(env) {
      let browser;
      try {
        browser = await puppeteer.launch(env.MYBROWSER);
        const page = await browser.newPage();
        await page.goto("https://example.com");
        // Your browser automation logic
      } catch (error) {
        console.error("Browser session ended unexpectedly:", error.message);
        // Retry or return an error response
      } finally {
        await browser?.close();
      }
    }

For long-running or critical workflows, consider adding retry logic:
    
    
    async function runWithRetry(env, maxRetries = 3) {
      for (let attempt = 1; attempt <= maxRetries; attempt++) {
        try {
          return await runBrowser(env);
        } catch (error) {
          if (attempt === maxRetries) throw error;
          console.log(`Attempt ${attempt} failed, retrying...`);
        }
      }
    }

[Previousrobots.txt and sitemaps](https://developers.cloudflare.com/browser-run/reference/robots-txt/)[NextWrangler](https://developers.cloudflare.com/browser-run/reference/wrangler/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/reference/browser-close-reasons.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
