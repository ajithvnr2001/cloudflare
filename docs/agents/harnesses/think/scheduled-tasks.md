---
url: https://developers.cloudflare.com/agents/harnesses/think/scheduled-tasks/
title: Scheduled tasks \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:13.499592+00:00
---

# Scheduled tasks · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/think/scheduled-tasks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Harnesses](https://developers.cloudflare.com/agents/harnesses/)

  4. /[Think](https://developers.cloudflare.com/agents/harnesses/think/)
  5. /Scheduled tasks



# Scheduled tasks

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/harnesses/think/scheduled-tasks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use a workflow instead

Use `getScheduledTasks()` when code should create recurring Think turns or deterministic scheduled handlers. Think reconciles the declarations on startup, stores a durable one-shot schedule for the next occurrence, and re-arms the next occurrence after each run.
    
    
    import { Think, defineScheduledTasks } from "@cloudflare/think";
    
    export class DigestAgent extends Think {
    	getDefaultTimezone() {
    		return "Europe/London";
    	}
    
    	getScheduledTasks() {
    		return defineScheduledTasks({
    			weeklyCommitReport: {
    				schedule: "every week on monday at 09:00",
    				prompt:
    					"Compile all my GitHub commits for the last week and send a concise summary.",
    			},
    			workout: {
    				schedule: "every day at 08:00 in Europe/London",
    				prompt: "Start my workout.",
    			},
    			customerDigest: {
    				schedule: "every day at 09:00",
    				timezone: "America/New_York",
    				metadata: { workflowName: "customer-digest" },
    				retry: { maxAttempts: 3 },
    				handler: async ({
    					idempotencyKey,
    					scheduledFor,
    					scheduleKind,
    					timezone,
    				}) => {
    					await this.env.DIGEST_WORKFLOW.create({
    						id: idempotencyKey,
    						params: { scheduledFor, scheduleKind, timezone },
    					});
    				},
    			},
    		});
    	}
    }
    
    
    import { Think, defineScheduledTasks } from "@cloudflare/think";
    
    export class DigestAgent extends Think<Env> {
    	getDefaultTimezone() {
    		return "Europe/London";
    	}
    
    	getScheduledTasks() {
    		return defineScheduledTasks({
    			weeklyCommitReport: {
    				schedule: "every week on monday at 09:00",
    				prompt:
    					"Compile all my GitHub commits for the last week and send a concise summary.",
    			},
    			workout: {
    				schedule: "every day at 08:00 in Europe/London",
    				prompt: "Start my workout.",
    			},
    			customerDigest: {
    				schedule: "every day at 09:00",
    				timezone: "America/New_York",
    				metadata: { workflowName: "customer-digest" },
    				retry: { maxAttempts: 3 },
    				handler: async ({
    					idempotencyKey,
    					scheduledFor,
    					scheduleKind,
    					timezone,
    				}) => {
    					await this.env.DIGEST_WORKFLOW.create({
    						id: idempotencyKey,
    						params: { scheduledFor, scheduleKind, timezone },
    					});
    				},
    			},
    		});
    	}
    }

The DSL supports `every <n> minutes`, `every <n> hours`, `every day at HH:mm`, `every weekday at HH:mm`, and `every week on monday,wednesday at HH:mm`. Wall-clock schedules require either an inline timezone, a task `timezone`, or `getDefaultTimezone()`. If an alarm is late, Think runs the intended occurrence once and schedules the next future occurrence; it does not backfill missed runs.

Each task must define exactly one of `prompt` or `handler`. Prompt tasks create a durable submission with [`submitMessages()`](https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/). Handler tasks receive `{ taskId, scheduledFor, scheduledForDate, occurrenceKey, idempotencyKey, schedule, scheduleKind, timezone, metadata }` and are intended for app-owned work such as creating a Workflow run or writing a run ledger. Delivery is at-least-once; use `idempotencyKey` or `occurrenceKey` for your own durable idempotency.

Static declarations reconcile on startup. If `getScheduledTasks()` reads product-owned data that can change while the Durable Object is live, call `internal_reconcileScheduledTasks()` after updating that data. During reconciliation Think records the task row before creating the underlying Agent schedule, so a missing `schedule_id` is only a pending reconcile state and is repaired on the next reconcile. The task `retry` option retries the prompt or handler action before the failure is logged. The next occurrence is still scheduled after the action succeeds or exhausts its retries, so failed occurrences do not block future runs.

## When to use a workflow instead

For a recurring job whose steps matter — multiple deterministic steps, long waits, or human approval — use a handler task to create a [Think Workflow](https://developers.cloudflare.com/agents/harnesses/think/workflows/) run. Keep simple recurring prompts as prompt tasks, and keep one-off background turns on [`submitMessages()`](https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/).

[PreviousChannels](https://developers.cloudflare.com/agents/harnesses/think/channels/)[NextWorkflows](https://developers.cloudflare.com/agents/harnesses/think/workflows/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/think/scheduled-tasks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
