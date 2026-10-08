---
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/troubleshooting/
title: Troubleshooting \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:58.054456+00:00
---

# Troubleshooting · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features[Function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/)

  4. /[Embedded](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/)
  5. /Troubleshooting



# Troubleshooting

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLogging Function invocations Logging within runWithToolsPerformanceCommon Errors

This section will describe tools for troubleshooting and address common errors.

## Logging

General [logging](https://developers.cloudflare.com/workers/observability/logs/) capabilities for Workers also apply to embedded function calling.

### Function invocations

The invocations of tools can be logged as in any Worker using `console.log()`:

Logging tool invocationsts
    
    
    export default {
    	async fetch(request, env, ctx) {
    		const sum = (args: { a: number; b: number }): Promise<string> => {
    			const { a, b } = args;
          // Logging from within embedded function invocations
          console.log(`The sum function has been invoked with the arguments a: ${a} and b: ${b}`)
    			return Promise.resolve((a + b).toString());
    		};
        ...
      }
    }

### Logging within `runWithTools`

The `runWithTools` function has a `verbose` mode that emits helpful logs for debugging of function calls as well input and output statistics.

Enabled verbose modets
    
    
    const response = await runWithTools(
      env.AI,
      '@hf/nousresearch/hermes-2-pro-mistral-7b',
      {
        messages: [
          ...
        ],
        tools: [
          ...
        ],
      },
      // Enable verbose mode
      { verbose: true }
    );

## Performance

To respond to a LLM prompt with embedded function, potentially multiple AI inference requests and function invocations are needed, which can have an impact on user experience.

Consider the following to improve performance:

  * Shorten prompts (to reduce time for input processing)
  * Reduce number of tools provided
  * Stream the final response to the end user (to minimize the time to interaction). See example below:

Streamed response examplets
    
    
    async fetch(request, env, ctx) {
      const response = (await runWithTools(
        env.AI,
        '@hf/nousresearch/hermes-2-pro-mistral-7b',
        {
          messages: [
            ...
          ],
          tools: [
            ...
          ],
        },
        {
          // Enable response streaming
          streamFinalResponse: true,
        }
      )) as ReadableStream;
    
      // Set response headers for streaming
      return new Response(response, {
        headers: {
          'content-type': 'text/event-stream',
        },
      });
    }

## Common Errors

If you are getting a `BadInput` error, your inputs may exceed our current context window for our models. Try reducing input tokens to resolve this error.

[PreviousAPI Reference](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/)[NextTraditional](https://developers.cloudflare.com/workers-ai/features/function-calling/traditional/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/function-calling/embedded/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
