---
url: https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/
title: Programmatic submissions \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:13.340414+00:00
---

# Programmatic submissions · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Harnesses](https://developers.cloudflare.com/agents/harnesses/)

  4. /[Think](https://developers.cloudflare.com/agents/harnesses/think/)
  5. /Programmatic submissions



# Programmatic submissions

Last updated Jun 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewsubmitMessagesSubmission statusesIdempotent retriesInspect, list, cancel, and deleteSession behaviorCompared with Workflows

Durably accept a Think turn and return before inference runs. Use `submitMessages()` for webhook handlers, RPC callers, and parent Workers that need a fast acknowledgement, safe retry, and later status inspection.

Declarative [scheduled prompt tasks](https://developers.cloudflare.com/agents/harnesses/think/scheduled-tasks/) use the same durable submission path under the hood. Use `getScheduledTasks()` when the trigger is recurring and code-declared; use `submitMessages()` directly when an external caller or webhook creates one-off work. To wait for the response inline, use [`saveMessages()`](https://developers.cloudflare.com/agents/harnesses/think/sub-agents/#savemessages) instead.

## submitMessages
    
    
    async submitMessages(
    	messages: UIMessage[],
    	options?: {
    		submissionId?: string;
    		idempotencyKey?: string;
    		metadata?: Record<string, unknown>;
    	},
    ): Promise<SubmitMessagesResult>

`submitMessages()` accepts serializable `UIMessage[]` values. It does not accept the function form supported by `saveMessages((messages) => ...)`, because durable submissions persist work before execution and cannot store closures. The array must contain at least one message.
    
    
    const submission = await this.submitMessages(
    	[
    		{
    			id: crypto.randomUUID(),
    			role: "user",
    			parts: [{ type: "text", text: "Process webhook event 123" }],
    		},
    	],
    	{ idempotencyKey: "webhook-event-123" },
    );
    
    return Response.json({
    	submissionId: submission.submissionId,
    	status: submission.status,
    	accepted: submission.accepted,
    });
    
    
    const submission = await this.submitMessages(
    	[
    		{
    			id: crypto.randomUUID(),
    			role: "user",
    			parts: [{ type: "text", text: "Process webhook event 123" }],
    		},
    	],
    	{ idempotencyKey: "webhook-event-123" },
    );
    
    return Response.json({
    	submissionId: submission.submissionId,
    	status: submission.status,
    	accepted: submission.accepted,
    });

## Submission statuses

Status | Meaning  
---|---  
`pending` | Accepted and waiting for its turn  
`running` | Claimed by the agent and executing  
`completed` | The Think turn completed successfully  
`aborted` | The submission was cancelled  
`skipped` | Turn state was reset before the submission ran  
`error` | Execution failed or recovery was unsafe  
  
## Idempotent retries

Pass an `idempotencyKey` from your external system. Retrying with the same key returns the existing submission with `accepted: false` instead of inserting duplicate messages:
    
    
    const first = await this.submitMessages(messages, {
    	idempotencyKey: payload.id,
    });
    
    const retry = await this.submitMessages(messages, {
    	idempotencyKey: payload.id,
    });
    
    console.log(first.submissionId === retry.submissionId); // true
    console.log(retry.accepted); // false
    
    
    const first = await this.submitMessages(messages, {
    	idempotencyKey: payload.id,
    });
    
    const retry = await this.submitMessages(messages, {
    	idempotencyKey: payload.id,
    });
    
    console.log(first.submissionId === retry.submissionId); // true
    console.log(retry.accepted); // false

If you pass both `submissionId` and `idempotencyKey`, they must identify the same submission. If they point at different existing submissions, `submitMessages()` throws.

## Inspect, list, cancel, and delete

Use the submission APIs to inspect active work, cancel a durable submission, and clean up terminal records:
    
    
    const current = await this.inspectSubmission(submission.submissionId);
    
    const active = await this.listSubmissions({
    	status: ["pending", "running"],
    });
    
    await this.cancelSubmission(submission.submissionId, "No longer needed");
    
    await this.deleteSubmissions({
    	status: ["completed", "error", "aborted"],
    	completedBefore: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000),
    });
    
    
    const current = await this.inspectSubmission(submission.submissionId);
    
    const active = await this.listSubmissions({
    	status: ["pending", "running"],
    });
    
    await this.cancelSubmission(submission.submissionId, "No longer needed");
    
    await this.deleteSubmissions({
    	status: ["completed", "error", "aborted"],
    	completedBefore: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000),
    });

Use `cancelSubmission(submissionId)` for durable cancellation across Worker and Durable Object RPC boundaries. Use `AbortSignal` with `saveMessages()` or `continueLastTurn()` only when the caller creates the signal inside the Durable Object that runs the turn.

## Session behavior

Think stores accepted submissions in a submission ledger first. It appends submitted messages to the conversation Session only when the submission starts executing. Later accepted submissions are not visible to the model until their own turn starts, which preserves first-in, first-out turn semantics.

If you cancel a submission before its messages have been applied, including one that has been claimed but is still waiting for its turn, those messages are not persisted to the conversation.

If the chat is cleared or turn state is reset before a pending submission runs, the submission is marked `skipped`.

## Compared with Workflows

Use Workflows for multi-step orchestration, retries per step, long waits, external events, human approvals, or pipelines that may trigger Think as one part of a larger process. Refer to [Think Workflows](https://developers.cloudflare.com/agents/harnesses/think/workflows/).

[PreviousSub-agent RPC and programmatic turns](https://developers.cloudflare.com/agents/harnesses/think/sub-agents/)[NextDurable recovery](https://developers.cloudflare.com/agents/harnesses/think/recovery/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/think/programmatic-submissions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
