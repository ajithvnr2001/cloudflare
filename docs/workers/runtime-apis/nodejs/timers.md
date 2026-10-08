---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/
title: timers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:47.031070+00:00
---

# timers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /timers



# timers

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

Use [`node:timers` ↗︎](https://nodejs.org/api/timers.html) APIs to schedule functions to be executed later.

This includes [`setTimeout` ↗︎](https://nodejs.org/api/timers.html#settimeoutcallback-delay-args) for calling a function after a delay, [`setInterval` ↗︎](https://nodejs.org/api/timers.html#clearintervaltimeout) for calling a function repeatedly, and [`setImmediate` ↗︎](https://nodejs.org/api/timers.html#setimmediatecallback-args) for calling a function in the next iteration of the event loop.

index.jsjs
    
    
    import timers from "node:timers";
    
    export default {
    	async fetch() {
    		console.log("first");
    		const { promise: promise1, resolve: resolve1 } = Promise.withResolvers();
    		const { promise: promise2, resolve: resolve2 } = Promise.withResolvers();
    		timers.setTimeout(() => {
    			console.log("last");
    			resolve1();
    		}, 10);
    
    		timers.setTimeout(() => {
    			console.log("next");
    			resolve2();
    		});
    
    		await Promise.all([promise1, promise2]);
    
    		return new Response("ok");
    	},
    };

index.tsts
    
    
    import timers from "node:timers";
    
    export default {
      async fetch(): Promise<Response> {
        console.log("first");
        const { promise: promise1, resolve: resolve1 } = Promise.withResolvers<void>();
        const { promise: promise2, resolve: resolve2 } = Promise.withResolvers<void>();
        timers.setTimeout(() => {
          console.log("last");
          resolve1();
        }, 10);
    
        timers.setTimeout(() => {
          console.log("next");
          resolve2();
        });
    
        await Promise.all([promise1, promise2]);
    
        return new Response("ok");
      }
    } satisfies ExportedHandler<Env>;

Note

Due to [security-based restrictions on timers](https://developers.cloudflare.com/workers/reference/security-model/#step-1-disallow-timers-and-multi-threading) in Workers, timers are limited to returning the time of the last I/O. This means that while setTimeout, setInterval, and setImmediate will defer your function execution until after other events have run, they will not delay them for the full time specified.

Note

When called from a global level (on [`globalThis` ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)), functions such as `clearTimeout` and `setTimeout` will respect web standards rather than Node.js-specific functionality. For complete Node.js compatibility, you must call functions from the `node:timers` module.

The full `node:timers` API is documented in the [Node.js documentation for `node:timers` ↗︎](https://nodejs.org/api/timers.html).

[Previoustest](https://developers.cloudflare.com/workers/runtime-apis/nodejs/test/)[Nexttls](https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/timers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
