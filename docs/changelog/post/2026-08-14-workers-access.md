---
url: https://developers.cloudflare.com/changelog/post/2026-08-14-workers-access/
title: You can now enable Access on a Worker or all Workers at once \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:08.592871+00:00
---

# You can now enable Access on a Worker or all Workers at once · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-14-workers-access/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 14, 2026

## You can now enable Access on a Worker or all Workers at once

[Workers](https://developers.cloudflare.com/workers/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-14-workers-access/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You now have two new ways to protect your [Workers](https://developers.cloudflare.com/workers/) with [Cloudflare Access](https://developers.cloudflare.com/workers/configuration/cloudflare-access/).

**Protect an application across all its domains at once**

Until now, if a Worker was reachable on a route, a Custom Domain, and a `workers.dev` URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.

Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.

![Access setting for protecting a single Worker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1476,height=689,format=webp/_astro/protect-one-worker.BSpeeOry.png)

**Protect all new and existing Workers by default**

Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.

![Account-wide Access setting that protects all Workers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2436,height=1432,format=webp/_astro/protect-all-workers._AWy-S-E.png)

If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.

![Make a Worker public when all Workers are protected](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1228,height=756,format=webp/_astro/make-worker-public.D3yjPjtf.png)

Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.

For more advanced policy options, edit the policy in [Zero Trust ↗︎](https://dash.cloudflare.com/?to=/:account/one/access/apps).

![Access policy configuration for controlling who can sign in](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1276,height=1220,format=webp/_astro/choose-who-can-sign-in.DKf3kWAK.png)

**View all of your Worker Access policies**

You can view and manage all of your Access policies in the **Access** tab of the Workers & Pages section in the dashboard.

![Access tab showing all configured Access policies](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1646,height=1366,format=webp/_astro/access-policies.DN7yCwHX.png)

**See who is accessing your Worker**

When Access is enabled on your Worker, every authenticated request includes `ctx.access`. Call [`ctx.access.getIdentity()`](https://developers.cloudflare.com/workers/runtime-apis/context/#access) to get the user's email, name, and groups — no manual JWT validation required.
    
    
    export default {
      async fetch(request, env, ctx) {
        if (!ctx.access) {
          return new Response("Access did not run", { status: 401 });
        }
    
        const identity = await ctx.access.getIdentity();
        return Response.json({ aud: ctx.access.aud, email: identity?.email });
      },
    };

**Test Access locally**

You can now test Cloudflare Access locally with `wrangler dev`. Add a `dev` block to your `wrangler.jsonc`:
    
    
    {
      "access": {
        "dev": {
          "aud": "my-app",
          "identity": { "email": "admin@example.com" }
        }
      }
    }

Your Worker will receive this identity through `ctx.access` and `ctx.access.getIdentity()`, letting you test authenticated and unauthenticated flows without deploying. Remove the `dev` block to simulate unauthenticated requests.

**API and programmatic access**

You can also set up these policies through the [Workers API](https://developers.cloudflare.com/workers/configuration/cloudflare-access/) instead of the dashboard.
