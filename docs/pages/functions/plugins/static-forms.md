---
url: https://developers.cloudflare.com/pages/functions/plugins/static-forms/
title: Static Forms \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:33.858061+00:00
---

# Static Forms · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/plugins/static-forms/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /…

[Functions](https://developers.cloudflare.com/pages/functions/)

  4. /[Pages Plugins](https://developers.cloudflare.com/pages/functions/plugins/)
  5. /Static Forms



# Static Forms

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/plugins/static-forms/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationUsage

The Static Forms Pages Plugin intercepts all form submissions made which have the `data-static-form-name` attribute set. This allows you to take action on these form submissions by, for example, saving the submission to KV.

## Installation

npmyarnpnpmbun
    
    
    npm i @cloudflare/pages-plugin-static-forms
    
    
    yarn add @cloudflare/pages-plugin-static-forms
    
    
    pnpm add @cloudflare/pages-plugin-static-forms
    
    
    bun add @cloudflare/pages-plugin-static-forms

## Usage
    
    
    import staticFormsPlugin from "@cloudflare/pages-plugin-static-forms";
    
    export const onRequest: PagesFunction = staticFormsPlugin({
    	respondWith: ({ formData, name }) => {
    		const email = formData.get("email");
    		return new Response(
    			`Hello, ${email}! Thank you for submitting the ${name} form.`,
    		);
    	},
    });
    
    
    <body>
    	<h1>Sales enquiry</h1>
    	<form data-static-form-name="sales">
    		<label>Email address <input type="email" name="email" /></label>
    		<label>Message <textarea name="message"></textarea></label>
    		<button type="submit">Submit</button>
    	</form>
    </body>

The Plugin takes a single argument, an object with a `respondWith` property. This function takes an object with a `formData` property (the [`FormData` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/FormData) instance) and `name` property (the name value of your `data-static-form-name` attribute). It should return a `Response` or `Promise` of a `Response`. It is in this `respondWith` function that you can take action such as serializing the `formData` and saving it to a KV namespace.

The `method` and `action` attributes of the HTML form do not need to be set. The Plugin will automatically override them to allow it to intercept the submission.

[PreviousSentry](https://developers.cloudflare.com/pages/functions/plugins/sentry/)[NextStytch](https://developers.cloudflare.com/pages/functions/plugins/stytch/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/plugins/static-forms.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
