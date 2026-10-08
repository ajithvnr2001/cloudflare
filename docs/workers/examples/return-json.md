---
url: https://developers.cloudflare.com/workers/examples/return-json/
title: Return JSON \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:25.255818+00:00
---

# Return JSON · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/return-json/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Return Json



# Return JSON

Return JSON directly from a Worker script, useful for building APIs and middleware.

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/return-json/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/return-json)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.
    
    
    export default {
      async fetch(request) {
        const data = {
          hello: "world",
        };
    
        return Response.json(data);
      },
    };
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		const data = {
    			hello: "world",
    		};
    
    		return Response.json(data);
    	},
    } satisfies ExportedHandler;
    
    
    from workers import WorkerEntrypoint, Response
    import json
    
    class Default(WorkerEntrypoint):
        def fetch(self, request):
            data = json.dumps({"hello": "world"})
            headers = {"content-type": "application/json"}
            return Response(data, headers=headers)
    
    
    use serde::{Deserialize, Serialize};
    use worker::*;
    
    #[derive(Deserialize, Serialize, Debug)]
    struct Json {
        hello: String,
    }
    
    #[event(fetch)]
    async fn fetch(_req: Request, _env: Env, _ctx: Context) -> Result<Response> {
        let data = Json {
            hello: String::from("world"),
        };
        Response::from_json(&data)
    }
    
    
    import { Hono } from "hono";
    
    const app = new Hono();
    
    app.get("*", (c) => {
    	const data = {
    		hello: "world",
    	};
    
    	return c.json(data);
    });
    
    export default app;

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/return-json.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
