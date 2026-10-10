---
url: https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/
title: Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.529210+00:00
---

# Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 22, 2025

## Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've shipped a new release for the [Agents SDK ↗︎](https://github.com/cloudflare/agents) v0.3.0 bringing full compatibility with [AI SDK v6 ↗︎](https://ai-sdk.dev/docs/introduction) and introducing the unified tool pattern, dynamic tool approval, and enhanced React hooks with improved tool handling.

This release includes improved streaming and tool support, dynamic tool approval (for "human in the loop" systems), enhanced React hooks with `onToolCall` callback, improved error handling for streaming responses, and seamless migration from v5 patterns.

This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable tool execution and approval workflows.

Additionally, we've updated **workers-ai-provider v3.0.0** , the official provider for Cloudflare Workers AI models, and **ai-gateway-provider v3.0.0** , the provider for Cloudflare AI Gateway, to be compatible with AI SDK v6.

#### Agents SDK v0.3.0

#### Unified Tool Pattern

AI SDK v6 introduces a unified tool pattern where all tools are defined on the server using the `tool()` function. This replaces the previous client-side `AITool` pattern.

#### Server-Side Tool Definition
    
    
    import { tool } from "ai";
    import { z } from "zod";
    
    // Server: Define ALL tools on the server
    const tools = {
    	// Server-executed tool
    	getWeather: tool({
    		description: "Get weather for a city",
    		inputSchema: z.object({ city: z.string() }),
    		execute: async ({ city }) => fetchWeather(city)
    	}),
    
    	// Client-executed tool (no execute = client handles via onToolCall)
    	getLocation: tool({
    		description: "Get user location from browser",
    		inputSchema: z.object({})
    		// No execute function
    	}),
    
    	// Tool requiring approval (dynamic based on input)
    	processPayment: tool({
    		description: "Process a payment",
    		inputSchema: z.object({ amount: z.number() }),
    		needsApproval: async ({ amount }) => amount > 100,
    		execute: async ({ amount }) => charge(amount)
    	})
    };

#### Client-Side Tool Handling
    
    
    // Client: Handle client-side tools via onToolCall callback
    import { useAgentChat } from "agents/ai-react";
    
    const { messages, sendMessage, addToolOutput } = useAgentChat({
    	agent,
    	onToolCall: async ({ toolCall, addToolOutput }) => {
    		if (toolCall.toolName === "getLocation") {
    			const position = await new Promise((resolve, reject) => {
    				navigator.geolocation.getCurrentPosition(resolve, reject);
    			});
    			addToolOutput({
    				toolCallId: toolCall.toolCallId,
    				output: {
    					lat: position.coords.latitude,
    					lng: position.coords.longitude
    				}
    			});
    		}
    	}
    });

**Key benefits of the unified tool pattern:**

  * **Server-defined tools** : All tools are defined in one place on the server
  * **Dynamic approval** : Use `needsApproval` to conditionally require user confirmation
  * **Cleaner client code** : Use `onToolCall` callback instead of managing tool configs
  * **Type safety** : Full TypeScript support with proper tool typing



#### useAgentChat(options)

Creates a new chat interface with enhanced v6 capabilities.
    
    
    // Basic chat setup with onToolCall
    const { messages, sendMessage, addToolOutput } = useAgentChat({
    	agent,
    	onToolCall: async ({ toolCall, addToolOutput }) => {
    		// Handle client-side tool execution
    		await addToolOutput({
    			toolCallId: toolCall.toolCallId,
    			output: { result: "success" }
    		});
    	}
    });

#### Dynamic Tool Approval

Use `needsApproval` on server tools to conditionally require user confirmation:
    
    
    const paymentTool = tool({
    	description: "Process a payment",
    	inputSchema: z.object({
    		amount: z.number(),
    		recipient: z.string()
    	}),
    	needsApproval: async ({ amount }) => amount > 1000,
    	execute: async ({ amount, recipient }) => {
    		return await processPayment(amount, recipient);
    	}
    });

#### Tool Confirmation Detection

The `isToolUIPart` and `getToolName` functions now check both static and dynamic tool parts:
    
    
    import { isToolUIPart, getToolName } from "ai";
    
    const pendingToolCallConfirmation = messages.some((m) =>
    	m.parts?.some(
    		(part) => isToolUIPart(part) && part.state === "input-available",
    	),
    );
    
    // Handle tool confirmation
    if (pendingToolCallConfirmation) {
    	await addToolOutput({
    		toolCallId: part.toolCallId,
    		output: "User approved the action"
    	});
    }

If you need the v5 behavior (static-only checks), use the new functions:
    
    
    import { isStaticToolUIPart, getStaticToolName } from "ai";

#### convertToModelMessages() is now async

The `convertToModelMessages()` function is now asynchronous. Update all calls to await the result:
    
    
    import { convertToModelMessages } from "ai";
    
    const result = streamText({
    	messages: await convertToModelMessages(this.messages),
    	model: openai("gpt-4o")
    });

#### ModelMessage type

The `CoreMessage` type has been removed. Use `ModelMessage` instead:
    
    
    import { convertToModelMessages, type ModelMessage } from "ai";
    
    const modelMessages: ModelMessage[] = await convertToModelMessages(messages);

#### generateObject mode option removed

The `mode` option for `generateObject` has been removed:
    
    
    // Before (v5)
    const result = await generateObject({
    	mode: "json",
    	model,
    	schema,
    	prompt
    });
    
    // After (v6)
    const result = await generateObject({
    	model,
    	schema,
    	prompt
    });

#### Structured Output with generateText

While `generateObject` and `streamObject` are still functional, the recommended approach is to use `generateText`/`streamText` with the `Output.object()` helper:
    
    
    import { generateText, Output, stepCountIs } from "ai";
    
    const { output } = await generateText({
    	model: openai("gpt-4"),
    	output: Output.object({
    		schema: z.object({ name: z.string() })
    	}),
    	stopWhen: stepCountIs(2),
    	prompt: "Generate a name"
    });

> **Note** : When using structured output with `generateText`, you must configure multiple steps with `stopWhen` because generating the structured output is itself a step.

#### workers-ai-provider v3.0.0

Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v3.0.0 with AI SDK v6 support.

#### Model Setup with Workers AI

Use Cloudflare Workers AI models directly in your agent workflows:
    
    
    import { createWorkersAI } from "workers-ai-provider";
    import { useAgentChat } from "agents/ai-react";
    
    // Create Workers AI model (v3.0.0 - enhanced v6 internals)
    const model = createWorkersAI({
    	binding: env.AI,
    })("@cf/meta/llama-3.2-3b-instruct");

#### Enhanced File and Image Support

Workers AI models now support v6 file handling with automatic conversion:
    
    
    // Send images and files to Workers AI models
    sendMessage({
    	role: "user",
    	parts: [
    		{ type: "text", text: "Analyze this image:" },
    		{
    			type: "file",
    			data: imageBuffer,
    			mediaType: "image/jpeg",
    		},
    	],
    });
    
    // Workers AI provider automatically converts to proper format

#### Streaming with Workers AI

Enhanced streaming support with automatic warning detection:
    
    
    // Streaming with Workers AI models
    const result = await streamText({
    	model: createWorkersAI({ binding: env.AI })("@cf/meta/llama-3.2-3b-instruct"),
    	messages: await convertToModelMessages(messages),
    	onChunk: (chunk) => {
    		// Enhanced streaming with warning handling
    		console.log(chunk);
    	},
    });

#### ai-gateway-provider v3.0.0

The ai-gateway-provider v3.0.0 now supports AI SDK v6, enabling you to use Cloudflare AI Gateway with multiple AI providers including Anthropic, Azure, AWS Bedrock, Google Vertex, and Perplexity.

#### AI Gateway Setup

Use Cloudflare AI Gateway to add analytics, caching, and rate limiting to your AI applications:
    
    
    import { createAIGateway } from "ai-gateway-provider";
    
    // Create AI Gateway provider (v3.0.0 - enhanced v6 internals)
    const model = createAIGateway({
    	gatewayUrl: "https://gateway.ai.cloudflare.com/v1/your-account-id/gateway",
    	headers: {
    		"Authorization": `Bearer ${env.AI_GATEWAY_TOKEN}`
    	}
    })({
    	provider: "openai",
    	model: "gpt-4o"
    });

#### Migration from v5

#### Deprecated APIs

The following APIs are deprecated in favor of the unified tool pattern:

Deprecated | Replacement  
---|---  
`AITool` type | Use AI SDK's `tool()` function on server  
`extractClientToolSchemas()` | Define tools on server, no client schemas needed  
`createToolsFromClientSchemas()` | Define tools on server with `tool()`  
`toolsRequiringConfirmation` option | Use `needsApproval` on server tools  
`experimental_automaticToolResolution` | Use `onToolCall` callback  
`tools` option in `useAgentChat` | Use `onToolCall` for client-side execution  
`addToolResult()` | Use `addToolOutput()`  
  
#### Breaking Changes Summary

  1. **Unified Tool Pattern** : All tools must be defined on the server using `tool()`
  2. **`convertToModelMessages()` is async**: Add `await` to all calls
  3. **`CoreMessage` removed**: Use `ModelMessage` instead
  4. **`generateObject` mode removed**: Remove `mode` option
  5. **`isToolUIPart` behavior changed**: Now checks both static and dynamic tool parts



#### Installation

Update your dependencies to use the latest versions:
    
    
    npm install agents@^0.3.0 workers-ai-provider@^3.0.0 ai-gateway-provider@^3.0.0 ai@^6.0.0 @ai-sdk/react@^3.0.0 @ai-sdk/openai@^3.0.0

#### Resources

  * [Migration Guide ↗︎](https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v6.md) \- Comprehensive migration documentation from v5 to v6
  * [AI SDK v6 Documentation ↗︎](https://ai-sdk.dev/docs/migration-guides/migration-guide-6-0) \- Official AI SDK migration guide
  * [AI SDK v6 Announcement ↗︎](https://vercel.com/blog/ai-sdk-6) \- Learn about new features in v6
  * [AI SDK Documentation ↗︎](https://sdk.vercel.ai/docs) \- Complete AI SDK reference
  * [GitHub Issues ↗︎](https://github.com/cloudflare/agents/issues) \- Report bugs or request features



#### Feedback Welcome

We'd love your feedback! We're particularly interested in feedback on:

  * **Migration experience** \- How smooth was the upgrade from v5 to v6?
  * **Unified tool pattern** \- How does the new server-defined tool pattern work for you?
  * **Dynamic tool approval** \- Does the `needsApproval` feature meet your needs?
  * **AI Gateway integration** \- How well does the new provider work with your setup?


