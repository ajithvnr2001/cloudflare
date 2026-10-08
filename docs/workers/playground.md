---
url: https://developers.cloudflare.com/workers/playground/
title: Playground \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:39.149513+00:00
---

# Playground · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/playground/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Playground



# Playground

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/playground/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHello Cloudflare WorkersUse the PlaygroundLog viewerShareDeploy

Browser support

The Cloudflare Workers Playground is currently only supported in Firefox and Chrome desktop browsers. In Safari, it will show a `PreviewRequestFailed` error message.

The quickest way to experiment with Cloudflare Workers is in the [Playground ↗︎](https://workers.cloudflare.com/playground). It does not require any setup or authentication. The Playground is a sandbox which gives you an instant way to preview and test a Worker directly in the browser.

The Playground uses the same editor as the authenticated experience. The Playground provides the ability to share the code you write as well as deploy it instantly to Cloudflare's global network. This way, you can try new things out and deploy them when you are ready.

[Launch the Playground](https://workers.cloudflare.com/playground)

## Hello Cloudflare Workers

When you arrive in the Playground, you will see this default code:
    
    
    import welcome from "welcome.html";
    
    /**
     * @typedef {Object} Env
     */
    
    export default {
    	/**
    	 * @param {Request} request
    	 * @param {Env} env
    	 * @param {ExecutionContext} ctx
    	 * @returns {Response}
    	 */
    	fetch(request, env, ctx) {
    		console.log("Hello Cloudflare Workers!");
    
    		return new Response(welcome, {
    			headers: {
    				"content-type": "text/html",
    			},
    		});
    	},
    };

This is an example of a multi-module Worker that is receiving a [request](https://developers.cloudflare.com/workers/runtime-apis/request/), logging a message to the console, and then returning a [response](https://developers.cloudflare.com/workers/runtime-apis/response/) body containing the content from `welcome.html`.

Refer to the [Fetch handler documentation](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/) to learn more.

## Use the Playground

As you edit the default code, the Worker will auto-update such that the preview on the right shows your Worker running just as it would in a browser. If your Worker uses URL paths, you can enter those in the input field on the right to navigate to them. The Playground provides type-checking via JSDoc comments and [`workers-types` ↗︎](https://www.npmjs.com/package/@cloudflare/workers-types). The Playground also provides pretty error pages in the event of application errors.

To test a raw HTTP request (for example, to test a `POST` request), go to the **HTTP** tab and select **Send**. You can add and edit headers via this panel, as well as edit the body of a request.

## Log viewer

The Playground and the quick editor in the Workers dashboard include a lightweight log viewer at the bottom of the preview panel. The log viewer displays the output of any calls to `console.log` made during preview runs.

The log viewer supports the following:

  * Logging primitive values, objects, and arrays.
  * Clearing the log output between runs.



At this time, the log viewer does not support logging class instances or their properties (for example, `request.url`).

If you need a more complete development experience with full debugging capabilities, you can use [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) locally. To clone an existing Worker from your dashboard for local development, sign up and use the [`wrangler init --from-dash`](https://developers.cloudflare.com/workers/wrangler/commands/general/#init) command once your worker is deployed.

## Share

To share what you have created, select **Copy Link** in the top right of the screen. This will copy a unique URL to your clipboard that you can share with anyone. These links do not expire, so you can bookmark your creation and share it at any time. Users that open a shared link will see the Playground with the shared code and preview.

## Deploy

You can deploy a Worker from the Playground. If you are already logged in, you can review the Worker before deploying. Otherwise, you will be taken through the first-time user onboarding flow before you can review and deploy.

Once deployed, your Worker will get its own unique URL and be available almost instantly on Cloudflare's global network. From here, you can add [Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), [storage resources](https://developers.cloudflare.com/workers/platform/storage-options/), and more.

[PreviousShare a local dev server](https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/)[NextOverview](https://developers.cloudflare.com/workers/configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/playground.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
