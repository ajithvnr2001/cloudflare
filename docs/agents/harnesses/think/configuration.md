---
url: https://developers.cloudflare.com/agents/harnesses/think/configuration/
title: Configuration \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:12.726672+00:00
---

# Configuration · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/think/configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Harnesses](https://developers.cloudflare.com/agents/harnesses/)

  4. /[Think](https://developers.cloudflare.com/agents/harnesses/think/)
  5. /Configuration



# Configuration

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/harnesses/think/configuration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfiguration overridesDynamic configurationSession integrationPackage exportsDependencies

Think is configured by overriding methods and properties on your `Think` subclass. Most agents only override `getModel()`.

## Configuration overrides

Method / Property | Default | Description  
---|---|---  
`getModel()` | throws | Return the `LanguageModel` to use  
`getSystemPrompt()` | `"You are a helpful assistant."` | System prompt (fallback when no context blocks)  
`getTools()` | `{}` | AI SDK `ToolSet` for the agentic loop  
`getScheduledTasks()` | `{}` | Code-declared recurring prompts or handlers — refer to [Scheduled tasks](https://developers.cloudflare.com/agents/harnesses/think/scheduled-tasks/)  
`getDefaultTimezone()` | `undefined` | Default timezone for wall-clock scheduled tasks  
`getMessengers()` | `{}` | Messenger ingress and delivery declarations — refer to [Messengers](https://developers.cloudflare.com/agents/harnesses/think/messengers/)  
`maxSteps` | `10` | Max tool-call rounds per turn  
`sendReasoning` | `true` | Send reasoning chunks to chat clients  
`configureSession()` | identity | Add context blocks, compaction, search, skills — refer to [Sessions](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/)  
`getSkills()` | `[]` | Return Agent Skills sources for on-demand skill activation — refer to [Agent Skills](https://developers.cloudflare.com/agents/runtime/execution/agent-skills/)  
`getSkillScriptRunner()` | `null` | Enable the optional `run_skill_script` tool  
`workspaceBash` | `true` | Include or configure the default workspace `bash` tool — refer to [Tools](https://developers.cloudflare.com/agents/harnesses/think/tools/)  
`messageConcurrency` | `"queue"` | How overlapping submits behave — refer to [Client tools](https://developers.cloudflare.com/agents/harnesses/think/client-tools/#message-concurrency)  
`includeMcpTools` | `true` | Convert connected MCP tools to AI SDK tools and add them to model turns. Refer to [MCP tools](https://developers.cloudflare.com/agents/harnesses/think/tools/#mcp-tools)  
`waitForMcpConnections` | `false` | Wait for MCP servers before inference  
`chatRecovery` | Always on | Durable recovery configuration. Refer to [Durable recovery](https://developers.cloudflare.com/agents/harnesses/think/recovery/) for all options and defaults  
`chatStreamStallTimeoutMs` | `0` (off) | Opt-in inactivity watchdog: abort a turn whose model stream produces no chunk for this long (measures the gap between chunks, including tool execution). A stall routes into bounded recovery  
`contextOverflow` | `undefined` | Opt-in mid-turn context-overflow handling with `reactive`, `maxRetries`, and `proactive` options. Requires `classifyChatError` plus a session compaction function — refer to [Context-window overflow recovery](https://developers.cloudflare.com/agents/harnesses/think/recovery/#context-window-overflow-recovery)  
  
For `chatRecovery` and `chatStreamStallTimeoutMs` behavior, refer to [Durable recovery](https://developers.cloudflare.com/agents/harnesses/think/recovery/).

## Dynamic configuration

Think's class generics match `Agent<Env, State, Props>`. Persisted runtime configuration is typed at the `configure<T>()` and `getConfig<T>()` call sites, stored in SQLite, and survives hibernation and restarts.
    
    
    export class MyAgent extends Think {
    	getModel() {
    		const tier = this.getConfig()?.modelTier ?? "fast";
    		const models = {
    			fast: "@cf/moonshotai/kimi-k2.6",
    			capable: "@cf/meta/llama-4-scout-17b-16e-instruct",
    		};
    		return createWorkersAI({ binding: this.env.AI })(models[tier]);
    	}
    }
    
    
    type MyConfig = { modelTier: "fast" | "capable"; theme: string };
    
    export class MyAgent extends Think<Env> {
    	getModel() {
    		const tier = this.getConfig<MyConfig>()?.modelTier ?? "fast";
    		const models = {
    			fast: "@cf/moonshotai/kimi-k2.6",
    			capable: "@cf/meta/llama-4-scout-17b-16e-instruct",
    		};
    		return createWorkersAI({ binding: this.env.AI })(models[tier]);
    	}
    }

Method | Description  
---|---  
`configure<T>(config: T)` | Persist a typed configuration object  
`getConfig<T>(): T | null` | Read the persisted configuration, or null if never configured  
  
Expose configuration to the client via `@callable`:
    
    
    import { callable } from "agents";
    
    export class MyAgent extends Think {
    	getModel() {
    		/* ... */
    	}
    
    	@callable()
    	updateConfig(config) {
    		this.configure(config);
    	}
    }
    
    
    import { callable } from "agents";
    
    export class MyAgent extends Think<Env> {
    	getModel() {
    		/* ... */
    	}
    
    	@callable()
    	updateConfig(config: MyConfig) {
    		this.configure<MyConfig>(config);
    	}
    }

## Session integration

Think stores conversations in a [Session](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/) — the storage layer that holds your messages and gives the model writable memory. Two concepts come up here: **context blocks** are labelled sections of the system prompt the model can read and update (for example, a `memory` block of facts about the user), and **compaction** summarizes older messages so long conversations stay within the model's context window. Override `configureSession` to add persistent memory, compaction, search, and skills:
    
    
    import { Think, Session } from "@cloudflare/think";
    
    export class MyAgent extends Think {
    	getModel() {
    		/* ... */
    	}
    
    	configureSession(session) {
    		return session
    			.withContext("soul", {
    				provider: { get: async () => "You are a helpful coding assistant." },
    			})
    			.withContext("memory", {
    				description: "Important facts learned during conversation.",
    				maxTokens: 2000,
    			})
    			.withCachedPrompt();
    	}
    }
    
    
    import { Think, Session } from "@cloudflare/think";
    
    export class MyAgent extends Think<Env> {
    	getModel() {
    		/* ... */
    	}
    
    	configureSession(session: Session) {
    		return session
    			.withContext("soul", {
    				provider: { get: async () => "You are a helpful coding assistant." },
    			})
    			.withContext("memory", {
    				description: "Important facts learned during conversation.",
    				maxTokens: 2000,
    			})
    			.withCachedPrompt();
    	}
    }

When `configureSession` adds context blocks, Think builds the system prompt from those blocks instead of using `getSystemPrompt()`. Think's `this.messages` getter reads directly from Session's tree-structured storage.

For the full Session API — context blocks, compaction, search, skills, and multi-session support — refer to the [Sessions documentation](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/).

## Package exports

Export | Description  
---|---  
`@cloudflare/think` | `Think`, `Session`, `Workspace`, `skills` namespace  
`@cloudflare/think/messengers` | Messenger contracts, Chat SDK bridge, state agent, delivery  
`@cloudflare/think/messengers/telegram` | Telegram messenger provider and delivery helpers  
`@cloudflare/think/workflows` | `ThinkWorkflow`, `step.prompt()` — Workflow prompts  
`@cloudflare/think/tools/workspace` | `createWorkspaceTools()` — for custom storage backends  
`@cloudflare/think/tools/execute` | `createExecuteTool()` — sandboxed code execution via Code Mode  
`@cloudflare/think/tools/browser` | `createBrowserTools()` — Chrome DevTools Protocol tools  
`@cloudflare/think/tools/extensions` | `createExtensionTools()` — LLM-driven extension loading  
`@cloudflare/think/extensions` | `ExtensionManager`, `HostBridgeLoopback` — extension runtime  
  
## Dependencies

Peer dependencies you provide:

Package | Required | Notes  
---|---|---  
`agents` | yes | Cloudflare Agents SDK  
`ai` | yes | AI SDK v6  
`zod` | yes | Schema validation (v4)  
`@chat-adapter/telegram` | optional | Required for Telegram messengers  
  
Bundled with `@cloudflare/think`:

Package | Notes  
---|---  
`@cloudflare/shell` | `Workspace` filesystem  
`@cloudflare/codemode` | Code execution for `createExecuteTool()`  
`just-bash` | Sandboxed shell for the default workspace `bash` tool  
  
The Agent Skills engine and its script runner live in [`agents/skills`](https://developers.cloudflare.com/agents/runtime/execution/agent-skills/), so skill scripts pull `@cloudflare/worker-bundler` and `just-bash` through `agents`, not Think.

[PreviousGetting started](https://developers.cloudflare.com/agents/harnesses/think/getting-started/)[NextTools](https://developers.cloudflare.com/agents/harnesses/think/tools/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/think/configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
