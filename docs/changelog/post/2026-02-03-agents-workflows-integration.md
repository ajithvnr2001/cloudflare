---
url: https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/
title: Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery() \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.477332+00:00
---

# Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery() · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 3, 2026

## Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()

[Agents](https://developers.cloudflare.com/agents/)[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) brings first-class support for [Cloudflare Workflows](https://developers.cloudflare.com/workflows/), synchronous state management, and new scheduling capabilities.

#### Cloudflare Workflows integration

Agents excel at real-time communication and state management. Workflows excel at durable execution. Together, they enable powerful patterns where Agents handle WebSocket connections while Workflows handle long-running tasks, retries, and human-in-the-loop flows.

Use the new `AgentWorkflow` class to define workflows with typed access to your Agent:
    
    
    import { AgentWorkflow } from "agents/workflows";
    
    export class ProcessingWorkflow extends AgentWorkflow {
    	async run(event, step) {
    		// Call Agent methods via RPC
    		await this.agent.updateStatus(event.payload.taskId, "processing");
    
    		// Non-durable: progress reporting to clients
    		await this.reportProgress({ step: "process", percent: 0.5 });
    		this.broadcastToClients({ type: "update", taskId: event.payload.taskId });
    
    		// Durable via step: idempotent, won't repeat on retry
    		await step.mergeAgentState({ taskProgress: 0.5 });
    
    		const result = await step.do("process", async () => {
    			return processData(event.payload.data);
    		});
    
    		await step.reportComplete(result);
    		return result;
    	}
    }
    
    
    import { AgentWorkflow } from "agents/workflows";
    import type { AgentWorkflowEvent, AgentWorkflowStep } from "agents/workflows";
    
    export class ProcessingWorkflow extends AgentWorkflow<MyAgent, TaskParams> {
    	async run(event: AgentWorkflowEvent<TaskParams>, step: AgentWorkflowStep) {
    		// Call Agent methods via RPC
    		await this.agent.updateStatus(event.payload.taskId, "processing");
    
    		// Non-durable: progress reporting to clients
    		await this.reportProgress({ step: "process", percent: 0.5 });
    		this.broadcastToClients({ type: "update", taskId: event.payload.taskId });
    
    		// Durable via step: idempotent, won't repeat on retry
    		await step.mergeAgentState({ taskProgress: 0.5 });
    
    		const result = await step.do("process", async () => {
    			return processData(event.payload.data);
    		});
    
    		await step.reportComplete(result);
    		return result;
    	}
    }

Start workflows from your Agent with `runWorkflow()` and handle lifecycle events:
    
    
    export class MyAgent extends Agent {
    	async startTask(taskId, data) {
    		const instanceId = await this.runWorkflow("PROCESSING_WORKFLOW", {
    			taskId,
    			data,
    		});
    		return { instanceId };
    	}
    
    	async onWorkflowProgress(workflowName, instanceId, progress) {
    		this.broadcast(JSON.stringify({ type: "progress", progress }));
    	}
    
    	async onWorkflowComplete(workflowName, instanceId, result) {
    		console.log(`Workflow ${instanceId} completed`);
    	}
    
    	async onWorkflowError(workflowName, instanceId, error) {
    		console.error(`Workflow ${instanceId} failed:`, error);
    	}
    }
    
    
    export class MyAgent extends Agent {
    	async startTask(taskId: string, data: string) {
    		const instanceId = await this.runWorkflow("PROCESSING_WORKFLOW", {
    			taskId,
    			data,
    		});
    		return { instanceId };
    	}
    
    	async onWorkflowProgress(
    		workflowName: string,
    		instanceId: string,
    		progress: unknown,
    	) {
    		this.broadcast(JSON.stringify({ type: "progress", progress }));
    	}
    
    	async onWorkflowComplete(
    		workflowName: string,
    		instanceId: string,
    		result?: unknown,
    	) {
    		console.log(`Workflow ${instanceId} completed`);
    	}
    
    	async onWorkflowError(
    		workflowName: string,
    		instanceId: string,
    		error: unknown,
    	) {
    		console.error(`Workflow ${instanceId} failed:`, error);
    	}
    }

Key workflow methods on your Agent:

  * `runWorkflow(workflowName, params, options?)` — Start a workflow with optional metadata
  * `getWorkflow(workflowId)` / `getWorkflows(criteria?)` — Query workflows with cursor-based pagination
  * `approveWorkflow(workflowId)` / `rejectWorkflow(workflowId)` — Human-in-the-loop approval flows
  * `pauseWorkflow()`, `resumeWorkflow()`, `terminateWorkflow()` — Workflow control



#### Synchronous setState()

State updates are now synchronous with a new `validateStateChange()` validation hook:
    
    
    export class MyAgent extends Agent {
    	validateStateChange(oldState, newState) {
    		// Return false to reject the change
    		if (newState.count < 0) return false;
    		// Return modified state to transform
    		return { ...newState, lastUpdated: Date.now() };
    	}
    }
    
    
    export class MyAgent extends Agent<Env, State> {
    	validateStateChange(oldState: State, newState: State): State | false {
    		// Return false to reject the change
    		if (newState.count < 0) return false;
    		// Return modified state to transform
    		return { ...newState, lastUpdated: Date.now() };
    	}
    }

#### scheduleEvery() for recurring tasks

The new `scheduleEvery()` method enables fixed-interval recurring tasks with built-in overlap prevention:
    
    
    // Run every 5 minutes
    await this.scheduleEvery("syncData", 5 * 60 * 1000, { source: "api" });
    
    
    // Run every 5 minutes
    await this.scheduleEvery("syncData", 5 * 60 * 1000, { source: "api" });

#### Callable system improvements

  * **Client-side RPC timeout** — Set timeouts on callable method invocations
  * **`StreamingResponse.error(message)`** — Graceful stream error signaling
  * **`getCallableMethods()`** — Introspection API for discovering callable methods
  * **Connection close handling** — Pending calls are automatically rejected on disconnect


    
    
    await agent.call("method", [args], {
    	timeout: 5000,
    	stream: { onChunk, onDone, onError },
    });
    
    
    await agent.call("method", [args], {
    	timeout: 5000,
    	stream: { onChunk, onDone, onError },
    });

#### Email and routing enhancements

**Secure email reply routing** — Email replies are now secured with HMAC-SHA256 signed headers, preventing unauthorized routing of emails to agent instances.

**Routing improvements:**

  * `basePath` option to bypass default URL construction for custom routing
  * Server-sent identity — Agents send `name` and `agent` type on connect
  * New `onIdentity` and `onIdentityChange` callbacks on the client


    
    
    const agent = useAgent({
    	basePath: "user",
    	onIdentity: (name, agentType) => console.log(`Connected to ${name}`),
    });
    
    
    const agent = useAgent({
    	basePath: "user",
    	onIdentity: (name, agentType) => console.log(`Connected to ${name}`),
    });

#### Upgrade

To update to the latest version:
    
    
    npm i agents@latest

For the complete Workflows API reference and patterns, see [Run Workflows](https://developers.cloudflare.com/agents/runtime/execution/run-workflows/).
