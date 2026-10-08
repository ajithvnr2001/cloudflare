---
url: https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/
title: Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:37.393872+00:00
---

# Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 17, 2026

## Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-17-agents-sdk-v0.5.0/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) adds built-in retry utilities, per-connection protocol message control, and a fully rewritten `@cloudflare/ai-chat` with data parts, tool approval persistence, and zero breaking changes.

#### Retry utilities

A new `this.retry()` method lets you retry any async operation with exponential backoff and jitter. You can pass an optional `shouldRetry` predicate to bail early on non-retryable errors.
    
    
    class MyAgent extends Agent {
    	async onRequest(request) {
    		const data = await this.retry(() => callUnreliableService(), {
    			maxAttempts: 4,
    			shouldRetry: (err) => !(err instanceof PermanentError),
    		});
    		return Response.json(data);
    	}
    }
    
    
    class MyAgent extends Agent {
    	async onRequest(request: Request) {
    		const data = await this.retry(() => callUnreliableService(), {
    			maxAttempts: 4,
    			shouldRetry: (err) => !(err instanceof PermanentError),
    		});
    		return Response.json(data);
    	}
    }

Retry options are also available per-task on `queue()`, `schedule()`, `scheduleEvery()`, and `addMcpServer()`:
    
    
    // Per-task retry configuration, persisted in SQLite alongside the task
    await this.schedule(
    	Date.now() + 60_000,
    	"sendReport",
    	{ userId: "abc" },
    	{
    		retry: { maxAttempts: 5 },
    	},
    );
    
    // Class-level retry defaults
    class MyAgent extends Agent {
    	static options = {
    		retry: { maxAttempts: 3 },
    	};
    }
    
    
    // Per-task retry configuration, persisted in SQLite alongside the task
    await this.schedule(Date.now() + 60_000, "sendReport", { userId: "abc" }, {
    	retry: { maxAttempts: 5 },
    });
    
    // Class-level retry defaults
    class MyAgent extends Agent {
    	static options = {
    		retry: { maxAttempts: 3 },
    	};
    }

Retry options are validated eagerly at enqueue/schedule time, and invalid values throw immediately. Internal retries have also been added for workflow operations (`terminateWorkflow`, `pauseWorkflow`, and others) with Durable Object-aware error detection.

#### Per-connection protocol message control

Agents automatically send JSON text frames (identity, state, MCP server lists) to every WebSocket connection. You can now suppress these per-connection for clients that cannot handle them — binary-only devices, MQTT clients, or lightweight embedded systems.
    
    
    class MyAgent extends Agent {
    	shouldSendProtocolMessages(connection, ctx) {
    		// Suppress protocol messages for MQTT clients
    		const subprotocol = ctx.request.headers.get("Sec-WebSocket-Protocol");
    		return subprotocol !== "mqtt";
    	}
    }
    
    
    class MyAgent extends Agent {
    	shouldSendProtocolMessages(connection: Connection, ctx: ConnectionContext) {
    		// Suppress protocol messages for MQTT clients
    		const subprotocol = ctx.request.headers.get("Sec-WebSocket-Protocol");
    		return subprotocol !== "mqtt";
    	}
    }

Connections with protocol messages disabled still fully participate in RPC and regular messaging. Use `isConnectionProtocolEnabled(connection)` to check a connection's status at any time. The flag persists across Durable Object hibernation.

See [Protocol messages](https://developers.cloudflare.com/agents/runtime/communication/protocol-messages/) for full documentation.

#### `@cloudflare/ai-chat` v0.1.0

The first stable release of `@cloudflare/ai-chat` ships alongside this release with a major refactor of `AIChatAgent` internals — new `ResumableStream` class, WebSocket `ChatTransport`, and simplified SSE parsing — with zero breaking changes. Existing code using `AIChatAgent` and `useAgentChat` works as-is.

Key new features:

  * **Data parts** — Attach typed JSON blobs (`data-*`) to messages alongside text. Supports reconciliation (type+id updates in-place), append, and transient parts (ephemeral via `onData` callback). See [Data parts](https://developers.cloudflare.com/agents/communication-channels/chat/chat-agents/#data-parts).
  * **Tool approval persistence** — The `needsApproval` approval UI now survives page refresh and DO hibernation. The streaming message is persisted to SQLite when a tool enters `approval-requested` state.
  * **`maxPersistedMessages`** — Cap SQLite message storage with automatic oldest-message deletion.
  * **`body` option on `useAgentChat`** — Send custom data with every request (static or dynamic).
  * **Incremental persistence** — Hash-based cache to skip redundant SQL writes.
  * **Row size guard** — Automatic two-pass compaction when messages approach the SQLite 2 MB limit.
  * **`autoContinueAfterToolResult` defaults to `true`** — Client-side tool results and tool approvals now automatically trigger a server continuation, matching server-executed tool behavior. Set `autoContinueAfterToolResult: false` in `useAgentChat` to restore the previous behavior.



Notable bug fixes:

  * Resolved stream resumption race conditions
  * Resolved an issue where `setMessages` functional updater sent empty arrays
  * Resolved an issue where client tool schemas were lost after DO hibernation
  * Resolved `InvalidPromptError` after tool approval (`approval.id` was dropped)
  * Resolved an issue where message metadata was not propagated on broadcast/resume paths
  * Resolved an issue where `clearAll()` did not clear in-memory chunk buffers
  * Resolved an issue where `reasoning-delta` silently dropped data when `reasoning-start` was missed during stream resumption



#### Synchronous queue and schedule getters

`getQueue()`, `getQueues()`, `getSchedule()`, `dequeue()`, `dequeueAll()`, and `dequeueAllByCallback()` were unnecessarily `async` despite only performing synchronous SQL operations. They now return values directly instead of wrapping them in Promises. This is backward compatible — existing code using `await` on these methods will continue to work.

#### Other improvements

  * **Fix TypeScript "excessively deep" error** — A depth counter on `CanSerialize` and `IsSerializableParam` types bails out to `true` after 10 levels of recursion, preventing the "Type instantiation is excessively deep" error with deeply nested types like AI SDK `CoreMessage[]`.
  * **POST SSE keepalive** — The POST SSE handler now sends `event: ping` every 30 seconds to keep the connection alive, matching the existing GET SSE handler behavior. This prevents POST response streams from being silently dropped by proxies during long-running tool calls.
  * **Widened peer dependency ranges** — Peer dependency ranges across packages have been widened to prevent cascading major bumps during 0.x minor releases. `@cloudflare/ai-chat` and `@cloudflare/codemode` are now marked as optional peer dependencies.



#### Upgrade

To update to the latest version:
    
    
    npm i agents@latest @cloudflare/ai-chat@latest
