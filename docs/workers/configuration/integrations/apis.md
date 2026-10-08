---
url: https://developers.cloudflare.com/workers/configuration/integrations/apis/
title: APIs \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:14.726913+00:00
---

# APIs · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/configuration/integrations/apis/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Configuration](https://developers.cloudflare.com/workers/configuration/)

  4. /[Integrations](https://developers.cloudflare.com/workers/configuration/integrations/)
  5. /APIs



# APIs

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/configuration/integrations/apis/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAuthenticationTips

To integrate with third party APIs from Cloudflare Workers, use the [fetch API](https://developers.cloudflare.com/workers/runtime-apis/fetch/) to make HTTP requests to the API endpoint. Then use the response data to modify or manipulate your content as needed.

For example, if you want to integrate with a weather API, make a fetch request to the API endpoint and retrieve the current weather data. Then use this data to display the current weather conditions on your website.

To make the `fetch()` request, add the following code to your project's `src/index.js` file:
    
    
    async function handleRequest(request) {
    	// Make the fetch request to the third party API endpoint
    	const response = await fetch("https://weather-api.com/endpoint", {
    		method: "GET",
    		headers: {
    			"Content-Type": "application/json",
    		},
    	});
    
    	// Retrieve the data from the response
    	const data = await response.json();
    
    	// Use the data to modify or manipulate your content as needed
    	return new Response(data);
    }

## Authentication

If your API requires authentication, use Wrangler secrets to securely store your credentials. To do this, create a secret in your Cloudflare Workers project using the following [`wrangler secret`](https://developers.cloudflare.com/workers/wrangler/commands/general/#secret) command:
    
    
    wrangler secret put SECRET_NAME

Then, retrieve the secret value in your code using the following code snippet:
    
    
    const secretValue = env.SECRET_NAME;

Then use the secret value to authenticate with the external service. For example, if the external service requires an API key for authentication, include it in your request headers.

For services that require mTLS authentication, use [mTLS certificates](https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls) to present a client certificate.

## Tips

  * Use the [Cache API](https://developers.cloudflare.com/workers/runtime-apis/cache/) to cache data from the third party API. This allows you to optimize cacheable requests made to the API. Integrating with third party APIs from Cloudflare Workers adds additional functionality and features to your application.

  * Use [Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) when communicating with external APIs, which treat your Worker as your core application.




[PreviousOverview](https://developers.cloudflare.com/workers/configuration/integrations/)[NextExternal Services](https://developers.cloudflare.com/workers/configuration/integrations/external-services/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/configuration/integrations/apis.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
