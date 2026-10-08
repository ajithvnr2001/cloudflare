---
url: https://developers.cloudflare.com/agents/getting-started/quick-start/
title: Quick start \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:11.784798+00:00
---

# Quick start · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/getting-started/quick-start/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Getting started
  4. /Quick start



# Quick start

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/getting-started/quick-start/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a new projectYour first agentConnect from ReactHow it works Key conceptsConnect from vanilla JavaScriptDeploy to CloudflareCommon integration patterns Agents behind authentication Custom agent path prefix Accessing agents from server code Adding multiple agentsTroubleshooting Agent not found, or 404 errors No such Durable Object class error WebSocket connection fails State not persisting "Method X is not callable" errors Type errors with agent.stub SyntaxError: Invalid or unexpected token with @callable()Next steps Common next steps Explore more

Build AI agents that persist, think, and act. Agents run on Cloudflare's global network, maintain state across requests, and connect to clients in real-time via WebSockets.

**What you will build:** A counter agent with persistent state that syncs to a React frontend in real-time.

**Time:** ~10 minutes

## Create a new project

npmyarnpnpm
    
    
    npm create cloudflare@latest -- --template cloudflare/agents-starter
    
    
    yarn create cloudflare --template cloudflare/agents-starter
    
    
    pnpm create cloudflare@latest --template cloudflare/agents-starter

Then install dependencies and start the dev server:
    
    
    cd agents-starter
    npm install
    npm run dev

This creates a project with:

  * `src/server.ts` — Your agent code
  * `src/client.tsx` — React frontend
  * `wrangler.jsonc` — Cloudflare configuration
  * `tsconfig.json` — Extends `agents/tsconfig` for correct decorator and module settings
  * `vite.config.ts` — Includes the `agents/vite` plugin for decorator support



The starter template includes two important SDK integrations. If you are setting up a project manually, add both:

**tsconfig.json** — extends `agents/tsconfig`, which sets `target: "ES2021"` and other recommended options:
    
    
    {
    	"extends": "agents/tsconfig"
    }

**vite.config.ts** — includes the `agents()` plugin, which handles TC39 decorator transforms (required for `@callable()` in Vite 8):
    
    
    import { cloudflare } from "@cloudflare/vite-plugin";
    import react from "@vitejs/plugin-react";
    import agents from "agents/vite";
    import { defineConfig } from "vite";
    
    export default defineConfig({
    	plugins: [agents(), react(), cloudflare()],
    });

Open <http://localhost:5173>[ ↗︎](http://localhost:5173) to see your agent in action.

## Your first agent

Build a simple counter agent from scratch. Replace `src/server.ts`:
    
    
    import { Agent, routeAgentRequest, callable } from "agents";
    
    // Define the state shape
    
    // Create the agent
    export class CounterAgent extends Agent {
    	// Initial state for new instances
    	initialState = { count: 0 };
    
    	// Methods marked with @callable can be called from the client
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
    
    	@callable()
    	reset() {
    		this.setState({ count: 0 });
    	}
    }
    
    // Route requests to agents
    export default {
    	async fetch(request, env, ctx) {
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    };

src/server.tsts
    
    
    import { Agent, routeAgentRequest, callable } from "agents";
    
    // Define the state shape
    export type CounterState = {
    	count: number;
    };
    
    // Create the agent
    export class CounterAgent extends Agent<Env, CounterState> {
    	// Initial state for new instances
    	initialState: CounterState = { count: 0 };
    
    	// Methods marked with @callable can be called from the client
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
    
    	@callable()
    	reset() {
    		this.setState({ count: 0 });
    	}
    }
    
    // Route requests to agents
    export default {
    	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

Update `wrangler.jsonc` to register the agent:
    
    
    {
    	"name": "my-agent",
    	"main": "src/server.ts",
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
    
    
    name = "my-agent"
    main = "src/server.ts"
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



## Connect from React

Replace `src/client.tsx`:

src/client.tsxtsx
    
    
    import "./styles.css";
    import { createRoot } from "react-dom/client";
    import { useState } from "react";
    import { useAgent } from "agents/react";
    import type { CounterAgent, CounterState } from "./server";
    
    export default function App() {
    	const [count, setCount] = useState(0);
    
    	// Connect to the Counter agent
    	const agent = useAgent<CounterAgent, CounterState>({
    		agent: "CounterAgent",
    		onStateUpdate: (state) => setCount(state.count),
    	});
    
    	return (
    		<div style={{ padding: "2rem", fontFamily: "system-ui" }}>
    			<h1>Counter Agent</h1>
    			<p style={{ fontSize: "3rem" }}>{count}</p>
    			<div style={{ display: "flex", gap: "1rem" }}>
    				<button onClick={() => agent.stub.decrement()}>-</button>
    				<button onClick={() => agent.stub.reset()}>Reset</button>
    				<button onClick={() => agent.stub.increment()}>+</button>
    			</div>
    		</div>
    	);
    }
    
    const root = createRoot(document.getElementById("root")!);
    root.render(<App />);

Key points:

  * `useAgent` connects to your agent via WebSocket
  * `onStateUpdate` fires whenever the agent's state changes
  * `agent.stub.methodName()` calls methods marked with `@callable()` on your agent



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
  
## Connect from vanilla JavaScript

If you are not using React:
    
    
    import { AgentClient } from "agents/client";
    
    const agent = new AgentClient({
    	agent: "CounterAgent",
    	name: "my-counter", // optional, defaults to "default"
    	onStateUpdate: (state) => {
    		console.log("New count:", state.count);
    	},
    });
    
    // Call methods
    await agent.call("increment");
    await agent.call("reset");
    
    
    import { AgentClient } from "agents/client";
    
    const agent = new AgentClient({
    	agent: "CounterAgent",
    	name: "my-counter", // optional, defaults to "default"
    	onStateUpdate: (state) => {
    		console.log("New count:", state.count);
    	},
    });
    
    // Call methods
    await agent.call("increment");
    await agent.call("reset");

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

[PreviousOverview](https://developers.cloudflare.com/agents/)[NextAdd to existing project](https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/getting-started/quick-start.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
