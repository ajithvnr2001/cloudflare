---
url: https://developers.cloudflare.com/pages/functions/plugins/sentry/
title: Sentry \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:33.732792+00:00
---

# Sentry · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/plugins/sentry/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /…

[Functions](https://developers.cloudflare.com/pages/functions/)

  4. /[Pages Plugins](https://developers.cloudflare.com/pages/functions/plugins/)
  5. /Sentry



# Sentry

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/plugins/sentry/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationUsage Additional context

Note

Sentry now provides official support for Cloudflare Workers and Pages. Refer to the [Sentry documentation ↗︎](https://docs.sentry.io/platforms/javascript/guides/cloudflare/) for more details.

The Sentry Pages Plugin captures and logs all exceptions which occur below it in the execution chain of your Pages Functions. It is therefore recommended that you install this Plugin at the root of your application in `functions/_middleware.ts` as the very first Plugin.

## Installation

npmyarnpnpmbun
    
    
    npm i @cloudflare/pages-plugin-sentry
    
    
    yarn add @cloudflare/pages-plugin-sentry
    
    
    pnpm add @cloudflare/pages-plugin-sentry
    
    
    bun add @cloudflare/pages-plugin-sentry

## Usage
    
    
    import sentryPlugin from "@cloudflare/pages-plugin-sentry";
    
    export const onRequest: PagesFunction = sentryPlugin({
    	dsn: "https://sentry.io/welcome/xyz",
    });

The Plugin uses [Toucan ↗︎](https://github.com/robertcepa/toucan-js). Refer to the Toucan README to [review the options it can take ↗︎](https://github.com/robertcepa/toucan-js#other-options). `context`, `request`, and `event` are automatically populated and should not be manually configured.

If your [DSN ↗︎](https://docs.sentry.io/product/sentry-basics/dsn-explainer/) is held as an environment variable or in KV, you can access it like so:
    
    
    import sentryPlugin from "@cloudflare/pages-plugin-sentry";
    
    export const onRequest: PagesFunction<{
    	SENTRY_DSN: string;
    }> = (context) => {
    	return sentryPlugin({ dsn: context.env.SENTRY_DSN })(context);
    };
    
    
    import sentryPlugin from "@cloudflare/pages-plugin-sentry";
    
    export const onRequest: PagesFunction<{
    	KV: KVNamespace;
    }> = async (context) => {
    	return sentryPlugin({ dsn: await context.env.KV.get("SENTRY_DSN") })(context);
    };

### Additional context

If you need to set additional context for Sentry (for example, user information or additional logs), use the `data.sentry` instance in any Function below the Plugin in the execution chain.

For example, you can access `data.sentry` and set user information like so:
    
    
    import type { PluginData } from "@cloudflare/pages-plugin-sentry";
    
    export const onRequest: PagesFunction<unknown, any, PluginData> = async ({
    	data,
    	next,
    }) => {
    	// Authenticate the user from the request and extract user's email address
    	const email = await getEmailFromRequest(request);
    
    	data.sentry.setUser({ email });
    
    	return next();
    };

Again, the full list of features can be found in [Toucan's documentation ↗︎](https://github.com/robertcepa/toucan-js#features).

[PreviousHoneycomb](https://developers.cloudflare.com/pages/functions/plugins/honeycomb/)[NextStatic Forms](https://developers.cloudflare.com/pages/functions/plugins/static-forms/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/plugins/sentry.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
