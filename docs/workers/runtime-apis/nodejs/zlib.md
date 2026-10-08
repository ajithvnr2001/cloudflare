---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/zlib/
title: zlib \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:48.418717+00:00
---

# zlib · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/zlib/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /zlib



# zlib

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/zlib/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The node:zlib module provides compression functionality implemented using Gzip, Deflate/Inflate, and Brotli. To access it:
    
    
    import zlib from "node:zlib";

The full `node:zlib` API is documented in the [Node.js documentation for `node:zlib` ↗︎](https://nodejs.org/api/zlib.html).

[Previousutil](https://developers.cloudflare.com/workers/runtime-apis/nodejs/util/)[NextPerformance and timers](https://developers.cloudflare.com/workers/runtime-apis/performance/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/zlib.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
