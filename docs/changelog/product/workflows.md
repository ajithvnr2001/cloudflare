---
url: https://developers.cloudflare.com/changelog/product/workflows/
title: Workflows Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:59.452141+00:00
---

# Workflows Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/workflows/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 8, 2026

## [Create Workflow instance batches by count or list](https://developers.cloudflare.com/changelog/post/2026-10-08-create-batch-object-form/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

[`createBatch()`](https://developers.cloudflare.com/workflows/build/workers-api/#createbatch) now accepts an options object that creates up to 100 Workflow instances in one call. The result lists the created instances and explains why any others were not created. To use this form in local development and get its types from `wrangler types`, use Wrangler 4.148.0 or later.

To create instances that share the same options, pass `count`. Each instance receives a generated ID:
    
    
    const result = await env.MY_WORKFLOW.createBatch({
    	count: 10,
    	params: { report: "daily" },
    });
    
    
    const result = await env.MY_WORKFLOW.createBatch({
    	count: 10,
    	params: { report: "daily" },
    });

To give each instance its own ID or options, pass `instances`:
    
    
    const { created, errors } = await env.MY_WORKFLOW.createBatch({
    	instances: [
    		{ id: "order-1", params: { orderId: 1 } },
    		{ id: "order-2", params: { orderId: 2 } },
    	],
    });
    
    for (const error of errors) {
    	console.log(error.index, error.id, error.code, error.message);
    }
    
    
    const { created, errors } = await env.MY_WORKFLOW.createBatch({
    	instances: [
    		{ id: "order-1", params: { orderId: 1 } },
    		{ id: "order-2", params: { orderId: 2 } },
    	],
    });
    
    for (const error of errors) {
    	console.log(error.index, error.id, error.code, error.message);
    }

`created` contains the created instances. `errors` contains each entry that was not created, identified by its position in the input. IDs that already exist and IDs repeated within the batch are reported as errors instead of being skipped silently.

Passing an array to `createBatch()` is deprecated. Existing code that uses the array form continues to work.

For more information, refer to [`createBatch`](https://developers.cloudflare.com/workflows/build/workers-api/#createbatch).

Sep 27, 2026

## [Call Workflows declared in `exports` through `ctx.exports`](https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

A Worker can now call the Workflows it declares in the [`exports`](https://developers.cloudflare.com/workers/wrangler/configuration/#workflow-exports) field of its Wrangler configuration through [`ctx.exports`](https://developers.cloudflare.com/workers/runtime-apis/context/#exports). You no longer need a `workflows` binding to call a Workflow from the Worker that defines it.

Each Workflow is keyed by class name, and has the same API as a Workflow binding:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env, ctx) {
    		const instance = await ctx.exports.MyWorkflow.create({
    			params: { name: "World" },
    		});
    		return Response.json({ id: instance.id });
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		const instance = await ctx.exports.MyWorkflow.create({
    			params: { name: "World" },
    		});
    		return Response.json({ id: instance.id });
    	},
    } satisfies ExportedHandler<Env>;

A `workflows` binding and a `workflow` export with the same `name` share their instances. You can move a Workflow from a binding to an export without losing its instances.

`wrangler dev`, the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), and the [Workers Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/) run Workflows on `ctx.exports` locally. Local development requires Wrangler 4.142.0, `@cloudflare/vite-plugin` 1.61.0, or `@cloudflare/vitest-plugin` 1.3.0 or above.

In Vitest, `introspectWorkflow()` and `introspectWorkflowInstance()` still need a Workflow binding. To introspect a Workflow declared in `exports`, add a [test-only binding](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/#introspect-workflows-declared-in-exports) to it.

For more information, refer to [Call a Workflow through `ctx.exports`](https://developers.cloudflare.com/workflows/build/workers-api/#call-a-workflow-through-ctxexports).

Sep 24, 2026

## [Declare Workflows in the `exports` configuration](https://developers.cloudflare.com/changelog/post/2026-09-24-workflow-exports/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

You can now declare the Workflows a Worker defines in the [`exports`](https://developers.cloudflare.com/workers/wrangler/configuration/#workflow-exports) field of your Wrangler configuration file. Previously, a Worker could only define a Workflow through a `workflows` binding, even when the Worker never called the Workflow itself.

Key each entry by the name of the class that extends `WorkflowEntrypoint`:
    
    
    {
    	"exports": {
    		"MyWorkflow": {
    			"type": "workflow",
    			"name": "my-workflow",
    			"limits": {
    				"steps": 25000,
    			},
    			"schedules": ["0 * * * *"],
    		},
    	},
    }
    
    
    [exports.MyWorkflow]
    type = "workflow"
    name = "my-workflow"
    schedules = [ "0 * * * *" ]
    
      [exports.MyWorkflow.limits]
      steps = 25_000

A `workflow` export accepts the same settings as a `workflows` binding: `limits`, `schedules`, and `default_retention`. When you run `wrangler deploy`, Wrangler creates or updates the Workflow with these settings.

You can declare a Workflow as both a binding and an export. Both declarations must use the same class, and cannot set the same setting to different values.

A `workflows` binding to a Workflow in another Worker cannot use the same `name` as a Workflow export in this Worker. Workflow names are unique per account.

Workflow exports require Wrangler 4.139.0 or above.

For more information, refer to [Declare Workflows in `exports`](https://developers.cloudflare.com/workflows/build/workers-api/#declare-workflows-in-exports).

Sep 17, 2026

## [Delete Workflow instances individually or in batches](https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

You can now delete one or up to 100 Workflow instances and their stored state via the [Workflows API](https://developers.cloudflare.com/workflows/build/workers-api/) or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. [Storage billing](https://developers.cloudflare.com/workflows/reference/pricing/#storage-usage) is based on the average daily peak.

Delete one instance by calling [`delete()`](https://developers.cloudflare.com/workflows/build/workers-api/#delete) on its handle:
    
    
    const instance = await env.MY_WORKFLOW.get("instance-abc");
    await instance.delete();

If a Workflow deletes its own instance, execution stops during `await instance.delete()`. Code after the call does not run.

Delete multiple instances by calling [`deleteBatch()`](https://developers.cloudflare.com/workflows/build/workers-api/#deletebatch) on the Workflow binding:
    
    
    const result = await env.MY_WORKFLOW.deleteBatch([
    	"instance-abc",
    	"instance-def",
    ]);
    
    console.log(result.deleted);
    console.log(result.errors);

The batch result contains `{ id }` entries for successful deletions and per-instance errors. IDs that do not exist are returned as errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position.

Wrangler accepts positional instance IDs, a file containing a top-level JSON array of strings, or both, up to 100 IDs total. Use `latest` to delete the most recently created instance. Use `--local` against a local `wrangler dev` session:

instance-ids.jsonjson
    
    
    ["instance-abc", "instance-def"]
    
    
    npx wrangler workflows instances delete my-workflow <INSTANCE_ID>
    npx wrangler workflows instances delete my-workflow <INSTANCE_ID> <INSTANCE_ID>
    npx wrangler workflows instances delete my-workflow latest
    npx wrangler workflows instances delete my-workflow --filename ./instance-ids.json
    npx wrangler workflows instances delete my-workflow <INSTANCE_ID> --local

For more information, refer to [Delete Workflow instances](https://developers.cloudflare.com/workflows/build/trigger-workflows/#delete-workflow-instances), [`delete`](https://developers.cloudflare.com/workflows/build/workers-api/#delete), and [`deleteBatch`](https://developers.cloudflare.com/workflows/build/workers-api/#deletebatch).

Sep 15, 2026

## [Stream Workflow instance events in your Worker or via the API with .subscribe()](https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

You can now stream Workflow instance events via `WorkflowInstance.subscribe()` and the `GET /subscribe` API endpoint. Workers and HTTP clients can react to [workflow](https://developers.cloudflare.com/workflows/build/events-and-parameters/) and [step](https://developers.cloudflare.com/workflows/build/step-context/#workflowstepcontext) events, including attempts, sleeps, waits, and rollbacks, without polling for instance status.

A subscription first streams the entire event history of the Workflow instance. After streaming past events, the subscription waits for new events as the instance runs. You can use `filter` to receive only specific event types or `cursor` to start a subscription at a specific event.

Use `.subscribe()` to update Workflow status in user-facing dashboards, send notifications when steps complete, or trigger follow-up work for specific events.
    
    
    const instance = await env.MY_WORKFLOW.get("report-123");
    
    using subscription = await instance.subscribe();
    
    while (true) {
    	const { value, done } = await subscription.next();
    	if (done) {
    		break;
    	}
    
    	console.log(value.type, value);
    }
    
    
    const instance = await env.MY_WORKFLOW.get("report-123");
    
    using subscription = await instance.subscribe();
    
    while (true) {
    	const { value, done } = await subscription.next();
    	if (done) {
    		break;
    	}
    
    	console.log(value.type, value);
    }

For event types, available fields, and subscription options, refer to [Subscribe to events](https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/).

Sep 10, 2026

## [Default instance retention for new Workflows on Workers Paid is seven days](https://developers.cloudflare.com/changelog/post/2026-09-10-paid-retention-default/)

[Workflows](https://developers.cloudflare.com/workflows/)

[Workflows](https://developers.cloudflare.com/workflows/) created on or after September 10, 2026, on the Workers Paid plan retain completed and errored instance state for seven days by default (previously 30 days). The seven day default helps to reduce storage costs by default. The maximum retention [limit](https://developers.cloudflare.com/workflows/reference/limits/) remains 30 days.

The retention period for existing Workflows is unchanged. The Workers Free plan retains its three-day default and limit.

To set the retention period for a Workflow instance, specify `successRetention`, `errorRetention`, or both:
    
    
    const instance = await env.MY_WORKFLOW.create({
    	retention: {
    		successRetention: "2 days",
    		errorRetention: "30 days",
    	},
    });
    
    
    const instance = await env.MY_WORKFLOW.create({
    	retention: {
    		successRetention: "2 days",
    		errorRetention: "30 days",
    	},
    });

You can also set the retention period per Workflow and per instance in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/workflows).

For retention details, refer to [Workflows pricing](https://developers.cloudflare.com/workflows/reference/pricing/) and the [`WorkflowInstanceCreateOptions` API reference](https://developers.cloudflare.com/workflows/build/workers-api/#workflowinstancecreateoptions).

Aug 4, 2026

## [Build and deploy Artifacts repos on every push](https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/)

[Artifacts](https://developers.cloudflare.com/artifacts/)[Workflows](https://developers.cloudflare.com/workflows/)

You can now run your CI/CD pipeline on your [Artifacts](https://developers.cloudflare.com/artifacts/) repo by defining a CI [Workflow](https://developers.cloudflare.com/workflows/) with the [CI SDK ↗︎](https://github.com/cloudflare/ci), automatically triggered on Artifacts push events.

This allows you to:

  * Automatically build and deploy application code stored in Artifacts.
  * Run linting, type checking, tests, and other checks on every push.
  * Reuse dependencies when the lockfile (i.e. `pnpm-lock.yaml`) has not changed.
  * Stop deployment when a check or build fails.
  * Restrict API token access to the deployment step.
  * Deploy the output to a [Worker](https://developers.cloudflare.com/workers/) or a [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) User Worker.



Define your CI steps with `@cloudflare/ci`. Each `ci.runner()` spins up an isolated sandbox, and the `cache` option reuses installed dependencies across each sandboxed step in your CI job.

Point `cache.inputs` at your lockfile (i.e. `pnpm-lock.yaml`, `bun.lock`), and the install step only runs again when that lockfile changes:

src/index.jsjs
    
    
    const deps = await ci.runner({
    	name: "install",
    	command: "bun install --frozen-lockfile",
    	cache: { inputs: ["package.json", "bun.lock"] },
    });
    
    await Promise.all([
    	deps.runner({ name: "lint", command: "bun run lint" }),
    	deps.runner({ name: "test", command: "bun run test" }),
    	deps.runner({ name: "typecheck", command: "bun run typecheck" }),
    	deps.runner({ name: "build", command: "bun run build" }),
    ]);
    
    await deps.runner({ name: "deploy", command: "bun wrangler deploy" });

src/index.tsts
    
    
    const deps = await ci.runner({
    	name: "install",
    	command: "bun install --frozen-lockfile",
    	cache: { inputs: ["package.json", "bun.lock"] },
    });
    
    await Promise.all([
    	deps.runner({ name: "lint", command: "bun run lint" }),
    	deps.runner({ name: "test", command: "bun run test" }),
    	deps.runner({ name: "typecheck", command: "bun run typecheck" }),
    	deps.runner({ name: "build", command: "bun run build" }),
    ]);
    
    await deps.runner({ name: "deploy", command: "bun wrangler deploy" });

To start the Workflow automatically after each push, add a `cf.artifacts.repo.pushed` trigger to your Wrangler configuration:
    
    
    {
    	"triggers": {
    		"events": [
    			{
    				"type": "cf.artifacts.repo.pushed",
    				"filter": {
    					"namespace": "CI",
    					"repoName": "my-repo",
    				},
    				"target": {
    					"scriptName": "my-ci-worker",
    					"workflowName": "ci-workflow",
    				},
    			},
    		],
    	},
    }
    
    
    [[triggers.events]]
    type = "cf.artifacts.repo.pushed"
    
      [triggers.events.filter]
      namespace = "CI"
      repoName = "my-repo"
    
      [triggers.events.target]
      scriptName = "my-ci-worker"
      workflowName = "ci-workflow"

To learn more, refer to [Build and deploy Artifacts repos](https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/).

Jul 9, 2026

## [Workflows now supports delay functions when retrying](https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/)

[Workflows](https://developers.cloudflare.com/workflows/)

With [Workflows](https://developers.cloudflare.com/workflows/), you can configure built-in retry behavior for each step. Previously, you could configure step retries with fixed delay durations, such as seconds, minutes, or hours, and backoff strategies such as `constant`, `linear`, or `exponential`.

Step retries now support dynamic delay functions. Instead of choosing only a base delay and backoff strategy, pass a function to `retries.delay` and calculate the next delay from the failed attempt and thrown error.

This is useful when retries should depend on the failure. Your Workflow may need to wait longer after a rate-limit error, but retry sooner after a short network failure. The delay function can also accommodate provider guidance if, for example, a downstream API returns a `Retry-After` value in its error messaging.
    
    
    await step.do(
    	"sync customer",
    	{
    		retries: {
    			limit: 5,
    			delay: ({ ctx, error }) => {
    				if (error.message.includes("rate limit")) {
    					return `${ctx.attempt * 30} seconds`;
    				}
    
    				return "10 seconds";
    			},
    		},
    	},
    	async () => {
    		await syncCustomer();
    	},
    );
    
    
    await step.do(
    	"sync customer",
    	{
    		retries: {
    			limit: 5,
    			delay: ({ ctx, error }) => {
    				if (error.message.includes("rate limit")) {
    					return `${ctx.attempt * 30} seconds`;
    				}
    
    				return "10 seconds";
    			},
    		},
    	},
    	async () => {
    		await syncCustomer();
    	},
    );

Dynamic delay functions can return a duration string, a number, or a promise that resolves to a duration. Use them to add adaptive retry behavior without writing separate queue or scheduling logic. For more information, refer to [Sleeping and retrying](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/).

Jul 7, 2026

## [Workflows pricing adds per-step billing. Step and storage billing to start no earlier than August 10, 2026.](https://developers.cloudflare.com/changelog/post/2026-07-07-workflows-billing-updates/)

[Workflows](https://developers.cloudflare.com/workflows/)

[Workflows](https://developers.cloudflare.com/workflows/) pricing now includes per-step billing. Requests and CPU time billing have been enabled since the initial public beta and is not changing.

#### Workflows adds step billing

A step is each unit of work executed by a Workflow, including step operations such as [sleeping](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/) or [waiting for events](https://developers.cloudflare.com/workflows/build/events-and-parameters/).

You can query Workflows analytics, including `stepCount` for a Workflow instance, with the [GraphQL Analytics API](https://developers.cloudflare.com/workflows/observability/metrics-analytics/#query-via-the-graphql-api).

#### Steps and storage billing to take effect August 10th, 2026

Starting no earlier than August 10th, 2026, Cloudflare will begin billing for step and storage usage on Workers Paid plans.

Storage pricing has been published since Workflows became generally available and is not changing. Storage is measured as persisted Workflow state in GB-months.

Dimension | Workers Free | Workers Paid  
---|---|---  
Steps | 3,000 included per day | 500,000 included per month, then $0.80 per additional 100,000 steps  
Storage | 1 GB-month included | 1 GB-month included, then $0.20 per additional GB-month  
  
Developers on the Workers Free plan will not be charged for steps or storage beyond the included amounts.

Cloudflare will not bill step and storage usage before August 10, 2026.

You can review Workflows usage in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) before this change takes effect. To reduce costs, consider reducing the number of steps per Workflow or improving the memory efficiency of your stored state.

Refer to the [Workflows pricing](https://developers.cloudflare.com/workflows/reference/pricing/) page for full details.

Jun 23, 2026

## [Workflows rollback handlers now include step context](https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/)

[Workflows](https://developers.cloudflare.com/workflows/)

[Workflows](https://developers.cloudflare.com/workflows/) makes it easier to build reliable multi-step applications that can recover when downstream systems fail. Rollback handlers now receive the original [step context](https://developers.cloudflare.com/workflows/build/step-context/) via a `ctx` object for the step being rolled back. This includes `ctx.step.name`, `ctx.step.count`, `ctx.attempt`, and the step `config` with defaults applied.

The [step configuration](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstepconfig) includes the retry and timeout settings used for that step, so you can customize your step recovery logic according to those fields.
    
    
    await step.do(
    	"create charge",
    	async () => {
    		const charge = await createCharge();
    		return { chargeId: charge.id };
    	},
    	{
    		rollback: async ({ ctx, output, error }) => {
    			// `output` is the value returned by the step being rolled back.
    			const { chargeId } = output as { chargeId: string };
    			await refundCharge(chargeId, {
    				// `ctx` is the original step context, including step name, count, attempt, and config.
    				reason: `${ctx.step.name}: ${error.message}`,
    			});
    		},
    		rollbackConfig: {
    			// `rollbackConfig` controls retries and timeout for the rollback handler.
    			retries: { limit: 3, delay: "30 seconds", backoff: "linear" },
    			timeout: "5 minutes",
    		},
    	},
    );

Refer to [rollback options](https://developers.cloudflare.com/workflows/build/workers-api/#rollback-options) to learn more.

Jun 5, 2026

## [Rollback support now available in Workflows](https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/)

[Workflows](https://developers.cloudflare.com/workflows/)

[Workflows](https://developers.cloudflare.com/workflows/) now supports saga-style rollbacks, allowing you to add compensating logic to each `step.do()` in case of downstream failures. If the instance fails, the rollback handlers will execute in reverse `step-start` order.

This is useful for multi-step operations that touch external systems, such as inventory reservations, payment authorization, ticket creation, or infrastructure provisioning. Instead of writing all cleanup logic in a top-level `catch`, you can keep each compensating action next to the step it undoes.

Rollback handlers support their own retry and timeout configuration, and Workflows now exposes rollback outcomes in instance status responses. Workflows analytics also emits rollback lifecycle events, making it easier to distinguish a forward execution failure from a rollback failure when debugging production workflows.
    
    
    await step.do(
    	"provision resource",
    	async () => {
    		const resource = await provisionResource();
    		return { resourceId: resource.id };
    	},
    	{
    		rollback: async ({ output }) => {
    			const { resourceId } = output;
    			await deleteResource(resourceId);
    		},
    		rollbackConfig: {
    			retries: { limit: 3, delay: "15 seconds", backoff: "linear" },
    			timeout: "2 minutes",
    		},
    	},
    );
    
    
    await step.do(
    	"provision resource",
    	async () => {
    		const resource = await provisionResource();
    		return { resourceId: resource.id };
    	},
    	{
    		rollback: async ({ output }) => {
    			const { resourceId } = output as { resourceId: string };
    			await deleteResource(resourceId);
    		},
    		rollbackConfig: {
    			retries: { limit: 3, delay: "15 seconds", backoff: "linear" },
    			timeout: "2 minutes",
    		},
    	},
    );

Refer to [rollback options](https://developers.cloudflare.com/workflows/build/workers-api/#rollback-options) to learn more.

Jun 2, 2026

## [Schedule Workflow instances directly from your Workflow binding](https://developers.cloudflare.com/changelog/post/2026-06-02-cron-workflows/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

You can now attach cron schedules directly to a Workflow binding in `wrangler.jsonc`. Each scheduled run creates a new Workflow instance automatically, so you do not need to define a separate Worker with a `scheduled` handler just to trigger your Workflow on an interval.

For example, you can configure hourly, every-15-minute, or weekday schedules on the same Workflow:
    
    
    {
    	"workflows": [
    		{
    			"name": "my-scheduled-workflow",
    			"binding": "MY_WORKFLOW",
    			"class_name": "MyScheduledWorkflow",
    			"schedules": ["0 * * * *", "*/15 * * * *", "0 9 * * MON-FRI"],
    		},
    	],
    }

Cron workloads get all the same benefits of Workflows with built-in retries, multi-step durable execution, and configurable timeouts of Workflows.
    
    
    import {
    	WorkflowEntrypoint,
    	WorkflowEvent,
    	WorkflowStep,
    } from "cloudflare:workers";
    
    // Runs automatically on each cron schedule defined for the MY_WORKFLOW binding in wrangler.jsonc.
    export class MyScheduledWorkflow extends WorkflowEntrypoint<Env> {
    	async run(event: WorkflowEvent, step: WorkflowStep) {
    		const data = await step.do("fetch source data", async () => {
    			return await fetchSourceData();
    		});
    
    		// If this step fails, only this step is retried with the custom logic below
    		await step.do(
    			"process and store results",
    			{
    				retries: { limit: 5, delay: "30 seconds", backoff: "exponential" },
    				timeout: "10 minutes",
    			},
    			async () => {
    				await processAndStore(data);
    			},
    		);
    	}
    }

This makes it easier to build recurring, scheduled jobs such as database backups, invoice generation, report aggregation, and cleanup tasks without wiring up a separate Cron Trigger entrypoint.

For more information, refer to [Trigger Workflows](https://developers.cloudflare.com/workflows/build/trigger-workflows/).

May 1, 2026

## [Run Workflows inside Dynamic Workers with the @cloudflare/dynamic-workflows library](https://developers.cloudflare.com/changelog/post/2026-05-01-dynamic-workflows/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

You can now use [`@cloudflare/dynamic-workflows` ↗︎](https://github.com/cloudflare/dynamic-workflows) to run a [Workflow](https://developers.cloudflare.com/workflows/) inside a [Dynamic Worker](https://developers.cloudflare.com/dynamic-workers/), ensuring durable execution for code that is loaded at runtime.

The Worker Loader loads Dynamic Workers on demand, which previously made durability challenging. Even within a Dynamic Worker, a Workflow might sleep for hours or days between steps, and by the time it resumes, the original Dynamic Worker code would no longer be in memory.

The library solves this by tagging each Workflow instance with metadata that identifies which Dynamic Worker to load — for example, a tenant ID — then reloading the matching Dynamic Worker through the Worker Loader whenever a Workflow awakens.

Because Dynamic Workers are created on-demand, you do not have to register each Workflow up front or manage them individually. Load the Workflow code in the Dynamic Worker when it is needed, and the Workflows engine handles persistence and retries behind the scenes. Your Workflow code itself is unaffected by the routing and behaves as normal.

This unlocks patterns where the Workflow code itself is dynamic. For example, this is useful with:

  * **SaaS platforms** where each tenant defines their own automation, such as onboarding sequences, approval chains, or billing retry logic.
  * **AI agent frameworks** where agents generate and execute multi-step plans at runtime, surviving restarts and waiting for human approval between tool calls.
  * **Multi-tenant job systems** where each customer submits their own processing logic and every step persists progress and retries on failure.


    
    
    import {
    	createDynamicWorkflowEntrypoint,
    	DynamicWorkflowBinding,
    	wrapWorkflowBinding,
    	type WorkflowRunner,
    } from "@cloudflare/dynamic-workflows";
    
    export { DynamicWorkflowBinding };
    
    interface Env {
    	WORKFLOWS: Workflow;
    	LOADER: WorkerLoader;
    }
    
    function loadTenant(env: Env, tenantId: string) {
    	return env.LOADER.get(tenantId, async () => ({
    		compatibilityDate: "2026-01-01",
    		mainModule: "index.js",
    		modules: { "index.js": await fetchTenantCode(tenantId) },
    		// The Dynamic Worker uses this exactly like a real Workflow binding;
    		// every create() is tagged with { tenantId } automatically.
    		env: { WORKFLOWS: wrapWorkflowBinding({ tenantId }) },
    	}));
    }
    
    // The entrypoint name must match `class_name` in the workflows binding of your Wrangler config file.
    export const DynamicWorkflow = createDynamicWorkflowEntrypoint<Env>(
    	async ({ env, metadata }) => {
    		const stub = loadTenant(env, metadata.tenantId as string);
    		return stub.getEntrypoint("TenantWorkflow") as unknown as WorkflowRunner;
    	},
    );
    
    export default {
    	fetch(request: Request, env: Env) {
    		const tenantId = request.headers.get("x-tenant-id")!;
    		return loadTenant(env, tenantId).getEntrypoint().fetch(request);
    	},
    };

For a full walkthrough, refer to the [Dynamic Workflows guide](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/).

Apr 21, 2026

## [Additional step context and ReadableStream support now available in Workflows step.do()](https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/)

[Workflows](https://developers.cloudflare.com/workflows/)

[Workflows](https://developers.cloudflare.com/workflows/) now provides additional context inside `step.do()` callbacks and supports returning `ReadableStream` to handle larger step outputs.

#### Step context properties

The `step.do()` callback receives a context object with new properties [alongside](https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/) `attempt`:

  * **`step.name`** — The name passed to `step.do()`
  * **`step.count`** — How many times a step with that name has been invoked in this instance (1-indexed) 
    * Useful when running the same step in a loop.
  * **`config`** — The resolved step configuration, including `timeout` and `retries` with defaults applied


    
    
    type ResolvedStepConfig = {
    	retries: {
    		limit: number;
    		delay: WorkflowDelayDuration | number;
    		backoff?: "constant" | "linear" | "exponential";
    	};
    	timeout: WorkflowTimeoutDuration | number;
    };
    
    type WorkflowStepContext = {
    	step: {
    		name: string;
    		count: number;
    	};
    	attempt: number;
    	config: ResolvedStepConfig;
    };

#### ReadableStream support in `step.do()`

Steps can now return a `ReadableStream` directly. Although non-stream step outputs are [limited to 1 MiB](https://developers.cloudflare.com/workflows/reference/limits/), streamed outputs support much larger payloads.
    
    
    const largePayload = await step.do("fetch-large-file", async () => {
    	const object = await env.MY_BUCKET.get("large-file.bin");
    	return object.body;
    });

Note that streamed outputs are still considered part of the Workflow instance storage limit.

Apr 15, 2026

## [Increased concurrency, creation rate, and queued instance limits for Workflows instances](https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

[Workflows](https://developers.cloudflare.com/workflows/) limits have been raised to the following:

Limit | Previous | New  
---|---|---  
Concurrent instances (running in parallel) | 10,000 | 50,000  
Instance creation rate (per account) | 100/second per account | 300/second per account, 100/second per workflow  
Queued instances per Workflow 1 | 1 million | 2 million  
  
These increases apply to all users on the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/). Refer to the [Workflows limits documentation](https://developers.cloudflare.com/workflows/reference/limits/) for more details.

#### Footnotes

  1. Queued instances are instances that have been created or awoken and are waiting for a concurrency slot. ↩




Apr 1, 2026

## [All Wrangler commands for Workflows now support local development](https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

All `wrangler workflows` commands now accept a `--local` flag to target a Workflow running in a local `wrangler dev` session instead of the production API.

You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:
    
    
    npx wrangler workflows list --local
    npx wrangler workflows trigger my-workflow --local
    npx wrangler workflows instances list my-workflow --local
    npx wrangler workflows instances pause my-workflow <INSTANCE_ID> --local
    npx wrangler workflows instances send-event my-workflow <INSTANCE_ID> --type my-event --local

All commands also accept `--port` to target a specific `wrangler dev` session (defaults to `8787`).

For more information, refer to [Workflows local development](https://developers.cloudflare.com/workflows/build/local-development/).

Mar 23, 2026

## [Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development](https://developers.cloudflare.com/changelog/post/2026-03-23-local-dev-instance-methods/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Workflow instance methods `pause()`, `resume()`, `restart()`, and `terminate()` are now available in local development when using `wrangler dev`.

You can now test the full Workflow instance lifecycle locally:
    
    
    const instance = await env.MY_WORKFLOW.create({
    	id: "my-instance-id",
    });
    
    await instance.pause(); // pauses a running workflow instance
    await instance.resume(); // resumes a paused instance
    await instance.restart(); // restarts the instance from the beginning
    await instance.terminate(); // terminates the instance immediately

Mar 6, 2026

## [Workflow steps now expose retry attempt number via step context](https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Cloudflare Workflows allows you to configure specific retry logic for each step in your workflow execution. Now, you can access **which** retry attempt is currently executing for calls to `step.do()`:
    
    
    await step.do("my-step", async (ctx) => {
    	// ctx.attempt is 1 on first try, 2 on first retry, etc.
    	console.log(`Attempt ${ctx.attempt}`);
    });

You can use the step context for improved logging & observability, progressive backoff, or conditional logic in your workflow definition.

Note that the current attempt number is 1-indexed. For more information on retry behavior, refer to [Sleeping and Retrying](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/).

Mar 3, 2026

## [Workflows step limit increased to 25,000 steps per instance](https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Each Workflow on Workers Paid now supports 10,000 steps by default, configurable up to 25,000 steps in your `wrangler.jsonc` file:
    
    
    {
    	"workflows": [
    		{
    			"name": "my-workflow",
    			"binding": "MY_WORKFLOW",
    			"class_name": "MyWorkflow",
    			"limits": {
    				"steps": 25000
    			}
    		}
    	]
    }

Previously, each instance was limited to 1,024 steps. Now, Workflows can support more complex, long-running executions without the additional complexity of recursive or child workflow calls.

Note that the maximum persisted state limit per Workflow instance remains **100 MB** for Workers Free and **1 GB** for Workers Paid. Refer to [Workflows limits](https://developers.cloudflare.com/workflows/reference/limits/) for more information.

Feb 4, 2026

## [Visualize your Workflows in the Cloudflare dashboard](https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Cloudflare Workflows now automatically generates visual diagrams from your code

Your Workflow is parsed to provide a visual map of the Workflow structure, allowing you to:

  * Understand how steps connect and execute
  * Visualize loops and nested logic
  * Follow branching paths for conditional logic

![Example diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1927,height=1530,format=webp/_astro/2026-02-03-workflows-diagram.BfQAnWL3.png)

You can collapse loops and nested logic to see the high-level flow, or expand them to see every step.

Workflow diagrams are available in beta for all JavaScript and TypeScript Workflows. Find your Workflows in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/workflows) to see their diagrams.

Feb 3, 2026

## [Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()](https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/)

[Agents](https://developers.cloudflare.com/agents/)[Workflows](https://developers.cloudflare.com/workflows/)

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

Oct 31, 2025

## [Increased Workflows instance and concurrency limits](https://developers.cloudflare.com/changelog/post/2025-10-28-raising-limits/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

We've raised the [Cloudflare Workflows](https://developers.cloudflare.com/workflows/) account-level limits for all accounts on the [Workers paid plan](https://developers.cloudflare.com/workers/platform/pricing/):

  * **Instance creation rate** increased from 100 workflow instances per 10 seconds to 100 instances per second
  * **Concurrency limit** increased from 4,500 to 10,000 workflow instances per account



These increases mean you can create new instances up to 10x faster, and have more workflow instances concurrently executing. To learn more and get started with Workflows, refer to [the getting started guide](https://developers.cloudflare.com/workflows/get-started/guide/).

If your application requires a higher limit, fill out the [Limit Increase Request Form](https://developers.cloudflare.com/workers/platform/limits/) or contact your account team. Please refer to [Workflows pricing](https://developers.cloudflare.com/workflows/reference/pricing/) for more information.

Aug 22, 2025

## [Build durable multi-step applications in Python with Workflows (now in beta)](https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

You can now build [Workflows](https://developers.cloudflare.com/workflows/) using Python. With Python Workflows, you get automatic retries, state persistence, and the ability to run multi-step operations that can span minutes, hours, or weeks using Python’s familiar syntax and the [Python Workers](https://developers.cloudflare.com/workers/languages/python/) runtime.

Python Workflows use the same step-based execution model as JavaScript Workflows, but with Python syntax and access to Python’s ecosystem. Python Workflows also enable [DAG (Directed Acyclic Graph) workflows](https://developers.cloudflare.com/workflows/python/dag/), where you can define complex dependencies between steps using the depends parameter.

Here’s a simple example:
    
    
    from workers import Response, WorkflowEntrypoint
    
    class PythonWorkflowStarter(WorkflowEntrypoint):
        async def run(self, event, step):
            @step.do("my first step")
            async def my_first_step():
                # do some work
                return "Hello Python!"
    
            await my_first_step()
    
            await step.sleep("my-sleep-step", "10 seconds")
    
            @step.do("my second step")
            async def my_second_step():
                # do some more work
                return "Hello again!"
    
            await my_second_step()
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            await self.env.MY_WORKFLOW.create()
            return Response("Hello Workflow creation!")

Note

Python Workflows requires a `compatibility_date = "2025-08-01"`, or lower, in your wrangler toml file.

Python Workflows support the same core capabilities as JavaScript Workflows, including sleep scheduling, event-driven workflows, and built-in error handling with configurable retry policies.

To learn more and get started, refer to [Python Workflows documentation](https://developers.cloudflare.com/workflows/python/).

Jun 25, 2025

## [Run AI-generated code on-demand with Code Sandboxes (new)](https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)[Workflows](https://developers.cloudflare.com/workflows/)

AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing [Sandboxes ↗︎](https://www.npmjs.com/package/@cloudflare/sandbox), which let your Worker run actual processes in a secure, container-based environment.
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    		return sandbox.exec("ls", ["-la"]);
    	},
    };

#### Methods

  * `exec(command: string, args: string[], options?: { stream?: boolean })`:Execute a command in the sandbox.
  * `gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })`: Checkout a git repository in the sandbox.
  * `mkdir(path: string, options: { recursive?: boolean; stream?: boolean })`: Create a directory in the sandbox.
  * `writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })`: Write content to a file in the sandbox.
  * `readFile(path: string, options: { encoding?: string; stream?: boolean })`: Read content from a file in the sandbox.
  * `deleteFile(path: string, options?: { stream?: boolean })`: Delete a file from the sandbox.
  * `renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })`: Rename a file in the sandbox.
  * `moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })`: Move a file from one location to another in the sandbox.
  * `ping()`: Ping the sandbox.



Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.

You can try it today from your Worker, with just a few lines of code. Let us know what you build.

Apr 7, 2025

## [Workflows is now Generally Available](https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

[Workflows](https://developers.cloudflare.com/workflows/) is now _Generally Available_ (or "GA"): in short, it's ready for production workloads. Alongside marking Workflows as GA, we've introduced a number of changes during the beta period, including:

  * A new `waitForEvent` API that allows a Workflow to wait for an event to occur before continuing execution.
  * Increased concurrency: you can [run up to 4,500 Workflow instances](https://developers.cloudflare.com/changelog/2025-02-25-workflows-concurrency-increased/) concurrently — and this will continue to grow.
  * Improved observability, including new CPU time metrics that allow you to better understand which Workflow instances are consuming the most resources and/or contributing to your bill.
  * Support for `vitest` for testing Workflows locally and in CI/CD pipelines.



Workflows also supports the new [increased CPU limits](https://developers.cloudflare.com/changelog/2025-03-25-higher-cpu-limits/) that apply to Workers, allowing you to run more CPU-intensive tasks (up to 5 minutes of CPU time per instance), not including the time spent waiting on network calls, AI models, or other I/O bound tasks.

#### Human-in-the-loop

The new `step.waitForEvent` API allows a Workflow instance to wait on events and data, enabling human-in-the-the-loop interactions, such as approving or rejecting a request, directly handling webhooks from other systems, or pushing event data to a Workflow while it's running.

Because Workflows are just code, you can conditionally execute code based on the result of a `waitForEvent` call, and/or call `waitForEvent` multiple times in a single Workflow based on what the Workflow needs.

For example, if you wanted to implement a human-in-the-loop approval process, you could use `waitForEvent` to wait for a user to approve or reject a request, and then conditionally execute code based on the result.
    
    
    import {
    	WorkflowEntrypoint,
    	WorkflowStep,
    	WorkflowEvent,
    } from "cloudflare:workers";
    
    export class MyWorkflow extends WorkflowEntrypoint {
    	async run(event, step) {
    		// Other steps in your Workflow
    		let stripeEvent = await step.waitForEvent(
    			"receive invoice paid webhook from Stripe",
    			{ type: "stripe-webhook", timeout: "1 hour" },
    		);
    		// Rest of your Workflow
    	}
    }
    
    
    import { WorkflowEntrypoint, WorkflowStep, WorkflowEvent } from "cloudflare:workers";
    
    export class MyWorkflow extends WorkflowEntrypoint<Env, Params> {
    	async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
    		// Other steps in your Workflow
    		let stripeEvent = await step.waitForEvent<IncomingStripeWebhook>("receive invoice paid webhook from Stripe", { type: "stripe-webhook", timeout: "1 hour" })
    		// Rest of your Workflow
    	}
    }

You can then send a Workflow an event from an external service via HTTP or from within a Worker using the [Workers API](https://developers.cloudflare.com/workflows/build/workers-api/) for Workflows:
    
    
    export default {
    	async fetch(req, env) {
    		const instanceId = new URL(req.url).searchParams.get("instanceId");
    		const webhookPayload = await req.json();
    
    		let instance = await env.MY_WORKFLOW.get(instanceId);
    		// Send our event, with `type` matching the event type defined in
    		// our step.waitForEvent call
    		await instance.sendEvent({
    			type: "stripe-webhook",
    			payload: webhookPayload,
    		});
    
    		return Response.json({
    			status: await instance.status(),
    		});
    	},
    };
    
    
    export default {
      async fetch(req: Request, env: Env) {
        const instanceId = new URL(req.url).searchParams.get("instanceId")
        const webhookPayload = await req.json<Payload>()
    
        let instance = await env.MY_WORKFLOW.get(instanceId);
        // Send our event, with `type` matching the event type defined in
        // our step.waitForEvent call
        await instance.sendEvent({type: "stripe-webhook", payload: webhookPayload})
    
        return Response.json({
          status: await instance.status(),
        });
      },
    };

Read the [GA announcement blog ↗︎](https://blog.cloudflare.com/workflows-is-now-generally-available/) to learn more about what landed as part of the Workflows GA.

← Prev

1[2](https://developers.cloudflare.com/changelog/product/workflows/2/)

[Next →](https://developers.cloudflare.com/changelog/product/workflows/2/)
