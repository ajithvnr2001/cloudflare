---
url: https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/
title: Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:42.134737+00:00
---

# Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 23, 2026

## Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) exposes agent state as a readable property, prevents duplicate schedule rows across Durable Object restarts, brings full TypeScript inference to `AgentClient`, and migrates to Zod 4.

#### Readable `state` on `useAgent` and `AgentClient`

Both `useAgent` (React) and `AgentClient` (vanilla JS) now expose a `state` property that reflects the current agent state. Previously, reading state required manually tracking it through the `onStateUpdate` callback.

**React (`useAgent`)**
    
    
    const agent = useAgent({
    	agent: "game-agent",
    	name: "room-123",
    });
    
    // Read state directly — no separate useState + onStateUpdate needed
    return <div>Score: {agent.state?.score}</div>;
    
    // Spread for partial updates
    agent.setState({ ...agent.state, score: (agent.state?.score ?? 0) + 10 });
    
    
    const agent = useAgent<GameAgent, GameState>({
    	agent: "game-agent",
    	name: "room-123",
    });
    
    // Read state directly — no separate useState + onStateUpdate needed
    return <div>Score: {agent.state?.score}</div>;
    
    // Spread for partial updates
    agent.setState({ ...agent.state, score: (agent.state?.score ?? 0) + 10 });

`agent.state` is reactive — the component re-renders when state changes from either the server or a client-side `setState()` call.

**Vanilla JS (`AgentClient`)**
    
    
    const client = new AgentClient({
    	agent: "game-agent",
    	name: "room-123",
    	host: "your-worker.workers.dev",
    });
    
    client.setState({ score: 100 });
    console.log(client.state); // { score: 100 }
    
    
    const client = new AgentClient<GameAgent>({
    	agent: "game-agent",
    	name: "room-123",
    	host: "your-worker.workers.dev",
    });
    
    client.setState({ score: 100 });
    console.log(client.state); // { score: 100 }

State starts as `undefined` and is populated when the server sends the initial state on connect (from `initialState`) or when `setState()` is called. Use optional chaining (`agent.state?.field`) for safe access. The `onStateUpdate` callback continues to work as before — the new `state` property is additive.

#### Idempotent `schedule()`

`schedule()` now supports an `idempotent` option that deduplicates by `(type, callback, payload)`, preventing duplicate rows from accumulating when called in places that run on every Durable Object restart such as `onStart()`.

**Cron schedules are idempotent by default.** Calling `schedule("0 * * * *", "tick")` multiple times with the same callback, expression, and payload returns the existing schedule row instead of creating a new one. Pass `{ idempotent: false }` to override.

Delayed and date-scheduled types support opt-in idempotency:
    
    
    import { Agent } from "agents";
    
    class MyAgent extends Agent {
    	async onStart() {
    		// Safe across restarts — only one row is created
    		await this.schedule(60, "maintenance", undefined, { idempotent: true });
    	}
    }
    
    
    import { Agent } from "agents";
    
    class MyAgent extends Agent {
    	async onStart() {
    		// Safe across restarts — only one row is created
    		await this.schedule(60, "maintenance", undefined, { idempotent: true });
    	}
    }

Two new warnings help catch common foot-guns:

  * Calling `schedule()` inside `onStart()` without `{ idempotent: true }` emits a `console.warn` with actionable guidance (once per callback; skipped for cron and when `idempotent` is set explicitly).
  * If an alarm cycle processes 10 or more stale one-shot rows for the same callback, the SDK emits a `console.warn` and a `schedule:duplicate_warning` diagnostics channel event.



#### Typed `AgentClient` with `call` inference and `stub` proxy

`AgentClient` now accepts an optional agent type parameter for full type inference on RPC calls, matching the typed experience already available with `useAgent`.
    
    
    const client = new AgentClient({
    	agent: "my-agent",
    	host: window.location.host,
    });
    
    // Typed call — method name autocompletes, args and return type inferred
    const value = await client.call("getValue");
    
    // Typed stub — direct RPC-style proxy
    await client.stub.getValue();
    await client.stub.add(1, 2);
    
    
    const client = new AgentClient<MyAgent>({
    	agent: "my-agent",
    	host: window.location.host,
    });
    
    // Typed call — method name autocompletes, args and return type inferred
    const value = await client.call("getValue");
    
    // Typed stub — direct RPC-style proxy
    await client.stub.getValue();
    await client.stub.add(1, 2);

State is automatically inferred from the agent type, so `onStateUpdate` is also typed:
    
    
    const client = new AgentClient({
    	agent: "my-agent",
    	host: window.location.host,
    	onStateUpdate: (state) => {
    		// state is typed as MyAgent's state type
    	},
    });
    
    
    const client = new AgentClient<MyAgent>({
    	agent: "my-agent",
    	host: window.location.host,
    	onStateUpdate: (state) => {
    		// state is typed as MyAgent's state type
    	},
    });

Existing untyped usage continues to work without changes. The RPC type utilities (`AgentMethods`, `AgentStub`, `RPCMethods`) are now exported from `agents/client` for advanced typing scenarios. `agents`, `@cloudflare/ai-chat`, and `@cloudflare/codemode` now require `zod ^4.0.0`. Zod v3 is no longer supported.

#### `@cloudflare/ai-chat` fixes

  * **Turn serialization** — `onChatMessage()` and `_reply()` work is now queued so user requests, tool continuations, and `saveMessages()` never stream concurrently.
  * **Duplicate messages on stop** — Clicking stop during an active stream no longer splits the assistant message into two entries.
  * **Duplicate messages after tool calls** — Orphaned client IDs no longer leak into persistent storage.



#### `keepAlive()` and `keepAliveWhile()` are no longer experimental

`keepAlive()` now uses a lightweight in-memory ref count instead of schedule rows. Multiple concurrent callers share a single alarm cycle. The `@experimental` tag has been removed from both `keepAlive()` and `keepAliveWhile()`.

#### `@cloudflare/codemode`: TanStack AI integration

A new entry point `@cloudflare/codemode/tanstack-ai` adds support for [TanStack AI's ↗︎](https://tanstack.com/ai) `chat()` as an alternative to the Vercel AI SDK's `streamText()`:
    
    
    import {
    	createCodeTool,
    	tanstackTools,
    } from "@cloudflare/codemode/tanstack-ai";
    import { chat } from "@tanstack/ai";
    
    const codeTool = createCodeTool({
    	tools: [tanstackTools(myServerTools)],
    	executor,
    });
    
    const stream = chat({ adapter, tools: [codeTool], messages });
    
    
    import { createCodeTool, tanstackTools } from "@cloudflare/codemode/tanstack-ai";
    import { chat } from "@tanstack/ai";
    
    const codeTool = createCodeTool({
    	tools: [tanstackTools(myServerTools)],
    	executor,
    });
    
    const stream = chat({ adapter, tools: [codeTool], messages });

#### Upgrade

To update to the latest version:
    
    
    npm i agents@latest @cloudflare/ai-chat@latest
