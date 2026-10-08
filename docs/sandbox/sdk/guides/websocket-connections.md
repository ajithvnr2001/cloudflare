---
url: https://developers.cloudflare.com/sandbox/sdk/guides/websocket-connections/
title: WebSocket connections (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:26.137908+00:00
---

# WebSocket connections (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/guides/websocket-connections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)
  5. /WebSocket connections



# WebSocket connections

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/websocket-connections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose your approachConnect to WebSocket echo serverExpose WebSocket service via preview URLConnect from Worker to get real-time data Local developmentRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

This guide shows you how to work with WebSocket servers running in your sandboxes.

## Choose your approach

**Expose via preview URL** \- Get a public URL for external clients to connect to. Best for public chat rooms, multiplayer games, or real-time dashboards.

**Connect with wsConnect()** \- Your Worker establishes the WebSocket connection. Best for custom routing logic, authentication gates, or when your Worker needs real-time data from sandbox services.

## Connect to WebSocket echo server

**Create the echo server:**

echo-server.tstypescript
    
    
    Bun.serve({
    	port: 8080,
    	hostname: "0.0.0.0",
    	fetch(req, server) {
    		if (server.upgrade(req)) {
    			return;
    		}
    		return new Response("WebSocket echo server");
    	},
    	websocket: {
    		message(ws, message) {
    			ws.send(`Echo: ${message}`);
    		},
    		open(ws) {
    			console.log("Client connected");
    		},
    		close(ws) {
    			console.log("Client disconnected");
    		},
    	},
    });
    
    console.log("WebSocket server listening on port 8080");

**Extend the Dockerfile:**

Dockerfiledockerfile
    
    
    FROM docker.io/cloudflare/sandbox:0.3.3
    
    # Copy echo server into the container
    COPY echo-server.ts /workspace/echo-server.ts
    
    # Create custom startup script
    COPY startup.sh /container-server/startup.sh
    RUN chmod +x /container-server/startup.sh

**Create startup script:**

startup.shbash
    
    
    #!/bin/bash
    # Start your WebSocket server in the background
    bun /workspace/echo-server.ts &
    # Start SDK's control plane (needed for the SDK to work)
    exec bun dist/index.js

**Connect from your Worker:**
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request, env) {
    		if (request.headers.get("Upgrade")?.toLowerCase() === "websocket") {
    			const sandbox = getSandbox(env.Sandbox, "echo-service");
    			return await sandbox.wsConnect(request, 8080);
    		}
    
    		return new Response("WebSocket endpoint");
    	},
    };
    
    
    import { getSandbox } from '@cloudflare/sandbox';
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        if (request.headers.get('Upgrade')?.toLowerCase() === 'websocket') {
          const sandbox = getSandbox(env.Sandbox, 'echo-service');
          return await sandbox.wsConnect(request, 8080);
        }
    
        return new Response('WebSocket endpoint');
    
    }
    };

**Client connects:**
    
    
    const ws = new WebSocket('wss://your-worker.com');
    ws.onmessage = (event) => console.log(event.data);
    ws.send('Hello!'); // Receives: "Echo: Hello!"

## Expose WebSocket service via preview URL

Get a public URL for your WebSocket server:
    
    
    import { getSandbox, proxyToSandbox } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request, env) {
    		// Auto-route all requests via proxyToSandbox first
    		const proxyResponse = await proxyToSandbox(request, env);
    		if (proxyResponse) return proxyResponse;
    
    		// Extract hostname from request
    		const { hostname } = new URL(request.url);
    		const sandbox = getSandbox(env.Sandbox, "echo-service");
    
    		// Expose the port to get preview URL
    		const { url } = await sandbox.exposePort(8080, { hostname });
    
    		// Return URL to clients
    		if (request.url.includes("/ws-url")) {
    			return Response.json({ url: url.replace("https", "wss") });
    		}
    
    		return new Response("Not found", { status: 404 });
    	},
    };
    
    
    import { getSandbox, proxyToSandbox } from '@cloudflare/sandbox';
    
    export { Sandbox } from '@cloudflare/sandbox';
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        // Auto-route all requests via proxyToSandbox first
        const proxyResponse = await proxyToSandbox(request, env);
        if (proxyResponse) return proxyResponse;
    
        // Extract hostname from request
        const { hostname } = new URL(request.url);
        const sandbox = getSandbox(env.Sandbox, 'echo-service');
    
        // Expose the port to get preview URL
        const { url } = await sandbox.exposePort(8080, { hostname });
    
        // Return URL to clients
        if (request.url.includes('/ws-url')) {
          return Response.json({ url: url.replace('https', 'wss') });
        }
    
        return new Response('Not found', { status: 404 });
    
    }
    };

Alternative: quick tunnels

Quick tunnels also handle WebSocket upgrades and do not require a custom domain, so they work on `.workers.dev`. Swap `sandbox.exposePort(8080, { hostname })` for `sandbox.tunnels.get(8080)` to get a `*.trycloudflare.com` URL.

**Client connects to preview URL:**
    
    
    // Get the preview URL
    const response = await fetch('https://your-worker.com/ws-url');
    const { url } = await response.json();
    
    // Connect
    const ws = new WebSocket(url);
    ws.onmessage = (event) => console.log(event.data);
    ws.send('Hello!'); // Receives: "Echo: Hello!"

## Connect from Worker to get real-time data

Your Worker can connect to a WebSocket service to get real-time data, even when the incoming request isn't a WebSocket:
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    let initialized = false;
    
    export default {
    	async fetch(request, env) {
    		// Get or create a sandbox instance
    		const sandbox = getSandbox(env.Sandbox, "data-processor");
    
    		// Check for WebSocket upgrade
    		const upgrade = request.headers.get("Upgrade")?.toLowerCase();
    
    		if (upgrade === "websocket") {
    			// Initialize server on first connection
    			if (!initialized) {
    				await sandbox.writeFile(
    					"/workspace/server.js",
    					`Bun.serve({
                port: 8080,
                fetch(req, server) {
                  server.upgrade(req);
                },
                websocket: {
                  message(ws, msg) {
                    ws.send(\`Echo: \${msg}\`);
                  }
                }
              });`,
    				);
    				await sandbox.startProcess("bun /workspace/server.js");
    				initialized = true;
    			}
    			// Connect to WebSocket server
    			return await sandbox.wsConnect(request, 8080);
    		}
    
    		return new Response("Processed real-time data");
    	},
    };
    
    
    import { getSandbox } from '@cloudflare/sandbox';
    
    export { Sandbox } from '@cloudflare/sandbox';
    
    let initialized = false;
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
    
         // Get or create a sandbox instance
        const sandbox = getSandbox(env.Sandbox, 'data-processor');
    
    
        // Check for WebSocket upgrade
        const upgrade = request.headers.get('Upgrade')?.toLowerCase();
    
        if (upgrade === 'websocket') {
          // Initialize server on first connection
          if (!initialized) {
            await sandbox.writeFile(
              '/workspace/server.js',
              `Bun.serve({
                port: 8080,
                fetch(req, server) {
                  server.upgrade(req);
                },
                websocket: {
                  message(ws, msg) {
                    ws.send(\`Echo: \${msg}\`);
                  }
                }
              });`
            );
            await sandbox.startProcess(
              'bun /workspace/server.js'
            );
            initialized = true;
          }
          // Connect to WebSocket server
          return await sandbox.wsConnect(request, 8080);
        }
    
        return new Response('Processed real-time data');
    
    }
    };

This pattern is useful when you need streaming data from sandbox services but want to return HTTP responses to clients.

## Troubleshooting

### Upgrade failed

Verify request has WebSocket headers:
    
    
    console.log(request.headers.get("Upgrade")); // 'websocket'
    console.log(request.headers.get("Connection")); // 'Upgrade'
    
    
    console.log(request.headers.get('Upgrade'));    // 'websocket'
    console.log(request.headers.get('Connection')); // 'Upgrade'

### Local development

Expose ports in Dockerfile for `wrangler dev`:

Dockerfiledockerfile
    
    
    FROM docker.io/cloudflare/sandbox:0.3.3
    
    COPY echo-server.ts /workspace/echo-server.ts
    COPY startup.sh /container-server/startup.sh
    RUN chmod +x /container-server/startup.sh
    
    # Required for local development
    EXPOSE 8080

Note

Port exposure in Dockerfile is only required for local development. In production, all ports are automatically accessible.

## Related resources

  * [Ports API reference](https://developers.cloudflare.com/sandbox/sdk/api/ports/) \- Complete API documentation
  * [Preview URLs concept](https://developers.cloudflare.com/sandbox/sdk/concepts/preview-urls/) \- How preview URLs work
  * [Tunnels API](https://developers.cloudflare.com/sandbox/sdk/api/tunnels/) \- Zero-config `*.trycloudflare.com` URLs for WebSocket services in development
  * [Background processes guide](https://developers.cloudflare.com/sandbox/sdk/guides/background-processes/) \- Managing long-running services



[PreviousUse code interpreter](https://developers.cloudflare.com/sandbox/sdk/guides/code-execution/)[NextWork with Git](https://developers.cloudflare.com/sandbox/sdk/guides/git-workflows/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/guides/websocket-connections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
