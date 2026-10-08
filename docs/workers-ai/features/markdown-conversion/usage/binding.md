---
url: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/
title: Workers Binding \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:58.630054+00:00
---

# Workers Binding · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features[Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/)

  4. /Usage
  5. /Workers Binding



# Workers Binding

Last updated Jul 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExamples Converting files Getting supported file formatsMethods async env.AI.toMarkdown() async env.AI.toMarkdown().transform() async env.AI.toMarkdown().supported()

Cloudflare’s serverless platform allows you to run code at the edge to build full-stack applications with [Workers](https://developers.cloudflare.com/workers/). A [binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/) enables your Worker or Pages Function to interact with resources on the Cloudflare Developer Platform.

To use our Markdown Conversion service directly from your Workers, create an AI binding either in the Cloudflare dashboard (refer to [AI bindings](https://developers.cloudflare.com/pages/functions/bindings/#workers-ai) for instructions), or you can update your [Wrangler file](https://developers.cloudflare.com/workers/wrangler/configuration/). Add the following to your Wrangler file:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "ai": {
        "binding": "AI"
      }
    }
    
    
    [ai]
    binding = "AI" # i.e. available in your Worker on env.AI

## Examples

### Converting files

In this example, we fetch a PDF document and an image from R2 and feed them both to `env.AI.toMarkdown`. The result is a list of converted documents. Workers AI models are used automatically to detect and summarize the image.
    
    
    import { Env } from "./env";
    
    export default {
    	async fetch(request, env, ctx) {
    		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/somatosensory.pdf
    		const pdf = await env.R2.get("somatosensory.pdf");
    
    		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/cat.jpeg
    		const cat = await env.R2.get("cat.jpeg");
    
    		return Response.json(
    			await env.AI.toMarkdown([
    				{
    					name: "somatosensory.pdf",
    					blob: new Blob([await pdf.arrayBuffer()], {
    						type: "application/pdf",
    					}),
    				},
    				{
    					name: "cat.jpeg",
    					blob: new Blob([await cat.arrayBuffer()], {
    						type: "image/jpeg",
    					}),
    				},
    			]),
    		);
    	},
    };
    
    
    import { Env } from "./env";
    
    export default {
    	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/somatosensory.pdf
    		const pdf = await env.R2.get("somatosensory.pdf");
    
    		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/cat.jpeg
    		const cat = await env.R2.get("cat.jpeg");
    
    		return Response.json(
    			await env.AI.toMarkdown([
    				{
    					name: "somatosensory.pdf",
    					blob: new Blob([await pdf.arrayBuffer()], {
    						type: "application/pdf",
    					}),
    				},
    				{
    					name: "cat.jpeg",
    					blob: new Blob([await cat.arrayBuffer()], {
    						type: "image/jpeg",
    					}),
    				},
    			]),
    		);
    	},
    };

### Getting supported file formats
    
    
    import { Env } from "./env";
    
    export default {
    	async fetch(request, env, ctx) {
    		return Response.json(await env.AI.toMarkdown().supported());
    	},
    };
    
    
    import { Env } from "./env";
    
    export default {
    	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    		return Response.json(await env.AI.toMarkdown().supported());
    	},
    };

## Methods

### async env.AI.toMarkdown()

Takes a document or list of documents in different formats and converts them to Markdown.
    
    
    const result = await env.AI.toMarkdown({
    	name: "document.pdf",
    	blob: new Blob([documentBuffer]),
    });
    
    
    const result = await env.AI.toMarkdown({
    	name: "document.pdf",
    	blob: new Blob([documentBuffer]),
    });

#### Parameter

  * `files`: `MarkdownDocument | MarkdownDocument[]`\- an instance of or an array of `MarkdownDocument`s.

  * `conversionOptions`: `ConversionOptions`\- options that control how conversion happens. See [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/) for further details.




#### Return values

  * `results`: `Promise<ConversionResult | ConversionResult[]>`\- An instance of or an array of `ConversionResult`s.



#### `MarkdownDocument` definition

  * `name` `string`

    * Name of the document to convert.
  * `blob` `Blob`

    * A new [Blob ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Blob/Blob) object with the document content.



#### `ConversionResult` definition

  * `id` `string`

    * ID associated to this object.
  * `name` `string`

    * Name of the converted document. Matches the input name.
  * `format` `'markdown' | 'text' | 'error'`

    * The format of this `ConversionResult` object. Equals `text` when you set the [`output.format`](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/#output) option to `text`.
  * `mimetype` `string`

    * The detected [mime type ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types) of the document.
  * `tokens` `number`

    * The estimated number of tokens of the converted document. Not present if `format` is equal to `error`.
  * `data` `string`

    * The content of the converted document. Not present if `format` is equal to `error`.
  * `error` `string`

    * The error message explaining why this conversion failed. Only present if `format` is equal to `error`.



### async env.AI.toMarkdown().transform()

This method is similar to `env.AI.toMarkdown` except that it is exposed through a new handle. It takes the same arguments and returns the same values.
    
    
    const result = await env.AI.toMarkdown().transform({
    	name: "document.pdf",
    	blob: new Blob([documentBuffer]),
    });
    
    
    const result = await env.AI.toMarkdown().transform({
    	name: "document.pdf",
    	blob: new Blob([documentBuffer]),
    });

### async env.AI.toMarkdown().supported()

Returns a list of file formats that are currently supported for markdown conversion. See [Supported formats](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/) for the full list of file formats that can be converted into Markdown.
    
    
    const formats = await env.AI.toMarkdown().supported();
    
    
    const formats = await env.AI.toMarkdown().supported();

#### Return values

  * `results`: `SupportedFormat[]`\- An array of all formats supported for markdown conversion.



#### `SupportedFormat` definition

  * `extension` `string`

    * Extension of files in this format.
  * `mimeType` `string`

    * The [mime type ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types) of files of this format



[PreviousOverview](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/)[NextREST API](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/markdown-conversion/usage/binding.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
