---
url: https://developers.cloudflare.com/workers/examples/redirect/
title: Redirect \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:24.558813+00:00
---

# Redirect · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/redirect/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Redirect



# Redirect

Redirect requests from one URL to another or from one set of URLs to another set.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/redirect/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRedirect all requests to one URLRedirect requests from one domain to another

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/redirect)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

## Redirect all requests to one URL
    
    
    export default {
      async fetch(request) {
        const destinationURL = "https://example.com";
        const statusCode = 301;
        return Response.redirect(destinationURL, statusCode);
      },
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		const destinationURL = "https://example.com";
    		const statusCode = 301;
    		return Response.redirect(destinationURL, statusCode);
    	},
    } satisfies ExportedHandler;
    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        def fetch(self, request):
            destinationURL = "https://example.com"
            statusCode = 301
            return Response.redirect(destinationURL, statusCode)
    
    
    use worker::*;
    
    #[event(fetch)]
    async fn fetch(_req: Request, _env: Env, _ctx: Context) -> Result<Response> {
        let destination_url = Url::parse("https://example.com")?;
        let status_code = 301;
        Response::redirect_with_status(destination_url, status_code)
    }
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    app.all("*", (c) => {
    	const destinationURL = "https://example.com";
    	const statusCode = 301;
    	return c.redirect(destinationURL, statusCode);
    });
    
    export default app;

## Redirect requests from one domain to another
    
    
    export default {
    	async fetch(request) {
    		const base = "https://example.com";
    		const statusCode = 301;
    
    		const url = new URL(request.url);
    		const { pathname, search } = url;
    
    		const destinationURL = `${base}${pathname}${search}`;
    		console.log(destinationURL);
    
    		return Response.redirect(destinationURL, statusCode);
    	},
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		const base = "https://example.com";
    		const statusCode = 301;
    
    		const url = new URL(request.url);
    		const { pathname, search } = url;
    
    		const destinationURL = `${base}${pathname}${search}`;
    		console.log(destinationURL);
    
    		return Response.redirect(destinationURL, statusCode);
    	},
    } satisfies ExportedHandler;
    
    
    from workers import WorkerEntrypoint, Response
    from urllib.parse import urlparse
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            base = "https://example.com"
            statusCode = 301
    
            url = urlparse(request.url)
    
            destinationURL = f'{base}{url.path}{url.query}'
            print(destinationURL)
    
            return Response.redirect(destinationURL, statusCode)
    
    
    use worker::*;
    
    #[event(fetch)]
    async fn fetch(req: Request, _env: Env, _ctx: Context) -> Result<Response> {
        let mut base = Url::parse("https://example.com")?;
        let status_code = 301;
    
        let url = req.url()?;
    
        base.set_path(url.path());
        base.set_query(url.query());
    
        console_log!("{:?}", base.to_string());
    
        Response::redirect_with_status(base, status_code)
    }
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    app.all("*", (c) => {
    	const base = "https://example.com";
    	const statusCode = 301;
    
    	const { pathname, search } = new URL(c.req.url);
    
    	const destinationURL = `${base}${pathname}${search}`;
    	console.log(destinationURL);
    
    	return c.redirect(destinationURL, statusCode);
    });
    
    export default app;

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/redirect.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
