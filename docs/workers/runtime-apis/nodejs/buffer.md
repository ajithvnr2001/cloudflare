---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/buffer/
title: Buffer \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:45.418775+00:00
---

# Buffer · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/buffer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /Buffer



# Buffer

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/buffer/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The [`Buffer` ↗︎](https://nodejs.org/docs/latest/api/buffer.html) API in Node.js is one of the most commonly used Node.js APIs for manipulating binary data. Every `Buffer` instance extends from the standard [`Uint8Array` ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) class, but adds a range of unique capabilities such as built-in base64 and hex encoding/decoding, byte-order manipulation, and encoding-aware substring searching.
    
    
    import { Buffer } from "node:buffer";
    
    const buf = Buffer.from("hello world", "utf8");
    
    console.log(buf.toString("hex"));
    // Prints: 68656c6c6f20776f726c64
    console.log(buf.toString("base64"));
    // Prints: aGVsbG8gd29ybGQ=

A Buffer extends from `Uint8Array`. Therefore, it can be used in any Workers API that currently accepts `Uint8Array`, such as creating a new Response:
    
    
    const response = new Response(Buffer.from("hello world"));

You can also use the `Buffer` API when interacting with streams:
    
    
    const writable = getWritableStreamSomehow();
    const writer = writable.getWriter();
    writer.write(Buffer.from("hello world"));

One key difference between the Workers implementation of `Buffer` and the Node.js implementation is that some methods of creating a `Buffer` in Node.js will allocate those from a global memory pool as a performance optimization. The Workers implementation does not use a memory pool and all `Buffer` instances are allocated independently.

Further, in Node.js it is possible to allocate a `Buffer` with uninitialized memory using the `Buffer.allocUnsafe()` method. This is not supported in Workers and `Buffer` instances are always initialized so that the `Buffer` is always filled with null bytes (`0x00`) when allocated.

Refer to the [Node.js documentation for `Buffer` ↗︎](https://nodejs.org/dist/latest-v19.x/docs/api/buffer.html) for more information.

[PreviousAsyncLocalStorage](https://developers.cloudflare.com/workers/runtime-apis/nodejs/asynclocalstorage/)[Nextcrypto](https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/buffer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
