---
url: https://developers.cloudflare.com/sandbox/sdk/configuration/transport/
title: Transport modes (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:23.547894+00:00
---

# Transport modes (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/configuration/transport/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[Configuration](https://developers.cloudflare.com/sandbox/sdk/configuration/)
  5. /Transport modes



# Transport modes

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/configuration/transport/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOverviewWhen to use RPC transport Subrequest limits How RPC transport helpsConfiguration HTTP transport (default) RPC transportTransport behavior Connection lifecycle Streaming support Error handlingChoosing a transportMigration guide Switch from HTTP to RPC Switch from RPC to HTTP Switch from deprecated WebSocket to RPCRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Configure how the Sandbox SDK communicates with containers using transport modes.

## Overview

The Sandbox SDK supports three transport modes for communication between the Durable Object and the container:

  * **HTTP transport** (default) - Each SDK operation makes a separate HTTP request to the container.
  * **NEW: RPC transport** \- All SDK operations are multiplexed over a single persistent WebSocket connection. Will replace HTTP as the default transport in future. Available since 0.9.1.
  * **Deprecated: WebSocket transport** \- All SDK operations are multiplexed over a single persistent WebSocket. Superseded by RPC transport which uses an improved protocol.



## When to use RPC transport

Use the RPC transport when your Worker or Durable Object makes many SDK operations per request. This avoids hitting [subrequest limits](https://developers.cloudflare.com/workers/platform/limits/#subrequests).

### Subrequest limits

Cloudflare Workers have subrequest limits that apply when making requests to external services, including container API calls:

  * **Workers Free** : 50 subrequests per request
  * **Workers Paid** : 1,000 subrequests per request



With HTTP transport (default), each SDK operation (`exec()`, `readFile()`, `writeFile()`, etc.) consumes one subrequest. Applications that perform many sandbox operations in a single request can hit these limits.

### How RPC transport helps

RPC transport establishes a single persistent connection to the container and multiplexes all SDK operations over it. The WebSocket upgrade counts as **one subrequest** regardless of how many operations you perform afterwards.

**Example with HTTP transport (4 subrequests):**
    
    
    await sandbox.exec("python setup.py");
    await sandbox.writeFile("/app/config.json", config);
    await sandbox.exec("python process.py");
    const result = await sandbox.readFile("/app/output.txt");

**Same code with RPC transport (1 subrequest):**
    
    
    // Identical code - transport is configured via environment variable
    await sandbox.exec("python setup.py");
    await sandbox.writeFile("/app/config.json", config);
    await sandbox.exec("python process.py");
    const result = await sandbox.readFile("/app/output.txt");

RPC transport also removes the [32 MiB limitation](https://developers.cloudflare.com/workers/runtime-apis/rpc/#limitations) that the HTTP transport has. Pass a `ReadableStream` instance to the `writeFile()` method.
    
    
    const req = await fetch("https://example.com/archive.tar.gz");
    await sandbox.writeFile("/archive.tar.gz", req.body);

## Configuration

Set the `SANDBOX_TRANSPORT` environment variable in your Worker's configuration. The SDK reads this from the Worker environment bindings (not from inside the container).

### HTTP transport (default)

HTTP transport is the default and requires no additional configuration.

### RPC transport

Enable RPC transport by adding `SANDBOX_TRANSPORT` to your Worker's `vars`:
    
    
    {
    	"name": "my-sandbox-worker",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"vars": {
    		"SANDBOX_TRANSPORT": "rpc"
    	},
    	"containers": [
    		{
    			"class_name": "Sandbox",
    			"image": "./Dockerfile",
    		},
    	],
    	"durable_objects": {
    		"bindings": [
    			{
    				"class_name": "Sandbox",
    				"name": "Sandbox",
    			},
    		],
    	},
    }
    
    
    name = "my-sandbox-worker"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [vars]
    SANDBOX_TRANSPORT = "rpc"
    
    [[containers]]
    class_name = "Sandbox"
    image = "./Dockerfile"
    
    [[durable_objects.bindings]]
    class_name = "Sandbox"
    name = "Sandbox"

No application code changes are needed. The SDK automatically uses the configured transport for all operations.

## Transport behavior

### Connection lifecycle

**HTTP transport:**

  * Creates a new HTTP request for each SDK operation
  * No persistent connection
  * Each request is independent and stateless



**RPC transport:**

  * Establishes a WebSocket connection on the first SDK operation
  * Maintains the persistent connection for all subsequent operations
  * Connection is closed when the sandbox sleeps or is evicted
  * Automatically reconnects if the connection drops



### Streaming support

All transports support streaming operations (like `exec()` with real-time output):

  * **HTTP transport** \- Uses Server-Sent Events (SSE)
  * **RPC transport** \- Uses WebSocket streaming messages



Your code remains identical regardless of transport mode.

### Error handling

All transports provide identical error handling behavior. The SDK automatically retries on transient errors (like 503 responses) with exponential backoff.

WebSocket-specific behavior:

  * Connection failures trigger automatic reconnection
  * The SDK transparently handles WebSocket disconnections
  * In-flight operations are not lost during reconnection



## Choosing a transport

We expect the RPC transport to replace the default HTTP transport in a future release. New functionality may support only the RPC transport. Switching to use it now will avoid migrations in the future.

## Migration guide

Switching between transports requires no code changes.

### Switch from HTTP to RPC

Requires staged deployment

Using the `rpc` transport requires version 0.9.1 or newer. If you are using an older version of the Sandbox SDK upgrade and deploy your application with the newer `@cloudflare/sandbox` and image first. Otherwise there will be issues with newer SDK clients attempting to connect to older sandboxes that do not support the new transport.

Add `SANDBOX_TRANSPORT` to your `wrangler.jsonc`:
    
    
    {
    	"vars": {
    		"SANDBOX_TRANSPORT": "rpc"
    	},
    }
    
    
    [vars]
    SANDBOX_TRANSPORT = "rpc"

Then deploy:
    
    
    npx wrangler deploy

### Switch from RPC to HTTP

Remove the `SANDBOX_TRANSPORT` variable (or set it to `"http"`):
    
    
    {
    	"vars": {
    		// Remove SANDBOX_TRANSPORT or set to "http"
    	},
    }
    
    
    vars = { }

### Switch from deprecated WebSocket to RPC

Requires staged deployment

Using the `rpc` transport requires version 0.9.1 or newer. If you are using an older version of the Sandbox SDK upgrade and deploy your application with the newer `@cloudflare/sandbox` and image first. Otherwise there will be issues with newer SDK clients attempting to connect to older sandboxes that do not support the new transport.

Set the `SANDBOX_TRANSPORT` variable to `"rpc"`:
    
    
    {
    	"vars": {
    		"SANDBOX_TRANSPORT": "rpc"
    	},
    }
    
    
    [vars]
    SANDBOX_TRANSPORT = "rpc"

## Related resources

  * [Wrangler configuration](https://developers.cloudflare.com/sandbox/sdk/configuration/wrangler/) \- Complete Worker configuration
  * [Environment variables](https://developers.cloudflare.com/sandbox/sdk/configuration/environment-variables/) \- Passing configuration to sandboxes
  * [Workers subrequest limits](https://developers.cloudflare.com/workers/platform/limits/#subrequests) \- Understanding subrequest limits
  * [Architecture](https://developers.cloudflare.com/sandbox/sdk/concepts/architecture/) \- How Sandbox SDK components communicate



[PreviousSandbox options](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/)[NextOverview](https://developers.cloudflare.com/sandbox/sdk/bridge/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/configuration/transport.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
