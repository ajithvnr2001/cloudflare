---
url: https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/
title: Non-JavaScript modules \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:05.035949+00:00
---

# Non-JavaScript modules · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/)

  4. /Reference
  5. /Non-JavaScript modules



# Non-JavaScript modules

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In addition to TypeScript and JavaScript, the following module types are automatically configured to be importable in your Worker code.

Module extension | Imported type  
---|---  
`.txt` | `string`  
`.html` | `string`  
`.sql` | `string`  
`.bin` | `ArrayBuffer`  
`.wasm`, `.wasm?module` | `WebAssembly.Module`  
  
For example, with the following import, `text` will be a string containing the contents of `example.txt`:
    
    
    import text from "./example.txt";

This is also the basis for importing Wasm, as in the following example:
    
    
    import wasm from "./example.wasm";
    
    // Instantiate Wasm modules in the module scope
    const instance = await WebAssembly.instantiate(wasm);
    
    export default {
    	fetch() {
    		const result = instance.exports.exported_func();
    
    		return new Response(result);
    	},
    };

Note

Cloudflare Workers does not support `WebAssembly.instantiateStreaming()`.

[PreviousCloudflare Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/cloudflare-environments/)[NextProgrammatic configuration](https://developers.cloudflare.com/workers/vite-plugin/reference/programmatic-configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/vite-plugin/reference/non-javascript-modules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
