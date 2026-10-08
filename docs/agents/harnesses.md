---
url: https://developers.cloudflare.com/agents/harnesses/
title: Harnesses \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:11.829454+00:00
---

# Harnesses · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Harnesses



# Harnesses

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/harnesses/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow harnesses fitChoose an approachCurrent harnessesWhat a harness usually ownsRelated resources

A harness is the loop that makes an agent behave like an agent instead of a single model call.

It is responsible for the turn-by-turn work around the model: building the prompt, loading memory, selecting tools, handling tool results, streaming responses, persisting messages, and deciding whether the agent should continue or stop.

You can build this loop yourself on top of the [Agents SDK runtime](https://developers.cloudflare.com/agents/runtime/agents-api/), use an opinionated harness like [Project Think](https://developers.cloudflare.com/agents/harnesses/think/), or run an external harness such as [Pi](https://developers.cloudflare.com/agents/harnesses/pi/) on a Durable Object.

## How harnesses fit

Harnesses sit on top of the Agents SDK runtime:

  * **The runtime** gives the agent durable infrastructure: the [`Agent` class](https://developers.cloudflare.com/agents/runtime/lifecycle/agent-class/), [state](https://developers.cloudflare.com/agents/runtime/lifecycle/state/), [sessions](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/), [routing](https://developers.cloudflare.com/agents/runtime/communication/routing/), [WebSockets](https://developers.cloudflare.com/agents/runtime/communication/websockets/), [scheduling](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/), [fibers](https://developers.cloudflare.com/agents/runtime/execution/durable-execution/), and [observability](https://developers.cloudflare.com/agents/runtime/operations/observability/).
  * **The harness** gives the agent behavior: model calls, prompt construction, tool selection, stream handling, memory strategy, and lifecycle hooks.



The runtime answers “where does this agent live and how does it stay durable?” The harness answers “what does this agent do on each turn?”

## Choose an approach

Use a build-your-own harness when you need full control over the model call, message format, tool loop, or UI protocol. This is the right approach when you want to compose low-level APIs directly from the Agents SDK.

Use Project Think when you want an opinionated chat-agent harness with defaults for memory, workspace tools, streaming, lifecycle hooks, sub-agent RPC, and durable chat recovery.

Use Pi (beta) when you want [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/) to own the agent loop, transcript, and recovery. `PiHarness` runs it inside an `Agent` or a plain Durable Object and wakes it after eviction. You choose the transport.

## Current harnesses

### [Project Think](https://developers.cloudflare.com/agents/harnesses/think/)

An opinionated chat agent harness with built-in tools, persistent memory, lifecycle hooks, streaming, and sub-agent RPC.

### [Pi (beta)](https://developers.cloudflare.com/agents/harnesses/pi/)

Run Pi Durable sessions inside an Agent or Durable Object, with storage in SQLite and recovery after eviction.

## What a harness usually owns

A harness usually owns:

  * **Prompt construction** — system prompts, memory, retrieved context, and per-turn instructions.
  * **Model execution** — the call to Workers AI, OpenAI, Anthropic, Gemini, or another provider.
  * **Tool orchestration** — server tools, client tools, MCP tools, approval flows, and continuation after tool results.
  * **Message persistence** — how user, assistant, and tool messages are saved and replayed.
  * **Streaming and recovery** — how responses stream to clients and resume after disconnects or Durable Object eviction.
  * **Extension points** — hooks before and after turns, steps, tool calls, and recovery events.



## Related resources

### [Agents SDK runtime](https://developers.cloudflare.com/agents/runtime/agents-api/)

Build your own harness directly on the Agent class.

### [Sessions](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/)

Store conversation context and memory across turns.

### [Durable execution with fibers](https://developers.cloudflare.com/agents/runtime/execution/durable-execution/)

Recover long-running agent work after Durable Object eviction.

[PreviousPi AI](https://developers.cloudflare.com/agents/models/pi-ai/)[NextOverview](https://developers.cloudflare.com/agents/harnesses/think/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
