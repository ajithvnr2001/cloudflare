---
url: https://developers.cloudflare.com/changelog/product/workers/
title: Workers Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:02.195376+00:00
---

# Workers Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/workers/

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
    	"compatibility_date": "2026-10-10",
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
    compatibility_date = "2026-10-10"
    
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

Oct 1, 2026

## [Artifacts is now in open beta](https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/)

[Artifacts](https://developers.cloudflare.com/artifacts/)[Workers](https://developers.cloudflare.com/workers/)

[Artifacts](https://developers.cloudflare.com/artifacts/), Cloudflare's versioned file system that speaks Git, is now in open beta. Artifacts is built for scale, so you can create a repository per project, user, session, or task.

With Artifacts, you can:

  * **Deploy repositories to Workers** — Connect an Artifacts repository through [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/). Pushes to the production branch deploy the updated Worker, while other branches create or update [Worker Previews](https://developers.cloudflare.com/workers/previews/).
  * **Programmatically manage repositories** — Use an [Artifacts binding](https://developers.cloudflare.com/artifacts/api/workers-binding/) from a Worker to create or fork repos, inspect files and commits, read files by path, and issue repo-scoped Git tokens.
  * **React to repository changes** — [Subscribe to events](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/) when a repository is created, imported, forked, deleted, pushed to, cloned, or fetched.
  * **Control where repository data is stored** — Choose to [store and process](https://developers.cloudflare.com/artifacts/guides/data-localization/) your data in the US or EU.
  * **Monitor repository usage** — View total operations, pulls, pushes, errors, and error rates in the Cloudflare dashboard or [via API for analytics](https://developers.cloudflare.com/artifacts/observability/metrics/).



Artifacts is available for customers on the Workers Paid plan. Cloudflare will begin [billing](https://developers.cloudflare.com/artifacts/platform/pricing/) for Artifacts on October 14, 2026.

#### Build the next GitHub on Cloudflare

We are hosting a competition to see who can build the next GitHub on Cloudflare using Workers and Artifacts.

[Apply today ↗︎](https://www.cloudflare.com/git-competition/) — submissions are open until October 14, 2026.

The first-place team will receive $25,000 in Cloudflare credits. The top three teams will be flown to San Francisco to present what they built at Cloudflare Connect.

Get started with the [Artifacts documentation](https://developers.cloudflare.com/artifacts/).

Oct 1, 2026

## [Web Crypto adds ML-KEM and ML-DSA support](https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/)

[Workers](https://developers.cloudflare.com/workers/)

The Workers Web Crypto API now supports ML-KEM-768, ML-KEM-1024, ML-DSA-44, ML-DSA-65, and ML-DSA-87. ML-KEM establishes shared secrets, while ML-DSA signs and verifies data.

The opt-in API also adds key encapsulation and decapsulation methods, `getPublicKey()`, `SubtleCrypto.supports()`, and JSON Web Keys (JWKs) with the `AKP` key type.

Turn on the `webcrypto_modern_algorithms` compatibility flag to use these features:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "compatibility_flags": [
        "webcrypto_modern_algorithms"
      ]
    }
    
    
    compatibility_flags = ["webcrypto_modern_algorithms"]

This example uses ML-KEM-768 to establish the same shared secret on both sides:

src/index.jsjs
    
    
    const keyPair = await crypto.subtle.generateKey("ML-KEM-768", false, [
    	"encapsulateBits",
    	"decapsulateBits",
    ]);
    
    if (!("publicKey" in keyPair)) {
    	throw new Error("Expected an ML-KEM key pair");
    }
    
    const { sharedKey, ciphertext } = await crypto.subtle.encapsulateBits(
    	"ML-KEM-768",
    	keyPair.publicKey,
    );
    
    const recoveredSharedKey = await crypto.subtle.decapsulateBits(
    	"ML-KEM-768",
    	keyPair.privateKey,
    	ciphertext,
    );

src/index.tsts
    
    
    const keyPair = await crypto.subtle.generateKey("ML-KEM-768", false, [
    	"encapsulateBits",
    	"decapsulateBits",
    ]);
    
    if (!("publicKey" in keyPair)) {
    	throw new Error("Expected an ML-KEM key pair");
    }
    
    const { sharedKey, ciphertext } = await crypto.subtle.encapsulateBits(
    	"ML-KEM-768",
    	keyPair.publicKey,
    );
    
    const recoveredSharedKey = await crypto.subtle.decapsulateBits(
    	"ML-KEM-768",
    	keyPair.privateKey,
    	ciphertext,
    );

Workers implements a subset of the evolving [Modern Algorithms in the Web Cryptography API ↗︎](https://wicg.github.io/webcrypto-modern-algos/) draft. ML-KEM-512 and the draft's other algorithms are not supported. The API may change as the draft evolves.

For current algorithm and operation support, refer to [Web Crypto supported algorithms](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/#supported-algorithms).

Sep 29, 2026

## [Workers Cache — mark cached responses stale with invalidate()](https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/)

[Workers](https://developers.cloudflare.com/workers/)

[Workers Cache](https://developers.cloudflare.com/workers/cache/) now supports `invalidate()`, the soft counterpart of `purge()`. `purge()` deletes matching cached responses, so the next request is a cache miss. `invalidate()` keeps them but marks them stale, so the cache revalidates them with your Worker instead.

To revalidate a response, the cache sends your Worker a conditional request built from the validators stored with it — for example, `If-None-Match` carrying the cached `ETag`. If your Worker answers `304 Not Modified`, the cache keeps the stored body. If your Worker answers with a full `200` response, that response replaces the cached one.

`invalidate()` accepts the same options as `purge()`: `tags`, `pathPrefixes`, or `purgeEverything`. It follows the same per-entrypoint scoping and resolves to the same result object. Call it as `ctx.cache.invalidate()`, or import `cache` from `cloudflare:workers` and call `cache.invalidate()`.

Use `invalidate()` when one call covers many cached responses but only some of them changed. Your Worker needs to emit `ETag` or `Last-Modified` and answer matching conditional requests with `304`. Each unchanged response then costs a validator check instead of a full regeneration:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env, ctx) {
    		if (request.method === "POST") {
    			// Write the updated catalog, then mark every cached product page stale.
    			await syncCatalog(env, await request.json());
    			await ctx.cache.invalidate({ tags: ["products"] });
    			return new Response("Synced");
    		}
    
    		const product = await getProduct(env, request);
    		const etag = `"${product.revision}"`;
    		const headers = {
    			"Cache-Control": "public, max-age=86400",
    			"Cache-Tag": "products",
    			ETag: etag,
    		};
    
    		// The product has not changed since it was cached. Answer 304, and the
    		// cache keeps the body it already has.
    		if (request.headers.get("If-None-Match") === etag) {
    			return new Response(null, { status: 304, headers });
    		}
    
    		return new Response(renderProductPage(product), { headers });
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		if (request.method === "POST") {
    			// Write the updated catalog, then mark every cached product page stale.
    			await syncCatalog(env, await request.json());
    			await ctx.cache.invalidate({ tags: ["products"] });
    			return new Response("Synced");
    		}
    
    		const product = await getProduct(env, request);
    		const etag = `"${product.revision}"`;
    		const headers = {
    			"Cache-Control": "public, max-age=86400",
    			"Cache-Tag": "products",
    			ETag: etag,
    		};
    
    		// The product has not changed since it was cached. Answer 304, and the
    		// cache keeps the body it already has.
    		if (request.headers.get("If-None-Match") === etag) {
    			return new Response(null, { status: 304, headers });
    		}
    
    		return new Response(renderProductPage(product), { headers });
    	},
    } satisfies ExportedHandler<Env>;

For more information, refer to [Invalidate cached responses](https://developers.cloudflare.com/workers/cache/purge/#invalidate-cached-responses).

Sep 28, 2026

## [Cloudflare CLI is now in beta](https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, is now in beta. `cf` is one command-line interface for the public Cloudflare API and for Workers projects. Use it to manage zones, DNS, storage, and security settings, and to create, develop, and deploy Workers, without switching between tools.

Install `cf` globally, then sign in:

npmyarnpnpmbun
    
    
    npm install --global cf
    
    
    yarn global add cf
    
    
    pnpm add --global cf
    
    
    bun add --global cf
    
    
    cf auth login

With `cf`, you can:

  * **Manage resources across Cloudflare.** More than 2,900 commands cover the public Cloudflare API, and most print their results as JSON.
  * **Create and deploy Workers.** `cf init` creates a project that uses [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), a typed configuration file. `cf dev`, `cf build`, and `cf deploy` develop, build, and deploy it.
  * **Move from Wrangler.** `cf migrate` converts a Wrangler configuration file to `cloudflare.config.ts`. You can also run `cf` resource commands in an existing Wrangler project without migrating it.
  * **Work with coding agents.** `cf cli search` finds the command for a task from a plain-language description, so an agent can find and run commands without prior knowledge of `cf`.



`cf` is in beta. Commands, configuration, and Build Output can change before the stable release.

To get started, refer to [Install and sign in](https://developers.cloudflare.com/cf/get-started/). To move an existing project, refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

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

Sep 25, 2026

## [Workers tracing — new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs](https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/)

[Workers](https://developers.cloudflare.com/workers/)

[Custom spans](https://developers.cloudflare.com/workers/observability/traces/custom-spans/) in Workers now support more of the OpenTelemetry span API, so you can instrument more of your code and record errors directly on your spans.

  * **`tracing.startSpan(name)`** creates a span without making it the active span, and returns it. Other spans do not nest under it. Call `span.end()` when the operation is complete.
  * **`tracing.getActiveSpan()`** returns the currently active span. Use it to annotate the current span from helper functions and libraries without passing the span object through your code. Outside any custom span, it returns the invocation's root span.
  * **`span.recordException(exception)`** records an exception event on a span. It accepts an `Error`, a string, or an object with a `code`, `name`, or `message`.
  * **`span.setAttributes(attributes)`** sets multiple attributes at once. `setAttribute()` and `setAttributes()` now return the span, so you can chain calls.



src/index.jsjs
    
    
    import { tracing } from "cloudflare:workers";
    
    export default {
    	async fetch(request, env) {
    		const user = await authenticate(request, env);
    
    		// Annotate the invocation's root span
    		tracing.getActiveSpan()?.setAttributes({
    			"user.id": user.id,
    			"user.plan": user.plan,
    		});
    
    		const span = tracing.startSpan("load-profile");
    		try {
    			return Response.json(await loadProfile(env, user.id));
    		} catch (err) {
    			span.recordException(err);
    			throw err;
    		} finally {
    			span.end();
    		}
    	},
    };

src/index.tsts
    
    
    import { tracing } from "cloudflare:workers";
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const user = await authenticate(request, env);
    
    		// Annotate the invocation's root span
    		tracing.getActiveSpan()?.setAttributes({
    			"user.id": user.id,
    			"user.plan": user.plan,
    		});
    
    		const span = tracing.startSpan("load-profile");
    		try {
    			return Response.json(await loadProfile(env, user.id));
    		} catch (err) {
    			span.recordException(err as Error);
    			throw err;
    		} finally {
    			span.end();
    		}
    	},
    };

For more details, refer to the [custom spans documentation](https://developers.cloudflare.com/workers/observability/traces/custom-spans/).

Sep 25, 2026

## [See every release and gradual deployment on Workers Metrics charts](https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/)

[Workers](https://developers.cloudflare.com/workers/)

[Workers Metrics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/) charts now show every release in the selected time range, including the full progression of [gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/). This makes it easier to correlate changes in memory, CPU time, errors, or latency with the code that was serving traffic.

![Memory usage chart showing a gradual deployment as a shaded rollout band](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1350,format=webp/_astro/2026-09-25-release-flow-memory-usage.C5rkO7VY.png)

A gradual deployment appears as a single rollout across the chart, with shading that increases as more traffic moves to the new version. Hover over a rollout to see the previous and new versions, the rollout duration, and the traffic percentage configured at each step.

![Invocations chart showing traffic shifting from the previous version to the new version during a gradual deployment](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1350,format=webp/_astro/2026-09-25-release-flow-invocations.BvQMAKnw.png)

Use these annotations to:

  * **Find when a regression started** — See which traffic percentage was configured when errors, latency, CPU time, or wall time changed.
  * **Compare rollout stages** — Check whether a metric changed as more traffic moved to the new version.
  * **Confirm rollbacks** — Rollbacks appear as separate release events, so you can check whether metrics recovered after a rollback.



Direct deployments that send 100% of traffic to a single version still appear as individual markers. Nearby direct deployments are grouped to reduce visual clutter. Versions that are only uploaded, or only configured at 0%, do not appear on metrics charts.

To view release annotations, open the **Metrics** tab for your [Worker ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics).

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

Sep 22, 2026

## [Workers Builds now supports Cursor Origin](https://developers.cloudflare.com/changelog/post/2026-09-22-cursor-origin-workers-builds/)

[Workers](https://developers.cloudflare.com/workers/)

Workers Builds now supports repositories hosted in Cursor Origin. Connect a Cursor Origin repository to automatically build and deploy production changes, preview non-production branches, and see build status in pull requests.

Pushes to your production branch automatically build and deploy your Worker. When you enable [non-production branch builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds), each branch receives a version-specific preview URL and a stable preview URL that follows the latest build.

Cloudflare posts build status and preview links to the Cursor Origin pull request and creates a check run for each triggered build.

To get started, install the [Cloudflare app in Cursor ↗︎](https://cursor.com/codebase/settings/apps/public/cloudflare), choose the Cursor Origin repositories Cloudflare can access, and follow the prompts to configure your Worker build. For details, refer to the [Cursor Origin integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/cursor-origin-integration/).

Sep 22, 2026

## [Test every pull request in an isolated environment with Worker Previews](https://developers.cloudflare.com/changelog/post/2026-09-22-worker-previews/)

[Workers](https://developers.cloudflare.com/workers/)

You can now test every change you make in an isolated, production-like environment with [Worker Previews ↗︎](https://blog.cloudflare.com/worker-previews/). [Each Preview](https://developers.cloudflare.com/workers/previews/) runs under the same Worker with its own code, configuration, URL, and observability, isolated from production and every other Preview.

#### Configure each Preview

Define the variables, bindings, and settings that new Previews start with in the [`previews` block of your Wrangler configuration file](https://developers.cloudflare.com/workers/previews/configuration/). Set secrets with Wrangler commands. You can override one Preview without changing production or other Previews.

For [Durable Objects](https://developers.cloudflare.com/workers/previews/resources/#durable-objects) and [Containers](https://developers.cloudflare.com/workers/previews/resources/#containers), Cloudflare automatically provisions separate namespaces, storage, apps, and instances for every Preview. State changes, sessions, memory, migrations, and concurrent tests remain scoped to that Preview. To isolate KV, D1, R2, or another account-level resource, [bind the Preview to a separate resource](https://developers.cloudflare.com/workers/previews/resources/).

![Diagram comparing production with three Previews, each with its own URL, code, configuration, and Durable Object state](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1370,format=webp/_astro/preview-resource-isolation.CyeUXRJS.png)

#### Deploy and share every change

Use Wrangler 4.135.0 or later to [deploy a Preview](https://developers.cloudflare.com/workers/previews/get-started/):
    
    
    npx wrangler preview

Or [connect your repository to Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-preview-builds) to create Previews automatically and post their URLs to pull requests.

Each Preview gets a [stable URL](https://developers.cloudflare.com/workers/previews/#urls) that updates with every push, so reviewers always see the latest changes. Each deployment also gets an immutable URL, so you can compare or return to an exact version.

After you create a Preview, use the environment breadcrumb next to your Worker's name to switch between Production and every Preview:

![Worker dashboard showing the Preview dropdown and an overview of bindings, metrics, and deployments](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2386,height=1304,format=webp/_astro/previews-dash-overview.BL1UHZHT.png)

#### Inspect and revise before production

Each Preview has its own [logs, errors, metrics, and traces](https://developers.cloudflare.com/workers/previews/test-and-debug/). Send traffic to its URL, inspect what happened, push a fix, and verify the next deployment before production.

![Preview Observability tab showing success and error events for a pull request](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1418,height=1236,format=webp/_astro/preview-observability.COYT0y5H.png)

#### Use production-like hostnames

Serve Preview URLs on `workers.dev`, a [custom domain](https://developers.cloudflare.com/workers/previews/custom-domains/), or both. Custom domains let authentication providers, cookies, cross-origin resource sharing (CORS), and OAuth redirects work as they will in production. You can also protect Preview URLs with Cloudflare Access.

Configure a domain for Preview traffic from the Worker's **Domains** tab:

![Domains tab showing a custom domain configured for Preview traffic](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2876,height=1454,format=webp/_astro/customdomainonly.8AG_6tc-.png)

For setup instructions and current limitations, refer to the [Worker Previews documentation](https://developers.cloudflare.com/workers/previews/).

Sep 21, 2026

## [Give teammates access to specific Workers directly from the dashboard](https://developers.cloudflare.com/changelog/post/2026-09-21-invite-members-to-workers/)

[Workers](https://developers.cloudflare.com/workers/)

You can now grant teammates scoped access to specific Workers directly from the Workers dashboard.

Go to your Worker and click **Invite**.

![Invite button on a Worker's overview page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2366,height=1134,format=webp/_astro/invite-button.BtZmWRrA.png)

Enter the teammate's email address, choose the appropriate access level, and click **Invite**.

![Dialog for inviting a teammate and choosing their access level](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=748,height=724,format=webp/_astro/invite-dialog.Bo5P-iat.png)

You can grant a user one of the following access levels:

  * **Metadata Read-Only** : View settings, metrics, logs, and traces without access to Worker code or the ability to make changes.
  * **Content Read-Only** : Read Worker code, settings, and observability data without the ability to modify or deploy changes.
  * **Editor** : Update and deploy a Worker without the ability to delete it.
  * **Admin** : Everything included with Editor, plus the ability to delete the Worker.



If the teammate is already an account member, they will receive access to the Worker immediately. If they are not an account member, Cloudflare will send them an invitation to join the account, and they will receive access to the Worker after accepting the invitation.

Only account members with the Super Administrator role can invite users from a Worker's dashboard.

For details about available roles and scopes, refer to the [Workers roles and permissions documentation](https://developers.cloudflare.com/workers/authorization/workers/).

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

Sep 17, 2026

## [Workers traces now automatically include JavaScript RPC session spans](https://developers.cloudflare.com/changelog/post/2026-09-17-javascript-rpc-session-spans/)

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Workers traces can now follow JavaScript RPC calls across Worker boundaries and into Durable Objects. Previously, a trace stopped at the caller's RPC boundary. The dashboard now shows the caller-side session and method calls alongside the callee invocation, nested calls, and callbacks into another Worker.

A session span covers the lifetime of a caller-side session and groups calls that reuse it. Individual call spans show each method invocation. Execution colors distinguish the Workers or Durable Object entrypoints involved, while arrows mark outgoing and incoming calls. Together, these details show where time was spent, which calls reused a session, and how returned stubs and callbacks fit into the request.

![A Workers trace of a Worker-to-Worker RPC session, showing the session span, the caller's getCounter and increment call spans, and the callee's invocation and matching call spans](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2878,height=1576,format=webp/_astro/jsrpc-session-spans.DQuwQrpm.png)

Enable tracing with one setting in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/#observability):
    
    
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

Cloudflare records these spans automatically. You do not need to change your application code or add an observability SDK.

For supported spans and attributes, refer to [Spans and attributes](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/).

Sep 16, 2026

## [Hyperdrive support for Python Workers](https://developers.cloudflare.com/changelog/post/2026-09-16-hyperdrive-python-workers/)

[Workers](https://developers.cloudflare.com/workers/)[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

[Python Workers](https://developers.cloudflare.com/workers/languages/python/) can now connect to PostgreSQL and MySQL through Hyperdrive.

For setup, code examples, and limitations, refer to [Use Hyperdrive from Python Workers](https://developers.cloudflare.com/hyperdrive/examples/python-workers/).

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

Sep 15, 2026

## [Grant teammates and agents access to specific Workers](https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/)

[Workers](https://developers.cloudflare.com/workers/)

You can now grant access to specific Workers and choose from four roles to control the level of access you give teammates, agents, and CI/CD workflows.

Choose from four roles to control the level of access:

  * **Metadata Read-Only** : View settings, metrics, logs, and traces without access to Worker code or the ability to make changes.
  * **Content Read-Only** : Read Worker code, settings, and observability data without the ability to modify or deploy changes.
  * **Editor** : Update and deploy a Worker without the ability to delete it.
  * **Admin** : Everything in Editor, plus the ability to delete the Worker.

![Permission policy form showing four roles scoped to an individual Worker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1752,height=888,format=webp/_astro/individual-worker-permission-roles.Cn5i9cW0.png)

Worker-level access controls are available today for all customers. You can configure them in the Cloudflare dashboard, through the API, or with Terraform.

#### Roles designed for how teams build

Give **Metadata Read-Only** to a debugging agent so it can inspect settings and observability data without seeing Worker code. Give **Content Read-Only** to a code review agent so it can read code without changing it. Give **Editor** to a CI/CD workflow so it can deploy without deleting the Worker or accessing other Workers. **Admin** gives a teammate or agent full control over the Worker, including the ability to delete it.

Apply these roles across all Developer Platform products, across all Workers, or to an individual Worker.

#### Durable Objects

You can use granular permissions to control access to Durable Objects. Durable Objects do not have their own roles or scopes. Instead, they inherit the permissions assigned to the Worker that implements them.

Learn more about granular permissions in the [Durable Objects documentation](https://developers.cloudflare.com/workers/authorization/durable-objects/).

#### Grant access to members and User Groups

In the Cloudflare dashboard, go to **Manage Account** > **Members** and select a [member](https://developers.cloudflare.com/fundamentals/manage-members/manage/). Create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), set the scope to **Individual Workers** , select the Workers they need, and choose a role to grant the right level of access.

If several people on the same team or project need the same access, assign the permission policy to a [User Group](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) instead of each member individually. Everyone added to the group automatically inherits the policy.

#### Create a scoped API token

For an agent or CI/CD workflow, go to **Manage Account** > **Account API Tokens** and create an [account-owned API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/). Set the scope to **Specified Workers** , select the Workers the token can access, and choose a role to grant the right level of access.

![Account API token policy with Metadata Read-Only access scoped to a specific Worker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1778,height=652,format=webp/_astro/scoped-worker-api-token-permissions.DR6OL7W0.png)

For more information, refer to the [Workers roles and permissions documentation](https://developers.cloudflare.com/workers/authorization/workers/).

Sep 8, 2026

## [Miniflare v5 prepares local development for the cf CLI](https://developers.cloudflare.com/changelog/post/2026-09-08-miniflare-v5/)

[Workers](https://developers.cloudflare.com/workers/)

Miniflare v5 prepares Cloudflare local development tooling for the upcoming `cf` CLI.

Miniflare powers local Workers development behind `wrangler dev`, the Cloudflare Vite plugin, and `@cloudflare/vitest-plugin`. Most projects should use those tools instead of depending on Miniflare directly, and Miniflare v5 will not require any action.

The most significant change is a new configuration shape which aligns Miniflare with `cloudflare.config.ts`, the programmatic Cloudflare configuration format now available for testing.

Other breaking changes include:

  * Removed deprecated APIs and options, such as legacy alpha D1 bindings.
  * Removed now-unused, internal APIs like `wrappedBindings`
  * Removed Miniflare's built-in module discovery; higher-level tools like Wrangler and the Vite plugin should be providing the module graph.
  * Moved local-only /cdn-cgi routes under /cdn-cgi/local.
  * Replaced per-resource persistence options with shared persistence root options.



For a more comprehensive list, refer to [Miniflare's changelog ↗︎](https://github.com/cloudflare/workers-sdk/blob/main/packages/miniflare/CHANGELOG.md#5202607300-alpha)

This work sets up a cleaner foundation for the next generation of local development tooling, including the new `cf` CLI.

Sep 8, 2026

## [Python 3.14 for Python Workers](https://developers.cloudflare.com/changelog/post/2026-09-08-python-workers-314/)

[Workers](https://developers.cloudflare.com/workers/)

Python workers now use Python 3.14 by default.

This change applies to all new Python workers using compatibility date `2026-09-08` or later.

Internally, this change updates the Pyodide runtime to 314.0.6.

Sep 4, 2026

## [Manage Email Routing rules with Wrangler](https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/)

[Email Service](https://developers.cloudflare.com/email-service/)[Workers](https://developers.cloudflare.com/workers/)

You can now manage Email Routing rules that route emails to Workers from your Wrangler configuration. Add literal addresses or a catch-all address to the top-level `addresses` field:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "invoice-handler",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-10",
      "addresses": [
        "invoice@yourdomain.com"
      ]
    }
    
    
    name = "invoice-handler"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-10"
    addresses = ["invoice@yourdomain.com"]

When you run `wrangler deploy`, Wrangler creates rules for new addresses, updates existing rules managed by the Worker, and removes managed rules that are no longer in the configuration. Wrangler shows the planned changes and asks for confirmation before applying potentially destructive changes.

Email Routing rules created by Wrangler also appear in the dashboard but with an icon that identifies them.

![Email Routing rule created by Wrangler in dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2440,height=526,format=webp/_astro/wrangler-email-routing-rules-dash.BZQZlAJI.png)

Refer to [Configure rules with Wrangler](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#configure-rules-with-wrangler) for more information.

Sep 4, 2026

## [Enterprise customers can self-serve CDN upload limits up to 5 GB](https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)

Enterprise customers can now configure a zone's CDN **Maximum Upload Size** up to 5 GB directly from the **Network** page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.

The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.

Refer to [Cache upload limits](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#upload-limits) and [Workers request body size limits](https://developers.cloudflare.com/workers/platform/limits/#request-and-response-limits) for details.

Sep 4, 2026

## [Deploy larger Workers — up to 64 MiB for both free and paid plans](https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/)

[Workers](https://developers.cloudflare.com/workers/)

You can now deploy Workers with larger dependencies, heavier frameworks, and more code without hitting size limits.

When you deploy a Worker, Wrangler bundles your code and compresses it before uploading. Previously, Cloudflare checked that compressed size and rejected deploys over 3 MB (Free) or 10 MB (Paid). That limit has been removed. Cloudflare now only checks the uncompressed size of your bundle, which is 64 MiB across all plans.

To check your Worker's bundle size before deploying:
    
    
    wrangler deploy --outdir bundled/ --dry-run
    
    
    Total Upload: 259.61 KiB / gzip: 47.23 KiB

The `Total Upload` value is your uncompressed bundle size. This is what counts against the 64 MiB limit. The `gzip` value is shown for reference but is no longer a limit.

For more information, refer to the [Worker size limits documentation](https://developers.cloudflare.com/workers/platform/limits/#worker-size).

Sep 2, 2026

## [Python Workers now support WSGI web frameworks like Django and Flask](https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/)

[Workers](https://developers.cloudflare.com/workers/)

Python web frameworks following the [Web Server Gateway Interface (WSGI) ↗︎](https://peps.python.org/pep-3333/) or [Asynchronous Server Gateway Interface (ASGI) ↗︎](https://asgi.readthedocs.io/) specification can now be used in Python Workers.

#### Using web frameworks with Python Workers

Based on the web framework you are using, you can use either `wsgi` or `asgi` from the `workers` module.

#### WSGI frameworks

For WSGI frameworks like Django or Flask:
    
    
    from workers import wsgi
    
    from django.core.wsgi import get_wsgi_application
    
    app = get_wsgi_application()
    Default = wsgi.entrypoint(app)

The `wsgi.entrypoint` is equivalent to creating a `WorkerEntrypoint` class and using the `wsgi.fetch` method. If you want more control over the `WorkerEntrypoint` class, you can do so:
    
    
    from workers import wsgi, WorkerEntrypoint
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            return await wsgi.fetch(app, request, self.env)

#### ASGI frameworks

For ASGI frameworks like FastAPI or Starlette:
    
    
    from workers import asgi
    
    from fastapi import FastAPI
    
    app = FastAPI()
    Default = asgi.entrypoint(app)

For more information about using individual web frameworks, refer to the [packages documentation in Python Workers](https://developers.cloudflare.com/workers/languages/python/packages/).

← Prev

1[2](https://developers.cloudflare.com/changelog/product/workers/2/)…[11](https://developers.cloudflare.com/changelog/product/workers/11/)

[Next →](https://developers.cloudflare.com/changelog/product/workers/2/)
