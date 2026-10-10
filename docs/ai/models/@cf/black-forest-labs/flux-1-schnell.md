---
url: https://developers.cloudflare.com/ai/models/%40cf/black-forest-labs/flux-1-schnell/
title: flux-1-schnell (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:23.409439+00:00
---

# flux-1-schnell (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/black-forest-labs/flux-1-schnell/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# flux-1-schnell

Text-to-Image • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/black-forest-labs/flux-1-schnell`

  * Cloudflare-hosted



FLUX.1 [schnell] is a 12 billion parameter rectified flow transformer capable of generating images from text descriptions. 

Model Info|   
---|---  
Terms and License| [link ↗](https://bfl.ai/legal/terms-of-service)  
  
## Usage
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const response = await env.AI.run('@cf/black-forest-labs/flux-1-schnell', {
    			prompt: 'a cyberpunk lizard',
    			seed: Math.floor(Math.random() * 10)
    		});
    		// response.image is base64 encoded which can be used directly as an <img src=""> data URI
    		const dataURI = `data:image/jpeg;charset=utf-8;base64,${response.image}`;
    		return Response.json({ dataURI });
    	},
    } satisfies ExportedHandler<Env>;
    
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const response = await env.AI.run('@cf/black-forest-labs/flux-1-schnell', {
    			prompt: 'a cyberpunk lizard',
    			seed: Math.floor(Math.random() * 10)
    		});
    		// Convert from base64 string
    		const binaryString = atob(response.image);
    		// Create byte representation
    		const img = Uint8Array.from(binaryString, (m) => m.codePointAt(0));
    		return new Response(img, {
    			headers: {
    				'Content-Type': 'image/jpeg',
    			},
    		});
    	},
    } satisfies ExportedHandler<Env>;
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/black-forest-labs/flux-1-schnell  \
      -X POST  \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \
      -d '{ "prompt": "cyberpunk cat", "seed": "Random positive integer" }'

## Parameters

prompt

`string`requiredminLength: 1maxLength: 2048A text description of the image you want to generate.

steps

`integer`maximum: 8The number of diffusion steps; higher values can improve quality but take longer. Default is 4

image

`string`The generated image in Base64 format.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/black-forest-labs/flux-1-schnell/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/black-forest-labs/flux-1-schnell/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/black-forest-labs/flux-1-schnell/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/black-forest-labs/flux-1-schnell/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
