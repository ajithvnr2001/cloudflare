---
url: https://developers.cloudflare.com/sandbox/sdk/tutorials/ai-code-executor/
title: Build an AI code executor (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:28.874947+00:00
---

# Build an AI code executor (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/tutorials/ai-code-executor/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[Tutorials](https://developers.cloudflare.com/sandbox/sdk/tutorials/)
  5. /Build an AI code executor



# Build an AI code executor

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/tutorials/ai-code-executor/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat you'll buildPrerequisites1\. Create your project2\. Install dependencies3\. Build your code executor4\. Set up local environment variables5\. Test locally6\. Deploy7\. Test your deploymentWhat you builtNext stepsRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Build an AI code interpreter](https://developers.cloudflare.com/sandbox/get-started/build-an-ai-code-interpreter/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Build an AI-powered code execution system using Sandbox SDK and Claude. Turn natural language questions into Python code, execute it securely, and return results.

**Time to complete:** 20 minutes

## What you'll build

An API that accepts questions like "What's the 100th Fibonacci number?", uses Claude to generate Python code, executes it in an isolated sandbox, and returns the results.

## Prerequisites

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

You'll also need:

  * An [Anthropic API key ↗︎](https://console.anthropic.com/) for Claude
  * [Docker ↗︎](https://www.docker.com/) running locally



## 1\. Create your project

Create a new Sandbox SDK project:

npmyarnpnpm
    
    
    npm create cloudflare@latest -- ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal#v0
    
    
    yarn create cloudflare ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal#v0
    
    
    pnpm create cloudflare@latest ai-code-executor --template=cloudflare/sandbox-sdk/examples/minimal#v0
    
    
    cd ai-code-executor

## 2\. Install dependencies

Install the Anthropic SDK:

npmyarnpnpmbun
    
    
    npm i @anthropic-ai/sdk
    
    
    yarn add @anthropic-ai/sdk
    
    
    pnpm add @anthropic-ai/sdk
    
    
    bun add @anthropic-ai/sdk

## 3\. Build your code executor

Replace the contents of `src/index.ts`:
    
    
    import { getSandbox, type Sandbox } from '@cloudflare/sandbox';
    import Anthropic from '@anthropic-ai/sdk';
    
    export { Sandbox } from '@cloudflare/sandbox';
    
    interface Env {
    	Sandbox: DurableObjectNamespace<Sandbox>;
    	ANTHROPIC_API_KEY: string;
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		if (request.method !== 'POST' || new URL(request.url).pathname !== '/execute') {
    			return new Response('POST /execute with { "question": "your question" }');
    		}
    
    		try {
    			const { question } = await request.json();
    
    			if (!question) {
    				return Response.json({ error: 'Question is required' }, { status: 400 });
    			}
    
    			// Use Claude to generate Python code
    			const anthropic = new Anthropic({ apiKey: env.ANTHROPIC_API_KEY });
    			const codeGeneration = await anthropic.messages.create({
    				model: 'claude-sonnet-4-5',
    				max_tokens: 1024,
    				messages: [{
    					role: 'user',
    					content: `Generate Python code to answer: "${question}"
    
    Requirements:
    - Use only Python standard library
    - Print the result using print()
    - Keep code simple and safe
    
    Return ONLY the code, no explanations.`
    				}],
    			});
    
    			const generatedCode = codeGeneration.content[0]?.type === 'text'
    				? codeGeneration.content[0].text
    				: '';
    
    			if (!generatedCode) {
    				return Response.json({ error: 'Failed to generate code' }, { status: 500 });
    			}
    
    			// Strip markdown code fences if present
    			const cleanCode = generatedCode
    				.replace(/^```python?\n?/, '')
    				.replace(/\n?```\s*$/, '')
    				.trim();
    
    			// Execute the code in a sandbox
    			const sandbox = getSandbox(env.Sandbox, 'demo-user');
    			await sandbox.writeFile('/tmp/code.py', cleanCode);
    			const result = await sandbox.exec('python /tmp/code.py');
    
    			return Response.json({
    				success: result.success,
    				question,
    				code: generatedCode,
    				output: result.stdout,
    				error: result.stderr
    			});
    
    		} catch (error: any) {
    			return Response.json(
    				{ error: 'Internal server error', message: error.message },
    				{ status: 500 }
    			);
    		}
    	},
    };

**How it works:**

  1. Receives a question via POST to `/execute`
  2. Uses Claude to generate Python code
  3. Writes code to `/tmp/code.py` in the sandbox
  4. Executes with `sandbox.exec('python /tmp/code.py')`
  5. Returns both the code and execution results



## 4\. Set up local environment variables

Create a `.dev.vars` file in your project root for local development:
    
    
    echo "ANTHROPIC_API_KEY=your_api_key_here" > .dev.vars

Replace `your_api_key_here` with your actual API key from the [Anthropic Console ↗︎](https://console.anthropic.com/).

Note

The `.dev.vars` file is automatically gitignored and only used during local development with `npm run dev`.

## 5\. Test locally

Start the development server:
    
    
    npm run dev

Note

First run builds the Docker container (2-3 minutes). Subsequent runs are much faster.

Test with curl:
    
    
    curl -X POST http://localhost:8787/execute \
      -H "Content-Type: application/json" \
      -d '{"question": "What is the 10th Fibonacci number?"}'

Response:
    
    
    {
      "success": true,
      "question": "What is the 10th Fibonacci number?",
      "code": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\nprint(fibonacci(10))",
      "output": "55\n",
      "error": ""
    }

## 6\. Deploy

Deploy your Worker:
    
    
    npx wrangler deploy

Then set your Anthropic API key as a production secret:
    
    
    npx wrangler secret put ANTHROPIC_API_KEY

Paste your API key from the [Anthropic Console ↗︎](https://console.anthropic.com/) when prompted.

Caution

After first deployment, wait 2-3 minutes for container provisioning. Check status with `npx wrangler containers list`.

## 7\. Test your deployment

Try different questions:
    
    
    # Factorial
    curl -X POST https://ai-code-executor.YOUR_SUBDOMAIN.workers.dev/execute \
      -H "Content-Type: application/json" \
      -d '{"question": "Calculate the factorial of 5"}'
    
    # Statistics
    curl -X POST https://ai-code-executor.YOUR_SUBDOMAIN.workers.dev/execute \
      -H "Content-Type: application/json" \
      -d '{"question": "What is the mean of [10, 20, 30, 40, 50]?"}'
    
    # String manipulation
    curl -X POST https://ai-code-executor.YOUR_SUBDOMAIN.workers.dev/execute \
      -H "Content-Type: application/json" \
      -d '{"question": "Reverse the string \"Hello World\""}'

## What you built

You created an AI code execution system that:

  * Accepts natural language questions
  * Generates Python code with Claude
  * Executes code securely in isolated sandboxes
  * Returns results with error handling



## Next steps

  * [Code interpreter with Workers AI](https://developers.cloudflare.com/sandbox/sdk/tutorials/workers-ai-code-interpreter/) \- Use Cloudflare's native AI models with official packages
  * [Analyze data with AI](https://developers.cloudflare.com/sandbox/sdk/tutorials/analyze-data-with-ai/) \- Add pandas and matplotlib for data analysis
  * [Code Interpreter API](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/) \- Use the built-in code interpreter instead of exec
  * [Streaming output](https://developers.cloudflare.com/sandbox/sdk/guides/streaming-output/) \- Show real-time execution progress
  * [API reference](https://developers.cloudflare.com/sandbox/sdk/api/) \- Explore all available methods



## Related resources

  * [Anthropic Claude documentation ↗︎](https://docs.anthropic.com/)
  * [Workers AI](https://developers.cloudflare.com/workers-ai/) \- Use Cloudflare's built-in models
  * [workers-ai-provider package ↗︎](https://github.com/cloudflare/ai/tree/main/packages/workers-ai-provider) \- Official Workers AI integration



[PreviousOverview](https://developers.cloudflare.com/sandbox/sdk/tutorials/)[NextAnalyze data with AI](https://developers.cloudflare.com/sandbox/sdk/tutorials/analyze-data-with-ai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/tutorials/ai-code-executor.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
