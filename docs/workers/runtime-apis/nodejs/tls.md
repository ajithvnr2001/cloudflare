---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/
title: tls \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:47.611660+00:00
---

# tls · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /tls



# tls

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

You can use [`node:tls` ↗︎](https://nodejs.org/api/tls.html) to create secure connections to external services using [TLS ↗︎](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security) (Transport Layer Security).
    
    
    import { connect } from "node:tls";
    
    // ... in a request handler ...
    const connectionOptions = { key: env.KEY, cert: env.CERT };
    const socket = connect(url, connectionOptions, () => {
    	if (socket.authorized) {
    		console.log("Connection authorized");
    	}
    });
    
    socket.on("data", (data) => {
    	console.log(data);
    });
    
    socket.on("end", () => {
    	console.log("server ends connection");
    });

The following APIs are available:

  * [`connect` ↗︎](https://nodejs.org/api/tls.html#tlsconnectoptions-callback)
  * [`TLSSocket` ↗︎](https://nodejs.org/api/tls.html#class-tlstlssocket)
  * [`checkServerIdentity` ↗︎](https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert)
  * [`createSecureContext` ↗︎](https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions)



All other APIs, including [`tls.Server` ↗︎](https://nodejs.org/api/tls.html#class-tlsserver) and [`tls.createServer` ↗︎](https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener), are not supported and will throw a `Not implemented` error when called.

The full `node:tls` API is documented in the [Node.js documentation for `node:tls` ↗︎](https://nodejs.org/api/tls.html).

[Previoustimers](https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/)[Nexturl](https://developers.cloudflare.com/workers/runtime-apis/nodejs/url/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/tls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
