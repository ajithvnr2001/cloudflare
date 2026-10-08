---
url: https://developers.cloudflare.com/changelog/post/2025-01-28-nodejs-compat-improvements/
title: Support for Node.js DNS, Net, and Timer APIs in Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:02.369147+00:00
---

# Support for Node.js DNS, Net, and Timer APIs in Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-28-nodejs-compat-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 28, 2025

## Support for Node.js DNS, Net, and Timer APIs in Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-28-nodejs-compat-improvements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When using a Worker with the [`nodejs_compat`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) compatibility flag enabled, you can now use the following Node.js APIs:

  * [`node:net`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/)
  * [`node:dns`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/)
  * [`node:timers`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/)



#### node:net

You can use [`node:net` ↗︎](https://nodejs.org/api/net.html) to create a direct connection to servers via a TCP sockets with [`net.Socket` ↗︎](https://nodejs.org/api/net.html#class-netsocket).

index.jsjs
    
    
    import net from "node:net";
    
    const exampleIP = "127.0.0.1";
    
    export default {
    	async fetch(req) {
    		const socket = new net.Socket();
    		socket.connect(4000, exampleIP, function () {
    			console.log("Connected");
    		});
    
    		socket.write("Hello, Server!");
    		socket.end();
    
    		return new Response("Wrote to server", { status: 200 });
    	},
    };

index.tsts
    
    
    import net from "node:net";
    
    const exampleIP = "127.0.0.1";
    
    export default {
      async fetch(req): Promise<Response> {
        const socket = new net.Socket();
        socket.connect(4000, exampleIP, function () {
          console.log("Connected");
        });
    
        socket.write("Hello, Server!");
        socket.end();
    
        return new Response("Wrote to server", { status: 200 });
      },
    } satisfies ExportedHandler;

Additionally, you can now use other APIs including [`net.BlockList` ↗︎](https://nodejs.org/api/net.html#class-netblocklist) and [`net.SocketAddress` ↗︎](https://nodejs.org/api/net.html#class-netsocketaddress).

Note that [`net.Server` ↗︎](https://nodejs.org/api/net.html#class-netserver) is not supported.

#### node:dns

You can use [`node:dns` ↗︎](https://nodejs.org/api/dns.html) for name resolution via [DNS over HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/) using [Cloudflare DNS ↗︎](https://www.cloudflare.com/application-services/products/dns/) at 1.1.1.1.

index.jsjs
    
    
    import dns from "node:dns";
    
    let response = await dns.promises.resolve4("cloudflare.com", "NS");

index.tsts
    
    
    import dns from 'node:dns';
    
    let response = await dns.promises.resolve4('cloudflare.com', 'NS');

All `node:dns` functions are available, except `lookup`, `lookupService`, and `resolve` which throw "Not implemented" errors when called.

#### node:timers

You can use [`node:timers` ↗︎](https://nodejs.org/api/timers.html) to schedule functions to be called at some future period of time.

This includes [`setTimeout` ↗︎](https://nodejs.org/api/timers.html#settimeoutcallback-delay-args) for calling a function after a delay, [`setInterval` ↗︎](https://nodejs.org/api/timers.html#setintervalcallback-delay-args) for calling a function repeatedly, and [`setImmediate` ↗︎](https://nodejs.org/api/timers.html#setimmediatecallback-args) for calling a function in the next iteration of the event loop.

index.jsjs
    
    
    import timers from "node:timers";
    
    console.log("first");
    timers.setTimeout(() => {
    	console.log("last");
    }, 10);
    
    timers.setTimeout(() => {
    	console.log("next");
    });

index.tsts
    
    
    import timers from "node:timers";
    
    console.log("first");
    timers.setTimeout(() => {
      console.log("last");
    }, 10);
    
    timers.setTimeout(() => {
      console.log("next");
    });
