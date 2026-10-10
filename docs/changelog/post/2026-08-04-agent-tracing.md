---
url: https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/
title: Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.742093+00:00
---

# Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 4, 2026

## Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Agent tracing is now available for applications built with the Agents SDK. Traces show each agent turn alongside model calls, tool runs, approvals, token usage, and Workers runtime operations.

Turn on Workers tracing in your Wrangler configuration:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "observability": {
        "traces": {
          "enabled": true
        }
      }
    }
    
    
    [observability.traces]
    enabled = true

Think and Flue applications emit agent traces automatically. For direct AI SDK calls, wrap the AI SDK namespace once. `wrapAISDK()` supports AI SDK v6 and v7. This AI SDK v7 example also supplies the agent identity:
    
    
    import * as ai from "ai";
    import { wrapAISDK } from "agents/observability/ai";
    
    const tracedAI = wrapAISDK(ai);
    
    await tracedAI.generateText({
    	model,
    	prompt: "Find an available appointment",
    	runtimeContext: {
    		agentId: "booking-agent-production",
    		conversationId: "conversation-123",
    	},
    	telemetry: {
    		functionId: "booking-agent",
    		includeRuntimeContext: {
    			agentId: true,
    			conversationId: true,
    		},
    	},
    });
    
    
    import * as ai from "ai";
    import { wrapAISDK } from "agents/observability/ai";
    
    const tracedAI = wrapAISDK(ai);
    
    await tracedAI.generateText({
    	model,
    	prompt: "Find an available appointment",
    	runtimeContext: {
    		agentId: "booking-agent-production",
    		conversationId: "conversation-123",
    	},
    	telemetry: {
    		functionId: "booking-agent",
    		includeRuntimeContext: {
    			agentId: true,
    			conversationId: true,
    		},
    	},
    });

Message and tool payload recording is off by default. Turn it on only when the payloads are safe to store:
    
    
    const tracedAI = wrapAISDK(ai, {
    	storeMessages: true,
    	storeTools: true,
    });
    
    
    const tracedAI = wrapAISDK(ai, {
    	storeMessages: true,
    	storeTools: true,
    });

Open the [**Agents** tab ↗︎](https://dash.cloudflare.com/?to=/:account/agents) in the Cloudflare dashboard to inspect sessions, replay conversations, and view trace waterfalls. For advanced setup, privacy controls, and trace structure, refer to [Agent tracing](https://developers.cloudflare.com/agents/runtime/operations/observability/tracing/).
