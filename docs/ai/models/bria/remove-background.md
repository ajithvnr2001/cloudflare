---
url: https://developers.cloudflare.com/ai/models/bria/remove-background/
title: Remove Background (bria) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:53.995177+00:00
---

# Remove Background (bria) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bria/remove-background/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



b

# Remove Background

Image-to-Image • bria

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/bria/remove-background/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bria/remove-background`

  * Third-party



Bria's RMBG 2.0 model removes the background from an image and returns a PNG cutout with a transparent background. Partial transparency from the input's alpha channel is kept by default.

Model Info|   
---|---  
Terms and License| [link ↗](https://bria.ai/terms-of-use)  
More information| [link ↗](https://docs.bria.ai/image-editing/editing/background-remove)  
Pricing| 

  * Per image$0.018

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bria/remove-background',
      { image: 'https://labs-assets.bria.ai/sandbox-example-inputs/remove_background_example.jpg' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bria/remove-background",
      "input": {
        "image": "https://labs-assets.bria.ai/sandbox-example-inputs/remove_background_example.jpg"
      }
    }'

![Portrait Cutout](https://examples.aig.cloudflare.com/bria/remove-background/portrait-cutout.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/bria/remove-background/portrait-cutout.png"
      }
    }

## Parameters

image

`string`requiredminLength: 1JPEG or PNG image (RGB, RGBA, or CMYK), a public URL or base64-encoded image data (a `data:` URI prefix is accepted).

preserve_alpha

`boolean`Keep partial transparency from the input alpha channel. When false, every foreground pixel is fully opaque. Default true.

visual_input_content_moderation

`boolean`Reject the request if the input image fails content moderation. Default false.

visual_output_content_moderation

`boolean`Fail the request if the result fails content moderation. Default false.

image

`string`format: uriURL of the PNG cutout with a transparent background. Bria hosts it for a limited time (3 days by default); download it to keep it.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bria/remove-background/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bria/remove-background/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bria/remove-background/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bria/remove-background/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
