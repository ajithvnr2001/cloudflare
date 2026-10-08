---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/
title: EventEmitter \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:45.804417+00:00
---

# EventEmitter · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /EventEmitter



# EventEmitter

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

An [`EventEmitter` ↗︎](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) is an object that emits named events that cause listeners to be called.
    
    
    import { EventEmitter } from "node:events";
    
    const emitter = new EventEmitter();
    emitter.on("hello", (...args) => {
    	console.log(...args); // 1 2 3
    });
    
    emitter.emit("hello", 1, 2, 3);

The implementation in the Workers runtime supports the entire Node.js `EventEmitter` API. This includes the [`captureRejections` ↗︎](https://nodejs.org/docs/latest/api/events.html#capture-rejections-of-promises) option that allows improved handling of async functions as event handlers:
    
    
    const emitter = new EventEmitter({ captureRejections: true });
    emitter.on("hello", async (...args) => {
    	throw new Error("boom");
    });
    emitter.on("error", (err) => {
    	// the async promise rejection is emitted here!
    });

Like Node.js, when an `'error'` event is emitted on an `EventEmitter` and there is no listener for it, the error will be immediately thrown. However, in Node.js it is possible to add a handler on the `process` object for the `'uncaughtException'` event to catch globally uncaught exceptions. The `'uncaughtException'` event, however, is currently not implemented in the Workers runtime. It is strongly recommended to always add an `'error'` listener to any `EventEmitter` instance.

Refer to the [Node.js documentation for `EventEmitter` ↗︎](https://nodejs.org/api/events.html#class-eventemitter) for more information.

[Previousdns](https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/)[Nextfs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/fs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/EventEmitter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
