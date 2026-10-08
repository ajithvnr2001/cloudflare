---
url: https://developers.cloudflare.com/d1/examples/d1-and-remix/
title: Query D1 from Remix \u00b7 Cloudflare D1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:37.787731+00:00
---

# Query D1 from Remix · Cloudflare D1 docs

> Source: https://developers.cloudflare.com/d1/examples/d1-and-remix/

  1. [Home](https://developers.cloudflare.com/)
  2. /[D1](https://developers.cloudflare.com/d1/)
  3. /Examples
  4. /Query D1 from Remix



# Query D1 from Remix

Query your D1 database from a Remix application.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/d1/examples/d1-and-remix/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

Remix is no longer recommended for new projects. For new applications, use [React Router](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router) instead. If you have an existing Remix application, consider [migrating to React Router ↗︎](https://reactrouter.com/upgrading/remix).

Remix is a full-stack web framework that operates on both client and server. You can query your D1 database(s) from Remix using Remix's [data loading ↗︎](https://remix.run/docs/en/main/guides/data-loading) API with the [`useLoaderData` ↗︎](https://remix.run/docs/en/main/hooks/use-loader-data) hook.

To set up a new Remix site on Cloudflare Pages that can query D1:

  1. **Refer to[the Remix guide](https://developers.cloudflare.com/pages/framework-guides/deploy-a-remix-site/)**.
  2. Bind a D1 database to your [Pages Function](https://developers.cloudflare.com/pages/functions/bindings/#d1-databases).
  3. Pass the `--d1 BINDING_NAME=DATABASE_ID` flag to `wrangler dev` when developing locally. `BINDING_NAME` should match what call in your code, and `DATABASE_ID` should match the `database_id` defined in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/): for example, `--d1 DB=xxxx-xxxx-xxxx-xxxx-xxxx`.



The following example shows you how to define a Remix [`loader` ↗︎](https://remix.run/docs/en/main/route/loader) that has a binding to a D1 database.

  * Bindings are passed through on the `context.cloudflare.env` parameter passed to a `LoaderFunction`.
  * If you configured a [binding](https://developers.cloudflare.com/pages/functions/bindings/#d1-databases) named `DB`, then you would access [D1 Workers Binding API](https://developers.cloudflare.com/d1/worker-api/prepared-statements/) methods via `context.cloudflare.env.DB`.


    
    
    import type { LoaderFunction } from "@remix-run/cloudflare";
    import { json } from "@remix-run/cloudflare";
    import { useLoaderData } from "@remix-run/react";
    
    interface Env {
      DB: D1Database;
    }
    
    export const loader: LoaderFunction = async ({ context, params }) => {
      let env = context.cloudflare.env as Env;
    
      try {
        let { results } = await env.DB.prepare("SELECT * FROM users LIMIT 5").run();
        return json(results);
      } catch (error) {
        return json({ error: "Failed to fetch users" }, { status: 500 });
      }
    };
    
    export default function Index() {
      const results = useLoaderData<typeof loader>();
      return (
        <div style={{ fontFamily: "system-ui, sans-serif", lineHeight: "1.8" }}>
          <h1>Welcome to Remix</h1>
          <div>
            A value from D1:
            <pre>{JSON.stringify(results)}</pre>
          </div>
        </div>
      );
    }

[PreviousExport and save D1 database ↗︎](https://developers.cloudflare.com/workflows/examples/backup-d1/)[NextQuery D1 from Hono](https://developers.cloudflare.com/d1/examples/d1-and-hono/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/d1/examples/d1-and-remix.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
