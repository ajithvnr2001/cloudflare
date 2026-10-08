---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/test/
title: test \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:46.946868+00:00
---

# test · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/test/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /test



# test

Last updated Jun 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/test/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMockTracker

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

## `MockTracker`

The `MockTracker` API in Node.js provides a means of tracking and managing mock objects in a test environment.
    
    
    import { mock } from 'node:test';
    
    const fn = mock.fn();
    fn(1,2,3);  // does nothing... but
    
    console.log(fn.mock.callCount());  // Records how many times it was called
    console.log(fn.mock.calls[0].arguments);  // Records the arguments that were passed each call

The full `MockTracker` API is documented in the [Node.js documentation for `MockTracker` ↗︎](https://nodejs.org/docs/latest/api/test.html#class-mocktracker).

The Workers implementation of `MockTracker` currently does not include an implementation of the [Node.js mock timers API ↗︎](https://nodejs.org/docs/latest/api/test.html#class-mocktimers).

[PreviousStringDecoder](https://developers.cloudflare.com/workers/runtime-apis/nodejs/string-decoder/)[Nexttimers](https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/test.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
