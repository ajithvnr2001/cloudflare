---
url: https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/
title: Interact with Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:57.464171+00:00
---

# Interact with Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)

  4. /[Integration test harness](https://developers.cloudflare.com/workers/testing/test-harness/)
  5. /Interact with Workers



# Interact with Workers

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTest route dispatch across WorkersInteract with a specific WorkerAssert logged behaviorInspect and control Workflow execution

Use the test harness to send requests through configured routes or target a specific Worker directly. You can also dispatch events like scheduled events.

## Test route dispatch across Workers

When a test harness runs multiple Workers, add each Worker to the `workers` array. The first Worker is the primary Worker. `server.fetch()` sends relative URLs to the primary Worker and matches absolute URLs against configured routes. If no route matches, it falls back to the primary Worker:
    
    
    const server = createTestHarness({
    	workers: [
    		/** Includes `"routes": ["example.com/*"]` */
    		{ configPath: "./workers/web/wrangler.jsonc" },
    		/** Includes `"routes": ["api.example.com/v1/*"]` */
    		{ configPath: "./workers/api/wrangler.jsonc" },
    	],
    });
    
    const primaryResponse = await server.fetch("/");
    const apiResponse = await server.fetch("http://api.example.com/v1/users/123");
    const webResponse = await server.fetch("http://example.com/users/123");
    
    
    const server = createTestHarness({
    	workers: [
    		/** Includes `"routes": ["example.com/*"]` */
    		{ configPath: "./workers/web/wrangler.jsonc" },
    		/** Includes `"routes": ["api.example.com/v1/*"]` */
    		{ configPath: "./workers/api/wrangler.jsonc" },
    	],
    });
    
    const primaryResponse = await server.fetch("/");
    const apiResponse = await server.fetch("http://api.example.com/v1/users/123");
    const webResponse = await server.fetch("http://example.com/users/123");

## Interact with a specific Worker

Route dispatch tests the application boundary, but some tests might want to target one Worker or trigger other event handlers. Use `server.getWorker(name)` to bypass route matching and get a handle for that Worker.

You can then use this Worker handle to send requests directly or dispatch other events, such as `scheduled()`:
    
    
    const apiWorker = server.getWorker("api-worker");
    const response = await apiWorker.fetch("http://api.example.com/v1/users/123");
    
    await apiWorker.scheduled({
    	cron: "0 0 * * *",
    	scheduledTime: new Date(),
    });
    
    
    const apiWorker = server.getWorker("api-worker");
    const response = await apiWorker.fetch("http://api.example.com/v1/users/123");
    
    await apiWorker.scheduled({
    	cron: "0 0 * * *",
    	scheduledTime: new Date(),
    });

## Assert logged behavior

The test harness captures logs from the Workers runtime. To assert that a Worker logged a specific message, use `server.getLogs()` to retrieve the log entries.

Captured logs are reset when you call `server.reset()`. You can also call `server.clearLogs()` to isolate logs before and after a specific action:
    
    
    test("logs scheduled job results", async ({ expect }) => {
    	const apiWorker = server.getWorker("api-worker");
    
    	await apiWorker.scheduled({
    		cron: "0 0 * * *",
    		scheduledTime: new Date("2026-05-29T00:00:00.000Z"),
    	});
    
    	expect(server.getLogs()).toEqual([
    		expect.objectContaining({
    			level: "info",
    			message: "Generated daily report for 2026-05-29",
    		}),
    	]);
    
    	server.clearLogs();
    
    	await apiWorker.scheduled({
    		cron: "0 0 * * *",
    		scheduledTime: new Date("2026-05-30T00:00:00.000Z"),
    	});
    
    	expect(server.getLogs()).toEqual([
    		expect.objectContaining({
    			level: "info",
    			message: "Generated daily report for 2026-05-30",
    		}),
    	]);
    });
    
    
    test("logs scheduled job results", async ({ expect }) => {
    	const apiWorker = server.getWorker("api-worker");
    
    	await apiWorker.scheduled({
    		cron: "0 0 * * *",
    		scheduledTime: new Date("2026-05-29T00:00:00.000Z"),
    	});
    
    	expect(server.getLogs()).toEqual([
    		expect.objectContaining({
    			level: "info",
    			message: "Generated daily report for 2026-05-29",
    		}),
    	]);
    
    	server.clearLogs();
    
    	await apiWorker.scheduled({
    		cron: "0 0 * * *",
    		scheduledTime: new Date("2026-05-30T00:00:00.000Z"),
    	});
    
    	expect(server.getLogs()).toEqual([
    		expect.objectContaining({
    			level: "info",
    			message: "Generated daily report for 2026-05-30",
    		}),
    	]);
    });

## Inspect and control Workflow execution

If your Worker starts a Workflow, you can use `worker.introspectWorkflow(bindingName)` to control new instances and inspect their state.
    
    
    const worker = server.getWorker("api-worker");
    await using workflow = await worker.introspectWorkflow("MY_WORKFLOW");
    
    await workflow.modifyAll(async (modifier) => {
    	await modifier.disableSleeps([{ name: "wait-for-approval" }]);
    });
    
    await worker.fetch("/start-workflow");
    
    const [instance] = await workflow.get();
    await instance.waitForStatus("complete");
    expect(await instance.getOutput()).toEqual({ approved: true });
    
    
    const worker = server.getWorker<ApiEnv>("api-worker");
    await using workflow = await worker.introspectWorkflow("MY_WORKFLOW");
    
    await workflow.modifyAll(async (modifier) => {
    	await modifier.disableSleeps([{ name: "wait-for-approval" }]);
    });
    
    await worker.fetch("/start-workflow");
    
    const [instance] = await workflow.get();
    await instance.waitForStatus("complete");
    expect(await instance.getOutput()).toEqual({ approved: true });

If the test already knows the instance ID, you can also introspect that instance directly with `worker.introspectWorkflowInstance(bindingName, instanceId)`.
    
    
    const instance = await worker.introspectWorkflowInstance(
    	"MY_WORKFLOW",
    	"instance-id",
    );
    
    await instance.modify(async (modifier) => {
    	await modifier.mockStepResult({ name: "load-user" }, { id: "123" });
    });
    
    await instance.waitForStatus("complete");
    
    
    const instance = await worker.introspectWorkflowInstance(
    	"MY_WORKFLOW",
    	"instance-id",
    );
    
    await instance.modify(async (modifier) => {
    	await modifier.mockStepResult({ name: "load-user" }, { id: "123" });
    });
    
    await instance.waitForStatus("complete");

[PreviousPrepare test state](https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/)[NextIntegrations](https://developers.cloudflare.com/workers/testing/test-harness/integrations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/test-harness/interact-with-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
