---
url: https://developers.cloudflare.com/changelog/product/agents/
title: Agents Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:39.756954+00:00
---

# Agents Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/agents/

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

Oct 2, 2026

## [Run the Pi Durable harness on Cloudflare with the Agents SDK](https://developers.cloudflare.com/changelog/post/2026-10-02-pi-harness/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The [Agents SDK](https://developers.cloudflare.com/agents/) now provides first-class support for building agents using the Pi harness. You can build long-running agents using the combination of [Pi 1.0 ↗︎](https://earendil.com/posts/pi-1-0/), [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/), and the new `PiHarness` class that the Cloudflare Agents SDK provides, ensuring your agent's work is durably persisted, even if interrupted mid-turn.

Built with [Earendil ↗︎](https://earendil.com/), this integration is our first step toward first-class support for third-party agent harnesses on Cloudflare.

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi)

Beta

`PiHarness` is in beta. [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/) is a new, experimental package, and the `PiHarness` API will likely change as Pi Durable matures.

`PiHarness` is a new "Lifecycle capability" provided by the Cloudflare Agents SDK. Pi Durable provides the agent harness and the Lifecycle is responsible for keeping the agent running in the Durable Object. The Lifecycle is a core concept in the Agents SDK ensuring that long-running work can run in a Durable Object, surviving restarts, crashes, and network issues. We will share more on Lifecycle capabilities in the near future.

#### Install

npmyarnpnpmbun
    
    
    npm i agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    yarn add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    pnpm add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    bun add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai

Both Pi packages are optional peer dependencies of `agents`, so you only install them if you use the harness.

#### Use it in an Agent

Creating a Pi agent requires configuring the Pi `Harness` with a model, skills, and tools, then registering the `PiHarness` with the `Agent` class.
    
    
    import { Agent } from "agents";
    import { createModels } from "@earendil-works/pi-ai/models";
    import { createRegistry, Harness } from "@earendil-works/pi-durable";
    import { PiHarness } from "agents/harness/pi";
    import { createAI } from "agents/models/pi-ai";
    
    export class Assistant extends Agent {
    	ai = createAI({ binding: this.env.AI });
    	registry = createRegistry();
    
    	harness = new PiHarness({
    		harness: ({ storage, context }) => {
    			const models = createModels();
    			models.setProvider(this.ai.provider);
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    		defaults: { model: this.ai("@cf/moonshotai/kimi-k2.7-code") },
    	});
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		this.lifecycle.use(this.harness);
    	}
    
    	async ask(prompt) {
    		const { text } = await this.harness.prompt(prompt);
    		return text;
    	}
    }
    
    
    import { Agent } from "agents";
    import { createModels } from "@earendil-works/pi-ai/models";
    import { createRegistry, Harness } from "@earendil-works/pi-durable";
    import { PiHarness } from "agents/harness/pi";
    import { createAI } from "agents/models/pi-ai";
    
    export class Assistant extends Agent<Env> {
    	ai = createAI({ binding: this.env.AI });
    	registry = createRegistry();
    
    	harness = new PiHarness({
    		harness: ({ storage, context }) => {
    			const models = createModels();
    			models.setProvider(this.ai.provider);
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    		defaults: { model: this.ai("@cf/moonshotai/kimi-k2.7-code") },
    	});
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		this.lifecycle.use(this.harness);
    	}
    
    	async ask(prompt: string) {
    		const { text } = await this.harness.prompt(prompt);
    		return text;
    	}
    }

The `agents/models/pi-ai` entry point supports AI Gateway and Workers AI models, so you can get started with Cloudflare models right away or use your existing Pi AI provider.

#### Add tools with extensions

Both tools and system prompt sections are provided to the Pi `Harness` via extensions.
    
    
    import { Type } from "@earendil-works/pi-ai";
    
    import { skills } from "agents/harness/pi";
    
    const WordCount = Type.Object({ text: Type.String() });
    
    const wordCount = {
    	name: "word_count",
    	description: "Count the words in a text.",
    	parameters: WordCount,
    	replay: "safe",
    	async execute({ text }) {
    		const words = text.split(/\s+/).filter(Boolean).length;
    		return { content: [{ type: "text", text: String(words) }] };
    	},
    };
    
    // In the harness factory, before Harness.open():
    registry.install({
    	name: "editor",
    	sections: [
    		{ key: "preamble", render: () => "You are an editor.", tag: false },
    	],
    	tools: [wordCount],
    });
    registry.install(await skills(sources));
    
    
    import { Type } from "@earendil-works/pi-ai";
    import type { ToolRegistration } from "@earendil-works/pi-durable";
    import { skills } from "agents/harness/pi";
    
    const WordCount = Type.Object({ text: Type.String() });
    
    const wordCount: ToolRegistration<typeof WordCount> = {
    	name: "word_count",
    	description: "Count the words in a text.",
    	parameters: WordCount,
    	replay: "safe",
    	async execute({ text }) {
    		const words = text.split(/\s+/).filter(Boolean).length;
    		return { content: [{ type: "text", text: String(words) }] };
    	},
    };
    
    // In the harness factory, before Harness.open():
    registry.install({
    	name: "editor",
    	sections: [
    		{ key: "preamble", render: () => "You are an editor.", tag: false },
    	],
    	tools: [wordCount],
    });
    registry.install(await skills(sources));

For more information on creating and configuring extensions, refer to [Extensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/).

#### Learn more

  * [Pi harness documentation](https://developers.cloudflare.com/agents/harnesses/pi/)
  * [Pi harness extensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/)
  * [pi-ai model provider](https://developers.cloudflare.com/agents/models/pi-ai/)
  * [Pi harness example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi), with WebSockets, a browser UI, and a `@cloudflare/computer` Workspace for the model's tools
  * [Lifecycle ↗︎](https://github.com/cloudflare/agents/blob/main/docs/agents/lifecycle.md)
  * [Pi Durable announcement ↗︎](https://earendil.com/posts/pi-durable/) from Earendil



Oct 1, 2026

## [The best way to do MCP auth just got better: Workers OAuth Provider goes v1, with a new split API and full support for MCP 2026-07-28](https://developers.cloudflare.com/changelog/post/2026-10-01-workers-oauth-provider-1x/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

[`@cloudflare/workers-oauth-provider` ↗︎](https://github.com/cloudflare/workers-oauth-provider) is now v1, with a new split API. One Worker acts as the authorization server: it signs users in and issues tokens. Your MCP server acts as the resource server, and can run in another Worker. It validates each token with the authorization server over a [Service Binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/), without crossing the public Internet.

  * It supports the [MCP 2026-07-28 authorization specification ↗︎](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), including [Client ID Metadata Documents ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#client-id-metadata-documents) and [issuer identification ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#authorization-response-issuer). It still works with older clients, including those using [Dynamic Client Registration ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#dynamic-client-registration).
  * `insufficientScope()` gives you [step-up authorization ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#scopes-and-step-up-authorization) in one line.
  * The authorization server and the resource server can run in [different Workers ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/resource-servers.md#separate-workers) with different [WAF](https://developers.cloudflare.com/waf/) and [rate limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/) rules.
  * One authorization server can issue tokens for [many MCP servers ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#resources-and-token-audiences).
  * A [migration skill ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/skills/migrate-to-1.0/SKILL.md) ships in the npm package so a coding agent can perform the upgrade.



#### The split API
    
    
    import {
    	OAuthAuthorizationServer,
    	OAuthResourceServer,
    	insufficientScope,
    } from "@cloudflare/workers-oauth-provider";
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    // auth-server Worker: signs users in and issues tokens for both MCP servers.
    const authorizationServer = new OAuthAuthorizationServer({
    	issuer: "https://auth.example.com",
    	resources: [
    		"https://calendar.example.com/mcp",
    		"https://drive.example.com/mcp",
    	],
    	scopesSupported: ["calendar:read", "calendar:write", "offline_access"],
    	clientIdMetadataDocumentEnabled: true,
    });
    
    export class AuthServer extends WorkerEntrypoint {
    	fetch(request) {
    		if (new URL(request.url).pathname === "/authorize") {
    			return showConsent(request, this.env);
    		}
    		return authorizationServer.fetch(request, this.env, this.ctx);
    	}
    
    	validateToken(resource, token) {
    		return authorizationServer.validateToken(resource, token, this.env);
    	}
    }
    
    // calendar MCP Worker: checks tokens with AuthServer over a Service Binding.
    export const calendar = new OAuthResourceServer({
    	resourceMetadata: {
    		resource: "https://calendar.example.com/mcp",
    		authorization_servers: ["https://auth.example.com"],
    	},
    	requiredScopes: ["calendar:read"],
    	validateToken: (env) => env.AUTH_SERVER.validateToken,
    	handler: {
    		fetch(request, env, ctx) {
    			if (
    				request.method === "POST" &&
    				!ctx.auth.scope.includes("calendar:write")
    			) {
    				return insufficientScope(ctx.auth, ["calendar:read", "calendar:write"]);
    			}
    			return handleMcp(request, ctx.props);
    		},
    	},
    });
    
    
    import {
    	OAuthAuthorizationServer,
    	OAuthResourceServer,
    	insufficientScope,
    } from "@cloudflare/workers-oauth-provider";
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    // auth-server Worker: signs users in and issues tokens for both MCP servers.
    const authorizationServer = new OAuthAuthorizationServer<Env>({
    	issuer: "https://auth.example.com",
    	resources: [
    		"https://calendar.example.com/mcp",
    		"https://drive.example.com/mcp",
    	],
    	scopesSupported: ["calendar:read", "calendar:write", "offline_access"],
    	clientIdMetadataDocumentEnabled: true,
    });
    
    export class AuthServer extends WorkerEntrypoint<Env> {
    	fetch(request: Request) {
    		if (new URL(request.url).pathname === "/authorize") {
    			return showConsent(request, this.env);
    		}
    		return authorizationServer.fetch(request, this.env, this.ctx);
    	}
    
    	validateToken(resource: string, token: string) {
    		return authorizationServer.validateToken(resource, token, this.env);
    	}
    }
    
    // calendar MCP Worker: checks tokens with AuthServer over a Service Binding.
    export const calendar = new OAuthResourceServer<Env, AuthProps>({
    	resourceMetadata: {
    		resource: "https://calendar.example.com/mcp",
    		authorization_servers: ["https://auth.example.com"],
    	},
    	requiredScopes: ["calendar:read"],
    	validateToken: (env) => env.AUTH_SERVER.validateToken,
    	handler: {
    		fetch(request, env, ctx) {
    			if (
    				request.method === "POST" &&
    				!ctx.auth.scope.includes("calendar:write")
    			) {
    				return insufficientScope(ctx.auth, ["calendar:read", "calendar:write"]);
    			}
    			return handleMcp(request, ctx.props);
    		},
    	},
    });

In the example, `env.AUTH_SERVER.validateToken` is that Service Binding call. The calendar Worker needs no KV namespace of its own.
    
    
    {
    	"name": "calendar-mcp",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"services": [
    		{
    			"binding": "AUTH_SERVER",
    			"service": "auth-server",
    			"entrypoint": "AuthServer",
    		},
    	],
    }
    
    
    name = "calendar-mcp"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[services]]
    binding = "AUTH_SERVER"
    service = "auth-server"
    entrypoint = "AuthServer"

`OAuthResourceServer` publishes the [RFC 9728 ↗︎](https://datatracker.ietf.org/doc/html/rfc9728) protected resource metadata that MCP clients use to find your authorization server. It answers requests without a token with a `401` challenge that points to that metadata. It also rejects tokens issued for any other resource.

You can still use `OAuthProvider` as both the authorization server and the MCP server. For most 0.x deployments, the only required change is to add `resourceMetadata: { resource }`.

#### Other updates and helpers

  * [Consent page ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/consent-page.md) and [upstream sign-in ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/upstream-sign-in.md) helpers implement the MCP confused deputy protections.
  * [Sliding refresh token expiry ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#sliding-expiry) with `refreshTokenIdleTTL`.
  * [Resumable KV cleanup ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#kv-cleanup) with `purgeExpiredData()`.
  * An [internal reason ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#the-internal-reason) on every error passed to `onError`.



#### Upgrade with the migration skill

npmyarnpnpmbun
    
    
    npm i @cloudflare/workers-oauth-provider@latest
    
    
    yarn add @cloudflare/workers-oauth-provider@latest
    
    
    pnpm add @cloudflare/workers-oauth-provider@latest
    
    
    bun add @cloudflare/workers-oauth-provider@latest

Point your coding agent at `node_modules/@cloudflare/workers-oauth-provider/skills/migrate-to-1.0/SKILL.md`, or follow the [migration guide ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/migration-1.0.md).

For both Workers in full, refer to the [split Workers example ↗︎](https://github.com/cloudflare/workers-oauth-provider/tree/main/examples/split-workers).

Sep 11, 2026

## [Inspect Voice Agent turn latency and outcomes](https://developers.cloudflare.com/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/)

[Agents](https://developers.cloudflare.com/agents/)

`@cloudflare/voice` v0.4.0 now lets you inspect where each Voice Agent turn spends time and how it ends.
    
    
    client.addEventListener("turnmetrics", (turn) => {
    	console.log(turn.outcome, turn.turnTotalMs);
    });

#### About the Voice package

The `@cloudflare/voice` package lets you build real-time voice agents with Cloudflare Agents. It streams microphone audio to an Agent over WebSocket, transcribes speech, runs your model through `onTurn()`, converts the response to speech, and streams audio back to the caller.

A turn moves through several stages:
    
    
    User speaks -> speech-to-text -> model -> text-to-speech -> audio

Previously, the package's four aggregate metrics covered successful, non-empty speech turns. They did not show how failed, aborted, empty, or text turns ended.

#### Turn metrics

Each speech or text turn now produces a typed `VoiceTurnMetrics` summary with:

  * A `turnId` for correlating events from the same turn.
  * A terminal outcome such as `completed`, `no_output`, `output_limit`, `content_filtered`, `model_error`, `tts_error`, or `aborted`.
  * Timings for important stages, including speech-to-final-transcript, model-to-first-text, TTS-to-first-audio, and total turn duration.



These timings can overlap and are not additive. Timings for stages that a turn did not reach are omitted.

The latest summary is available through `VoiceClient`, `useVoiceAgent()`, and `useVoiceInput()`. Voice input includes only the speech and transcription timings it can measure.

If an agent produces no audio, you can now distinguish between the model returning no output, reaching an output limit, encountering content filtering, or failing.

#### Additional diagnostics

For local debugging, you can forward server lifecycle events to the browser console:
    
    
    import { Agent } from "agents";
    import { withVoice } from "@cloudflare/voice";
    
    const VoiceAgent = withVoice(Agent, {
    	diagnostics: {
    		browserConsole: true,
    	},
    });
    
    
    import { Agent } from "agents";
    import { withVoice } from "@cloudflare/voice";
    
    const VoiceAgent = withVoice(Agent, {
    	diagnostics: {
    		browserConsole: true,
    	},
    });

The browser console combines server lifecycle events with local microphone, connection, and playback events, including model start, first model text, first audio, and playback start. Diagnostics are off by default, and their event names and fields can change.

`VoiceClient` also exposes typed events for speech-to-text failures, connection errors, and model outcomes. The SDK removes known content fields and does not read arbitrary provider responses, but custom error messages must not contain sensitive data.

Install the release with a compatible Agents SDK version:

npmyarnpnpmbun
    
    
    npm i @cloudflare/voice@^0.4.0 agents@^0.22.0
    
    
    yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0
    
    
    pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0
    
    
    bun add @cloudflare/voice@^0.4.0 agents@^0.22.0

Refer to the [Voice pipeline metrics](https://developers.cloudflare.com/agents/communication-channels/voice/#pipeline-metrics) and [Voice Agent example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/voice-agent) to get started.

Aug 22, 2026

## [Choose OAuth scopes for Wrangler and the Cloudflare API MCP server](https://developers.cloudflare.com/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Wrangler and the [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) now use optional OAuth scopes. During authorization, you can choose which optional scopes to grant instead of approving every scope requested by each client.

The consent dialog now includes the option to edit the permissions you grant to Wrangler or the Cloudflare API MCP server:

![OAuth consent dialog with an Edit Permissions button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1368,height=1008,format=webp/_astro/oauth-optional-scopes-review.BMp1De1d.png)

You can then choose which specific permissions to grant:

![OAuth permission editor with controls for individual scopes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1366,height=1312,format=webp/_astro/oauth-optional-scopes-edit.BXIdjwS7.png)

Required scopes remain selected. Choosing fewer optional scopes limits each tool's access to the permissions needed for your workflow.

If a command or tool call needs a scope that you declined, reauthorize the client and grant that scope.

For more information, refer to [`wrangler login`](https://developers.cloudflare.com/workers/wrangler/commands/general/#login) and [Edit optional permissions](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions).

Aug 4, 2026

## [Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK](https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

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

Aug 3, 2026

## [Preview: @cloudflare/computer agent runtime](https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

We're releasing an early preview of [`@cloudflare/computer` ↗︎](https://github.com/cloudflare/computer), an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.

`@cloudflare/computer` provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.

Install the package via npm:
    
    
    npm install @cloudflare/computer

Instantiate a `Workspace` inside any Durable Object to give your agent a filesystem and execution runtime:
    
    
    import { Workspace } from "@cloudflare/computer";
    
    export class Agent {
    	workspace = new Workspace({
    		storage: this.ctx.storage,
    	});
    }

Several execution backends are included or you can write your own:

  * **Isolate runtime** — fast, horizontally scalable execution via `just-bash` and Dynamic Workers, ideal for file manipulation and data processing.
  * **Container runtime** — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.



The AI SDK-compatible toolkit provides common agent tools (`read`, `write`, `edit`, `ls`, `exec`) and guides the model to choose the appropriate backend for each task.

For more examples, including a step-by-step tutorial, visit the [`@cloudflare/computer` repository ↗︎](https://github.com/cloudflare/computer).

Read the announcement blog post for more details: [Your agent needs a computer, not a container ↗︎](https://blog.cloudflare.com/cloudflare-computer/).

Jul 28, 2026

## [Cloudflare MCP servers support the new MCP 2026-07-28 Specification](https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Cloudflare's [product-specific MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers) now support the new MCP 2026-07-28 Specification. Each request runs on a fresh stateless server without an MCP protocol session or protocol-specific Durable Object.

The `/mcp` endpoint also accepts stateless requests from 2025 Streamable HTTP clients. Most clients can reconnect without configuration changes.

Use `/mcp` for new connections. Historical `/sse` URLs continue to work as aliases for the same Streamable HTTP handler, but they no longer serve the deprecated HTTP+SSE transport. If a client forces SSE transport, change it to Streamable HTTP or automatic transport detection.

Jul 27, 2026

## [Agents SDK adds MCP Specification 2026-07-28 support](https://developers.cloudflare.com/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Agents SDK v0.20.0 adds client and server support for the [MCP 2026-07-28 release candidate ↗︎](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Workers can serve tools, prompts, resources, and elicitation without an MCP transport session or Durable Object. Agents can connect to both MCP 2026-07-28 servers and existing legacy servers.

#### Client support

The MCP client manager now uses `@modelcontextprotocol/client`. For each connection, it probes for MCP 2026-07-28 support with `server/discover`. If the server does not support the stateless protocol, the client continues with the legacy `initialize` handshake on the same connection. Existing `addMcpServer` calls do not need a protocol-version setting or separate clients for each protocol generation.

For stateless requests, elicitation uses `input_required` through multi-round-trip requests (MRTR). The legacy path uses the same form and URL handlers for pushed requests. The SDK collects input, retries the original operation, and resolves the original `callTool`, `getPrompt`, or `readResource` promise with its final result.

OAuth callbacks now validate issuer metadata through the v2 SDK. Discovery state and issuer-bound credentials persist across browser redirects and Durable Object hibernation.

#### Run stateless servers

`createMcpHandler` now accepts a factory that returns a server from `@modelcontextprotocol/server`. The factory creates an isolated server for each request.
    
    
    import { McpServer } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    
    function createServer() {
    	return new McpServer({ name: "example", version: "1.0.0" });
    }
    
    export default {
    	fetch(request, env, ctx) {
    		return createMcpHandler(createServer)(request, env, ctx);
    	},
    };
    
    
    import { McpServer } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    
    function createServer() {
    	return new McpServer({ name: "example", version: "1.0.0" });
    }
    
    export default {
    	fetch(request, env, ctx) {
    		return createMcpHandler(createServer)(request, env, ctx);
    	},
    } satisfies ExportedHandler;

The isolated `agents/mcp/server` entry keeps `McpAgent`, `WorkerTransport`, MCP client transports, and SDK v1 modules out of stateless server bundles.

The Workers wrapper validates present browser Origins, supports explicit delegation to trusted Origin middleware, and exposes request handling plus typed change notifications.

#### Backward compatibility

The same `createMcpHandler(createServer)(request, env, ctx)` route serves MCP 2026-07-28 clients and legacy clients that use stateless requests. You do not need separate routes or tool definitions for ordinary tools, prompts, and resources.

`McpAgent` is deprecated and feature-frozen. Migrate existing `McpAgent` servers to the stateless handler at your earliest convenience. If a server depends on protocol sessions, RPC, pushed server-to-client requests, standalone streams, or replay, use the [migration guide](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/) to design stateless equivalents and run both routes while clients transition.

#### Migrate existing SDK v1 servers

Upgrade the Agents SDK:

npmyarnpnpmbun
    
    
    npm i agents@latest
    
    
    yarn add agents@latest
    
    
    pnpm add agents@latest
    
    
    bun add agents@latest

Move ordinary SDK v1 server definitions into an SDK v2 factory and serve them with `createMcpHandler`. The handler's default legacy compatibility means most stateless deployments need only one route.

If an existing `McpAgent` server still needs sessionful features, add the stateless path beside it. Use `isLegacyRequest()` to send only legacy traffic to the existing route:
    
    
    import { isLegacyRequest } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    import { MyMcpAgent } from "./legacy-server";
    import { createServer } from "./server";
    
    const stateless = createMcpHandler(createServer, {
    	route: "/mcp",
    	legacy: "reject",
    });
    const legacy = MyMcpAgent.serve("/mcp");
    
    export default {
    	async fetch(request, env, ctx) {
    		if (await isLegacyRequest(request)) {
    			return legacy.fetch(request, env, ctx);
    		}
    		return stateless(request, env, ctx);
    	},
    };
    
    
    import { isLegacyRequest } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    import { MyMcpAgent } from "./legacy-server";
    import { createServer } from "./server";
    
    const stateless = createMcpHandler(createServer, {
    	route: "/mcp",
    	legacy: "reject",
    });
    const legacy = MyMcpAgent.serve("/mcp");
    
    export default {
    	async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    		if (await isLegacyRequest(request)) {
    			return legacy.fetch(request, env, ctx);
    		}
    		return stateless(request, env, ctx);
    	},
    } satisfies ExportedHandler<Env>;

Migrate the remaining sessionful features, allow existing sessions to drain, then remove the legacy route. Refer to [Migrate to MCP SDK v2](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/) for package changes, compatibility limits, and rollout steps.

#### Deprecations in v0.20.0

This release deprecates the following Agents SDK APIs:

Deprecated API | Replacement | Status  
---|---|---  
`McpAgent` | Use an SDK v2 factory with `createMcpHandler` for stateless servers. Use the migration guide to replace stateful features before removing a legacy route. | Feature-frozen. No removal version is announced.  
`createMcpHandler(v1Server, options)` | Move the server to an SDK v2 factory and call `createMcpHandler(factory, options)`. Use `createLegacyMcpHandler` only as a temporary bridge for sessionful features. | Scheduled for removal in the next major version.  
`MCPClientManager.callTool(params, resultSchema, options)` and the equivalent `withX402Client` overload | Use `callTool(params, options)` or `callTool(confirm, params, options)`. | Compatibility overload. No removal version is announced.  
  
The MCP 2026-07-28 draft separately deprecates Roots, Sampling, Logging, the old HTTP+SSE transport, and Dynamic Client Registration.

Jul 23, 2026

## [Agents SDK packages support AI SDK v6 and v7](https://developers.cloudflare.com/changelog/post/2026-07-23-ai-sdk-v6-v7-support/)

[Agents](https://developers.cloudflare.com/agents/)

The `agents`, `@cloudflare/ai-chat`, `@cloudflare/codemode`, and `@cloudflare/think` packages now support AI SDK v6 and v7. Existing applications can remain on v6 when updating these packages. Applications can also adopt v7 without changing the Cloudflare Agents APIs they use.

The supported peer ranges are `ai@^6 || ^7` and `@ai-sdk/react@^3 || ^4`. Use matching major versions: pair AI SDK v6 with `@ai-sdk/react` v3, or pair AI SDK v7 with `@ai-sdk/react` v4.

To install the latest packages with AI SDK v7:

npmyarnpnpmbun
    
    
    npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4
    
    
    yarn add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4
    
    
    pnpm add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4
    
    
    bun add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4

Think normalizes streaming, tool completion events, and telemetry across both AI SDK versions. Existing v6 applications do not need to migrate these integrations before updating Think.

For setup and usage details, refer to the [Think documentation](https://developers.cloudflare.com/agents/harnesses/think/).

Jul 22, 2026

## [Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs](https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

This release reduces repeated MCP schema conversion and adds an opt-out for Think's automatic MCP tool exposure. It also lets non-AI-SDK hosts invoke the durable Code Mode runtime directly.

#### Control direct MCP tool exposure in Think

Agents SDK MCP clients now reuse converted input and output schemas while a live connection keeps the same tool catalog. This avoids converting every MCP JSON Schema to Zod again for each model turn.

`@cloudflare/think` also adds `includeMcpTools`. Set it to `false` when you expose MCP tools through Code Mode or another mechanism outside Think's automatic tool set:
    
    
    import { Think } from "@cloudflare/think";
    
    export class MyAgent extends Think {
    	includeMcpTools = false;
    	waitForMcpConnections = true;
    }
    
    
    import { Think } from "@cloudflare/think";
    
    export class MyAgent extends Think<Env> {
    	includeMcpTools = false;
    	waitForMcpConnections = true;
    }

This setting skips Think's automatic `getAITools()` call. MCP registration, restoration, discovery, raw catalog access, direct calls, and Code Mode connectors continue to work.

Use [`listTools()`](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/#thismcplisttools) when you only need the raw MCP catalog. For connector setup, refer to [Use MCP tools with Code Mode](https://developers.cloudflare.com/agents/tools/codemode/mcp/).

#### Invoke the Code Mode runtime without the AI SDK

`@cloudflare/codemode@latest` adds `execute()`, `search()`, and `describe()` to the durable runtime handle. MCP servers and other hosts can now execute code and discover connector methods without adapting the runtime to an AI SDK tool.
    
    
    const matches = await runtime.search("create issue");
    const docs = await runtime.describe(matches.results[0].path);
    const outcome = await runtime.execute({
    	code: `async () => github.create_issue({ title: "Bug" })`,
    });
    
    
    const matches = await runtime.search("create issue");
    const docs = await runtime.describe(matches.results[0].path);
    const outcome = await runtime.execute({
    	code: `async () => github.create_issue({ title: "Bug" })`,
    });

Search and describe results include `requiresApproval: true` for protected connector methods. Resolve a paused execution with the existing `approve()` and `reject()` methods.

For setup and exact method types, refer to [Create a durable Code Mode runtime](https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/) and the [Code Mode API reference](https://developers.cloudflare.com/agents/tools/codemode/api-reference/).

#### Upgrade

npmyarnpnpmbun
    
    
    npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
    
    
    yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
    
    
    pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
    
    
    bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest

Jul 13, 2026

## [Agents can respond to MCP elicitation requests](https://developers.cloudflare.com/changelog/post/2026-07-13-mcp-client-elicitation/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Agents connected to Model Context Protocol (MCP) servers with [`addMcpServer`](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/) can now handle [elicitation ↗︎](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation) requests.

Elicitation lets an MCP server request user input while it handles a tool call. Form mode collects structured, non-sensitive data. URL mode asks for consent before opening an out-of-band flow, such as third-party authorization or payment.
    
    
    sequenceDiagram
        participant User
        participant Agent as Agent (MCP client)
        participant Server as MCP server
        participant Browser
    
        Server->>Agent: elicitation/create
        Agent->>User: Show server, reason, and input or URL
        User->>Agent: Submit, open, decline, or cancel
        Agent->>Browser: Open URL after consent (URL mode)
        Agent->>Server: accept, decline, or cancel
        Server-->>Agent: Optional URL completion notification
    

Register a handler for each mode your Agent supports in `onStart()`:
    
    
    import { Agent } from "agents";
    
    export class MyAgent extends Agent {
    	onStart() {
    		this.mcp.configureElicitationHandlers({
    			form: (request, serverId) => this.forwardToUser(request, serverId),
    			url: (request, serverId) => this.forwardToUser(request, serverId),
    		});
    	}
    
    	forwardToUser(request, serverId) {
    		// Show the request in your UI and resolve after the user responds.
    		throw new Error(
    			`Implement elicitation for ${serverId}: ${request.params.message}`,
    		);
    	}
    }
    
    
    import { Agent } from "agents";
    import type { ElicitRequest, ElicitResult } from "agents/mcp";
    
    export class MyAgent extends Agent<Env> {
    	onStart() {
    		this.mcp.configureElicitationHandlers({
    			form: (request, serverId) => this.forwardToUser(request, serverId),
    			url: (request, serverId) => this.forwardToUser(request, serverId),
    		});
    	}
    
    	private forwardToUser(
    		request: ElicitRequest,
    		serverId: string,
    	): Promise<ElicitResult> {
    		// Show the request in your UI and resolve after the user responds.
    		throw new Error(
    			`Implement elicitation for ${serverId}: ${request.params.message}`,
    		);
    	}
    }

Connections advertise only the modes with configured handlers. An Agent without handlers advertises no elicitation capability, which lets the server use its fallback. The SDK stores the advertised modes with each MCP server registration so they survive Durable Object hibernation. Callback functions remain in memory and reattach when `onStart()` runs.

For implementation details and a browser forwarding pattern, refer to [MCP client elicitation](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/#elicitation). The [`mcp-client` ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp-client) and [`mcp-elicitation` ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation) examples implement both sides.

#### Upgrade

To update to this release:

npmyarnpnpmbun
    
    
    npm i agents@latest
    
    
    yarn add agents@latest
    
    
    pnpm add agents@latest
    
    
    bun add agents@latest

Jun 26, 2026

## [Agents SDK adds background sub-agents and a unified turn entry point](https://developers.cloudflare.com/changelog/post/2026-06-26-agents-sdk-v0.17.0/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) makes it easier to run long work in the background, drive turns through one entry point, and keep chat agents working through deploys, evictions, and reconnects.

This release adds first-class detached (background) sub-agent runs with live progress and durable milestones, a single `runTurn` turn-admission entry point, and a large round of recovery and reliability fixes that continue converging `@cloudflare/think` and `@cloudflare/ai-chat` onto one model.

#### Background sub-agents with progress and milestones

`runAgentTool` can now dispatch a sub-agent without blocking the calling turn. A detached run returns a handle immediately and is owned by a durable, eviction-surviving backbone instead of being abandoned when the dispatching turn ends.
    
    
    class OrdersAgent extends Think {
    	async startImport(input) {
    		// Fire-and-forget, or wire a durable completion callback
    		// (by method name, like schedule()):
    		await this.runAgentTool(ImportAgent, {
    			input,
    			detached: { onFinish: "onImportDone", maxBudgetMs: 60 * 60 * 1000 },
    		});
    	}
    
    	// result.status: "completed" | "error" | "aborted" | "interrupted"
    	async onImportDone(run, result) {}
    }
    
    
    class OrdersAgent extends Think {
    	async startImport(input) {
    		// Fire-and-forget, or wire a durable completion callback
    		// (by method name, like schedule()):
    		await this.runAgentTool(ImportAgent, {
    			input,
    			detached: { onFinish: "onImportDone", maxBudgetMs: 60 * 60 * 1000 },
    		});
    	}
    
    	// result.status: "completed" | "error" | "aborted" | "interrupted"
    	async onImportDone(run, result) {}
    }

Highlights:

  * **Durable, exactly-once-on-the-happy-path completion** via a warm fast path plus a self-scheduling reconcile backbone that survives eviction and deploys.
  * **Bounded.** An absolute `maxBudgetMs` ceiling (default 24h) and `cancelAgentTool(runId)` keep abandoned runs from holding a concurrency slot forever.
  * **`detached: { notify: true }`** lets a finished background run inject a message back into the chat so the model reacts to the result — no hand-wired `onFinish` needed.



Sub-agents can also report mid-run progress that rides their own turn stream back to the parent's connected clients:
    
    
    // Inside the child sub-agent:
    await this.reportProgress({
    	fraction: 0.6,
    	phase: "deploying",
    	message: "Generating menu page…",
    });
    
    
    // Inside the child sub-agent:
    await this.reportProgress({
    	fraction: 0.6,
    	phase: "deploying",
    	message: "Generating menu page…",
    });

Progress surfaces on `AgentToolRunState.progress` via `useAgentToolEvents`, so a background-runs tray can render a live bar without drilling in, and the latest snapshot is persisted for inspection after eviction. Naming a `milestone` promotes a signal to a durable, replayable row, and `detached: { onMilestones }` can surface a milestone as a synthetic chat message (`"narrate"` for a cheap status line, or `"react"` to drive a model turn).

#### One entry point for turns: `runTurn`

`@cloudflare/think` adds a public `runTurn(options)` facade that unifies turn admission behind a single `mode`:
    
    
    await this.runTurn({ mode: "wait", messages }); // saveMessages / continueLastTurn
    await this.runTurn({ mode: "submit", messages }); // durable submitMessages
    await this.runTurn({ mode: "stream", messages }); // chat()
    
    
    await this.runTurn({ mode: "wait", messages }); // saveMessages / continueLastTurn
    await this.runTurn({ mode: "submit", messages }); // durable submitMessages
    await this.runTurn({ mode: "stream", messages }); // chat()

`stream` mode accepts array and function inputs to match `wait` mode, and all entry points now route through a shared internal admission path that throws a clear error on nested blocking admissions that previously could deadlock.

#### Recovery and reliability

A large part of this release continues hardening recovery and converging `@cloudflare/think` and `@cloudflare/ai-chat` onto one model:

  * **Stream stall watchdog.** `AIChatAgent` can detect and recover from a hung model/transport stream via the opt-in `chatStreamStallTimeoutMs` watchdog. With `chatRecovery` enabled the stall routes into the same bounded-recovery machinery a deploy or eviction uses; otherwise it surfaces as a terminal stream error so the spinner clears.
  * **Interrupted tool-call repair.** `AIChatAgent` now repairs a transcript with a dead server-tool call before re-entering inference (parity with `@cloudflare/think`), so a recovered turn no longer fails with `AI_MissingToolResultsError`. An overridable `repairInterruptedToolPart(part)` hook lets apps customize the repaired shape.
  * **Stuck status after reconnect.** Fixed AI SDK `status` getting stuck when a reconnect races a turn that has been accepted but has not started streaming yet, so the UI now renders the in-flight turn instead of settling on `ready`.
  * **Live "recovering…" on connect.** `AIChatAgent` now replays the recovering status to a client that connects mid-recovery, so `useAgentChat`'s `isRecovering` reflects in-progress recovery immediately instead of appearing frozen.
  * **Terminal connection failures.** The client stops reconnecting on terminal WebSocket close events and exposes them via `connectionError` / `onConnectionError` on `AgentClient`, `useAgent`, and `useAgentChat`.
  * **Agent-tool child recovery.** A healthy long-running sub-agent run is no longer abandoned as `interrupted` after a deploy (both `@cloudflare/think` and `AIChatAgent`).
  * **Workflows from sub-agent facets.** Agent Workflows can now start from sub-agent facets, with callbacks and Workflow RPC routed back to the originating facet.
  * Plus forward-progress crediting convergence, broadcast-first give-up ordering, an event-driven auto-continuation barrier, and structured row-size compaction in `AIChatAgent`.



#### Other improvements

  * **Shared chat React core.** A new `agents/chat/react` entry exposes `useAgentChat`, transport helpers, and shared wire types, with `syncMessagesToServer` for server-authoritative transcript storage. `@cloudflare/think/react` and `@cloudflare/ai-chat/react` are now thin wrappers over it.
  * **Optional`ai` peer.** The root `agents` and `@cloudflare/codemode` runtimes no longer reference AI SDK types, so they bundle without `ai` / `zod` installed; AI-specific entry points still require the peer when imported. `just-bash` likewise moves to an optional peer used only by the skills bash runner.
  * **Code Mode.** The default `DynamicWorkerExecutor` timeout increases from 30s to 60s, executions now dispose the dynamically-loaded Worker and its RPC stub after each run (fixing a flaky isolate-shutdown assertion), connector imports are cleaned up, and the outer MCP tool-call context is passed to `openApiMcpServer` request callbacks.
  * **Voice.** Voice turns now support AI SDK `fullStream` responses (and warn when `textStream` is used).
  * **MCP.** `McpAgent` server-to-client requests can now be sent from callbacks that do not inherit the agent's async context, including callbacks reached through Worker Loader RPC.
  * **Experimental: server actions and channels.** This release lays groundwork for guarded server actions (`action()` / `getActions()` with a durable replay ledger and approvals) and a unified channels surface (`configureChannels()`, `deliverNotice()`). Both are experimental and their APIs may change, so we don't recommend depending on them yet.



#### Upgrade

To update to the latest version:

npmyarnpnpmbun
    
    
    npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest
    
    
    yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest
    
    
    pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest
    
    
    bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest

Refer to the [Think documentation](https://developers.cloudflare.com/agents/harnesses/think/), [Code Mode documentation](https://developers.cloudflare.com/agents/tools/codemode/), and [Agents documentation](https://developers.cloudflare.com/agents/) for more information.

Jun 16, 2026

## [Agents SDK improves browser automation, code execution, and recovery](https://developers.cloudflare.com/changelog/post/2026-06-16-agents-sdk-v0.16.1/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) makes it easier to build agents that can safely interact with real systems and keep working through interruptions.

Agents can now browse websites through Browser Run, write code against external tools through Code Mode, use client-provided tools when delegating to Think sub-agents, and recover more reliably from deploys, Durable Object evictions, and connection churn.

#### Safer browser automation

Agents can now use [Browser Run](https://developers.cloudflare.com/browser-run/) through a single durable `browser_execute` tool. Instead of choosing from a fixed list of actions, the model writes code against the Chrome DevTools Protocol (CDP) and can inspect pages, capture screenshots, read rendered content, debug frontend behavior, and interact with live browser sessions.
    
    
    const browserTools = createBrowserTools({
    	ctx: this.ctx,
    	browser: this.env.BROWSER,
    	loader: this.env.LOADER,
    	session: { mode: "dynamic" },
    });
    
    
    const browserTools = createBrowserTools({
    	ctx: this.ctx,
    	browser: this.env.BROWSER,
    	loader: this.env.LOADER,
    	session: { mode: "dynamic" },
    });

Browser sessions can be one-time, reused, or promoted from one-time to persistent during a run. This is useful when an agent needs a human to log in, complete MFA, or approve a sensitive action. The run can pause, keep the same tabs and cookies, and resume after approval.

The browser tools also add Live View URLs, optional session recording, and quick actions such as `browser_markdown`, `browser_extract`, `browser_links`, and `browser_scrape` for one-shot browsing tasks.

#### Resumable code execution with approvals

Code Mode now uses `createCodemodeRuntime`, connectors, and a durable execution log. This lets you give a model one `codemode` tool instead of a large prompt full of tool definitions. The model can discover the capabilities it needs, write code against typed globals, and reuse saved snippets.
    
    
    const runtime = createCodemodeRuntime({
    	ctx: this.ctx,
    	executor: new DynamicWorkerExecutor({ loader: this.env.LOADER }),
    	connectors: [new GithubConnector(this.ctx, this.env, connection)],
    });
    
    const result = streamText({
    	model,
    	messages,
    	tools: { codemode: runtime.tool() },
    });
    
    
    const runtime = createCodemodeRuntime({
    	ctx: this.ctx,
    	executor: new DynamicWorkerExecutor({ loader: this.env.LOADER }),
    	connectors: [new GithubConnector(this.ctx, this.env, connection)],
    });
    
    const result = streamText({
    	model,
    	messages,
    	tools: { codemode: runtime.tool() },
    });

When the code reaches an approval-gated action, the runtime pauses execution and returns a pending approval. After approval, completed calls replay from the durable log, the approved action runs, and the same code continues. This makes it practical to build agents that create issues, update external systems, or perform other side effects without custom pause-and-resume logic for every tool.

#### Better Think delegation

Think sub-agents can now use client-defined tools over the RPC `chat()` path. A parent agent can pass tool schemas with `clientTools` and resolve tool calls through `onClientToolCall`. This lets delegated agents use caller-provided capabilities without requiring a browser WebSocket.
    
    
    await child.chat(message, callback, {
    	signal,
    	clientTools: [
    		{
    			name: "get_user_timezone",
    			description: "Get the caller's timezone",
    			parameters: { type: "object" },
    		},
    	],
    	onClientToolCall: async ({ toolName, input }) => {
    		return runClientTool(toolName, input);
    	},
    });
    
    
    await child.chat(message, callback, {
    	signal,
    	clientTools: [
    		{
    			name: "get_user_timezone",
    			description: "Get the caller's timezone",
    			parameters: { type: "object" },
    		},
    	],
    	onClientToolCall: async ({ toolName, input }) => {
    		return runClientTool(toolName, input);
    	},
    });

Think Workflows also improve `step.prompt()`. A prompt step now runs a full agentic turn before returning structured output, so the agent can call tools before producing the typed result. This makes Workflow steps more useful for durable triage, research, and approval flows.

The unified Think execute tool can also include `cdp.*` browser capabilities alongside `state.*` and `tools.*` when Browser Run is bound.

#### Voice output device selection

Voice clients can route assistant audio to a specific output device. Use `outputDeviceId` with `useVoiceAgent`, or call `client.setOutputDevice()` from the framework-agnostic client.
    
    
    const voice = useVoiceAgent({
    	agent: "MyVoiceAgent",
    	outputDeviceId: selectedSpeakerId,
    });
    
    
    const voice = useVoiceAgent({
    	agent: "MyVoiceAgent",
    	outputDeviceId: selectedSpeakerId,
    });

Browsers without speaker-selection support continue playing through the default output device and report a non-fatal `outputDeviceError`.

#### Reliability fixes

This release includes several fixes for production agents:

  * `useAgent` and `AgentClient` handle WebSocket replacement more reliably during reconnects and configuration changes.
  * Chat stream replay is more reliable after reconnects, deploys, and provider errors.
  * Fiber recovery continues across multi-pass scans and backs off when recovery hooks keep failing.
  * Agent teardown continues even when the request that started teardown is canceled.
  * Large session histories use byte-budgeted reads to reduce memory pressure during startup.



#### Upgrade

To update to the latest version:

npmyarnpnpmbun
    
    
    npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest
    
    
    yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest
    
    
    pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest
    
    
    bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest

Refer to the [Code Mode documentation](https://developers.cloudflare.com/agents/tools/codemode/), [Browser tools documentation](https://developers.cloudflare.com/agents/tools/browser/), [Think tools documentation](https://developers.cloudflare.com/agents/harnesses/think/tools/), and [Voice documentation](https://developers.cloudflare.com/agents/communication-channels/voice/) for more information.

Jun 16, 2026

## [Introducing GLM-5.2 on Workers AI](https://developers.cloudflare.com/changelog/post/2026-06-16-glm-5.2-workers-ai/)

[Workers](https://developers.cloudflare.com/workers/)[Agents](https://developers.cloudflare.com/agents/)[Workers AI](https://developers.cloudflare.com/workers-ai/)

We are excited to announce **GLM-5.2** on Workers AI, Z.ai's flagship agentic coding model.

[`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/) is a text generation model built for agentic coding workflows. With function calling and reasoning support, it can handle long codebases, multi-step planning, and tool-augmented agents.

**Key features and use cases:**

  * **Agentic coding** : Designed for autonomous coding tasks, long-horizon planning, and complex software engineering workflows
  * **Large context window** : GLM-5.2 supports up to a 1,048,576 token context window. Workers AI is launching the model with a 262,144 token context window and plans to increase this in the future
  * **Function calling** : Build agents that invoke tools and APIs across multiple conversation turns
  * **Reasoning** : Tackles complex problem-solving and step-by-step reasoning tasks



Use GLM-5.2 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

Pricing is available on the [model page](https://developers.cloudflare.com/workers-ai/models/glm-5.2/) or [pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Jun 2, 2026

## [Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery](https://developers.cloudflare.com/changelog/post/2026-06-02-agents-sdk-v0.14.0/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) adds four new ways to build with `@cloudflare/think`: on-demand Agent Skills, chat messengers (starting with Telegram), declarative scheduled tasks, and durable reasoning steps inside Workflows. This release also significantly hardens durable chat recovery, so turns reliably ride through deploys, evictions, and stalled model streams in production.

#### Agent Skills (experimental)

Give an agent a catalog of on-demand instructions, resources, and scripts. A skill source adds a catalog to the system prompt, and the model activates a skill only when a task matches — so a large library of capabilities does not bloat every prompt.
    
    
    import { Think, skills } from "@cloudflare/think";
    import bundledSkills from "agents:skills";
    
    export class SkillsAgent extends Think {
    	getSkills() {
    		return [
    			bundledSkills,
    			skills.r2(this.env.SKILLS_BUCKET, { prefix: "skills/" }),
    		];
    	}
    }
    
    
    import { Think, skills } from "@cloudflare/think";
    import bundledSkills from "agents:skills";
    
    export class SkillsAgent extends Think<Env> {
    	getSkills() {
    		return [
    			bundledSkills,
    			skills.r2(this.env.SKILLS_BUCKET, { prefix: "skills/" }),
    		];
    	}
    }

The `agents:skills` import bundles a local `./skills` directory through the Agents Vite plugin (one directory per skill, each with a `SKILL.md`). Skills can also load from R2 or a manifest. When skills are available, Think exposes `activate_skill`, `read_skill_resource`, and an optional `run_skill_script` tool. Skill loading is resilient: a duplicate or failing source is skipped with a warning instead of breaking the agent.

Agent Skills are **experimental** , and script execution in particular is early. The API may change in a future release. We would love your feedback — tell us what you are building and what is missing in the [Agents repository ↗︎](https://github.com/cloudflare/agents/discussions).

#### Messengers

Connect a Think agent directly to a chat platform. Think owns the webhook route, conversation routing, durable reply fiber, and streamed delivery back to the provider. Telegram ships as the first provider.
    
    
    import { Think } from "@cloudflare/think";
    import {
    	defineMessengers,
    	ThinkMessengerStateAgent,
    } from "@cloudflare/think/messengers";
    import telegramMessenger from "@cloudflare/think/messengers/telegram";
    
    export { ThinkMessengerStateAgent };
    
    export class SupportAgent extends Think {
    	getMessengers() {
    		return defineMessengers({
    			telegram: telegramMessenger({
    				token: this.env.TELEGRAM_BOT_TOKEN,
    				userName: "support_bot",
    				secretToken: this.env.TELEGRAM_WEBHOOK_SECRET_TOKEN,
    			}),
    		});
    	}
    }
    
    
    import { Think } from "@cloudflare/think";
    import {
    	defineMessengers,
    	ThinkMessengerStateAgent,
    } from "@cloudflare/think/messengers";
    import telegramMessenger from "@cloudflare/think/messengers/telegram";
    
    export { ThinkMessengerStateAgent };
    
    export class SupportAgent extends Think<Env> {
    	getMessengers() {
    		return defineMessengers({
    			telegram: telegramMessenger({
    				token: this.env.TELEGRAM_BOT_TOKEN,
    				userName: "support_bot",
    				secretToken: this.env.TELEGRAM_WEBHOOK_SECRET_TOKEN,
    			}),
    		});
    	}
    }

Each Chat SDK thread maps to its own Think sub-agent by default, so group chats and direct messages do not share memory. Multiple bots, custom conversation routing, and custom providers are all supported.

#### Scheduled tasks

Declare recurring, timezone-aware prompts and handlers with a typed domain-specific language (DSL). Think reconciles the declarations on startup and re-arms the next occurrence after each run, backed by durable idempotent submissions.
    
    
    import { Think, defineScheduledTasks } from "@cloudflare/think";
    
    export class DigestAgent extends Think {
    	getScheduledTasks() {
    		return defineScheduledTasks({
    			weeklyCommitReport: {
    				schedule: "every week on monday at 09:00",
    				prompt:
    					"Compile my GitHub commits for the last week and summarize them.",
    			},
    			workout: {
    				schedule: "every day at 08:00 in Europe/London",
    				prompt: "Start my workout.",
    			},
    		});
    	}
    }
    
    
    import { Think, defineScheduledTasks } from "@cloudflare/think";
    
    export class DigestAgent extends Think<Env> {
    	getScheduledTasks() {
    		return defineScheduledTasks({
    			weeklyCommitReport: {
    				schedule: "every week on monday at 09:00",
    				prompt:
    					"Compile my GitHub commits for the last week and summarize them.",
    			},
    			workout: {
    				schedule: "every day at 08:00 in Europe/London",
    				prompt: "Start my workout.",
    			},
    		});
    	}
    }

#### Think Workflows

Run a model-driven reasoning step inside a Cloudflare Workflow with `ThinkWorkflow` and `step.prompt()`, with durable typed structured output, long waits, and approval gates.
    
    
    import { z } from "zod";
    import { ThinkWorkflow } from "@cloudflare/think/workflows";
    
    const draftSchema = z.object({
    	title: z.string(),
    	summary: z.string(),
    	labels: z.array(z.string()),
    });
    
    export class TriageWorkflow extends ThinkWorkflow {
    	async run(event, step) {
    		const draft = await step.prompt("triage-issue", {
    			prompt: `Triage issue #${event.payload.issueNumber}`,
    			output: draftSchema,
    			timeout: "3 days",
    		});
    
    		await step.do("apply-labels", async () => {
    			await this.agent.applyLabels(draft.labels);
    		});
    	}
    }
    
    
    import { z } from "zod";
    import { ThinkWorkflow } from "@cloudflare/think/workflows";
    import type { ThinkWorkflowStep } from "@cloudflare/think/workflows";
    import type { AgentWorkflowEvent } from "agents/workflows";
    
    const draftSchema = z.object({
    	title: z.string(),
    	summary: z.string(),
    	labels: z.array(z.string()),
    });
    
    export class TriageWorkflow extends ThinkWorkflow<TriageAgent, Params> {
    	async run(event: AgentWorkflowEvent<Params>, step: ThinkWorkflowStep) {
    		const draft = await step.prompt("triage-issue", {
    			prompt: `Triage issue #${event.payload.issueNumber}`,
    			output: draftSchema,
    			timeout: "3 days",
    		});
    
    		await step.do("apply-labels", async () => {
    			await this.agent.applyLabels(draft.labels);
    		});
    	}
    }

#### Production hardening for durable chat recovery

Durable chat turns have always been designed to survive a mid-turn deploy or Durable Object eviction. This release is a major hardening pass on that machinery for production.

  * **Better recovery during deploys.** Turns now ride through continuous deploys and evictions without losing completed work or re-running tools that already ran.
  * **A live "recovering…" signal.** `useAgentChat` exposes a new `isRecovering` flag, so a recovering turn shows progress instead of looking frozen. Most UIs render `isStreaming || isRecovering` as "busy".
  * **Stalled streams recover.** Set `chatStreamStallTimeoutMs` to route a hung provider stream into the same recovery path instead of leaving an infinite spinner.
  * **Sub-agents re-attach.** On parent recovery, an in-flight `agentTool()` child is re-attached to its result rather than abandoned and re-run, so long-running children no longer lose work under deploys.



#### MCP transport improvements

  * **Resumable streams** — In-flight tool calls over Server-Sent Events (SSE) survive a dropped connection. Clients reconnect with `Last-Event-ID` and replay anything they missed.
  * **Readable server IDs** — `addMcpServer` accepts an optional `id`, so tools surface as readable keys (for example `tool_github_create_pull_request`) instead of opaque connection IDs.
  * **Better handling of concurrent requests** — Overlapping JSON-RPC requests are now correctly correlated to their responses across the HTTP and RPC transports.



#### Other improvements

  * **Compaction** — A `Session`'s `tokenCounter` now also drives the compaction boundary decision ("what to compress"), not just the fire/no-fire trigger.
  * **`@cloudflare/worker-bundler`** — Adds a `virtualModules` option to `createWorker` to provide in-memory module source during bundling.
  * **Client-tool continuations** — Parallel tool results now coalesce into a single continuation, immediate resume requests attach to the pending continuation, and server-side `needsApproval` continuations resume reliably after approval.



#### Upgrade

To update to the latest version:

npmyarnpnpmbun
    
    
    npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest
    
    
    yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest
    
    
    pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest
    
    
    bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest

Refer to the [Agents API reference](https://developers.cloudflare.com/agents/runtime/) and [Chat agents documentation](https://developers.cloudflare.com/agents/communication-channels/chat/chat-agents/) for more information.

May 29, 2026

## [Share sandbox previews through Cloudflare Tunnel](https://developers.cloudflare.com/changelog/post/2026-05-29-sandbox-named-tunnels/)

[Agents](https://developers.cloudflare.com/agents/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) can expose a service running inside the container on a public preview URL through the `sandbox.tunnels` namespace. The SDK uses `cloudflared` inside the sandbox so you can share a running service without configuring `exposePort()` or a custom domain.

By default, `sandbox.tunnels.get(port)` creates a [quick tunnel ↗︎](https://try.cloudflare.com/) on a zero-config `*.trycloudflare.com` URL — no Cloudflare account, DNS record, or custom domain required. This is perfect for quick development and for `.workers.dev` deployments.
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    await sandbox.startProcess("python -m http.server 8080");
    
    const tunnel = await sandbox.tunnels.get(8080);
    console.log(tunnel.url); // → https://random-words-here.trycloudflare.com
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    await sandbox.startProcess("python -m http.server 8080");
    
    const tunnel = await sandbox.tunnels.get(8080);
    console.log(tunnel.url); // → https://random-words-here.trycloudflare.com

#### Named tunnels

For more control you can create a named tunnel through `sandbox.tunnels.get(port, { name })`. A named tunnel binds a hostname (`<name>.<your-zone>`) backed by a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) and a CNAME record on your zone resulting in something like <https://my-app-preview.example.com>[ ↗︎](https://my-app-preview.example.com).

Unlike quick tunnels, which generate a new random URL each time, a named tunnel produces a persistent URL that survives container restarts. This makes named tunnels suitable for production use cases where you want control over the tunnel and it's origin.
    
    
    const tunnel = await sandbox.tunnels.get(8080, { name: "my-app-preview" });
    console.log(tunnel.url); // → https://my-app-preview.example.com
    
    
    const tunnel = await sandbox.tunnels.get(8080, { name: "my-app-preview" });
    console.log(tunnel.url); // → https://my-app-preview.example.com

Calling `sandbox.destroy()` tears down the Cloudflare Tunnel and the associated DNS record alongside the container, so you do not leave dangling tunnels or records behind.

#### Upgrade

To update to the latest version:

npmyarnpnpmbun
    
    
    npm i @cloudflare/sandbox@latest
    
    
    yarn add @cloudflare/sandbox@latest
    
    
    pnpm add @cloudflare/sandbox@latest
    
    
    bun add @cloudflare/sandbox@latest

For full API details, refer to the [Sandbox tunnels reference](https://developers.cloudflare.com/sandbox/api/tunnels/).

May 13, 2026

## [Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control](https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) brings more reliable chat recovery, fixes Agent state synchronization during reconnects, adds durable submissions for Think, exposes routing retry configuration, and adds connection control for Voice agents.

#### Chat recovery improvements

`@cloudflare/ai-chat` now keeps server turns running when a browser or client stream is interrupted. This is useful for long-running AI responses where users refresh the page, close a tab, or temporarily lose connection. Calling `stop()` still cancels the server turn.

Set `cancelOnClientAbort: true` if browser or client aborts should also cancel the server turn:
    
    
    const chat = useAgentChat({
    	agent: "assistant",
    	name: "user-123",
    	cancelOnClientAbort: true,
    });
    
    
    const chat = useAgentChat({
    	agent: "assistant",
    	name: "user-123",
    	cancelOnClientAbort: true,
    });

Notable bug fixes:

  * Chat stream resume negotiation no longer throws when replay races with a closed WebSocket connection.
  * Recovered chat continuations no longer leave `useAgentChat` stuck in a streaming state when the original socket disconnects before a terminal response.
  * Approval auto-continuation preserves reasoning parts and persists continuation reasoning in the final message.
  * `isServerStreaming` now resets correctly when a resumed stream moves from the fallback observer path to a transport-owned stream.



#### Agent state and routing fixes

`agents@0.12.4` prevents duplicate initial state frames during WebSocket connection setup. This avoids stale initial state messages overwriting state updates already sent by the client.

Agent recovery is also more reliable when tool calls span a Durable Object restart. Recovery now defers user finish hooks until after agent startup and isolates hook failures, so one failed hook does not block other recovered runs from finalizing.

`getAgentByName()` now supports `routingRetry` for transient Durable Object routing failures:
    
    
    import { getAgentByName } from "agents";
    
    const agent = await getAgentByName(env.AssistantAgent, "user-123", {
    	routingRetry: {
    		maxAttempts: 3,
    	},
    });
    
    
    import { getAgentByName } from "agents";
    
    const agent = await getAgentByName(env.AssistantAgent, "user-123", {
    	routingRetry: {
    		maxAttempts: 3,
    	},
    });

#### Durable Think submissions

`@cloudflare/think` now supports durable programmatic submissions. `submitMessages()` provides durable acceptance, idempotent retries, status inspection, cancellation, and cleanup for server-driven turns that should continue after the caller returns.

`Think.chat()` RPC turns now run inside chat recovery fibers and persist their stream chunks. Interrupted sub-agent turns can recover partial output instead of starting over.

`ChatOptions.tools` has been removed from the TypeScript API. Define durable tools on the child agent or use agent tools for orchestration. Runtime `options.tools` values passed by legacy callers are ignored with a warning.

#### Think message pruning behavior change

`@cloudflare/think` no longer applies `pruneMessages({ toolCalls: "before-last-2-messages" })` to model context by default. The previous default could strip client-side tool results from longer multi-turn flows.

`truncateOlderMessages` still runs as before, so context cost remains bounded. Subclasses that relied on the old aggressive pruning can opt back in from `beforeTurn`:
    
    
    import { Think } from "@cloudflare/think";
    import { pruneMessages } from "ai";
    
    export class MyAgent extends Think {
    	beforeTurn(ctx) {
    		return {
    			messages: pruneMessages({
    				messages: ctx.messages,
    				toolCalls: "before-last-2-messages",
    			}),
    		};
    	}
    }
    
    
    import { Think } from "@cloudflare/think";
    import { pruneMessages } from "ai";
    
    export class MyAgent extends Think<Env> {
    	beforeTurn(ctx) {
    		return {
    			messages: pruneMessages({
    				messages: ctx.messages,
    				toolCalls: "before-last-2-messages",
    			}),
    		};
    	}
    }

#### Voice agent connection control

`@cloudflare/voice` adds an `enabled` option to `useVoiceAgent`. React apps can now delay creating and connecting a `VoiceClient` until prerequisites such as capability tokens are ready.
    
    
    const voice = useVoiceAgent({
    	agent: "MyVoiceAgent",
    	enabled: Boolean(token),
    });
    
    
    const voice = useVoiceAgent({
    	agent: "MyVoiceAgent",
    	enabled: Boolean(token),
    });

This release also fixes Workers AI speech-to-text session edge cases and `withVoice` text streaming from AI SDK `textStream` responses.

#### Other improvements

  * **Streamable HTTP routing** — Server-to-client requests now route through the originating POST stream when no standalone SSE stream is available.
  * **Structured tool output** — Tool output shapes are preserved when truncating older messages or oversized persisted rows.
  * **Non-chat Think tool steps** — Think agent-tool children can complete without emitting assistant text and can return structured output through `getAgentToolOutput`.
  * **Sub-agent schedules** — Stale sub-agent schedule rows are pruned when their owning facet registry entry no longer exists.
  * **`@cloudflare/codemode`** — Adds a browser-safe export with an iframe sandbox executor and resolves OpenAPI specs inside the sandbox to avoid Worker Loader RPC size limits.



#### Upgrade

To update to the latest version:
    
    
    npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/think@latest @cloudflare/voice@latest

Refer to the [Agents API reference](https://developers.cloudflare.com/agents/runtime/) and [Chat agents documentation](https://developers.cloudflare.com/agents/communication-channels/chat/chat-agents/) for more information.

Apr 15, 2026

## [Agent Lee adds Write Operations and Generative UI](https://developers.cloudflare.com/changelog/post/2026-04-15-agentlee-writeops-genui/)

[Agents](https://developers.cloudflare.com/agents/)

#### Agent Lee adds Write Operations and Generative UI

We are excited to announce two major capability upgrades for **Agent Lee** , the AI co-pilot built directly into the Cloudflare dashboard. Agent Lee is designed to understand your specific account configuration, and with this release, it moves from a passive advisor to an active assistant that can help you manage your infrastructure and visualize your data through natural language.

#### Take action with Write Operations

Agent Lee can now perform changes on your behalf across your Cloudflare account. Whether you need to update DNS records, modify SSL/TLS settings, or configure Workers routes, you can simply ask.

To ensure security and accuracy, every write operation requires **explicit user approval**. Before any change is committed, Agent Lee will present a summary of the proposed action in plain language. No action is taken until you select **Confirm** , and this approval requirement is enforced at the infrastructure level to prevent unauthorized changes.

**Example requests:**

  * _"Add an A record for blog.example.com pointing to 192.0.2.10."_
  * _"Enable Always Use HTTPS on my zone."_
  * _"Set the SSL mode for example.com to Full (strict)."_



#### Visualize data with Generative UI

Understanding your traffic and security trends is now as easy as asking a question. Agent Lee now features **Generative UI** , allowing it to render inline charts and structured data visualizations directly within the chat interface using your actual account telemetry.

**Example requests:**

  * _"Show me a chart of my traffic over the last 7 days."_
  * _"What does my error rate look like for the past 24 hours?"_
  * _"Graph my cache hit rate for example.com this week."_



* * *

#### Availability

These features are currently available in **Beta** for all users on the **Free plan**. To get started, log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) and select **Ask AI** in the upper right corner.

To learn more about how to interact with your account using AI, refer to the [Agent Lee documentation](https://developers.cloudflare.com/agent-lee/).

Apr 13, 2026

## [Secure credential injection and dynamic egress policies for Sandboxes](https://developers.cloudflare.com/changelog/post/2026-04-13-sandbox-outbound-workers-tls-auth/)

[Containers](https://developers.cloudflare.com/containers/)[Agents](https://developers.cloudflare.com/agents/)

Outbound Workers for [Sandboxes](https://developers.cloudflare.com/sandbox/) and [Containers](https://developers.cloudflare.com/containers/) now support zero-trust credential injection, TLS interception, allow/deny lists, and dynamic per-instance egress policies. These features give platforms running agentic workloads full control over what leaves the sandbox, without exposing secrets to untrusted workloads, like user-generated code or coding agents.

#### Credential injection

Because outbound handlers run in the Workers runtime, outside the sandbox, they can hold secrets the sandbox never sees. A sandboxed workload can make a plain request, and credentials are transparently attached before a request is forwarded upstream.

For instance, you could run an agent in a sandbox and ensure that any requests it makes to Github are authenticated. But it will never be able to access the credentials:
    
    
    export class MySandbox extends Sandbox {}
    
    MySandbox.outboundByHost = {
    	"github.com": (request: Request, env: Env, ctx: OutboundHandlerContext) => {
    		const requestWithAuth = new Request(request);
    		requestWithAuth.headers.set("x-auth-token", env.SECRET);
    		return fetch(requestWithAuth);
    	},
    };

You can easily inject unique credentials for different instances by using `ctx.containerId`:
    
    
    MySandbox.outboundByHost = {
    	"my-internal-vcs.dev": async (
    		request: Request,
    		env: Env,
    		ctx: OutboundHandlerContext,
    	) => {
    		const authKey = await env.KEYS.get(ctx.containerId);
    
    		const requestWithAuth = new Request(request);
    		requestWithAuth.headers.set("x-auth-token", authKey);
    		return fetch(requestWithAuth);
    	},
    };

No token is ever passed into the sandbox. You can rotate secrets in the Worker environment and every request will pick them up immediately.

#### TLS interception

Outbound Workers now intercept HTTPS traffic. A unique ephemeral certificate authority (CA) and private key are created for each sandbox instance. The CA is placed into the sandbox and trusted by default. The ephemeral private key never leaves the container runtime sidecar process and is never shared across instances.

With TLS interception active, outbound Workers can act as a transparent proxy for both HTTP and HTTPS traffic.

#### Allow and deny hosts

Easily filter outbound traffic with `allowedHosts` and `deniedHosts`. When `allowedHosts` is set, it becomes a deny-by-default allowlist. Both properties support glob patterns.
    
    
    export class MySandbox extends Sandbox {
    	allowedHosts = ["github.com", "npmjs.org"];
    }

#### Dynamic outbound handlers

Define named outbound handlers then apply or remove them at runtime using `setOutboundHandler()` or `setOutboundByHost()`. This lets you change egress policy for a running sandbox without restarting it.
    
    
    export class MySandbox extends Sandbox {}
    
    MySandbox.outboundHandlers = {
    	allowHosts: async (req: Request, env: Env, ctx: OutboundHandlerContext ) => {
    		const url = new URL(req.url);
    		if (ctx.params.allowedHostnames.includes(url.hostname)) {
    			return fetch(req);
    		}
    		return new Response(null, { status: 403 });
    	},
    
    	noHttp: async () => {
    		return new Response(null, { status: 403 });
    	},
    };

Apply handlers programmatically from your Worker:
    
    
    const sandbox = getSandbox(env.Sandbox, userId);
    
    // Open network for setup
    await sandbox.setOutboundHandler("allowHosts", {
    	allowedHostnames: ["github.com", "npmjs.org"],
    });
    await sandbox.exec("npm install");
    
    // Lock down after setup
    await sandbox.setOutboundHandler("noHttp");

Handlers accept `params`, so you can customize behavior per instance without defining separate handler functions.

#### Get started

Upgrade to `@cloudflare/containers@0.3.0` or `@cloudflare/sandbox@0.8.9` to use these features.

For more details, refer to [Sandbox outbound traffic](https://developers.cloudflare.com/sandbox/guides/outbound-traffic/) and [Container outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/).

Mar 23, 2026

## [Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4](https://developers.cloudflare.com/changelog/post/2026-03-23-agents-sdk-v0.8.0/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) exposes agent state as a readable property, prevents duplicate schedule rows across Durable Object restarts, brings full TypeScript inference to `AgentClient`, and migrates to Zod 4.

#### Readable `state` on `useAgent` and `AgentClient`

Both `useAgent` (React) and `AgentClient` (vanilla JS) now expose a `state` property that reflects the current agent state. Previously, reading state required manually tracking it through the `onStateUpdate` callback.

**React (`useAgent`)**
    
    
    const agent = useAgent({
    	agent: "game-agent",
    	name: "room-123",
    });
    
    // Read state directly — no separate useState + onStateUpdate needed
    return <div>Score: {agent.state?.score}</div>;
    
    // Spread for partial updates
    agent.setState({ ...agent.state, score: (agent.state?.score ?? 0) + 10 });
    
    
    const agent = useAgent<GameAgent, GameState>({
    	agent: "game-agent",
    	name: "room-123",
    });
    
    // Read state directly — no separate useState + onStateUpdate needed
    return <div>Score: {agent.state?.score}</div>;
    
    // Spread for partial updates
    agent.setState({ ...agent.state, score: (agent.state?.score ?? 0) + 10 });

`agent.state` is reactive — the component re-renders when state changes from either the server or a client-side `setState()` call.

**Vanilla JS (`AgentClient`)**
    
    
    const client = new AgentClient({
    	agent: "game-agent",
    	name: "room-123",
    	host: "your-worker.workers.dev",
    });
    
    client.setState({ score: 100 });
    console.log(client.state); // { score: 100 }
    
    
    const client = new AgentClient<GameAgent>({
    	agent: "game-agent",
    	name: "room-123",
    	host: "your-worker.workers.dev",
    });
    
    client.setState({ score: 100 });
    console.log(client.state); // { score: 100 }

State starts as `undefined` and is populated when the server sends the initial state on connect (from `initialState`) or when `setState()` is called. Use optional chaining (`agent.state?.field`) for safe access. The `onStateUpdate` callback continues to work as before — the new `state` property is additive.

#### Idempotent `schedule()`

`schedule()` now supports an `idempotent` option that deduplicates by `(type, callback, payload)`, preventing duplicate rows from accumulating when called in places that run on every Durable Object restart such as `onStart()`.

**Cron schedules are idempotent by default.** Calling `schedule("0 * * * *", "tick")` multiple times with the same callback, expression, and payload returns the existing schedule row instead of creating a new one. Pass `{ idempotent: false }` to override.

Delayed and date-scheduled types support opt-in idempotency:
    
    
    import { Agent } from "agents";
    
    class MyAgent extends Agent {
    	async onStart() {
    		// Safe across restarts — only one row is created
    		await this.schedule(60, "maintenance", undefined, { idempotent: true });
    	}
    }
    
    
    import { Agent } from "agents";
    
    class MyAgent extends Agent {
    	async onStart() {
    		// Safe across restarts — only one row is created
    		await this.schedule(60, "maintenance", undefined, { idempotent: true });
    	}
    }

Two new warnings help catch common foot-guns:

  * Calling `schedule()` inside `onStart()` without `{ idempotent: true }` emits a `console.warn` with actionable guidance (once per callback; skipped for cron and when `idempotent` is set explicitly).
  * If an alarm cycle processes 10 or more stale one-shot rows for the same callback, the SDK emits a `console.warn` and a `schedule:duplicate_warning` diagnostics channel event.



#### Typed `AgentClient` with `call` inference and `stub` proxy

`AgentClient` now accepts an optional agent type parameter for full type inference on RPC calls, matching the typed experience already available with `useAgent`.
    
    
    const client = new AgentClient({
    	agent: "my-agent",
    	host: window.location.host,
    });
    
    // Typed call — method name autocompletes, args and return type inferred
    const value = await client.call("getValue");
    
    // Typed stub — direct RPC-style proxy
    await client.stub.getValue();
    await client.stub.add(1, 2);
    
    
    const client = new AgentClient<MyAgent>({
    	agent: "my-agent",
    	host: window.location.host,
    });
    
    // Typed call — method name autocompletes, args and return type inferred
    const value = await client.call("getValue");
    
    // Typed stub — direct RPC-style proxy
    await client.stub.getValue();
    await client.stub.add(1, 2);

State is automatically inferred from the agent type, so `onStateUpdate` is also typed:
    
    
    const client = new AgentClient({
    	agent: "my-agent",
    	host: window.location.host,
    	onStateUpdate: (state) => {
    		// state is typed as MyAgent's state type
    	},
    });
    
    
    const client = new AgentClient<MyAgent>({
    	agent: "my-agent",
    	host: window.location.host,
    	onStateUpdate: (state) => {
    		// state is typed as MyAgent's state type
    	},
    });

Existing untyped usage continues to work without changes. The RPC type utilities (`AgentMethods`, `AgentStub`, `RPCMethods`) are now exported from `agents/client` for advanced typing scenarios. `agents`, `@cloudflare/ai-chat`, and `@cloudflare/codemode` now require `zod ^4.0.0`. Zod v3 is no longer supported.

#### `@cloudflare/ai-chat` fixes

  * **Turn serialization** — `onChatMessage()` and `_reply()` work is now queued so user requests, tool continuations, and `saveMessages()` never stream concurrently.
  * **Duplicate messages on stop** — Clicking stop during an active stream no longer splits the assistant message into two entries.
  * **Duplicate messages after tool calls** — Orphaned client IDs no longer leak into persistent storage.



#### `keepAlive()` and `keepAliveWhile()` are no longer experimental

`keepAlive()` now uses a lightweight in-memory ref count instead of schedule rows. Multiple concurrent callers share a single alarm cycle. The `@experimental` tag has been removed from both `keepAlive()` and `keepAliveWhile()`.

#### `@cloudflare/codemode`: TanStack AI integration

A new entry point `@cloudflare/codemode/tanstack-ai` adds support for [TanStack AI's ↗︎](https://tanstack.com/ai) `chat()` as an alternative to the Vercel AI SDK's `streamText()`:
    
    
    import {
    	createCodeTool,
    	tanstackTools,
    } from "@cloudflare/codemode/tanstack-ai";
    import { chat } from "@tanstack/ai";
    
    const codeTool = createCodeTool({
    	tools: [tanstackTools(myServerTools)],
    	executor,
    });
    
    const stream = chat({ adapter, tools: [codeTool], messages });
    
    
    import { createCodeTool, tanstackTools } from "@cloudflare/codemode/tanstack-ai";
    import { chat } from "@tanstack/ai";
    
    const codeTool = createCodeTool({
    	tools: [tanstackTools(myServerTools)],
    	executor,
    });
    
    const stream = chat({ adapter, tools: [codeTool], messages });

#### Upgrade

To update to the latest version:
    
    
    npm i agents@latest @cloudflare/ai-chat@latest

Mar 17, 2026

## [@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules](https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The latest releases of [`@cloudflare/codemode` ↗︎](https://www.npmjs.com/package/@cloudflare/codemode) add a new MCP barrel export, remove `ai` and `zod` as required peer dependencies from the main entry point, and give you more control over the sandbox.

#### New `@cloudflare/codemode/mcp` export

A new `@cloudflare/codemode/mcp` entry point provides two functions that wrap MCP servers with Code Mode:

  * **`codeMcpServer({ server, executor })`** — wraps an existing MCP server with a single `code` tool where each upstream tool becomes a typed `codemode.*` method.
  * **`openApiMcpServer({ spec, executor, request })`** — creates `search` and `execute` MCP tools from an OpenAPI spec with host-side request proxying and automatic `$ref` resolution.


    
    
    import { codeMcpServer } from "@cloudflare/codemode/mcp";
    import { DynamicWorkerExecutor } from "@cloudflare/codemode";
    
    const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
    
    // Wrap an existing MCP server — all its tools become
    // typed methods the LLM can call from generated code
    const server = await codeMcpServer({ server: upstreamMcp, executor });
    
    
    import { codeMcpServer } from "@cloudflare/codemode/mcp";
    import { DynamicWorkerExecutor } from "@cloudflare/codemode";
    
    const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
    
    // Wrap an existing MCP server — all its tools become
    // typed methods the LLM can call from generated code
    const server = await codeMcpServer({ server: upstreamMcp, executor });

#### Zero-dependency main entry point

**Breaking change in v0.2.0:** `generateTypes` and the `ToolDescriptor` / `ToolDescriptors` types have moved to `@cloudflare/codemode/ai`:
    
    
    // Before
    import { generateTypes } from "@cloudflare/codemode";
    
    // After
    import { generateTypes } from "@cloudflare/codemode/ai";
    
    
    // Before
    import { generateTypes } from "@cloudflare/codemode";
    
    // After
    import { generateTypes } from "@cloudflare/codemode/ai";

The main entry point (`@cloudflare/codemode`) no longer requires the `ai` or `zod` peer dependencies. It now exports:

Export | Description  
---|---  
`sanitizeToolName` | Sanitize tool names into valid JS identifiers  
`normalizeCode` | Normalize LLM-generated code into async arrow functions  
`generateTypesFromJsonSchema` | Generate TypeScript type definitions from plain JSON Schema  
`jsonSchemaToType` | Convert a single JSON Schema to a TypeScript type string  
`DynamicWorkerExecutor` | Sandboxed code execution via Dynamic Worker Loader  
`ToolDispatcher` | RPC target for dispatching tool calls from sandbox to host  
  
The `ai` and `zod` peer dependencies are now optional — only required when importing from `@cloudflare/codemode/ai`.

#### Custom sandbox modules

`DynamicWorkerExecutor` now accepts an optional `modules` option to inject custom ES modules into the sandbox:
    
    
    const executor = new DynamicWorkerExecutor({
    	loader: env.LOADER,
    	modules: {
    		"utils.js": `export function add(a, b) { return a + b; }`,
    	},
    });
    
    // Sandbox code can then: import { add } from "utils.js"
    
    
    const executor = new DynamicWorkerExecutor({
    	loader: env.LOADER,
    	modules: {
    		"utils.js": `export function add(a, b) { return a + b; }`,
    	},
    });
    
    // Sandbox code can then: import { add } from "utils.js"

#### Internal normalization and sanitization

`DynamicWorkerExecutor` now normalizes code and sanitizes tool names internally. You no longer need to call `normalizeCode()` or `sanitizeToolName()` before passing code and functions to `execute()`.

#### Upgrade
    
    
    npm i @cloudflare/codemode@latest

See the [Code Mode documentation](https://developers.cloudflare.com/agents/tools/codemode/) for the full API reference.

Mar 3, 2026

## [Real-time file watching in Sandboxes](https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/)

[Agents](https://developers.cloudflare.com/agents/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) now support real-time filesystem watching via `sandbox.watch()`. The method returns a [Server-Sent Events ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) stream backed by native inotify, so your Worker receives `create`, `modify`, `delete`, and `move` events as they happen inside the container.

#### `sandbox.watch(path, options)`

Pass a directory path and optional filters. The returned stream is a standard `ReadableStream` you can proxy directly to a browser client or consume server-side.
    
    
    // Stream events to a browser client
    const stream = await sandbox.watch("/workspace/src", {
    	recursive: true,
    	include: ["*.ts", "*.js"],
    });
    
    return new Response(stream, {
    	headers: { "Content-Type": "text/event-stream" },
    });
    
    
    // Stream events to a browser client
    const stream = await sandbox.watch("/workspace/src", {
    	recursive: true,
    	include: ["*.ts", "*.js"],
    });
    
    return new Response(stream, {
    	headers: { "Content-Type": "text/event-stream" },
    });

#### Server-side consumption with `parseSSEStream`

Use `parseSSEStream` to iterate over events inside a Worker without forwarding them to a client.
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src", { recursive: true });
    
    for await (const event of parseSSEStream(stream)) {
    	console.log(event.type, event.path);
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src", { recursive: true });
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	console.log(event.type, event.path);
    }

Each event includes a `type` field (`create`, `modify`, `delete`, or `move`) and the affected `path`. Move events also include a `from` field with the original path.

#### Options

Option | Type | Description  
---|---|---  
`recursive` | `boolean` | Watch subdirectories. Defaults to `false`.  
`include` | `string[]` | Glob patterns to filter events. Omit to receive all events.  
  
#### Upgrade

To update to the latest version:
    
    
    npm i @cloudflare/sandbox@latest

For full API details, refer to the [Sandbox file watching reference](https://developers.cloudflare.com/sandbox/api/file-watching/).

Mar 2, 2026

## [Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections](https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) rewrites observability from scratch with `diagnostics_channel`, adds `keepAlive()` to prevent Durable Object eviction during long-running work, and introduces `waitForMcpConnections` so MCP tools are always available when `onChatMessage` runs.

#### Observability rewrite

The previous observability system used `console.log()` with a custom `Observability.emit()` interface. v0.7.0 replaces it with structured events published to [diagnostics channels](https://developers.cloudflare.com/workers/runtime-apis/nodejs/diagnostics-channel/) — silent by default, zero overhead when nobody is listening.

Every event has a `type`, `payload`, and `timestamp`. Events are routed to seven named channels:

Channel | Event types  
---|---  
`agents:state` | `state:update`  
`agents:rpc` | `rpc`, `rpc:error`  
`agents:message` | `message:request`, `message:response`, `message:clear`, `message:cancel`, `message:error`, `tool:result`, `tool:approval`  
`agents:schedule` | `schedule:create`, `schedule:execute`, `schedule:cancel`, `schedule:retry`, `schedule:error`, `queue:retry`, `queue:error`  
`agents:lifecycle` | `connect`, `destroy`  
`agents:workflow` | `workflow:start`, `workflow:event`, `workflow:approved`, `workflow:rejected`, `workflow:terminated`, `workflow:paused`, `workflow:resumed`, `workflow:restarted`  
`agents:mcp` | `mcp:client:preconnect`, `mcp:client:connect`, `mcp:client:authorize`, `mcp:client:discover`  
  
Use the typed `subscribe()` helper from `agents/observability` for type-safe access:
    
    
    import { subscribe } from "agents/observability";
    
    const unsub = subscribe("rpc", (event) => {
    	if (event.type === "rpc") {
    		console.log(`RPC call: ${event.payload.method}`);
    	}
    	if (event.type === "rpc:error") {
    		console.error(
    			`RPC failed: ${event.payload.method} — ${event.payload.error}`,
    		);
    	}
    });
    
    // Clean up when done
    unsub();
    
    
    import { subscribe } from "agents/observability";
    
    const unsub = subscribe("rpc", (event) => {
    	if (event.type === "rpc") {
    		console.log(`RPC call: ${event.payload.method}`);
    	}
    	if (event.type === "rpc:error") {
    		console.error(
    			`RPC failed: ${event.payload.method} — ${event.payload.error}`,
    		);
    	}
    });
    
    // Clean up when done
    unsub();

In production, all diagnostics channel messages are automatically forwarded to [Tail Workers](https://developers.cloudflare.com/workers/observability/logs/tail-workers/) — no subscription code needed in the agent itself:
    
    
    export default {
    	async tail(events) {
    		for (const event of events) {
    			for (const msg of event.diagnosticsChannelEvents) {
    				// msg.channel is "agents:rpc", "agents:workflow", etc.
    				console.log(msg.timestamp, msg.channel, msg.message);
    			}
    		}
    	},
    };
    
    
    export default {
    	async tail(events) {
    		for (const event of events) {
    			for (const msg of event.diagnosticsChannelEvents) {
    				// msg.channel is "agents:rpc", "agents:workflow", etc.
    				console.log(msg.timestamp, msg.channel, msg.message);
    			}
    		}
    	},
    };

The custom `Observability` override interface is still supported for users who need to filter or forward events to external services.

For the full event reference, refer to the [Diagnostics channels documentation](https://developers.cloudflare.com/agents/runtime/operations/observability/diagnostics-channels/).

#### `keepAlive()` and `keepAliveWhile()`

Durable Objects are evicted after a period of inactivity (typically 70-140 seconds with no incoming requests, WebSocket messages, or alarms). During long-running operations — streaming LLM responses, waiting on external APIs, running multi-step computations — the agent can be evicted mid-flight.

`keepAlive()` prevents this by creating a 30-second heartbeat schedule. The alarm firing resets the inactivity timer. Returns a disposer function that cancels the heartbeat when called.
    
    
    const dispose = await this.keepAlive();
    try {
    	const result = await longRunningComputation();
    	await sendResults(result);
    } finally {
    	dispose();
    }
    
    
    const dispose = await this.keepAlive();
    try {
    	const result = await longRunningComputation();
    	await sendResults(result);
    } finally {
    	dispose();
    }

`keepAliveWhile()` wraps an async function with automatic cleanup — the heartbeat starts before the function runs and stops when it completes:
    
    
    const result = await this.keepAliveWhile(async () => {
    	const data = await longRunningComputation();
    	return data;
    });
    
    
    const result = await this.keepAliveWhile(async () => {
    	const data = await longRunningComputation();
    	return data;
    });

Key details:

  * **Multiple concurrent callers** — Each `keepAlive()` call returns an independent disposer. Disposing one does not affect others.
  * **AIChatAgent built-in** — `AIChatAgent` automatically calls `keepAlive()` during streaming responses. You do not need to add it yourself.
  * **Uses the scheduling system** — The heartbeat does not conflict with your own schedules. It shows up in `getSchedules()` if you need to inspect it.



Note

`keepAlive()` is marked `@experimental` and may change between releases.

For the full API reference and when-to-use guidance, refer to [Schedule tasks — Keeping the agent alive](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/#keeping-the-agent-alive).

#### `waitForMcpConnections`

`AIChatAgent` now waits for MCP server connections to settle before calling `onChatMessage`. This ensures `this.mcp.getAITools()` returns the full set of tools, especially after Durable Object hibernation when connections are being restored in the background.
    
    
    export class ChatAgent extends AIChatAgent {
    	// Default — waits up to 10 seconds
    	// waitForMcpConnections = { timeout: 10_000 };
    
    	// Wait forever
    	waitForMcpConnections = true;
    
    	// Disable waiting
    	waitForMcpConnections = false;
    }
    
    
    export class ChatAgent extends AIChatAgent {
    	// Default — waits up to 10 seconds
    	// waitForMcpConnections = { timeout: 10_000 };
    
    	// Wait forever
    	waitForMcpConnections = true;
    
    	// Disable waiting
    	waitForMcpConnections = false;
    }

Value | Behavior  
---|---  
`{ timeout: 10_000 }` | Wait up to 10 seconds (default)  
`{ timeout: N }` | Wait up to `N` milliseconds  
`true` | Wait indefinitely until all connections ready  
`false` | Do not wait (old behavior before 0.2.0)  
  
For lower-level control, call `this.mcp.waitForConnections()` directly inside `onChatMessage` instead.

#### Other improvements

  * **MCP deduplication by name and URL** — `addMcpServer` with HTTP transport now deduplicates on both server name and URL. Calling it with the same name but a different URL creates a new connection. URLs are normalized before comparison (trailing slashes, default ports, hostname case).
  * **`callbackHost` optional for non-OAuth servers** — `addMcpServer` no longer requires `callbackHost` when connecting to MCP servers that do not use OAuth.
  * **MCP URL security** — Server URLs are validated before connection to prevent SSRF. Private IP ranges, loopback addresses, link-local addresses, and cloud metadata endpoints are blocked.
  * **Custom denial messages** — `addToolOutput` now supports `state: "output-error"` with `errorText` for custom denial messages in human-in-the-loop tool approval flows.
  * **`requestId` in chat options** — `onChatMessage` options now include a `requestId` for logging and correlating events.



#### Upgrade

To update to the latest version:
    
    
    npm i agents@latest @cloudflare/ai-chat@latest

Feb 25, 2026

## [Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes](https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) lets you define an Agent and an McpAgent in the same Worker and connect them over RPC — no HTTP, no network overhead. It also makes OAuth opt-in for simple MCP connections, hardens the schema converter for production workloads, and ships a batch of `@cloudflare/ai-chat` reliability fixes.

#### RPC transport for MCP

You can now connect an Agent to an McpAgent in the same Worker using a Durable Object binding instead of an HTTP URL. The connection stays entirely within the Cloudflare runtime — no network round-trips, no serialization overhead.

Pass the Durable Object namespace directly to `addMcpServer`:
    
    
    import { Agent } from "agents";
    
    export class MyAgent extends Agent {
    	async onStart() {
    		// Connect via DO binding — no HTTP, no network overhead
    		await this.addMcpServer("counter", env.MY_MCP);
    
    		// With props for per-user context
    		await this.addMcpServer("counter", env.MY_MCP, {
    			props: { userId: "user-123", role: "admin" },
    		});
    	}
    }
    
    
    import { Agent } from "agents";
    
    export class MyAgent extends Agent {
    	async onStart() {
    		// Connect via DO binding — no HTTP, no network overhead
    		await this.addMcpServer("counter", env.MY_MCP);
    
    		// With props for per-user context
    		await this.addMcpServer("counter", env.MY_MCP, {
    			props: { userId: "user-123", role: "admin" },
    		});
    	}
    }

The `addMcpServer` method now accepts `string | DurableObjectNamespace` as the second parameter with full TypeScript overloads, so HTTP and RPC paths are type-safe and cannot be mixed.

Key capabilities:

  * **Hibernation support** — RPC connections survive Durable Object hibernation automatically. The binding name and props are persisted to storage and restored on wake-up, matching the behavior of HTTP MCP connections.
  * **Deduplication** — Calling `addMcpServer` with the same server name returns the existing connection instead of creating duplicates. Connection IDs are stable across hibernation restore.
  * **Smaller surface area** — The RPC transport internals have been rewritten and reduced from 609 lines to 245 lines. `RPCServerTransport` now uses `JSONRPCMessageSchema` from the MCP SDK for validation instead of hand-written checks.



Note

RPC transport is experimental. The API may change based on feedback. Refer to [the tracking issue ↗︎](https://github.com/cloudflare/agents/issues/565) for updates.

#### Optional OAuth for MCP connections

`addMcpServer()` no longer eagerly creates an OAuth provider for every connection. For servers that do not require authentication, a simple call is all you need:
    
    
    // No callbackHost, no OAuth config — just works
    await this.addMcpServer("my-server", "https://mcp.example.com");
    
    
    // No callbackHost, no OAuth config — just works
    await this.addMcpServer("my-server", "https://mcp.example.com");

If the server responds with a 401, the SDK throws a clear error: `"This MCP server requires OAuth authentication. Provide callbackHost in addMcpServer options to enable the OAuth flow."` The restore-from-storage flow also handles missing callback URLs gracefully, skipping auth provider creation for non-OAuth servers.

#### Hardened JSON Schema to TypeScript converter

The schema converter used by `generateTypes()` and `getAITools()` now handles edge cases that previously caused crashes in production:

  * **Depth and circular reference guards** — Prevents stack overflows on recursive or deeply nested schemas
  * **`$ref` resolution** — Supports internal JSON Pointers (`#/definitions/...`, `#/$defs/...`, `#`)
  * **Tuple support** — `prefixItems` (JSON Schema 2020-12) and array `items` (draft-07)
  * **OpenAPI 3.0`nullable: true`** — Supported across all schema branches
  * **Per-tool error isolation** — One malformed schema cannot crash the full pipeline in `generateTypes()` or `getAITools()`
  * **Missing`inputSchema` fallback** — `getAITools()` falls back to `{ type: "object" }` instead of throwing



#### `@cloudflare/ai-chat` fixes

  * **Tool denial flow** — Denied tool approvals (`approved: false`) now transition to `output-denied` with a `tool_result`, fixing Anthropic provider compatibility. Custom denial messages are supported via `state: "output-error"` and `errorText`.
  * **Abort/cancel support** — Streaming responses now properly cancel the reader loop when the abort signal fires and send a done signal to the client.
  * **Duplicate message persistence** — `persistMessages()` now reconciles assistant messages by content and order, preventing duplicate rows when clients resend full history.
  * **`requestId` in `OnChatMessageOptions`** — Handlers can now send properly-tagged error responses for pre-stream failures.
  * **`redacted_thinking` preservation** — The message sanitizer no longer strips Anthropic `redacted_thinking` blocks.
  * **`/get-messages` reliability** — Endpoint handling moved from a prototype `onRequest()` override to a constructor wrapper, so it works even when users override `onRequest` without calling `super.onRequest()`.
  * **Client tool APIs undeprecated** — `createToolsFromClientSchemas`, `clientTools`, `AITool`, `extractClientToolSchemas`, and the `tools` option on `useAgentChat` are restored for SDK use cases where tools are defined dynamically at runtime.
  * **`jsonSchema` initialization** — Fixed `jsonSchema not initialized` error when calling `getAITools()` in `onChatMessage`.



#### Upgrade

To update to the latest version:
    
    
    npm i agents@latest @cloudflare/ai-chat@latest

Feb 23, 2026

## [Backup and restore API for Sandbox SDK](https://developers.cloudflare.com/changelog/post/2026-02-23-sandbox-backup-restore-api/)

[Agents](https://developers.cloudflare.com/agents/)[R2](https://developers.cloudflare.com/r2/)[Containers](https://developers.cloudflare.com/containers/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) now support `createBackup()` and `restoreBackup()` methods for creating and restoring point-in-time snapshots of directories.

This allows you to restore environments quickly. For instance, in order to develop in a sandbox, you may need to include a user's codebase and run a build step. Unfortunately `git clone` and `npm install` can take minutes, and you don't want to run these steps every time the user starts their sandbox.

Now, after the initial setup, you can just call `createBackup()`, then `restoreBackup()` the next time this environment is needed. This makes it practical to pick up exactly where a user left off, even after days of inactivity, without repeating expensive setup steps.
    
    
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    
    // Make non-trivial changes to the file system
    await sandbox.gitCheckout(endUserRepo, { targetDir: "/workspace" });
    await sandbox.exec("npm install", { cwd: "/workspace" });
    
    // Create a point-in-time backup of the directory
    const backup = await sandbox.createBackup({ dir: "/workspace" });
    
    // Store the handle for later use
    await env.KV.put(`backup:${userId}`, JSON.stringify(backup));
    
    // ... in a future session...
    
    // Restore instead of re-cloning and reinstalling
    await sandbox.restoreBackup(backup);

Backups are stored in [R2](https://developers.cloudflare.com/r2) and can take advantage of [R2 object lifecycle rules](https://developers.cloudflare.com/sandbox/guides/backup-restore/#configure-r2-lifecycle-rules-for-automatic-cleanup) to ensure they do not persist forever.

Key capabilities:

  * **Persist and reuse across sandbox sessions** — Easily store backup handles in KV, D1, or Durable Object storage for use in subsequent sessions
  * **Usable across multiple instances** — Fork a backup across many sandboxes for parallel work
  * **Named backups** — Provide optional human-readable labels for easier management
  * **TTLs** — Set time-to-live durations so backups are automatically removed from storage once they are no longer needed



Note

Backup and restore currently uses a FUSE overlay. Soon, native snapshotting at a lower level will be added to Containers and Sandboxes, improving speed and ergonomics. The current backup functionality provides a significant speed improvement over manually recreating a file system, but it will be further optimized in the future. The new snapshotting system will use a similar API, so changing to this system will be simple once it is available.

To get started, refer to the [backup and restore guide](https://developers.cloudflare.com/sandbox/guides/backup-restore/) for setup instructions and usage patterns, or the [Backups API reference](https://developers.cloudflare.com/sandbox/api/backups/) for full method documentation.

← Prev

1[2](https://developers.cloudflare.com/changelog/product/agents/2/)

[Next →](https://developers.cloudflare.com/changelog/product/agents/2/)
