---
url: https://developers.cloudflare.com/flagship/binding/
title: Binding API \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:17.246809+00:00
---

# Binding API · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/binding/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /Binding API



# Binding API

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/flagship/binding/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers access Flagship through a binding that you add to your Wrangler configuration file. The `binding` field sets the variable name you use in your Worker code.
    
    
    {
    	"flagship": [
    		{
    			"binding": "FLAGS",
    			"app_id": "<APP_ID>",
    		},
    	],
    }
    
    
    [[flagship]]
    binding = "FLAGS"
    app_id = "<APP_ID>"

Replace `<APP_ID>` with the app ID from your Flagship app. If you have not created an app yet, refer to the [Get started guide](https://developers.cloudflare.com/flagship/get-started/#create-an-app-and-a-flag). With this configuration, the binding is available as `env.FLAGS`. Refer to [Configuration](https://developers.cloudflare.com/flagship/configuration/) for additional options such as binding to multiple apps.

The binding provides type-safe methods for evaluating feature flags. If an evaluation fails or a flag is not found, the method returns the default value you provide.
    
    
    export default {
    	async fetch(request, env) {
    		const enabled = await env.FLAGS.getBooleanValue("new-feature", false, {
    			userId: "user-42",
    		});
    		return new Response(enabled ? "Feature on" : "Feature off");
    	},
    };
    
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const enabled = await env.FLAGS.getBooleanValue("new-feature", false, {
    			userId: "user-42",
    		});
    		return new Response(enabled ? "Feature on" : "Feature off");
    	},
    };

The binding has the type `Flagship` from the `@cloudflare/workers-types` package.

  * [Types](https://developers.cloudflare.com/flagship/binding/types/)
  * [Methods](https://developers.cloudflare.com/flagship/binding/methods/)



[PreviousBest practices](https://developers.cloudflare.com/flagship/best-practices/)[NextTypes](https://developers.cloudflare.com/flagship/binding/types/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/binding/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
