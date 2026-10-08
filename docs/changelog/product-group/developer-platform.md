---
url: https://developers.cloudflare.com/changelog/product-group/developer-platform/
title: Developer platform Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:30.044306+00:00
---

# Developer platform Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/developer-platform/

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

Oct 6, 2026

## [Standardize provider credential error responses in AI Gateway](https://developers.cloudflare.com/changelog/post/2026-10-05-provider-credential-errors/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway's REST API now returns consistent responses when an AI provider rejects credentials. The change applies to [`POST /ai/run` ↗︎](https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT_ID%7D/ai/run).

Scenario | Previous AI Gateway response | New AI Gateway response  
---|---|---  
ElevenLabs | Provider-specific `UserCredentialsError` with HTTP `403` | HTTP `401` with error code `2009`  
Google Vertex | HTTP `500` for rejected credentials, with upstream retries | HTTP `401` with error code `2009`; the request fails without retrying the provider  
All other providers | HTTP `402` or another provider-specific status for rejected credentials | HTTP `401` with error code `2009`  
When using [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), the provider rejects the credentials | Provider-specific authentication error | HTTP `503`  
  
Update applications that handle AI Gateway REST API errors to treat HTTP `401` as an invalid or rejected provider credential.

For details about providing provider credentials, refer to [Bring your own provider keys](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-key/).

Oct 2, 2026

## [Introducing Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Web Search API](https://developers.cloudflare.com/web-search/)

[Web Search API](https://developers.cloudflare.com/web-search/) is now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff.

At launch, you can choose between three search providers: [Ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/). All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare's [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) crawling standards.

Web Search API runs through [AI Gateway](https://developers.cloudflare.com/ai-gateway/), so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Call Web Search API with the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/websearch/ \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "What are some fun things to do in Salt Lake City as fall approaches?",
        "provider": "ceramic",
        "limit": 5,
        "options": { "gateway": { "id": "default" } }
      }'

Or from a Worker with the AI binding:
    
    
    const response = await env.AI.websearch({
    	gatewayId: "default",
    	query: "What are some fun things to do in Salt Lake City as fall approaches?",
    	provider: "exa",
    	limit: 5,
    });
    
    const results = await response.json();

To get started, refer to [How to use Web Search API](https://developers.cloudflare.com/web-search/how-to-use/).

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



Oct 2, 2026

## [United States jurisdiction](https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/)

[D1](https://developers.cloudflare.com/d1/)

You can create D1 databases with the `us` jurisdiction. These databases run and persist data within the United States.

Use this option for regional data residency requirements.

To create a database with the `us` jurisdiction, run:
    
    
    npx wrangler@latest d1 create db-with-us-jurisdiction --jurisdiction=us

For more information, refer to [D1 data location](https://developers.cloudflare.com/d1/configuration/data-location/).

Oct 2, 2026

## [Workers KV namespace jurisdictions are now generally available](https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/)

[KV](https://developers.cloudflare.com/kv/)

Jurisdictions for [Workers KV](https://developers.cloudflare.com/kv/) namespaces are now generally available. When you create a namespace, you can set a [jurisdiction](https://developers.cloudflare.com/kv/reference/data-location/) to make sure the namespace's data is only durably stored within that region. Jurisdictions can help you comply with data localization regulations such as GDPR or FedRAMP. Supported jurisdictions are `eu`, `us`, and `fedramp`.

A jurisdiction can only be set when a namespace is created, using the Cloudflare dashboard, Wrangler, the `cf` CLI, or the REST API, and cannot be added or changed afterwards.
    
    
    npx wrangler@latest kv namespace create <NAMESPACE_NAME> --jurisdiction=eu
    
    
    cf kv namespaces create --title <NAMESPACE_NAME> --jurisdiction eu
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/storage/kv/namespaces" \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "title": "<NAMESPACE_NAME>",
        "jurisdiction": "eu"
      }'

Workers can still access a namespace restricted to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction on Cloudflare's network. The jurisdiction only controls where the namespace's data is durably stored.

To learn more, refer to [Data location](https://developers.cloudflare.com/kv/reference/data-location/).

Oct 2, 2026

## [Protect Quick Tunnels with email authentication](https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)

You can now restrict who can access a [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/). Use the new `--allowed-mail` flag in `cloudflared` to require visitors to authenticate with a one-time PIN sent to their email before they reach your local service.
    
    
    cloudflared tunnel --url http://localhost:8080 --allowed-mail alice@example.com

![Protected Quick Tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1512,height=854,format=webp/_astro/protected-quick-tunnels.DlA306r_.gif)

Previously, anyone with a `trycloudflare.com` URL could access the service behind it. Protected Quick Tunnels let you share a local development server, webhook receiver, or demo with specific people without creating a Cloudflare account or configuring a domain.

You can allow:

  * A single email address: `--allowed-mail alice@example.com`
  * Multiple email addresses, by repeating the flag or using a comma-separated list: `--allowed-mail 'alice@example.com,bob@example.com'`
  * Every address on a domain: `--allowed-mail '*@example.com'`



Visitors do not need a Cloudflare account. Access ends for everyone when you stop the `cloudflared` process.

To get started, [update `cloudflared`](https://developers.cloudflare.com/tunnel/downloads/) to the latest version and refer to [Restrict access by email](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/#restrict-access-by-email).

Oct 1, 2026

## [Introducing Clef: Cloudflare's first open-source decision models, now on Workers AI](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Meet [`@cf/cloudflare/clef`](https://developers.cloudflare.com/workers-ai/models/clef/) and [`@cf/cloudflare/clef-flash`](https://developers.cloudflare.com/workers-ai/models/clef-flash/), the first models trained by the Cloudflare Workers AI team, available on Workers AI today.

Clef is a decision model, in the same family as [Typesafe's Jev ↗︎](https://typesafe.ai/blog/introducing-system-one-models-and-jev). Instead of generating text, it reads an input state and a set of typed questions, then returns a probability for every allowed answer. Your agent gets a structured decision it can act on immediately, for example: route the ticket, block the request, or escalate to a human. There is no free-form output to parse and no reasoning tokens to wait for.

Both models are hosted on Workers AI as [Clef](https://developers.cloudflare.com/workers-ai/models/clef/) and [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/). We are also open-sourcing the weights under the Apache 2.0 license on Hugging Face: [Clef ↗︎](https://huggingface.co/Cloudflare/clef) and [Clef-flash ↗︎](https://huggingface.co/Cloudflare/clef-flash). Read the [launch blog post ↗︎](https://blog.cloudflare.com/clef-decision-models/) for the full story, including how we trained them.

We are also launching a reinforcement learning (RL) fine-tuning service to help you tune Clef for your own workloads. [Sign up to work with us as a design partner ↗︎](https://www.cloudflare.com/resource/clef-rl-interest).

#### Built for the hot path

Clef is designed to be fast so decisions come back in milliseconds. Across our 43 benchmark runs, we achieved speeds where Clef is 2.5x faster than Jev at the median, and Clef-flash 13x faster.

Latency | Clef | Clef-flash | Jev  
---|---|---|---  
Median | 209.3 ms | **38.8 ms** | 524.1 ms  
p95 | 238.6 ms | **122.4 ms** | 536.0 ms  
  
Hosting on Workers AI adds to that speed. Requests run on GPUs across Cloudflare's network, running close to your users, so the network round trip stays short. You can put Clef directly in the request path of your agent, then hand off to an LLM on Workers AI to take action.

#### Leading the benchmarks

Across 10 decision benchmarks, a Clef model scores highest on 7, ahead of Jev and other open decision models. A few highlights:

Benchmark | Clef | Clef-flash | Jev  
---|---|---|---  
BFCL (case exact) | 98.47 | **98.76** | 95.75  
BANKING77 (macro-F1) | **94.20** | 90.93 | 79.74  
CLINC150+OOS (macro-F1) | **97.43** | 66.77 | 89.27  
Home appliances (case exact) | 82.95 | **97.73** | 52.27  
  
On Typesafe's own workflow evals, Clef beats Jev in 3 of 4 areas: invoice processing, customer service, and security incidents. The full results are on the [Hugging Face model card ↗︎](https://huggingface.co/Cloudflare/clef).

#### Drop-in compatible with Jev

Model | Size | Best for | Context window  
---|---|---|---  
[`@cf/cloudflare/clef`](https://developers.cloudflare.com/workers-ai/models/clef/) | 27B | Highest-precision decisions | 64K tokens  
[`@cf/cloudflare/clef-flash`](https://developers.cloudflare.com/workers-ai/models/clef-flash/) | 9B | Latency-critical, hot-path decisions | 64K tokens  
  
Clef follows the System One API, so you can switch an existing Jev integration to Clef by changing the endpoint and model. Ask up to 64 questions per request, in three types:

  * **`noul`** : A yes/no question. Returns the probability that the answer is yes.
  * **`choice`** : Pick one option from a set you define. Returns the chosen option, a probability per option, and a confidence value.
  * **`score`** : Rate against an ordered rubric. Returns a probability-weighted score and a probability per level.


    
    
    const response = await env.AI.run("@cf/cloudflare/clef", {
    	model: "clef",
    	state: "Checkout has been failing for every customer for the last hour.",
    	questions: {
    		urgent: {
    			type: "noul",
    			instructions: "Is this support request urgent?",
    		},
    		team: {
    			type: "choice",
    			instructions: "Which team should handle this request?",
    			criteria: {
    				billing: "Payments, invoices, and refunds",
    				technical: "Outages, errors, and configuration",
    				sales: "Plans and upgrades",
    			},
    		},
    	},
    });
    
    // response.answers.urgent.noul -> probability the request is urgent
    // response.answers.team.choice -> highest-probability team
    
    
    const response = await env.AI.run("@cf/cloudflare/clef", {
    	model: "clef",
    	state: "Checkout has been failing for every customer for the last hour.",
    	questions: {
    		urgent: {
    			type: "noul",
    			instructions: "Is this support request urgent?",
    		},
    		team: {
    			type: "choice",
    			instructions: "Which team should handle this request?",
    			criteria: {
    				billing: "Payments, invoices, and refunds",
    				technical: "Outages, errors, and configuration",
    				sales: "Plans and upgrades",
    			},
    		},
    	},
    });
    
    // response.answers.urgent.noul -> probability the request is urgent
    // response.answers.team.choice -> highest-probability team

#### What you can build with decision models

  * **Support triage** : Decide whether a ticket is urgent and which team owns it, then route it without a human in the loop.
  * **Threat intelligence** : Classify a website by category. Paired with [Browser Run](https://developers.cloudflare.com/browser-run/), Clef fetched, rendered, and classified a domain in 2.2 seconds, compared to 4.7 seconds for `gpt-oss-120b` in the same workflow.
  * **Trust and safety** : Score user submissions against your own policy rubric and act on the probability.
  * **Agent guardrails** : Let an agent check "should I take this action?" in tens of milliseconds before calling a tool.
  * **Visual classification** : Pass up to four images alongside the state. Unlike text-only decision models, Clef has a vision encoder.



#### Get started

Use Clef through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`) or the REST API at `/ai/run`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with these endpoints.

For more information, refer to the [Clef model page](https://developers.cloudflare.com/workers-ai/models/clef/), the [Clef-flash model page](https://developers.cloudflare.com/workers-ai/models/clef-flash/), and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

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

Oct 1, 2026

## [AI Search is generally available](https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/)

[AI Search](https://developers.cloudflare.com/ai-search/)

AI Search is now generally available. Usage-based billing begins on November 1, 2026, with included monthly ingestion, storage, semantic query, and full-text query usage. Cloudflare will send a reminder email the week before billing begins.

Refer to [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for rates and included usage.

#### Hybrid search is on by default

New AI Search instances use hybrid search by default. Hybrid search combines semantic vector retrieval with full-text matching. You can choose a different index method when you create an instance.

Refer to [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for details.

#### Workers AI embeddings and reranking are included

Workers AI embedding and reranking calls made by AI Search are included in AI Search pricing. These calls no longer appear on your Workers AI bill or in your AI Gateway logs. Generation, query rewriting, and external providers continue to use your account and gateway.

Refer to [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for details.

#### Multimodal model and image support

AI Search supports the `@cf/qwen/qwen3-vl-embedding-2b` and `google-ai-studio/gemini-embedding-2` multimodal embedding models. Search and chat requests can include images through the REST API and public endpoint.

Refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/) for the full list of embedding models.

#### OCR availability and increased file limits

Optical character recognition (OCR) is available on every account for scanned PDFs. Plain-text or code files and PDFs with OCR enabled can be up to 10 MiB. PDFs without OCR and other supported formats remain limited to 4 MiB.

Refer to [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/#file-limits) for file limits and [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for OCR pricing.

#### Source type inference

When you create an AI Search instance, the `type` field is optional. AI Search infers a website source from an HTTP or HTTPS URL, or an R2 source from an existing bucket name.

Refer to [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) for details.

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

## [Basin Pipelines ingest limit increased to 1 GB/s](https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/)

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

Each [Basin Pipelines stream](https://developers.cloudflare.com/basin-pipelines/streams/) can now ingest up to 1 GB/s, increased from 5 MB/s.

The higher per-stream limit gives high-volume application events, telemetry, and logs more room to grow without splitting ingestion across streams solely to stay within the previous limit.

For the full list of stream, sink, and pipeline limits, refer to [Basin Pipelines limits](https://developers.cloudflare.com/basin-pipelines/platform/limits/).

Oct 1, 2026

## [Cloudflare Basin is now generally available](https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/)

[Basin](https://developers.cloudflare.com/basin/)[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)[Basin SQL](https://developers.cloudflare.com/basin-sql/)

[Basin](https://developers.cloudflare.com/basin/), formerly the Cloudflare Data Platform, is now generally available. Basin brings an end-to-end analytics platform to the Developer Platform, enabling you to collect data from a variety of sources, such as apps, infrastructure, devices, and other Cloudflare services, then query it to answer analytical questions.

#### Basin Pipelines

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/), formerly Cloudflare Pipelines, ingests events from Workers, HTTP endpoints, and Cloudflare [Logpush](https://developers.cloudflare.com/logpush/). It transforms events with SQL and ingests them into Iceberg tables or files on R2. With Basin Pipelines you can:

  * Ingest application and device events through HTTP endpoints or Workers bindings.
  * Filter and reshape Cloudflare logs before storing them as Iceberg tables, Parquet, or JSON.
  * Catch schema mismatches with typed bindings and investigate dropped events in the dashboard.



#### Basin Catalog

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/), formerly R2 Data Catalog, manages and automatically maintains [Apache Iceberg tables ↗︎](https://iceberg.apache.org/) to keep them fast, cost-efficient, and accessible to any compatible query engine. With Basin Catalog you can:

  * Connect DuckDB, Spark, Snowflake, or PyIceberg to the same tables.
  * Maintain growing tables with compaction, snapshot expiration, and manifest optimization.
  * Share analytical data across tools and clouds without paying egress fees.



#### Basin SQL

[Basin SQL](https://developers.cloudflare.com/basin-sql/), formerly R2 SQL, is a serverless, distributed SQL engine for querying large Apache Iceberg tables in Basin Catalog without managing or scaling compute. With Basin SQL you can:

  * Summarize and rank data with standard and approximate aggregates, grouping sets, and window functions.
  * Combine and inspect datasets with joins, subqueries, common table expressions, set operations, schema discovery, and `EXPLAIN`.
  * Transform strings, timestamps, JSON, and complex values with more than 190 functions.



#### Get started

To get started with creating an end-to-end data pipeline, run:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup
    
    
    yarn wrangler basin pipelines setup
    
    
    pnpm wrangler basin pipelines setup

Or get started by referring to the [Basin getting started guide](https://developers.cloudflare.com/basin/get-started/guide/).

Note

Existing Cloudflare Pipelines, R2 Data Catalog, and R2 SQL resources and configurations will continue to work and will be deprecated over time.

Oct 1, 2026

## [Pending I/O operations allow Durable Objects to continue long-running work without a connected client](https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Durable Objects remain active while handling a request from a connected client. This change applies when no client is connected, such as when an agent continues a submitted job after its client disconnects.

This behavior is the default for Workers with a compatibility date of `2026-10-01` or later. To use it with an earlier date, add the [`durable_object_io_tasks_prevent_eviction`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#durable-object-io-tasks-prevent-eviction) compatibility flag. To opt out, add the `durable_object_io_tasks_do_not_prevent_eviction` flag.

Pending [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) requests now keep Durable Objects running while they wait for a response. Pending calls to another Durable Object through remote procedure call (RPC) or `fetch()`, as well as `this.ctx.container.monitor()`, now also keep the Durable Object running.

Promises passed to `this.ctx.waitUntil()` and pending `setTimeout()` and `setInterval()` timers also receive this protection.

Previously, Cloudflare could shut down an idle Durable Object while one of these operations remained pending without a connected client. This could stop unfinished work.

This change helps you run long-running tasks such as agents. An agent can call tools through service bindings, coordinate with other Durable Objects, or wait for a container process without relying on the original client to remain connected.

Outbound `fetch()` requests to external services, TCP sockets, and outbound WebSockets already keep Durable Objects running.

Each pending operation prevents idle shutdown for up to 15 minutes. Starting another one later can extend the Durable Object's time in memory. The limit applies to each operation, not to the total time in memory.

![Timeline of a service binding fetch, an RPC call, and monitor\(\) each preventing eviction for up to 15 minutes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=360,format=svg/_astro/pending-io-keep-alive.vVfDqYTX.svg)

Duration charges continue while an operation prevents eviction.

For more information, refer to [Lifecycle of a Durable Object](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/).

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

Sep 30, 2026

## [New scheduling policy for Containers to configure image and instance from Durable Objects](https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/)

[Containers](https://developers.cloudflare.com/containers/)

[Containers](https://developers.cloudflare.com/containers/) now support the `durable_object` scheduling policy in public beta. This policy lets a Durable Object select the image and instance size for a Container at runtime instead of using one centrally managed configuration for the application.

To use custom images, configure the policy and one or more named images in Wrangler:
    
    
    {
    	"containers": [
    		{
    			"class_name": "AgentComputer",
    			"scheduling_policy": "durable_object",
    			"images": {
    				"base": {
    					"dockerfile": "./container/Dockerfile",
    				},
    			},
    		},
    	],
    }
    
    
    [[containers]]
    class_name = "AgentComputer"
    scheduling_policy = "durable_object"
    
    [containers.images.base]
    dockerfile = "./container/Dockerfile"

Wrangler prepares each image and exposes its immutable reference through `ctx.container.images`. Supply that reference and an instance size when you start the Container:

src/index.jsjs
    
    
    this.ctx.container.start({
    	image: this.ctx.container.images.base,
    	enableInternet: false,
    	instance: "standard-2",
    });

src/index.tsts
    
    
    this.ctx.container.start({
    	image: this.ctx.container.images.base,
    	enableInternet: false,
    	instance: "standard-2",
    });

The `durable_object` policy also supports the new [`cloudflare/debian-trixie` Cloudflare-managed image](https://developers.cloudflare.com/containers/guides/image-management/#use-the-cloudflare-managed-image), which includes Node.js 24.20.0 on Debian Trixie slim. Start it directly without configuring a named image.

Durable Object-managed Container instances have independent lifecycles and do not participate in application-wide image rollouts.

For configuration, runtime sizing, snapshots, and update behavior, refer to [Scheduling Policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/).

Sep 30, 2026

## [Snapshot and restore Container filesystem](https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/)

[Containers](https://developers.cloudflare.com/containers/)

[Containers](https://developers.cloudflare.com/containers/) now support snapshot APIs in public beta for saving and restoring point-in-time filesystem state. Create a snapshot first, then pass it back to `start()` to restore files after container sleep, restart, or handoff to another Durable Object.

Use `snapshotContainer()` through the [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/) to capture the full container filesystem. Create a snapshot from a running Container, store its handle, and pass that handle to `start()` when you restore it later:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class MyDurableObject extends DurableObject {
    	async saveSnapshot() {
    		// Create a snapshot from the running Container.
    		const containerSnapshot = await this.ctx.container.snapshotContainer({});
    
    		await this.ctx.storage.put("containerSnapshot", containerSnapshot);
    	}
    
    	async restoreSnapshot() {
    		// Restore the saved snapshot later.
    		const containerSnapshot = await this.ctx.storage.get("containerSnapshot");
    
    		if (!containerSnapshot) {
    			return;
    		}
    
    		this.ctx.container.start({ containerSnapshot, enableInternet: false });
    	}
    }

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class MyDurableObject extends DurableObject {
    	async saveSnapshot() {
    		// Create a snapshot from the running Container.
    		const containerSnapshot = await this.ctx.container.snapshotContainer({});
    
    		await this.ctx.storage.put("containerSnapshot", containerSnapshot);
    	}
    
    	async restoreSnapshot() {
    		// Restore the saved snapshot later.
    		const containerSnapshot =
    			await this.ctx.storage.get<ContainerSnapshot>("containerSnapshot");
    
    		if (!containerSnapshot) {
    			return;
    		}
    
    		this.ctx.container.start({ containerSnapshot, enableInternet: false });
    	}
    }

Snapshots are only supported for Container applications that use the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy). Snapshots are immutable, so create a new snapshot to persist filesystem changes made after a restore.

For more information, refer to [Snapshots](https://developers.cloudflare.com/containers/guides/snapshots/) and the [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/).

Sep 30, 2026

## [Sandbox SDK 1.0: control every sandbox from your own Durable Object](https://developers.cloudflare.com/changelog/post/2026-09-30-sandbox-sdk-1-0/)

[Sandboxes](https://developers.cloudflare.com/sandbox/)

Sandbox SDK 1.0 is available. Your own Durable Object class now controls each sandbox container directly, through the [Durable Object container API](https://developers.cloudflare.com/containers/api/durable-object-container/) on `this.ctx.container`.

With 1.0, your class can:

  * Choose the image and instance size each time it starts a sandbox. One class can run sandboxes on different images, and a deploy does not restart sandboxes that are running.
  * Save the files of a sandbox as a [snapshot](https://developers.cloudflare.com/sandbox/files/save-and-restore-a-workspace/), in public beta, and start the same sandbox or a new one from it.
  * Decide when each sandbox stops, for example when a task finishes, when its user goes idle, or after it saves a snapshot.
  * Run commands with streamed input and output, send them signals, and open [terminals](https://developers.cloudflare.com/sandbox/commands/open-a-terminal-in-the-browser/).
  * Serve [previews](https://developers.cloudflare.com/sandbox/previews/) from ports in the sandbox, with your own hostnames and authentication.
  * Handle outbound requests for each hostname in Worker code, so [credentials](https://developers.cloudflare.com/sandbox/network/call-an-authenticated-api/) and bindings stay in your Worker.
  * Expose only the methods that you want callers to use.
  * Run an [agent](https://developers.cloudflare.com/agents/tools/sandbox/) in the same Durable Object, and give the model a tool that runs commands in the sandbox.



src/index.jsjs
    
    
    import { Files } from "@cloudflare/sandbox";
    import { DurableObject } from "cloudflare:workers";
    
    export class MySandbox extends DurableObject {
    	container;
    	files;
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		if (!ctx.container) {
    			throw new Error("No container is configured");
    		}
    		this.container = ctx.container;
    		this.files = new Files(ctx.container);
    	}
    
    	async run(script) {
    		if (!this.container.running) {
    			// Your code chooses the image, size, and network access.
    			this.container.start({
    				image: this.container.images.sandbox,
    				instance: "lite",
    				enableInternet: false,
    			});
    		}
    
    		await this.files.writeFile("/tmp/task.sh", script);
    		const proc = await this.container.exec(["sh", "/tmp/task.sh"]);
    		return proc.output();
    	}
    }

src/index.tsts
    
    
    import { Files } from "@cloudflare/sandbox";
    import { DurableObject } from "cloudflare:workers";
    
    export class MySandbox extends DurableObject<Env> {
    	private readonly container: Container;
    	private readonly files: Files;
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		if (!ctx.container) {
    			throw new Error("No container is configured");
    		}
    		this.container = ctx.container;
    		this.files = new Files(ctx.container);
    	}
    
    	async run(script: string) {
    		if (!this.container.running) {
    			// Your code chooses the image, size, and network access.
    			this.container.start({
    				image: this.container.images.sandbox,
    				instance: "lite",
    				enableInternet: false,
    			});
    		}
    
    		await this.files.writeFile("/tmp/task.sh", script);
    		const proc = await this.container.exec(["sh", "/tmp/task.sh"]);
    		return proc.output();
    	}
    }

Your class uses the container API directly, with the [`durable_object` scheduling policy](https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/) and [container snapshots](https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/), both in public beta. [`@cloudflare/sandbox`](https://developers.cloudflare.com/sandbox/reference/) adds classes for work that the API does not include:

  * `Files` streams files in and out of the running sandbox.
  * `S3Mount` mounts an S3-compatible bucket, such as R2. Your Worker signs each storage request, so the credentials stay out of the sandbox.
  * `DirectoryBackup` saves a directory to R2 and restores it into any sandbox, including one on a newer image.



#### If you use Sandbox SDK 0.x

Your 0.x applications keep running, and `@cloudflare/sandbox` 0.x stays on npm. Sandbox SDK 0.x receives bug and security fixes until 2026-12-31, and its documentation stays at [Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/).

When you are ready, [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/) shows the 1.0 code for each 0.x feature, including preview URLs, tunnels, background processes, terminals, backups, and the code interpreter. The guide keeps the preview URLs and named tunnels that your 0.x application created working. You can move every sandbox in one deploy, or run a 1.0 class next to your 0.x class and move sandboxes one at a time. The deploy that moves an existing class to the new policy is one-way, so the guide shows how to rehearse it first.

The [Sandboxes documentation](https://developers.cloudflare.com/sandbox/) also covers Dynamic Workers, for untrusted code in JavaScript, Python, or WebAssembly.

Sep 30, 2026

## [Pay for AI inference with Machine Payments](https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway now supports Machine Payments in beta. With Machine Payments, clients can use the x402 protocol to pay for eligible inference requests directly from a stablecoin wallet instead of maintaining a prepaid credit balance.

Machine Payments is available for the `/ai/run` endpoint with select open models. To request x402 payment, authenticate with a Cloudflare API token and include the Cloudflare-specific `Payment-Method: x402` header:
    
    
    curl -iX POST "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Payment-Method: x402" \
      --header "Content-Type: application/json" \
      --data '{
        "model": "z-ai/glm-4.7-flash",
        "input": {
          "messages": [
            {
              "role": "user",
              "content": "What is Cloudflare?"
            }
          ]
        }
      }'

An x402-compatible client handles the payment challenge, signs an authorization from the client's wallet, and retries the request. Machine Payments currently requires customers to be based in the United States and have a credit card on file.

For prerequisites, eligible models, and transaction details, refer to [Machine Payments (x402)](https://developers.cloudflare.com/ai-gateway/features/machine-payments/).

Sep 30, 2026

## [Realtime SFU WebSocket adapter is generally available](https://developers.cloudflare.com/changelog/post/2026-09-30-websocket-adapter-ga/)

[Realtime](https://developers.cloudflare.com/realtime/)

The [WebSocket adapter](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/) for [Cloudflare's Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) is now generally available. The SFU (selective forwarding unit) is managed WebRTC infrastructure for live audio, video, and data across [Cloudflare's global network in 330+ cities ↗︎](https://www.cloudflare.com/products/turn-sfu/).

The adapter connects live calls to any server that accepts WebSockets, such as a [Durable Object](https://developers.cloudflare.com/durable-objects/). It delivers uncompressed pulse-code modulation (PCM) audio and JPEG video frames. Your backend can process this media without implementing a WebRTC client.

#### What you can build

  * Transcribe or record call audio, or let a voice agent hear and respond to participants. The [AI audio example](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/) uses Durable Objects and Workers AI for transcription and speech generation. Separate adapters receive PCM audio and send generated speech back to participants.
  * Analyze images or build previews from live video. The [WebRTC-to-JPEG example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/video-to-jpeg) sends a browser's camera stream to a Durable Object as JPEG frames at one frame per second by default.



#### What changes for existing integrations

Existing adapter creation requests and media formats stay the same.

For WebRTC-to-WebSocket streaming, the SFU now automatically retries the same endpoint for up to 15 seconds instead of 5, with no additional API setting.

The [close API](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#close-adapter) is now idempotent and returns success even if the adapter has already closed:
    
    
    {
    	"tracks": [{ "adapterId": "<ADAPTER_ID>" }]
    }

Refer to the [WebSocket adapter guide](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/) for setup, media formats, and API requests.

Sep 29, 2026

## [Identify model overuse and potential savings with User Insights](https://developers.cloudflare.com/changelog/post/2026-09-29-user-insights-task-analysis/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway User Insights now gives you more context about the traffic flowing through your gateway. It shows what users and agents are doing with AI, and where a selected model may be more capable than a task requires.

On the analysis side, User Insights groups conversations by task, tracks conversation turns, and helps you compare model fit with cost and latency.

![User Insights task and model analysis grouped by task categories](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1434,height=606,format=webp/_astro/user-insights-task-analysis.CS2pm7wg.png)

The Potential Savings view highlights requests that may work with faster or less expensive models without compromising output quality. These are the same signals that Cloudflare's [Auto Router](https://developers.cloudflare.com/ai-gateway/features/auto-router/) uses to select a model based on task and cost.

![Potential Savings view comparing tasks and suggested models](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1506,height=669,format=webp/_astro/user-insights-potential-savings.C7j_Gjcn.png)

These new insights are available to all AI Gateway customers at no additional cost. For more information, refer to [User Insights](https://developers.cloudflare.com/ai-gateway/observability/user-insights/).

Sep 29, 2026

## [Connect multiple clients to one Browser Run session](https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Run](https://developers.cloudflare.com/browser-run/) sessions now accept multiple concurrent connections. Before, a session accepted only one connection at a time, and other Workers had to wait until that connection closed. Now multiple Workers can connect to the same browser at the same time.

Each `puppeteer.connect()` call opens its own Chrome DevTools Protocol (CDP) connection. Create a separate browser context for each request to keep its pages, cookies, and storage apart from other clients.
    
    
    const browser = await puppeteer.connect(env.MYBROWSER, sessionId);
    const context = await browser.createBrowserContext();
    
    try {
    	const page = await context.newPage();
    	await page.goto("https://example.com");
    	// ...
    } finally {
    	await context.close();
    	await browser.disconnect(); // keep the shared browser running
    }
    
    
    const browser = await puppeteer.connect(env.MYBROWSER, sessionId);
    const context = await browser.createBrowserContext();
    
    try {
    	const page = await context.newPage();
    	await page.goto("https://example.com");
    	// ...
    } finally {
    	await context.close();
    	await browser.disconnect(); // keep the shared browser running
    }

Sharing sessions means fewer new browsers to launch, less cold-start time, and fewer [concurrent browsers](https://developers.cloudflare.com/browser-run/limits/) counted against your limits.

Concurrent connections require `@cloudflare/puppeteer` version 1.1.0 or later.

Refer to [Reuse sessions](https://developers.cloudflare.com/browser-run/features/reuse-sessions/) for a full example.

Sep 29, 2026

## [Custom Container instance types no longer have a disk to memory ratio limit](https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/)

[Containers](https://developers.cloudflare.com/containers/)

[Containers](https://developers.cloudflare.com/containers/) custom instance types no longer limit disk based on memory. Previously, a custom instance type could have a maximum of 2 GB of disk for each 1 GiB of memory. You can now allocate up to the 20 GB disk maximum to any custom instance type.

Use this to run workloads that need more disk than memory, such as workloads with large container images, datasets, or build caches. The maximum image size is the same as the instance disk space, so more disk also lets you deploy larger images.

For example, a custom instance type with 1 vCPU and 3 GiB of memory was previously limited to 6 GB of disk. It can now use 20 GB:
    
    
    {
    	"containers": [
    		{
    			"image": "./Dockerfile",
    			"instance_type": {
    				"vcpu": 1,
    				"memory_mib": 3072,
    				"disk_mb": 20000,
    			},
    		},
    	],
    }
    
    
    [[containers]]
    image = "./Dockerfile"
    
      [containers.instance_type]
      vcpu = 1
      memory_mib = 3_072
      disk_mb = 20_000

The other custom instance type constraints do not change, including the minimum of 3 GiB of memory per vCPU. For the full list, refer to [Custom Instance Types](https://developers.cloudflare.com/containers/platform/limits/#custom-instance-types).

Sep 29, 2026

## [Identify Mesh, Workers VPC, and Cloudflare Tunnel replicas in network logs](https://developers.cloudflare.com/changelog/post/2026-09-29-mesh-workers-vpc-network-logs/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

You can now tell a person on a laptop apart from a Mesh node or an AI agent running on Workers, without matching on connector email addresses or Mesh IP ranges — and see exactly which Cloudflare Tunnel and `cloudflared` replica received each session.

[Gateway network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs) and [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) now identify two new kinds of traffic:

  * **Mesh** — Traffic sent from or delivered to a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node. Previously, Mesh nodes were logged the same way as devices running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), because Mesh nodes run the client in headless mode.
  * **Workers VPC** — Traffic sent by a Worker through a [Workers VPC](https://developers.cloudflare.com/workers-vpc/) binding. Previously, Workers VPC sessions were not recorded in Network Session Logs.

![Viewing Mesh and Workers VPC traffic in Gateway network logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1439,height=796,format=webp/_astro/2026-09-28-mesh-workers-vpc-network-logs.iGvLKYk7.gif)

#### Gateway network logs

To view these values in the dashboard, go to **Zero Trust** > **Insights & Logs** > **Logs** > **Network logs** , select **Columns** , and turn on **Traffic Source** and **Traffic Destination**. Both values also appear under **Network query details** when you open a log entry.

#### Network Session Logs

The `zero_trust_network_sessions` dataset, available through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/), includes the following fields:

Field | Description  
---|---  
`OnrampType` | How the session entered Cloudflare One. Values: `CF1_CLIENT`, `MESH`, `WORKERS_VPC`, `MAGIC`, `OTHER`.  
`Offramp` | Where the session was routed. Sessions routed to a Mesh node report `MESH`.  
`SourceName` | Name of the Worker that started the session. Only populated for Workers VPC sessions.  
`SourceID` | Stable identifier of the Worker that started the session. Only populated for Workers VPC sessions.  
`DestinationReplicaID` | The replica that served the session, such as a specific replica of a Mesh node or a `cloudflared` replica of a Cloudflare Tunnel.  
  
For example, `OnrampType = 'WORKERS_VPC' AND Offramp = 'MESH'` returns every session where a Worker reached a service behind a Mesh node, and `SourceName` tells you which Worker it was.

Redeploy your Workers

`SourceName` and `SourceID` are only populated for Workers deployed after 29 September 2026. To include them for an existing Worker, redeploy it — for example, with `npx wrangler deploy`. No code changes are required.

#### See which tunnel and replica received a session

With `DestinationReplicaID`, you can now confirm which [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and which `cloudflared` replica received traffic for a specific session. Combine it with the existing `DestinationTunnelID` field to trace a session to an exact tunnel replica — or Mesh node replica — when you run multiple replicas for high availability. The replica ID matches the **Connector ID** shown in the dashboard, so you can [stream that replica's logs](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) with `cloudflared tail --connector-id`.

Sessions logged before this change are not backfilled. For all available fields, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/).

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

## [Browser Run adds WebMCP to Kitesurf and moves to document.modelContext](https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/) now works in [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) sessions as well as [Lab sessions](https://developers.cloudflare.com/browser-run/features/webmcp/#get-started). Both backends use the `document.modelContext` API from the [WebMCP Community Group draft ↗︎](https://webmachinelearning.github.io/webmcp/). Lab sessions no longer expose `navigator.modelContextTesting`.

To list and run page tools:

  * **Chrome DevTools** : Use the **Application** > **WebMCP** panel in the live view of a Lab session or in the [Kitesurf playground ↗︎](https://kitesurf.dev/).
  * **AI agents** : Start [Chrome DevTools MCP](https://developers.cloudflare.com/browser-run/features/webmcp/#using-an-ai-agent) with the `--category-experimental-webmcp` flag to add the `list_webmcp_tools` and `execute_webmcp_tool` tools.
  * **CDP clients** : Use the `WebMCP` CDP domain.



← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/developer-platform/2/)…[25](https://developers.cloudflare.com/changelog/product-group/developer-platform/25/)

[Next →](https://developers.cloudflare.com/changelog/product-group/developer-platform/2/)
