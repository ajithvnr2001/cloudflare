---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/assert/
title: assert \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:45.052882+00:00
---

# assert · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/assert/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /assert



# assert

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/assert/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The [`node:assert` ↗︎](https://nodejs.org/docs/latest/api/assert.html) module in Node.js provides a number of useful assertions that are useful when building tests.
    
    
    import { strictEqual, deepStrictEqual, ok, doesNotReject } from "node:assert";
    
    strictEqual(1, 1); // ok!
    strictEqual(1, "1"); // fails! throws AssertionError
    
    deepStrictEqual({ a: { b: 1 } }, { a: { b: 1 } }); // ok!
    deepStrictEqual({ a: { b: 1 } }, { a: { b: 2 } }); // fails! throws AssertionError
    
    ok(true); // ok!
    ok(false); // fails! throws AssertionError
    
    await doesNotReject(async () => {}); // ok!
    await doesNotReject(async () => {
    	throw new Error("boom");
    }); // fails! throws AssertionError

Note

In the Workers implementation of `assert`, all assertions run in, what Node.js calls, the strict assertion mode. In strict assertion mode, non-strict methods behave like their corresponding strict methods. For example, `deepEqual()` will behave like `deepStrictEqual()`.

Refer to the [Node.js documentation for `assert` ↗︎](https://nodejs.org/dist/latest-v19.x/docs/api/assert.html) for more information.

[PreviousOverview](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)[NextAsyncLocalStorage](https://developers.cloudflare.com/workers/runtime-apis/nodejs/asynclocalstorage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/assert.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
