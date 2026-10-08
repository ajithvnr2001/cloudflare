---
url: https://developers.cloudflare.com/d1/examples/d1-and-hono/
title: Query D1 from Hono \u00b7 Cloudflare D1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:37.899998+00:00
---

# Query D1 from Hono · Cloudflare D1 docs

> Source: https://developers.cloudflare.com/d1/examples/d1-and-hono/

  1. [Home](https://developers.cloudflare.com/)
  2. /[D1](https://developers.cloudflare.com/d1/)
  3. /Examples
  4. /Query D1 from Hono



# Query D1 from Hono

Query D1 from the Hono web framework

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/d1/examples/d1-and-hono/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hono is a fast web framework for building API-first applications, and it includes first-class support for both [Workers](https://developers.cloudflare.com/workers/) and [Pages](https://developers.cloudflare.com/pages/).

When using Workers:

  * Ensure you have configured your [Wrangler configuration file](https://developers.cloudflare.com/d1/get-started/#3-bind-your-worker-to-your-d1-database) to bind your D1 database to your Worker.
  * You can access your D1 databases via Hono's [`Context` ↗︎](https://hono.dev/api/context) parameter: [bindings ↗︎](https://hono.dev/getting-started/cloudflare-workers#bindings) are exposed on `context.env`. If you configured a [binding](https://developers.cloudflare.com/pages/functions/bindings/#d1-databases) named `DB`, then you would access [D1 Workers Binding API](https://developers.cloudflare.com/d1/worker-api/prepared-statements/) methods via `c.env.DB`.
  * Refer to the Hono documentation for [Cloudflare Workers ↗︎](https://hono.dev/getting-started/cloudflare-workers).



If you are using [Pages Functions](https://developers.cloudflare.com/pages/functions/):

  1. Bind a D1 database to your [Pages Function](https://developers.cloudflare.com/pages/functions/bindings/#d1-databases).
  2. Pass the `--d1 BINDING_NAME=DATABASE_ID` flag to `wrangler dev` when developing locally. `BINDING_NAME` should match what call in your code, and `DATABASE_ID` should match the `database_id` defined in your Wrangler configuration file: for example, `--d1 DB=xxxx-xxxx-xxxx-xxxx-xxxx`.
  3. Refer to the Hono guide for [Cloudflare Pages ↗︎](https://hono.dev/getting-started/cloudflare-pages).



The following examples show how to access a D1 database bound to `DB` from both a Workers script and a Pages Function:
    
    
    import { Hono } from "hono";
    
    // This ensures c.env.DB is correctly typed
    type Bindings = {
    	DB: D1Database;
    };
    
    const app = new Hono<{ Bindings: Bindings }>();
    
    // Accessing D1 is via the c.env.YOUR_BINDING property
    app.get("/query/users/:id", async (c) => {
    	const userId = c.req.param("id");
    	try {
    		let { results } = await c.env.DB.prepare(
    			"SELECT * FROM users WHERE user_id = ?",
    		)
    			.bind(userId)
    			.run();
    		return c.json(results);
    	} catch (e) {
    		return c.json({ err: "Failed to query user" }, 500);
    	}
    });
    
    // Export our Hono app: Hono automatically exports a
    // Workers 'fetch' handler for you
    export default app;
    
    
    import { Hono } from "hono";
    import { handle } from "hono/cloudflare-pages";
    
    // This ensures c.env.DB is correctly typed
    type Bindings = {
    	DB: D1Database;
    };
    
    const app = new Hono<{ Bindings: Bindings }>().basePath("/api");
    
    // Accessing D1 is via the c.env.YOUR_BINDING property
    app.get("/query/users/:id", async (c) => {
    	const userId = c.req.param("id");
    	try {
    		let { results } = await c.env.DB.prepare(
    			"SELECT * FROM users WHERE user_id = ?",
    		)
    			.bind(userId)
    			.run();
    		return c.json(results);
    	} catch (e) {
    		return c.json({ err: "Failed to query user" }, 500);
    	}
    });
    
    // Export the Hono instance as a Pages onRequest function
    export const onRequest = handle(app);

[PreviousQuery D1 from Remix](https://developers.cloudflare.com/d1/examples/d1-and-remix/)[NextQuery D1 from SvelteKit](https://developers.cloudflare.com/d1/examples/d1-and-sveltekit/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/d1/examples/d1-and-hono.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
