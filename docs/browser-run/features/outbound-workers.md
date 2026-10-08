---
url: https://developers.cloudflare.com/browser-run/features/outbound-workers/
title: Outbound Workers \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:36.034054+00:00
---

# Outbound Workers · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/features/outbound-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Additional features
  4. /Outbound Workers



# Outbound Workers

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/features/outbound-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the bindingsRoute requests by hostnameConstraintsNext steps

Use `outboundByHost` to send browser requests for selected hostnames through another Worker. The outbound Worker can reach a private service, add authentication, or transform the response before it reaches the browser.

This feature is useful when the browser should request a hostname that has no public DNS record. Browser Run matches the hostname and sends the request to the Worker Fetcher instead of requiring public DNS resolution.

## Configure the bindings

Declare a Browser Run binding and a service binding for the outbound Worker:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "browser-runner",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "compatibility_flags": [
        "nodejs_compat"
      ],
      "browser": {
        "binding": "BROWSER"
      },
      "services": [
        {
          "binding": "OUTBOUND",
          "service": "outbound-worker"
        }
      ]
    }
    
    
    name = "browser-runner"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = ["nodejs_compat"]
    
    [browser]
    binding = "BROWSER"
    
    [[services]]
    binding = "OUTBOUND"
    service = "outbound-worker"

The service binding gives the browser Worker a `Fetcher` for the outbound Worker. The outbound Worker does not need a public route.

## Route requests by hostname

Pass the service binding to `launch()` or `acquire()` in the `outboundByHost` map. The map key must exactly match the hostname in the browser request.

The following example uses raw CDP commands. It opens a Browser Run session, routes `private.example.test` through the outbound Worker, and sends a `Page.navigate` command:

src/index.jsjs
    
    
    let nextCdpCommandId = 0;
    
    function sendCdpCommand(socket, method, params = {}) {
    	return new Promise((resolve, reject) => {
    		const id = ++nextCdpCommandId;
    		const timeout = setTimeout(() => {
    			cleanup();
    			reject(new Error(`CDP command "${method}" timed out`));
    		}, 30_000);
    
    		const cleanup = () => {
    			clearTimeout(timeout);
    			socket.removeEventListener("message", onMessage);
    			socket.removeEventListener("close", onClose);
    		};
    
    		const onClose = () => {
    			cleanup();
    			reject(new Error("CDP connection closed before the command completed"));
    		};
    
    		const onMessage = (event) => {
    			const message = JSON.parse(event.data);
    			if (message.id !== id) return;
    
    			cleanup();
    			if (message.error) {
    				reject(new Error(message.error.message));
    			} else {
    				resolve(message.result);
    			}
    		};
    
    		socket.addEventListener("message", onMessage);
    		socket.addEventListener("close", onClose);
    		try {
    			socket.send(JSON.stringify({ id, method, params }));
    		} catch (error) {
    			cleanup();
    			reject(error);
    		}
    	});
    }
    
    export default {
    	async fetch(_request, env) {
    		const connection = await env.BROWSER.launch({
    			outboundByHost: {
    				"private.example.test": env.OUTBOUND,
    			},
    		});
    		const response = await connection.webSocket.fetch(
    			"https://browser-binding.invalid",
    			{ headers: { Upgrade: "websocket" } },
    		);
    		if (!response.webSocket) {
    			throw new Error("Browser Run did not return a WebSocket");
    		}
    
    		const socket = response.webSocket;
    		socket.accept();
    
    		try {
    			await sendCdpCommand(socket, "Page.navigate", {
    				url: "http://private.example.test",
    			});
    			return new Response("Navigation sent through the outbound Worker");
    		} finally {
    			socket.close();
    			await env.BROWSER.closeSession(connection.sessionId);
    		}
    	},
    };

src/index.tsts
    
    
    interface Env {
    	BROWSER: Fetcher;
    	OUTBOUND: Fetcher;
    }
    
    type CdpResponse = {
    	id: number;
    	result?: unknown;
    	error?: { message: string };
    };
    
    let nextCdpCommandId = 0;
    
    function sendCdpCommand(
    	socket: WebSocket,
    	method: string,
    	params: Record<string, unknown> = {},
    ): Promise<unknown> {
    	return new Promise((resolve, reject) => {
    		const id = ++nextCdpCommandId;
    		const timeout = setTimeout(() => {
    			cleanup();
    			reject(new Error(`CDP command "${method}" timed out`));
    		}, 30_000);
    
    		const cleanup = () => {
    			clearTimeout(timeout);
    			socket.removeEventListener("message", onMessage);
    			socket.removeEventListener("close", onClose);
    		};
    
    		const onClose = () => {
    			cleanup();
    			reject(new Error("CDP connection closed before the command completed"));
    		};
    
    		const onMessage = (event: MessageEvent<string>) => {
    			const message = JSON.parse(event.data) as CdpResponse;
    			if (message.id !== id) return;
    
    			cleanup();
    			if (message.error) {
    				reject(new Error(message.error.message));
    			} else {
    				resolve(message.result);
    			}
    		};
    
    		socket.addEventListener("message", onMessage);
    		socket.addEventListener("close", onClose);
    		try {
    			socket.send(JSON.stringify({ id, method, params }));
    		} catch (error) {
    			cleanup();
    			reject(error);
    		}
    	});
    }
    
    export default {
    	async fetch(_request: Request, env: Env): Promise<Response> {
    		const connection = await env.BROWSER.launch({
    			outboundByHost: {
    				"private.example.test": env.OUTBOUND,
    			},
    		});
    		const response = await connection.webSocket.fetch(
    			"https://browser-binding.invalid",
    			{ headers: { Upgrade: "websocket" } },
    		);
    		if (!response.webSocket) {
    			throw new Error("Browser Run did not return a WebSocket");
    		}
    
    		const socket = response.webSocket;
    		socket.accept();
    
    		try {
    			await sendCdpCommand(socket, "Page.navigate", {
    				url: "http://private.example.test",
    			});
    			return new Response("Navigation sent through the outbound Worker");
    		} finally {
    			socket.close();
    			await env.BROWSER.closeSession(connection.sessionId);
    		}
    	},
    };

The `.test` top-level domain is reserved for testing. Use a hostname that does not resolve on public DNS for a virtual outbound route. The hostname must still match the key in `outboundByHost`.

Outbound Worker routing supports HTTP requests only. Use an `http://` URL for the routed hostname. HTTPS requests do not use the outbound Worker.

## Constraints

  * Use `outboundByHost` with Browser Run binding methods only. It is not supported by REST endpoints or legacy HTTP-only bindings.
  * Create the Fetcher and call `acquire()` or `launch()` in the same Worker invocation.
  * The Fetcher is not persisted with the browser session and cannot be reused by a later invocation.
  * Outbound routing applies to the hostnames in the map. Requests to other hostnames use the browser's normal network path.



## Next steps

  * Review the [Browser binding API](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/).
  * Learn how to use the [Chrome DevTools Protocol](https://developers.cloudflare.com/browser-run/cdp/).



[PreviousGuardrails](https://developers.cloudflare.com/browser-run/features/guardrails/)[NextExamples](https://developers.cloudflare.com/browser-run/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/features/outbound-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
