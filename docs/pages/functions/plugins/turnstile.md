---
url: https://developers.cloudflare.com/pages/functions/plugins/turnstile/
title: Turnstile \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:33.913551+00:00
---

# Turnstile · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/plugins/turnstile/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /…

[Functions](https://developers.cloudflare.com/pages/functions/)

  4. /[Pages Plugins](https://developers.cloudflare.com/pages/functions/plugins/)
  5. /Turnstile



# Turnstile

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/plugins/turnstile/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationUsageProperties

[Turnstile](https://developers.cloudflare.com/turnstile/) is Cloudflare's smart CAPTCHA alternative.

The Turnstile Pages Plugin validates Cloudflare Turnstile tokens.

## Installation

npmyarnpnpmbun
    
    
    npm i @cloudflare/pages-plugin-turnstile
    
    
    yarn add @cloudflare/pages-plugin-turnstile
    
    
    pnpm add @cloudflare/pages-plugin-turnstile
    
    
    bun add @cloudflare/pages-plugin-turnstile

## Usage
    
    
    import turnstilePlugin from "@cloudflare/pages-plugin-turnstile";
    
    /**
     * POST /api/submit-with-plugin
     */
    
    export const onRequestPost = [
    	turnstilePlugin({
    		// This is the demo secret key. In prod, we recommend you store
    		// your secret key(s) safely.
    		secret: "0x4AAAAAAASh4E5cwHGsTTePnwcPbnFru6Y",
    	}),
    	// Alternatively, this is how you can use a secret key which has been stored as an environment variable
    	// (async (context) => {
    	//   return turnstilePlugin({secret: context.env.SECRET_KEY})(context)
    	// }),
    	async (context) => {
    		// Request has been validated as coming from a human
    		const formData = await context.request.formData();
    		// Additional solve metadata data is available at context.data.turnstile
    		return new Response(
    			`Successfully verified! ${JSON.stringify(context.data.turnstile)}`,
    		);
    	},
    ];

This Plugin only exposes a single route to verify an incoming Turnstile response in a `POST` as the `cf-turnstile-response` parameter. It will be available wherever it is mounted. In the example above, it is mounted in `functions/register.ts`. As a result, it will validate requests to `/register`.

## Properties

The Plugin is mounted with a single object parameter with the following properties:

[`secret` ↗︎](https://dash.cloudflare.com/login) is mandatory and can both be found in your Turnstile dashboard.

`response` and `remoteip` are optional strings. `response` is the Turnstile token to verify. If it is not provided, the plugin will default to extracting `cf-turnstile-response` value from a `multipart/form-data` request). `remoteip` is the requester's IP address. This defaults to the `CF-Connecting-IP` header of the request.

`onError` is an optional function which takes the Pages Function context object and returns a `Promise` of a `Response`. By default, it will return a human-readable error `Response`.

`context.data.turnstile` will be populated in subsequent Pages Functions (including for the `onError` function) with [the Turnstile Siteverify response object](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/).

[PreviousStytch](https://developers.cloudflare.com/pages/functions/plugins/stytch/)[NextCommunity Plugins](https://developers.cloudflare.com/pages/functions/plugins/community-plugins/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/plugins/turnstile.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
