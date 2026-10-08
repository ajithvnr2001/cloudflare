---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/string-decoder/
title: StringDecoder \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:46.874741+00:00
---

# StringDecoder · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/string-decoder/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /StringDecoder



# StringDecoder

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/string-decoder/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The [`node:string_decoder` ↗︎](https://nodejs.org/api/string_decoder.html) is a legacy utility module that predates the WHATWG standard [TextEncoder](https://developers.cloudflare.com/workers/runtime-apis/encoding/#textencoder) and [TextDecoder](https://developers.cloudflare.com/workers/runtime-apis/encoding/#textdecoder) API. In most cases, you should use `TextEncoder` and `TextDecoder` instead. `StringDecoder` is available in the Workers runtime primarily for compatibility with existing npm packages that rely on it. `StringDecoder` can be accessed using:
    
    
    const { StringDecoder } = require("node:string_decoder");
    const decoder = new StringDecoder("utf8");
    
    const cent = Buffer.from([0xc2, 0xa2]);
    console.log(decoder.write(cent));
    
    const euro = Buffer.from([0xe2, 0x82, 0xac]);
    console.log(decoder.write(euro));

Refer to the [Node.js documentation for `string_decoder` ↗︎](https://nodejs.org/dist/latest-v20.x/docs/api/string_decoder.html) for more information.

[PreviousStreams](https://developers.cloudflare.com/workers/runtime-apis/nodejs/streams/)[Nexttest](https://developers.cloudflare.com/workers/runtime-apis/nodejs/test/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/string-decoder.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
