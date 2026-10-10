---
url: https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/
title: Improved support for Node.js Crypto and TLS APIs in Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.101432+00:00
---

# Improved support for Node.js Crypto and TLS APIs in Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 8, 2025

## Improved support for Node.js Crypto and TLS APIs in Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When using a Worker with the [`nodejs_compat`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) compatibility flag enabled, the following Node.js APIs are now available:

  * [`node:crypto`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/)
  * [`node:tls`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/)



This make it easier to reuse existing Node.js code in Workers or use npm packages that depend on these APIs.

#### node:crypto

The full [`node:crypto` ↗︎](https://nodejs.org/api/crypto.html) API is now available in Workers.

You can use it to verify and sign data:
    
    
    import { sign, verify } from "node:crypto";
    
    const signature = sign("sha256", "-data to sign-", env.PRIVATE_KEY);
    const verified = verify("sha256", "-data to sign-", env.PUBLIC_KEY, signature);

Or, to encrypt and decrypt data:
    
    
    import { publicEncrypt, privateDecrypt } from "node:crypto";
    
    const encrypted = publicEncrypt(env.PUBLIC_KEY, "some data");
    const plaintext = privateDecrypt(env.PRIVATE_KEY, encrypted);

See the [`node:crypto` documentation](https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/) for more information.

#### node:tls

The following APIs from `node:tls` are now available:

  * [`connect` ↗︎](https://nodejs.org/api/tls.html#tlsconnectoptions-callback)
  * [`TLSSocket` ↗︎](https://nodejs.org/api/tls.html#class-tlstlssocket)
  * [`checkServerIdentity` ↗︎](https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert)
  * [`createSecureContext` ↗︎](https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions)



This enables secure connections over TLS (Transport Layer Security) to external services.
    
    
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

See the [`node:tls` documentation](https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/) for more information.
