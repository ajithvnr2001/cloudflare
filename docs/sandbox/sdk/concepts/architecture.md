---
url: https://developers.cloudflare.com/sandbox/sdk/concepts/architecture/
title: Architecture (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:22.782767+00:00
---

# Architecture (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/concepts/architecture/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[Concepts](https://developers.cloudflare.com/sandbox/sdk/concepts/)
  5. /Architecture



# Architecture

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/concepts/architecture/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArchitecture overview Layer 1: Client SDK Layer 2: Durable Object Layer 3: Container RuntimeCommunication transports HTTP transport (default) RPC transport WebSocket transportRequest flowRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Sandbox SDK lets you execute untrusted code safely from your Workers. It combines three Cloudflare technologies to provide secure, stateful, and isolated execution:

  * **Workers** \- Your application logic that calls the Sandbox SDK
  * **Durable Objects** \- Persistent sandbox instances with unique identities
  * **Containers** \- Isolated Linux environments where code actually runs



## Architecture overview
    
    
    flowchart TB
        accTitle: Sandbox SDK Architecture
        accDescr: Three-layer architecture showing how Cloudflare Sandbox SDK combines Workers, Durable Objects, and Containers for secure code execution
    
        subgraph UserSpace["<b>Your Worker</b>"]
            Worker["Application code using the methods exposed by the Sandbox SDK"]
        end
    
        subgraph SDKSpace["<b>Sandbox SDK Implementation</b>"]
            DO["Sandbox Durable Object routes requests & maintains state"]
            Container["Isolated Ubuntu container executes untrusted code safely"]
    
            DO -->|HTTP API| Container
        end
    
        Worker -->|RPC call via the Durable Object stub returned by `getSandbox`| DO
    
        style UserSpace fill:#fff8f0,stroke:#f6821f,stroke-width:2px
        style SDKSpace fill:#f5f5f5,stroke:#666,stroke-width:2px,stroke-dasharray: 5 5
        style Worker fill:#ffe8d1,stroke:#f6821f,stroke-width:2px
        style DO fill:#dce9f7,stroke:#1d8cf8,stroke-width:2px
        style Container fill:#d4f4e2,stroke:#17b26a,stroke-width:2px
    

### Layer 1: Client SDK

The developer-facing API you use in your Workers:
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    const result = await sandbox.exec("python script.py");

**Purpose** : Provide a clean, type-safe TypeScript interface for all sandbox operations.

### Layer 2: Durable Object

Manages sandbox lifecycle and routing:
    
    
    export class Sandbox extends DurableObject<Env> {
    	// Extends Cloudflare Container for isolation
    	// Routes requests between client and container
    	// Manages preview URLs and state
    }

**Purpose** : Provide persistent, stateful sandbox instances with unique identities.

**Why Durable Objects** :

  * **Persistent identity** \- Same sandbox ID always routes to same instance
  * **Container management** \- Durable Object owns and manages the container lifecycle
  * **Geographic distribution** \- Sandboxes run close to users
  * **Automatic scaling** \- Cloudflare manages provisioning



### Layer 3: Container Runtime

Executes code in isolation with full Linux capabilities.

**Purpose** : Safely execute untrusted code.

**Why containers** :

  * **VM-based isolation** \- Each sandbox runs in its own VM
  * **Full environment** \- Ubuntu Linux with Python, Node.js, Git, etc.



## Communication transports

The SDK supports three transport protocols for communication between the Durable Object and container:

### HTTP transport (default)

Each SDK method makes a separate HTTP request to the container API. Simple, reliable, and works for most use cases.
    
    
    // Default behavior - uses HTTP
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    await sandbox.exec("python script.py");

### RPC transport

Multiplexes all SDK calls over a single persistent connection. It avoids [subrequest limits](https://developers.cloudflare.com/workers/platform/limits/#subrequests) when making many concurrent operations.

Enable RPC transport by setting the `SANDBOX_TRANSPORT` variable in your Worker's configuration:
    
    
    {
    	"vars": {
    		"SANDBOX_TRANSPORT": "rpc"
    	},
    }
    
    
    [vars]
    SANDBOX_TRANSPORT = "rpc"

### WebSocket transport

WebSocket transport is deprecated. Use RPC transport for new applications.

The transport layer is transparent to your application code — all SDK methods work identically regardless of transport. For details on when to use each transport and configuration examples, refer to [Transport modes](https://developers.cloudflare.com/sandbox/sdk/configuration/transport/).

## Request flow

When you execute a command:
    
    
    await sandbox.exec("python script.py");

**HTTP transport flow** :

  1. **Client SDK** validates parameters and sends HTTP request to Durable Object
  2. **Durable Object** authenticates and forwards HTTP request to container
  3. **Container Runtime** validates inputs, executes command, captures output
  4. **Response flows back** through all layers with proper error transformation



**RPC transport flow** :

  1. **Client SDK** validates parameters and sends the request to the Durable Object
  2. **Durable Object** maintains the persistent connection to the container and multiplexes concurrent requests
  3. **Container Runtime** adapts RPC messages to HTTP-style request and response handling
  4. **Response flows back** over the same connection with proper error transformation



The Durable Object establishes the persistent connection to the container on first SDK call and reuses it for all subsequent operations, reducing overhead for high-frequency operations.

## Related resources

  * [Sandbox lifecycle](https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/) \- How sandboxes are created and managed
  * [Container runtime](https://developers.cloudflare.com/sandbox/sdk/concepts/containers/) \- Inside the execution environment
  * [Security model](https://developers.cloudflare.com/sandbox/sdk/concepts/security/) \- How isolation and validation work
  * [Session management](https://developers.cloudflare.com/sandbox/sdk/concepts/sessions/) \- Advanced state management



[PreviousOverview](https://developers.cloudflare.com/sandbox/sdk/concepts/)[NextSandbox lifecycle](https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/concepts/architecture.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
