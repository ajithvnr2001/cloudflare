---
url: https://developers.cloudflare.com/turnstile/tutorials/conditionally-enforcing-turnstile/
title: Conditionally enforce Turnstile \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:08.858052+00:00
---

# Conditionally enforce Turnstile · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/tutorials/conditionally-enforcing-turnstile/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /[Tutorials](https://developers.cloudflare.com/turnstile/tutorials/)
  4. /Conditionally Enforcing Turnstile



# Conditionally enforce Turnstile

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/tutorials/conditionally-enforcing-turnstile/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOverviewImplementationServer-side integrationDemonstration

This tutorial explains how to conditionally enforce Turnstile based on the incoming request, such as a pre-shared secret in a header or a specific IP address.

## Overview

You may have setups such as automation that cannot load or run the Turnstile challenge. Using [`HTMLRewriter`](https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/), this tutorial will demonstrate how to conditionally handle the [client-side widget](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/) and [Siteverify API](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/) when specific criteria are met.

Note

While this tutorial removes Turnstile client-side elements when specific criteria are met, you could instead conditionally insert them.

Caution

It is critical to make sure you are validating tokens with the Siteverify API when your criteria for enforcing Turnstile are not met.

It is not sufficient to only remove the client-side widget from the page, as an attacker can forge the request to your API.

## Implementation

This tutorial will modify the existing [Turnstile demo ↗︎](https://github.com/cloudflare/turnstile-demo-workers/blob/main/src/) to conditionally remove the existing `script` and widget container elements.

src/index.mjsdiff
    
    
    export default {
      async fetch(request) {
        // ...
    
    +    if (request.headers.get("x-bypass-turnstile") === "VerySecretValue") {
    +      class RemoveHandler {
    +        element(element) {
    +          element.remove();
    +        }
    +      }
    +
    +      return new HTMLRewriter()
    +        // Remove the script tag
    +        .on(
    +          'script[src="https://challenges.cloudflare.com/turnstile/v0/api.js"]',
    +          new RemoveHandler(),
    +        )
    +       // Remove the container used in implicit rendering
    +				.on(
    +					'.cf-turnstile',
    +					new RemoveHandler(),
    +				)
    +       // Remove the container used in explicit rendering
    +				.on(
    +					'#myWidget',
    +					new RemoveHandler(),
    +				)
    +        .transform(body);
    +    }
    
        return new Response(body, {
          headers: {
            "Content-Type": "text/html",
          },
        });
      },
    };

## Server-side integration

We will exit early in our validation if the same logic we used to remove the client-side elements is present.

Caution

The same logic must be used in both the client-side and the server-side implementations.

src/index.mjsdiff
    
    
    async function handlePost(request) {
    +  if (request.headers.get("x-bypass-turnstile") === "VerySecretValue") {
    +    return new Response('Turnstile not enforced on this request')
    +  }
    	// Proceed with validation as normal!
    	const body = await request.formData();
      // Turnstile injects a token in "cf-turnstile-response".
      const token = body.get('cf-turnstile-response');
      const ip = request.headers.get('CF-Connecting-IP');
      // ...
    }

With these changes, Turnstile will not be enforced on requests with the header `x-bypass-turnstile: VerySecretValue` present.

## Demonstration

After running `npm run dev` in the project folder, you can test the changes by running the following command:
    
    
    curl -X POST http://localhost:8787/handler -H "x-bypass-turnstile: VerySecretValue"
    
    
    Turnstile not enforced on this request

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/tutorials/conditionally-enforcing-turnstile.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
