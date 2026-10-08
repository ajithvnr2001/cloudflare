---
url: https://developers.cloudflare.com/pages/functions/plugins/honeycomb/
title: Honeycomb \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:33.560265+00:00
---

# Honeycomb · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/plugins/honeycomb/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /…

[Functions](https://developers.cloudflare.com/pages/functions/)

  4. /[Pages Plugins](https://developers.cloudflare.com/pages/functions/plugins/)
  5. /Honeycomb



# Honeycomb

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/plugins/honeycomb/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationUsage Additional context

The Honeycomb Pages Plugin automatically sends traces to Honeycomb for analysis and observability.

## Installation

npmyarnpnpmbun
    
    
    npm i @cloudflare/pages-plugin-honeycomb
    
    
    yarn add @cloudflare/pages-plugin-honeycomb
    
    
    pnpm add @cloudflare/pages-plugin-honeycomb
    
    
    bun add @cloudflare/pages-plugin-honeycomb

## Usage

The following usage example uses environment variables you will need to set in your Pages project settings.
    
    
    import honeycombPlugin from "@cloudflare/pages-plugin-honeycomb";
    
    export const onRequest: PagesFunction<{
    	HONEYCOMB_API_KEY: string;
    	HONEYCOMB_DATASET: string;
    }> = (context) => {
    	return honeycombPlugin({
    		apiKey: context.env.HONEYCOMB_API_KEY,
    		dataset: context.env.HONEYCOMB_DATASET,
    	})(context);
    };

Alternatively, you can hard-code (not advisable for API key) your settings the following way:
    
    
    import honeycombPlugin from "@cloudflare/pages-plugin-honeycomb";
    
    export const onRequest = honeycombPlugin({
    	apiKey: "YOUR_HONEYCOMB_API_KEY",
    	dataset: "YOUR_HONEYCOMB_DATASET_NAME",
    });

This Plugin is based on the `@cloudflare/workers-honeycomb-logger` and accepts the same [configuration options ↗︎](https://github.com/cloudflare/workers-honeycomb-logger#config).

Ensure that you enable the option to **Automatically unpack nested JSON** and set the **Maximum unpacking depth** to **5** in your Honeycomb dataset settings.

![Follow the instructions above to toggle on Automatically unpack nested JSON and set the Maximum unpacking depth option to 5 in the Honeycomb dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=481,height=221,format=webp/_astro/honeycomb.MQ2Vf1tC.png)

### Additional context

`data.honeycomb.tracer` has two methods for attaching additional information about a given trace:

  * `data.honeycomb.tracer.log` which takes a single argument, a `String`.
  * `data.honeycomb.tracer.addData` which takes a single argument, an object of arbitrary data.



More information about these methods can be seen on [`@cloudflare/workers-honeycomb-logger`'s documentation ↗︎](https://github.com/cloudflare/workers-honeycomb-logger#adding-logs-and-other-data).

For example, if you wanted to use the `addData` method to attach user information:
    
    
    import type { PluginData } from "@cloudflare/pages-plugin-honeycomb";
    
    export const onRequest: PagesFunction<unknown, any, PluginData> = async ({
    	data,
    	next,
    	request,
    }) => {
    	// Authenticate the user from the request and extract user's email address
    	const email = await getEmailFromRequest(request);
    
    	data.honeycomb.tracer.addData({ email });
    
    	return next();
    };

[PrevioushCaptcha](https://developers.cloudflare.com/pages/functions/plugins/hcaptcha/)[NextSentry](https://developers.cloudflare.com/pages/functions/plugins/sentry/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/plugins/honeycomb.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
