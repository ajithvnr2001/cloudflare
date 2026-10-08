---
url: https://developers.cloudflare.com/workers/testing/miniflare/developing/live-reload/
title: Live Reload \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:55.428832+00:00
---

# Live Reload · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/developing/live-reload/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Developing
  5. /Live Reload



# Live Reload

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/developing/live-reload/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Miniflare automatically refreshes your browser when your Worker script changes when `liveReload` is set to `true`.
    
    
    const mf = new Miniflare({
    	liveReload: true,
    });

Miniflare will only inject the `<script>` tag required for live-reload at the end of responses with the `Content-Type` header set to `text/html`:
    
    
    export default {
    	fetch() {
    		const body = `
          <!DOCTYPE html>
          <html>
          <body>
            <p>Try update me!</p>
          </body>
          </html>
        `;
    
    		return new Response(body, {
    			headers: { "Content-Type": "text/html; charset=utf-8" },
    		});
    	},
    };

[PreviousAttaching a Debugger](https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/)[NextMigrating from Version 2](https://developers.cloudflare.com/workers/testing/miniflare/migrations/from-v2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/developing/live-reload.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
