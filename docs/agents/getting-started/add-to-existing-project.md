---
url: https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/
title: Add to existing project \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:11.577419+00:00
---

# Add to existing project · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Getting started
  4. /Add to existing project



# Add to existing project

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Install the package2\. Create an Agent3\. Update Wrangler configuration4\. Configure TypeScript and Vite5\. Export the Agent class6\. Wire up routing Plain Workers (fetch handler) Hono With static assets7\. Generate TypeScript types8\. Connect from the frontend React Vanilla JavaScriptHow it works Key conceptsDeploy to CloudflareCommon integration patterns Agents behind authentication Custom agent path prefix Accessing agents from server code Adding multiple agentsTroubleshooting Agent not found, or 404 errors No such Durable Object class error WebSocket connection fails State not persisting "Method X is not callable" errors Type errors with agent.stub SyntaxError: Invalid or unexpected token with @callable()Next steps Common next steps Explore more

This guide shows how to add agents to an existing Cloudflare Workers project. If you are starting fresh, refer to [Building a chat agent](https://developers.cloudflare.com/agents/examples/chat-agent/) instead.

## Prerequisites

  * An existing Cloudflare Workers project with a Wrangler configuration file
  * Node.js 18 or newer



## 1\. Install the package

npmyarnpnpmbun
    
    
    npm i agents
    
    
    yarn add agents
    
    
    pnpm add agents
    
    
    bun add agents

For React applications, no additional packages are needed — React bindings are included.

For Hono applications:

npmyarnpnpmbun
    
    
    npm i agents hono-agents
    
    
    yarn add agents hono-agents
    
    
    pnpm add agents hono-agents
    
    
    bun add agents hono-agents

## 2\. Create an Agent

Create a new file for your agent (for example, `src/agents/counter.ts`):
    
    
    import { Agent, callable } from "agents";
    
    export class CounterAgent extends Agent {
    	initialState = { count: 0 };
    
    	@callable()
    	increment() {
    		this.setState({ count: this.state.count + 1 });
    		return this.state.count;
    	}
    
    	@callable()
    	decrement() {
    		this.setState({ count: this.state.count - 1 });
    		return this.state.count;
    	}
    }
    
    
    import { Agent, callable } from "agents";
    
    export type CounterState = {
    	count: number;
    };
    
    export class CounterAgent extends Agent<Env, CounterState> {
    	initialState: CounterState = { count: 0 };
    
    	@callable()
    	increment() {
    		this.setState({ count: this.state.count + 1 });
    		return this.state.count;
    	}
    
    	@callable()
    	decrement() {
    		this.setState({ count: this.state.count - 1 });
    		return this.state.count;
    	}
    }

## 3\. Update Wrangler configuration

Add the Durable Object binding and migration:
    
    
    {
    	"name": "my-existing-project",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"compatibility_flags": ["nodejs_compat"],
    
    	"durable_objects": {
    		"bindings": [
    			{
    				"name": "CounterAgent",
    				"class_name": "CounterAgent",
    			},
    		],
    	},
    
    	"migrations": [
    		{
    			"tag": "v1",
    			"new_sqlite_classes": ["CounterAgent"],
    		},
    	],
    }
    
    
    name = "my-existing-project"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "nodejs_compat" ]
    
    [[durable_objects.bindings]]
    name = "CounterAgent"
    class_name = "CounterAgent"
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = [ "CounterAgent" ]

**Key points:**

  * `name` in bindings becomes the property on `env` (for example, `env.CounterAgent`)
  * `class_name` must exactly match your exported class name
  * `new_sqlite_classes` enables SQLite storage for state persistence
  * `nodejs_compat` flag is required for the agents package



## 4\. Configure TypeScript and Vite

If you use `@callable()` decorators (as in the example above), you need two build configurations.

**tsconfig.json** — extend `agents/tsconfig` (or set `"target": "ES2021"` manually):
    
    
    {
    	"extends": "agents/tsconfig"
    }

If you have an existing `tsconfig.json` with custom settings, you can extend and override:
    
    
    {
    	"extends": "agents/tsconfig",
    	"compilerOptions": {
    		"paths": { "~/*": ["./src/*"] }
    	}
    }

**vite.config.ts** — add the `agents()` plugin (handles TC39 decorator transforms for Vite 8):
    
    
    import agents from "agents/vite";
    
    export default defineConfig({
    	plugins: [
    		agents(),
    		// ... your existing plugins
    	],
    });
    
    
    import agents from "agents/vite";
    
    export default defineConfig({
    	plugins: [
    		agents(),
    		// ... your existing plugins
    	],
    });

If your project does not use Vite, the `tsconfig.json` change alone is sufficient — your bundler must support TC39 decorators (stage 3, version `2023-11`).

For more details, refer to the [TypeScript configuration](https://developers.cloudflare.com/agents/runtime/operations/configuration/#typescript-configuration) and [Vite configuration](https://developers.cloudflare.com/agents/runtime/operations/configuration/#vite-configuration) reference.

## 5\. Export the Agent class

Your agent class must be exported from your main entry point. Update your `src/index.ts`:
    
    
    // Export the agent class (required for Durable Objects)
    export { CounterAgent } from "./agents/counter";
    
    // Your existing exports...
    export default {
    	// ...
    };
    
    
    // Export the agent class (required for Durable Objects)
    export { CounterAgent } from "./agents/counter";
    
    // Your existing exports...
    export default {
    	// ...
    } satisfies ExportedHandler<Env>;

## 6\. Wire up routing

Choose the approach that matches your project structure:

### Plain Workers (fetch handler)
    
    
    import { routeAgentRequest } from "agents";
    export { CounterAgent } from "./agents/counter";
    
    export default {
    	async fetch(request, env, ctx) {
    		// Try agent routing first
    		const agentResponse = await routeAgentRequest(request, env);
    		if (agentResponse) return agentResponse;
    
    		// Your existing routing logic
    		const url = new URL(request.url);
    		if (url.pathname === "/api/hello") {
    			return Response.json({ message: "Hello!" });
    		}
    
    		return new Response("Not found", { status: 404 });
    	},
    };
    
    
    import { routeAgentRequest } from "agents";
    export { CounterAgent } from "./agents/counter";
    
    export default {
    	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    		// Try agent routing first
    		const agentResponse = await routeAgentRequest(request, env);
    		if (agentResponse) return agentResponse;
    
    		// Your existing routing logic
    		const url = new URL(request.url);
    		if (url.pathname === "/api/hello") {
    			return Response.json({ message: "Hello!" });
    		}
    
    		return new Response("Not found", { status: 404 });
    	},
    } satisfies ExportedHandler<Env>;

### Hono
    
    
    import { Hono } from "hono";
    import { agentsMiddleware } from "hono-agents";
    export { CounterAgent } from "./agents/counter";
    
    const app = new Hono();
    
    // Add agents middleware - handles WebSocket upgrades and agent HTTP requests
    app.use("*", agentsMiddleware());
    
    // Your existing routes continue to work
    app.get("/api/hello", (c) => c.json({ message: "Hello!" }));
    
    export default app;
    
    
    import { Hono } from "hono";
    import { agentsMiddleware } from "hono-agents";
    export { CounterAgent } from "./agents/counter";
    
    const app = new Hono<{ Bindings: Env }>();
    
    // Add agents middleware - handles WebSocket upgrades and agent HTTP requests
    app.use("*", agentsMiddleware());
    
    // Your existing routes continue to work
    app.get("/api/hello", (c) => c.json({ message: "Hello!" }));
    
    export default app;

### With static assets

If you are serving static assets alongside agents, static assets are served first by default. Your Worker code only runs for paths that do not match a static asset:
    
    
    import { routeAgentRequest } from "agents";
    export { CounterAgent } from "./agents/counter";
    
    export default {
    	async fetch(request, env, ctx) {
    		// Static assets are served automatically before this runs
    		// This only handles non-asset requests
    
    		// Route to agents
    		const agentResponse = await routeAgentRequest(request, env);
    		if (agentResponse) return agentResponse;
    
    		return new Response("Not found", { status: 404 });
    	},
    };
    
    
    import { routeAgentRequest } from "agents";
    export { CounterAgent } from "./agents/counter";
    
    export default {
    	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    		// Static assets are served automatically before this runs
    		// This only handles non-asset requests
    
    		// Route to agents
    		const agentResponse = await routeAgentRequest(request, env);
    		if (agentResponse) return agentResponse;
    
    		return new Response("Not found", { status: 404 });
    	},
    } satisfies ExportedHandler<Env>;

Configure assets in the Wrangler configuration file:
    
    
    {
    	"assets": {
    		"directory": "./public",
    	},
    }
    
    
    [assets]
    directory = "./public"

## 7\. Generate TypeScript types

Do not hand-write your `Env` interface. Run [`wrangler types`](https://developers.cloudflare.com/workers/wrangler/commands/general/#types) to generate a type definition file that matches your Wrangler configuration. This catches mismatches between your config and code at compile time instead of at deploy time.

Re-run `wrangler types` whenever you add or rename a binding.
    
    
    npx wrangler types

This creates a type definition file with all your bindings typed, including your agent Durable Object namespaces. The `Agent` class defaults to using the generated `Env` type, so you do not need to pass it as a type parameter — `extends Agent` is sufficient unless you need to pass a second type parameter for state (for example, `Agent<Env, CounterState>`).

Refer to [Configuration](https://developers.cloudflare.com/agents/runtime/operations/configuration/#generating-types) for more details on type generation.

## 8\. Connect from the frontend

### React
    
    
    import { useState } from "react";
    import { useAgent } from "agents/react";
    
    function CounterWidget() {
    	const [count, setCount] = useState(0);
    
    	const agent = useAgent({
    		agent: "CounterAgent",
    		onStateUpdate: (state) => setCount(state.count),
    	});
    
    	return (
    		<>
    			{count}
    			<button onClick={() => agent.stub.increment()}>+</button>
    			<button onClick={() => agent.stub.decrement()}>-</button>
    		</>
    	);
    }
    
    
    import { useState } from "react";
    import { useAgent } from "agents/react";
    import type { CounterAgent, CounterState } from "./agents/counter";
    
    function CounterWidget() {
    	const [count, setCount] = useState(0);
    
    	const agent = useAgent<CounterAgent, CounterState>({
    		agent: "CounterAgent",
    		onStateUpdate: (state) => setCount(state.count),
    	});
    
    	return (
    		<>
    			{count}
    			<button onClick={() => agent.stub.increment()}>+</button>
    			<button onClick={() => agent.stub.decrement()}>-</button>
    		</>
    	);
    }

Key points:

  * `useAgent` connects to your agent via WebSocket
  * `onStateUpdate` fires whenever the agent's state changes
  * `agent.stub.methodName()` calls methods marked with `@callable()` on your agent



### Vanilla JavaScript
    
    
    import { AgentClient } from "agents/client";
    
    const agent = new AgentClient({
    	agent: "CounterAgent",
    	name: "user-123", // Optional: unique instance name
    	onStateUpdate: (state) => {
    		document.getElementById("count").textContent = state.count;
    	},
    });
    
    // Call methods
    document.getElementById("increment").onclick = () => agent.call("increment");
    
    
    import { AgentClient } from "agents/client";
    
    const agent = new AgentClient({
    	agent: "CounterAgent",
    	name: "user-123", // Optional: unique instance name
    	onStateUpdate: (state) => {
    		document.getElementById("count").textContent = state.count;
    	},
    });
    
    // Call methods
    document.getElementById("increment").onclick = () => agent.call("increment");

## How it works

When you clicked the button:

  1. **Client** called `agent.stub.increment()` over WebSocket
  2. **Agent** ran `increment()`, updated state with `setState()`
  3. **State** persisted to SQLite automatically
  4. **Broadcast** sent to all connected clients
  5. **React** updated via `onStateUpdate`


    
    
    flowchart LR
        A["Browser<br/>(React)"] <-->|WebSocket| B["Agent<br/>(Counter)"]
        B --> C["SQLite<br/>(State)"]
    

### Key concepts

Concept | What it means  
---|---  
**Agent instance** | Each unique name gets its own agent. `CounterAgent:user-123` is separate from `CounterAgent:user-456`  
**Persistent state** | State survives restarts, deploys, and hibernation. It is stored in SQLite  
**Real-time sync** | All clients connected to the same agent receive state updates instantly  
**Hibernation** | When no clients are connected, the agent hibernates (no cost). It wakes on the next request  
  
## Deploy to Cloudflare
    
    
    npm run deploy

Your agent is now live on Cloudflare's global network, running close to your users.

## Common integration patterns

### Agents behind authentication

Check auth before routing to agents:
    
    
    export default {
    	async fetch(request, env) {
    		// Check auth for agent routes
    		if (request.url.includes("/agents/")) {
    			const authResult = await checkAuth(request, env);
    			if (!authResult.valid) {
    				return new Response("Unauthorized", { status: 401 });
    			}
    		}
    
    		const agentResponse = await routeAgentRequest(request, env);
    		if (agentResponse) return agentResponse;
    
    		// ... rest of routing
    	},
    };
    
    
    export default {
    	async fetch(request: Request, env: Env) {
    		// Check auth for agent routes
    		if (request.url.includes("/agents/")) {
    			const authResult = await checkAuth(request, env);
    			if (!authResult.valid) {
    				return new Response("Unauthorized", { status: 401 });
    			}
    		}
    
    		const agentResponse = await routeAgentRequest(request, env);
    		if (agentResponse) return agentResponse;
    
    		// ... rest of routing
    	},
    } satisfies ExportedHandler<Env>;

### Custom agent path prefix

By default, agents are routed at `/agents/{agent-name}/{instance-name}`. You can customize this:
    
    
    import { routeAgentRequest } from "agents";
    
    const agentResponse = await routeAgentRequest(request, env, {
    	prefix: "/api/agents", // Now routes at /api/agents/{agent-name}/{instance-name}
    });
    
    
    import { routeAgentRequest } from "agents";
    
    const agentResponse = await routeAgentRequest(request, env, {
    	prefix: "/api/agents", // Now routes at /api/agents/{agent-name}/{instance-name}
    });

Refer to [Routing](https://developers.cloudflare.com/agents/runtime/communication/routing/) for more options including CORS, custom instance naming, and location hints.

### Accessing agents from server code

You can interact with agents directly from your Worker code:
    
    
    import { getAgentByName } from "agents";
    
    export default {
    	async fetch(request, env) {
    		if (request.url.endsWith("/api/increment")) {
    			// Get a specific agent instance
    			const counter = await getAgentByName(env.CounterAgent, "shared-counter");
    			const newCount = await counter.increment();
    			return Response.json({ count: newCount });
    		}
    		// ...
    	},
    };
    
    
    import { getAgentByName } from "agents";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		if (request.url.endsWith("/api/increment")) {
    			// Get a specific agent instance
    			const counter = await getAgentByName(env.CounterAgent, "shared-counter");
    			const newCount = await counter.increment();
    			return Response.json({ count: newCount });
    		}
    		// ...
    	},
    } satisfies ExportedHandler<Env>;

### Adding multiple agents

Add more agents by extending the configuration:
    
    
    // src/agents/chat.ts
    export class Chat extends Agent {
    	// ...
    }
    
    // src/agents/scheduler.ts
    export class Scheduler extends Agent {
    	// ...
    }
    
    
    // src/agents/chat.ts
    export class Chat extends Agent {
    	// ...
    }
    
    // src/agents/scheduler.ts
    export class Scheduler extends Agent {
    	// ...
    }

Update the Wrangler configuration file:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "durable_objects": {
        "bindings": [
          {
            "name": "CounterAgent",
            "class_name": "CounterAgent"
          },
          {
            "name": "Chat",
            "class_name": "Chat"
          },
          {
            "name": "Scheduler",
            "class_name": "Scheduler"
          }
        ]
      },
      "migrations": [
        {
          "tag": "v1",
          "new_sqlite_classes": [
            "CounterAgent",
            "Chat",
            "Scheduler"
          ]
        }
      ]
    }
    
    
    [[durable_objects.bindings]]
    name = "CounterAgent"
    class_name = "CounterAgent"
    
    [[durable_objects.bindings]]
    name = "Chat"
    class_name = "Chat"
    
    [[durable_objects.bindings]]
    name = "Scheduler"
    class_name = "Scheduler"
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = ["CounterAgent", "Chat", "Scheduler"]

Export all agents from your entry point:
    
    
    export { CounterAgent } from "./agents/counter";
    export { Chat } from "./agents/chat";
    export { Scheduler } from "./agents/scheduler";
    
    
    export { CounterAgent } from "./agents/counter";
    export { Chat } from "./agents/chat";
    export { Scheduler } from "./agents/scheduler";

## Troubleshooting

### Agent not found, or 404 errors

  1. **Check the export** \- Agent class must be exported from your main entry point.
  2. **Check the binding** \- `class_name` in the Wrangler configuration file must exactly match the exported class name.
  3. **Check the route** \- Default route is `/agents/{'{agent-name}'}/{'{instance-name}'}`. Agent name in client matches the class name (case-insensitive).



### No such Durable Object class error

Add the migration to the Wrangler configuration file:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "migrations": [
        {
          "tag": "v1",
          "new_sqlite_classes": [
            "YourAgentClass"
          ]
        }
      ]
    }
    
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = ["YourAgentClass"]

### WebSocket connection fails

Ensure your routing passes the response unchanged:
    
    
    // Correct - return the response directly
    const agentResponse = await routeAgentRequest(request, env);
    if (agentResponse) return agentResponse;
    
    // Wrong - this breaks WebSocket connections
    if (agentResponse) return new Response(agentResponse.body);
    
    
    // Correct - return the response directly
    const agentResponse = await routeAgentRequest(request, env);
    if (agentResponse) return agentResponse;
    
    // Wrong - this breaks WebSocket connections
    if (agentResponse) return new Response(agentResponse.body);

### State not persisting

Check that:

  1. You are calling `this.setState()`, not mutating `this.state` directly.
  2. The agent class is in `new_sqlite_classes` in migrations.
  3. You are connecting to the same agent instance name.
  4. The `onStateUpdate` callback is wired up in your client.
  5. WebSocket connection is established (check browser dev tools).



### "Method X is not callable" errors

Make sure your methods are decorated with `@callable()`:
    
    
    import { Agent, callable } from "agents";
    
    export class MyAgent extends Agent {
    	@callable()
    	increment() {
    		// ...
    	}
    }
    
    
    import { Agent, callable } from "agents";
    
    export class MyAgent extends Agent {
    	@callable()
    	increment() {
    		// ...
    	}
    }

### Type errors with `agent.stub`

Add the agent and state type parameters:
    
    
    import { useAgent } from "agents/react";
    
    // Pass the agent and state types to useAgent
    const agent = useAgent({
    	agent: "CounterAgent",
    	onStateUpdate: (state) => setCount(state.count),
    });
    
    // Now agent.stub is fully typed
    agent.stub.increment();
    
    
    import { useAgent } from "agents/react";
    import type { CounterAgent, CounterState } from "./server";
    
    // Pass the agent and state types to useAgent
    const agent = useAgent<CounterAgent, CounterState>({
    	agent: "CounterAgent",
    	onStateUpdate: (state) => setCount(state.count),
    });
    
    // Now agent.stub is fully typed
    agent.stub.increment();

### `SyntaxError: Invalid or unexpected token` with `@callable()`

If your dev server fails with `SyntaxError: Invalid or unexpected token`, set `"target": "ES2021"` in your `tsconfig.json`. This ensures that Vite's esbuild transpiler downlevels TC39 decorators instead of passing them through as native syntax.
    
    
    {
    	"compilerOptions": {
    		"target": "ES2021"
    	}
    }

Caution

Do not set `"experimentalDecorators": true` in your `tsconfig.json`. The Agents SDK uses [TC39 standard decorators ↗︎](https://github.com/tc39/proposal-decorators), not TypeScript legacy decorators. Enabling `experimentalDecorators` applies an incompatible transform that silently breaks `@callable()` at runtime.

## Next steps

Now that you have a working agent, explore these topics:

### Common next steps

Learn how to | Refer to  
---|---  
Add AI/LLM capabilities | [Using AI models](https://developers.cloudflare.com/agents/runtime/operations/using-ai-models/)  
Expose tools via MCP | [MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/)  
Run background tasks | [Schedule tasks](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/)  
Handle emails | [Email routing](https://developers.cloudflare.com/agents/communication-channels/email/)  
Use Cloudflare Workflows | [Run Workflows](https://developers.cloudflare.com/agents/runtime/execution/run-workflows/)  
  
### Explore more

### [State management](https://developers.cloudflare.com/agents/runtime/lifecycle/state/)

Deep dive into setState(), initialState, and onStateChanged().

### [Client SDK](https://developers.cloudflare.com/agents/communication-channels/chat/client-sdk/)

Full useAgent and AgentClient API reference.

### [Callable methods](https://developers.cloudflare.com/agents/runtime/lifecycle/callable-methods/)

Expose methods to clients with @callable().

### [Schedule tasks](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/)

Run tasks on a delay, schedule, or cron.

### [Agent class internals](https://developers.cloudflare.com/agents/runtime/lifecycle/agent-class/)

Full lifecycle and methods reference.

### [Agents API](https://developers.cloudflare.com/agents/runtime/agents-api/)

Complete API reference for the Agents SDK.

[PreviousQuick start](https://developers.cloudflare.com/agents/getting-started/quick-start/)[NextTesting your Agents](https://developers.cloudflare.com/agents/getting-started/testing-your-agent/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/getting-started/add-to-existing-project.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
