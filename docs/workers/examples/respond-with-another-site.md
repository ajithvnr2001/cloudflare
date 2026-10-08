---
url: https://developers.cloudflare.com/workers/examples/respond-with-another-site/
title: Respond with another site \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:25.078457+00:00
---

# Respond with another site · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/respond-with-another-site/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Respond With Another Site



# Respond with another site

Respond to the Worker request with the response from another website (example.com in this example).

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/respond-with-another-site/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/respond-with-another-site)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.
    
    
    export default {
      async fetch(request) {
        function MethodNotAllowed(request) {
          return new Response(`Method ${request.method} not allowed.`, {
            status: 405,
            headers: {
              Allow: "GET",
            },
          });
        }
        // Only GET requests work with this proxy.
        if (request.method !== "GET") return MethodNotAllowed(request);
        return fetch(`https://example.com`);
      },
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		function MethodNotAllowed(request) {
    			return new Response(`Method ${request.method} not allowed.`, {
    				status: 405,
    				headers: {
    					Allow: "GET",
    				},
    			});
    		}
    		// Only GET requests work with this proxy.
    		if (request.method !== "GET") return MethodNotAllowed(request);
    		return fetch(`https://example.com`);
    	},
    } satisfies ExportedHandler;
    
    
    from workers import WorkerEntrypoint, Response, fetch
    
    class Default(WorkerEntrypoint):
        def fetch(self, request):
            def method_not_allowed(request):
                msg = f'Method {request.method} not allowed.'
                headers = {"Allow": "GET"}
                return Response(msg, headers=headers, status=405)
    
            # Only GET requests work with this proxy.
            if request.method != "GET":
                return method_not_allowed(request)
    
            return fetch("https://example.com")

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/respond-with-another-site.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
