---
url: https://developers.cloudflare.com/workers/testing/miniflare/core/web-sockets/
title: WebSockets \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:55.262700+00:00
---

# WebSockets · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/core/web-sockets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Core
  5. /WebSockets



# WebSockets

Last updated Jan 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/web-sockets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewServer

  * [WebSockets Reference](https://developers.cloudflare.com/workers/runtime-apis/websockets)
  * [Using WebSockets](https://developers.cloudflare.com/workers/examples/websockets/)



## Server

Miniflare will always upgrade Web Socket connections. The Worker must respond with a status `101 Switching Protocols` response including a `webSocket`. For example, the Worker below implements an echo WebSocket server:
    
    
    export default {
    	fetch(request) {
    		const [client, server] = Object.values(new WebSocketPair());
    
    		server.accept();
    		server.addEventListener("message", (event) => {
    			server.send(event.data);
    		});
    
    		return new Response(null, {
    			status: 101,
    			webSocket: client,
    		});
    	},
    };

When using `dispatchFetch`, you are responsible for handling WebSockets by using the `webSocket` property on `Response`. As an example, if the above worker script was stored in `echo.mjs`:
    
    
    import { Miniflare } from "miniflare";
    
    const mf = new Miniflare({
    	modules: true,
    	scriptPath: "echo.mjs",
    });
    
    const res = await mf.dispatchFetch("https://example.com", {
    	headers: {
    		Upgrade: "websocket",
    	},
    });
    const webSocket = res.webSocket;
    webSocket.accept();
    webSocket.addEventListener("message", (event) => {
    	console.log(event.data);
    });
    
    webSocket.send("Hello!"); // Above listener logs "Hello!"

[PreviousWeb Standards](https://developers.cloudflare.com/workers/testing/miniflare/core/standards/)[NextAttaching a Debugger](https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/core/web-sockets.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
