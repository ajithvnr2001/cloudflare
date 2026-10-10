---
url: https://developers.cloudflare.com/changelog/post/2026-06-16-agents-sdk-v0.16.1/
title: Agents SDK improves browser automation, code execution, and recovery \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.543482+00:00
---

# Agents SDK improves browser automation, code execution, and recovery · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-16-agents-sdk-v0.16.1/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 16, 2026

## Agents SDK improves browser automation, code execution, and recovery

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) makes it easier to build agents that can safely interact with real systems and keep working through interruptions.

Agents can now browse websites through Browser Run, write code against external tools through Code Mode, use client-provided tools when delegating to Think sub-agents, and recover more reliably from deploys, Durable Object evictions, and connection churn.

#### Safer browser automation

Agents can now use [Browser Run](https://developers.cloudflare.com/browser-run/) through a single durable `browser_execute` tool. Instead of choosing from a fixed list of actions, the model writes code against the Chrome DevTools Protocol (CDP) and can inspect pages, capture screenshots, read rendered content, debug frontend behavior, and interact with live browser sessions.
    
    
    const browserTools = createBrowserTools({
    	ctx: this.ctx,
    	browser: this.env.BROWSER,
    	loader: this.env.LOADER,
    	session: { mode: "dynamic" },
    });
    
    
    const browserTools = createBrowserTools({
    	ctx: this.ctx,
    	browser: this.env.BROWSER,
    	loader: this.env.LOADER,
    	session: { mode: "dynamic" },
    });

Browser sessions can be one-time, reused, or promoted from one-time to persistent during a run. This is useful when an agent needs a human to log in, complete MFA, or approve a sensitive action. The run can pause, keep the same tabs and cookies, and resume after approval.

The browser tools also add Live View URLs, optional session recording, and quick actions such as `browser_markdown`, `browser_extract`, `browser_links`, and `browser_scrape` for one-shot browsing tasks.

#### Resumable code execution with approvals

Code Mode now uses `createCodemodeRuntime`, connectors, and a durable execution log. This lets you give a model one `codemode` tool instead of a large prompt full of tool definitions. The model can discover the capabilities it needs, write code against typed globals, and reuse saved snippets.
    
    
    const runtime = createCodemodeRuntime({
    	ctx: this.ctx,
    	executor: new DynamicWorkerExecutor({ loader: this.env.LOADER }),
    	connectors: [new GithubConnector(this.ctx, this.env, connection)],
    });
    
    const result = streamText({
    	model,
    	messages,
    	tools: { codemode: runtime.tool() },
    });
    
    
    const runtime = createCodemodeRuntime({
    	ctx: this.ctx,
    	executor: new DynamicWorkerExecutor({ loader: this.env.LOADER }),
    	connectors: [new GithubConnector(this.ctx, this.env, connection)],
    });
    
    const result = streamText({
    	model,
    	messages,
    	tools: { codemode: runtime.tool() },
    });

When the code reaches an approval-gated action, the runtime pauses execution and returns a pending approval. After approval, completed calls replay from the durable log, the approved action runs, and the same code continues. This makes it practical to build agents that create issues, update external systems, or perform other side effects without custom pause-and-resume logic for every tool.

#### Better Think delegation

Think sub-agents can now use client-defined tools over the RPC `chat()` path. A parent agent can pass tool schemas with `clientTools` and resolve tool calls through `onClientToolCall`. This lets delegated agents use caller-provided capabilities without requiring a browser WebSocket.
    
    
    await child.chat(message, callback, {
    	signal,
    	clientTools: [
    		{
    			name: "get_user_timezone",
    			description: "Get the caller's timezone",
    			parameters: { type: "object" },
    		},
    	],
    	onClientToolCall: async ({ toolName, input }) => {
    		return runClientTool(toolName, input);
    	},
    });
    
    
    await child.chat(message, callback, {
    	signal,
    	clientTools: [
    		{
    			name: "get_user_timezone",
    			description: "Get the caller's timezone",
    			parameters: { type: "object" },
    		},
    	],
    	onClientToolCall: async ({ toolName, input }) => {
    		return runClientTool(toolName, input);
    	},
    });

Think Workflows also improve `step.prompt()`. A prompt step now runs a full agentic turn before returning structured output, so the agent can call tools before producing the typed result. This makes Workflow steps more useful for durable triage, research, and approval flows.

The unified Think execute tool can also include `cdp.*` browser capabilities alongside `state.*` and `tools.*` when Browser Run is bound.

#### Voice output device selection

Voice clients can route assistant audio to a specific output device. Use `outputDeviceId` with `useVoiceAgent`, or call `client.setOutputDevice()` from the framework-agnostic client.
    
    
    const voice = useVoiceAgent({
    	agent: "MyVoiceAgent",
    	outputDeviceId: selectedSpeakerId,
    });
    
    
    const voice = useVoiceAgent({
    	agent: "MyVoiceAgent",
    	outputDeviceId: selectedSpeakerId,
    });

Browsers without speaker-selection support continue playing through the default output device and report a non-fatal `outputDeviceError`.

#### Reliability fixes

This release includes several fixes for production agents:

  * `useAgent` and `AgentClient` handle WebSocket replacement more reliably during reconnects and configuration changes.
  * Chat stream replay is more reliable after reconnects, deploys, and provider errors.
  * Fiber recovery continues across multi-pass scans and backs off when recovery hooks keep failing.
  * Agent teardown continues even when the request that started teardown is canceled.
  * Large session histories use byte-budgeted reads to reduce memory pressure during startup.



#### Upgrade

To update to the latest version:

npmyarnpnpmbun
    
    
    npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest
    
    
    yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest
    
    
    pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest
    
    
    bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest

Refer to the [Code Mode documentation](https://developers.cloudflare.com/agents/tools/codemode/), [Browser tools documentation](https://developers.cloudflare.com/agents/tools/browser/), [Think tools documentation](https://developers.cloudflare.com/agents/harnesses/think/tools/), and [Voice documentation](https://developers.cloudflare.com/agents/communication-channels/voice/) for more information.
