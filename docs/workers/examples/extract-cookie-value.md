---
url: https://developers.cloudflare.com/workers/examples/extract-cookie-value/
title: Cookie parsing \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:22.489569+00:00
---

# Cookie parsing · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/extract-cookie-value/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Extract Cookie Value



# Cookie parsing

Given the cookie name, get the value of a cookie. You can also use cookies for A/B testing.

Last updated Sep 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/extract-cookie-value/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/extract-cookie-value)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.
    
    
    import { parseCookie } from "cookie";
    export default {
    	async fetch(request) {
    		// The name of the cookie
    		const COOKIE_NAME = "__uid";
    		const cookie = parseCookie(request.headers.get("Cookie") || "");
    		if (cookie[COOKIE_NAME] != null) {
    			// Respond with the cookie value
    			return new Response(cookie[COOKIE_NAME]);
    		}
    		return new Response("No cookie with name: " + COOKIE_NAME);
    	},
    };
    
    
    import { parseCookie } from "cookie";
    export default {
    	async fetch(request): Promise<Response> {
    		// The name of the cookie
    		const COOKIE_NAME = "__uid";
    		const cookie = parseCookie(request.headers.get("Cookie") || "");
    		if (cookie[COOKIE_NAME] != null) {
    			// Respond with the cookie value
    			return new Response(cookie[COOKIE_NAME]);
    		}
    		return new Response("No cookie with name: " + COOKIE_NAME);
    	},
    } satisfies ExportedHandler;
    
    
    from http.cookies import SimpleCookie
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            # Name of the cookie
            cookie_name = "__uid"
    
            cookies = SimpleCookie(request.headers["Cookie"] or "")
    
            if cookie_name in cookies:
                # Respond with cookie value
                return Response(cookies[cookie_name].value)
    
            return Response("No cookie with name: " + cookie_name)
    
    
    import { Hono } from 'hono';
    import { getCookie } from 'hono/cookie';
    
    const app = new Hono();
    
    app.get('*', (c) => {
      // The name of the cookie
      const COOKIE_NAME = "__uid";
    
      // Get the specific cookie value using Hono's cookie helper
      const cookieValue = getCookie(c, COOKIE_NAME);
    
      if (cookieValue) {
        // Respond with the cookie value
        return c.text(cookieValue);
      }
    
      return c.text("No cookie with name: " + COOKIE_NAME);
    });
    
    export default app;

External dependencies

This example requires the npm package [`cookie` ↗︎](https://www.npmjs.com/package/cookie) to be installed in your JavaScript project.

The Hono example uses the built-in cookie utilities provided by Hono, so no external dependencies are needed for that implementation.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/extract-cookie-value.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
