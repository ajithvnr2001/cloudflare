---
url: https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/
title: Add human feedback using Worker Bindings \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:29.179954+00:00
---

# Add human feedback using Worker Bindings · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ai Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /[Evaluations](https://developers.cloudflare.com/ai-gateway/evaluations/)
  4. /Add Human Feedback Bindings



# Add human feedback using Worker Bindings

Last updated Jun 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-bindings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Run an AI Evaluation2\. Send Human FeedbackFeedback parameters explanation patchLog: Send Feedback

This guide explains how to provide human feedback for AI Gateway evaluations using Worker bindings.

## 1\. Run an AI Evaluation

Start by sending a prompt to the AI model through your AI Gateway.
    
    
    const resp = await env.AI.run(
    	"@cf/meta/llama-3.1-8b-instruct",
    	{
    		prompt: "tell me a joke",
    	},
    	{
    		gateway: {
    			id: "my-gateway",
    		},
    	},
    );
    
    const myLogId = env.AI.aiGatewayLogId;

Let the user interact with or evaluate the AI response. This interaction will inform the feedback you send back to the AI Gateway.

## 2\. Send Human Feedback

Use the [`patchLog()`](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/#patchlog) method to provide feedback for the AI evaluation.
    
    
    await env.AI.gateway("my-gateway").patchLog(myLogId, {
    	feedback: 1, // all fields are optional; set values that fit your use case
    	score: 100,
    	metadata: {
    		user: "123", // Optional metadata to provide additional context
    	},
    });

## Feedback parameters explanation

  * `feedback`: is either `-1` for negative or `1` to positive, `0` is considered not evaluated.
  * `score`: A number between 0 and 100.
  * `metadata`: An object containing additional contextual information.



### patchLog: Send Feedback

The `patchLog` method allows you to send feedback, score, and metadata for a specific log ID. All object properties are optional, so you can include any combination of the parameters:
    
    
    gateway.patchLog("my-log-id", {
    	feedback: 1,
    	score: 100,
    	metadata: {
    		user: "123",
    	},
    });

Returns: `Promise<void>` (Make sure to `await` the request.)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/evaluations/add-human-feedback-bindings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
