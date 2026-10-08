---
url: https://developers.cloudflare.com/sandbox/sdk/api/ports/
title: Ports (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:21.815931+00:00
---

# Ports (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/api/ports/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[API reference](https://developers.cloudflare.com/sandbox/sdk/api/)
  5. /Ports



# Ports

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/api/ports/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewModule functions proxyToSandbox() validatePortToken() getExposedPorts()

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Preview a web application](https://developers.cloudflare.com/sandbox/previews/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Production requires custom domain

Preview URLs require a custom domain with wildcard DNS routing in production. See [Configure preview URLs on a custom domain](https://developers.cloudflare.com/sandbox/sdk/guides/preview-urls-custom-domain/).

Prefer `sandbox.tunnels` for public URLs

For most public-URL use cases — development, `.workers.dev` deployments, and production traffic — [`sandbox.tunnels`](https://developers.cloudflare.com/sandbox/sdk/api/tunnels/) is the recommended option. Use named tunnels for stable hostnames on a zone you control, or quick tunnels for zero-config `*.trycloudflare.com` URLs. `exposePort()` is appropriate when you want the Worker itself to front the request (for example, to inject authentication, rewrite responses, or call sandbox-only RPC methods on the same hostname).

Expose services running in your sandbox via public preview URLs. See [Preview URLs concept](https://developers.cloudflare.com/sandbox/sdk/concepts/preview-urls/) for details.

## Module functions

### `proxyToSandbox()`

Route incoming HTTP and WebSocket requests to the correct sandbox container. Call this at the top of your Worker's `fetch` handler, before any application logic, so that it intercepts and forwards preview URL requests automatically.
    
    
    proxyToSandbox(request: Request, env: Env): Promise<Response | null>

**Parameters** :

  * `request` \- The incoming `Request` object from the `fetch` handler.
  * `env` \- The `Env` object containing your Sandbox binding.



**Returns** : `Promise<Response | null>` — a `Response` if the request matched a preview URL and was routed to the sandbox, or `null` if the request did not match and should be handled by your application logic.

The function inspects the request hostname to determine whether it matches the subdomain pattern of an exposed port (for example, `8080-sandbox-id-token.yourdomain.com`). If it matches, `proxyToSandbox()` proxies the request to the correct Durable Object, and the sandbox service handles it. Both HTTP and WebSocket upgrade requests are supported.
    
    
    import { proxyToSandbox, getSandbox } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request, env) {
    		// Always call proxyToSandbox first to handle preview URL requests
    		const proxyResponse = await proxyToSandbox(request, env);
    		if (proxyResponse) return proxyResponse;
    
    		// Your application routes
    		const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    		// ...
    		return new Response("Not found", { status: 404 });
    	},
    };
    
    
    import { proxyToSandbox, getSandbox } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        // Always call proxyToSandbox first to handle preview URL requests
        const proxyResponse = await proxyToSandbox(request, env);
        if (proxyResponse) return proxyResponse;
    
        // Your application routes
        const sandbox = getSandbox(env.Sandbox, 'my-sandbox');
        // ...
        return new Response('Not found', { status: 404 });
      }
    };

Note

`proxyToSandbox` is a module-level function imported directly from `@cloudflare/sandbox` — it is not a method on a `Sandbox` instance. It requires the Sandbox Durable Object binding (`env.Sandbox`) to look up and route requests to the correct container.

## Methods

### `exposePort()`

Expose a port and get a preview URL for accessing services running in the sandbox.
    
    
    const response = await sandbox.exposePort(port: number, options: ExposePortOptions): Promise<ExposePortResponse>

**Parameters** :

  * `port` \- Port number to expose (1024-65535)
  * `options`: 
    * `hostname` \- Your Worker's domain name (e.g., `'example.com'`). Required to construct preview URLs with wildcard subdomains like `https://8080-sandbox-abc123token.example.com`. Cannot be a `.workers.dev` domain as it doesn't support wildcard DNS patterns.
    * `name` \- Friendly name for the port (optional)
    * `token` \- Custom token for the preview URL (optional). Must be 1-16 characters containing only lowercase letters (a-z), numbers (0-9), hyphens (-), and underscores (_). If not provided, a random 16-character token is generated automatically.



**Returns** : `Promise<ExposePortResponse>` with `port`, `url` (preview URL), `name`
    
    
    // Extract hostname from request
    const { hostname } = new URL(request.url);
    
    // Basic usage with auto-generated token
    await sandbox.startProcess("python -m http.server 8000");
    const exposed = await sandbox.exposePort(8000, { hostname });
    
    console.log("Available at:", exposed.url);
    // https://8000-sandbox-id-abc123random.yourdomain.com
    
    // With custom token for stable URLs across restarts
    const stable = await sandbox.exposePort(8080, {
    	hostname,
    	token: "my_service_v1", // 1-16 chars: a-z, 0-9, _
    });
    console.log("Stable URL:", stable.url);
    // https://8080-sandbox-id-my_service_v1.yourdomain.com
    
    // With custom token for stable URLs across deployments
    await sandbox.startProcess("node api.js");
    const api = await sandbox.exposePort(3000, {
    	hostname,
    	name: "api",
    	token: "prod-api-v1", // URL stays same across restarts
    });
    
    console.log("Stable API URL:", api.url);
    // https://3000-sandbox-id-prod-api-v1.yourdomain.com
    
    // Multiple services with custom tokens
    await sandbox.startProcess("npm run dev");
    const frontend = await sandbox.exposePort(5173, {
    	hostname,
    	name: "frontend",
    	token: "dev-ui",
    });
    
    
    // Extract hostname from request
    const { hostname } = new URL(request.url);
    
    // Basic usage with auto-generated token
    await sandbox.startProcess('python -m http.server 8000');
    const exposed = await sandbox.exposePort(8000, { hostname });
    
    console.log('Available at:', exposed.url);
    // https://8000-sandbox-id-abc123random.yourdomain.com
    
    // With custom token for stable URLs across restarts
    const stable = await sandbox.exposePort(8080, {
      hostname,
      token: 'my_service_v1' // 1-16 chars: a-z, 0-9, _
    });
    console.log('Stable URL:', stable.url);
    // https://8080-sandbox-id-my_service_v1.yourdomain.com
    
    // With custom token for stable URLs across deployments
    await sandbox.startProcess('node api.js');
    const api = await sandbox.exposePort(3000, {
      hostname,
      name: 'api',
      token: 'prod-api-v1'  // URL stays same across restarts
    });
    
    console.log('Stable API URL:', api.url);
    // https://3000-sandbox-id-prod-api-v1.yourdomain.com
    
    // Multiple services with custom tokens
    await sandbox.startProcess('npm run dev');
    const frontend = await sandbox.exposePort(5173, {
      hostname,
      name: 'frontend',
      token: 'dev-ui'
    });

Local development

When using `wrangler dev`, you must add `EXPOSE` directives to your Dockerfile for each port. See [Expose Services guide](https://developers.cloudflare.com/sandbox/sdk/guides/expose-services/#local-development) for details.

## Custom Tokens for Stable URLs

Custom tokens enable consistent preview URLs across container restarts and deployments. This is useful for:

  * **Production environments** \- Share stable URLs with users or teams
  * **Development workflows** \- Maintain bookmarks and integrations
  * **CI/CD pipelines** \- Reference consistent URLs in tests or deployment scripts



**Token Requirements:**

  * 1-16 characters in length
  * Only lowercase letters (a-z), numbers (0-9), hyphens (-), and underscores (_)
  * Must be unique per sandbox (cannot reuse tokens across different ports)


    
    
    // Production API with stable URL
    const { url } = await sandbox.exposePort(8080, {
    	hostname: "api.example.com",
    	token: "v1-stable", // Always the same URL
    });
    
    // Error: Token collision prevention
    await sandbox.exposePort(8081, { hostname, token: "v1-stable" });
    // Throws: Token 'v1-stable' is already in use by port 8080
    
    // Success: Re-exposing same port with same token (idempotent)
    await sandbox.exposePort(8080, { hostname, token: "v1-stable" });
    // Works - same port, same token
    
    
    // Production API with stable URL
    const { url } = await sandbox.exposePort(8080, {
      hostname: 'api.example.com',
      token: 'v1-stable'  // Always the same URL
    });
    
    // Error: Token collision prevention
    await sandbox.exposePort(8081, { hostname, token: 'v1-stable' });
    // Throws: Token 'v1-stable' is already in use by port 8080
    
    // Success: Re-exposing same port with same token (idempotent)
    await sandbox.exposePort(8080, { hostname, token: 'v1-stable' });
    // Works - same port, same token

### `validatePortToken()`

Validate if a token is authorized to access a specific exposed port. Useful for custom authentication or routing logic.
    
    
    const isValid = await sandbox.validatePortToken(port: number, token: string): Promise<boolean>

**Parameters** :

  * `port` \- Port number to check
  * `token` \- Token to validate



**Returns** : `Promise<boolean>` \- `true` if token is valid for the port, `false` otherwise
    
    
    // Custom validation in your Worker
    export default {
    	async fetch(request, env) {
    		const url = new URL(request.url);
    
    		// Extract token from custom header or query param
    		const customToken = request.headers.get("x-access-token");
    
    		if (customToken) {
    			const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    			const isValid = await sandbox.validatePortToken(8080, customToken);
    
    			if (!isValid) {
    				return new Response("Invalid token", { status: 403 });
    			}
    		}
    
    		// Handle preview URL routing
    		const proxyResponse = await proxyToSandbox(request, env);
    		if (proxyResponse) return proxyResponse;
    
    		// Your application routes
    		return new Response("Not found", { status: 404 });
    	},
    };
    
    
    // Custom validation in your Worker
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        const url = new URL(request.url);
        
        // Extract token from custom header or query param
        const customToken = request.headers.get('x-access-token');
        
        if (customToken) {
          const sandbox = getSandbox(env.Sandbox, 'my-sandbox');
          const isValid = await sandbox.validatePortToken(8080, customToken);
          
          if (!isValid) {
            return new Response('Invalid token', { status: 403 });
          }
        }
        
        // Handle preview URL routing
        const proxyResponse = await proxyToSandbox(request, env);
        if (proxyResponse) return proxyResponse;
        
        // Your application routes
        return new Response('Not found', { status: 404 });
      }
    };

### `unexposePort()`

Remove an exposed port and close its preview URL.
    
    
    await sandbox.unexposePort(port: number): Promise<void>

**Parameters** :

  * `port` \- Port number to unexpose


    
    
    await sandbox.unexposePort(8000);
    
    
    await sandbox.unexposePort(8000);

### `getExposedPorts()`

Get information about all currently exposed ports.
    
    
    const response = await sandbox.getExposedPorts(): Promise<GetExposedPortsResponse>

**Returns** : `Promise<GetExposedPortsResponse>` with `ports` array (containing `port`, `url`, `name`)
    
    
    const { ports } = await sandbox.getExposedPorts();
    
    for (const port of ports) {
    	console.log(`${port.name || port.port}: ${port.url}`);
    }
    
    
    const { ports } = await sandbox.getExposedPorts();
    
    for (const port of ports) {
      console.log(`${port.name || port.port}: ${port.url}`);
    }

### `wsConnect()`

Connect to WebSocket servers running in the sandbox. Use this when your Worker needs to establish WebSocket connections with services in the sandbox.

**Common use cases:**

  * Route incoming WebSocket upgrade requests with custom authentication or authorization
  * Connect from your Worker to get real-time data from sandbox services



For exposing WebSocket services via public preview URLs, use `exposePort()` with `proxyToSandbox()` instead. See [WebSocket Connections guide](https://developers.cloudflare.com/sandbox/sdk/guides/websocket-connections/) for examples.
    
    
    const response = await sandbox.wsConnect(request: Request, port: number): Promise<Response>

**Parameters** :

  * `request` \- Incoming WebSocket upgrade request
  * `port` \- Port number (1024-65535, excluding 3000)



**Returns** : `Promise<Response>` \- WebSocket response establishing the connection
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request, env) {
    		if (request.headers.get("Upgrade")?.toLowerCase() === "websocket") {
    			const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    			return await sandbox.wsConnect(request, 8080);
    		}
    
    		return new Response("WebSocket endpoint", { status: 200 });
    	},
    };
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        if (request.headers.get('Upgrade')?.toLowerCase() === 'websocket') {
          const sandbox = getSandbox(env.Sandbox, 'my-sandbox');
          return await sandbox.wsConnect(request, 8080);
        }
    
        return new Response('WebSocket endpoint', { status: 200 });
      }
    };

## Related resources

  * [Preview URLs concept](https://developers.cloudflare.com/sandbox/sdk/concepts/preview-urls/) \- How preview URLs work
  * [Expose Services guide](https://developers.cloudflare.com/sandbox/sdk/guides/expose-services/) \- Full workflow for starting services, exposing ports, and routing requests
  * [WebSocket Connections guide](https://developers.cloudflare.com/sandbox/sdk/guides/websocket-connections/) \- WebSocket routing via preview URLs
  * [Commands API](https://developers.cloudflare.com/sandbox/sdk/api/commands/) \- Start background processes
  * [Tunnels API](https://developers.cloudflare.com/sandbox/sdk/api/tunnels/) \- Zero-config `*.trycloudflare.com` URLs for quick development




[PreviousBackups](https://developers.cloudflare.com/sandbox/sdk/api/backups/)[NextSessions](https://developers.cloudflare.com/sandbox/sdk/api/sessions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/api/ports.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
