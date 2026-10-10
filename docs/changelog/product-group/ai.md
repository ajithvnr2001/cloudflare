---
url: https://developers.cloudflare.com/changelog/product-group/ai/
title: AI Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:28.514135+00:00
---

# AI Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/ai/

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

Oct 10, 2026

## [Cloudflare API MCP server serves Cloudflare skills](https://developers.cloudflare.com/changelog/post/2026-10-10-cloudflare-mcp-skills/)

[Agents](https://developers.cloudflare.com/agents/)

The [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#cloudflare-api-mcp-server) now serves [Cloudflare skills ↗︎](https://github.com/cloudflare/skills) through the [Skills over MCP extension ↗︎](https://modelcontextprotocol.io/extensions/skills/overview). MCP clients that support the extension discover the skills with `skills/list` and read their files at `skill://<name>/<path>`.

To use them, add `https://mcp.cloudflare.com/mcp` to an [MCP client that supports the extension ↗︎](https://modelcontextprotocol.io/extensions/client-matrix).

Oct 9, 2026

## [Clef-omni adds audio and video input, Clef-flash is now cheaper, and Clef is faster](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/cloudflare/clef-omni`](https://developers.cloudflare.com/workers-ai/models/clef-omni/) is now available on Workers AI. Clef-omni is a decision model that takes audio (WAV or MP3) and video (MP4 or WebM) input alongside text and images. It joins [Clef](https://developers.cloudflare.com/workers-ai/models/clef/) and [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/) in the Clef family of open-weight decision models. We also cut the price of Clef-flash, so it now costs less than Jev, and made Clef faster.

#### Clef-omni: one decision model for every modality

Previously, making a decision about a voice recording or a video meant chaining models together: transcribe the speech, split the audio and visual tracks, then pass the results to a text decision model. Clef-omni reads every modality directly in one request. A video's soundtrack is aligned with its frames, so the model can reason over what is seen and heard at the same time.

Clef-omni is built on a 30B-parameter mixture-of-experts (MoE) backbone with 3B active parameters. Like the rest of the Clef family, it does not generate text. It scores every allowed answer in a single pass, so decisions return quickly:

  * Text requests: about 20 ms
  * Image or audio inputs: under 100 ms
  * A 21-second video clip with sound: about 300 ms



Pass media as base64 data URLs in the `images`, `audio`, and `videos` fields:
    
    
    const response = await env.AI.run("@cf/cloudflare/clef-omni", {
    	model: "clef-omni",
    	state:
    		"Review the installation: a photo of the unit, an audio recording of it running, and a video of the fan.",
    	images: ["data:image/png;base64,<base64-png>"],
    	audio: ["data:audio/mpeg;base64,<base64-mp3>"],
    	videos: ["data:video/mp4;base64,<base64-mp4>"],
    	questions: {
    		label_visible: {
    			type: "noul",
    			instructions:
    				"Is the model and serial number label visible in the photo?",
    		},
    		sounds_normal: {
    			type: "noul",
    			instructions:
    				"Does the unit sound like it is running smoothly, without rattling or grinding?",
    		},
    		fan_running: {
    			type: "noul",
    			instructions: "Is the fan running in the video?",
    		},
    	},
    });
    
    
    const response = await env.AI.run("@cf/cloudflare/clef-omni", {
    	model: "clef-omni",
    	state:
    		"Review the installation: a photo of the unit, an audio recording of it running, and a video of the fan.",
    	images: ["data:image/png;base64,<base64-png>"],
    	audio: ["data:audio/mpeg;base64,<base64-mp3>"],
    	videos: ["data:video/mp4;base64,<base64-mp4>"],
    	questions: {
    		label_visible: {
    			type: "noul",
    			instructions:
    				"Is the model and serial number label visible in the photo?",
    		},
    		sounds_normal: {
    			type: "noul",
    			instructions:
    				"Does the unit sound like it is running smoothly, without rattling or grinding?",
    		},
    		fan_running: {
    			type: "noul",
    			instructions: "Is the fan running in the video?",
    		},
    	},
    });

Clef-omni scores highest of the Clef family on BANKING77, CLINC150+OOS, and Amazon ESCI:

Benchmark | Clef-omni | Clef | Clef-flash | Jev  
---|---|---|---|---  
BFCL (case exact) | 98.2 | 98.47 | **98.76** | 95.75  
BANKING77 (macro-F1) | **94.8** | 94.20 | 90.93 | 79.74  
CLINC150+OOS (macro-F1) | **97.7** | 97.43 | 66.77 | 89.27  
Amazon ESCI (macro-F1) | **57.8** | 57.48 | 57.39 | 55.21  
PhishNChips (accuracy) | 73.2 | **79.60** | 75.05 | 62.55  
  
#### Clef-flash is now cheaper

Clef-flash now costs **$0.038 per million input tokens** , down from $0.090, which makes it cheaper than Jev. To offer this price, the hosted Clef-flash context window is now 24K tokens, down from 64K. Based on usage data, only 0.24% of requests exceed 24K input tokens. If you need a larger context window, use Clef, which keeps its 64K context window.

The Clef-flash weights on Hugging Face are unchanged and support up to a 256K context window if you self-host.

Model | Price | Context window  
---|---|---  
[`@cf/cloudflare/clef-flash`](https://developers.cloudflare.com/workers-ai/models/clef-flash/) | $0.038 per M input tokens | 24K tokens  
[`@cf/cloudflare/clef`](https://developers.cloudflare.com/workers-ai/models/clef/) | $0.240 per M input tokens | 64K tokens  
[`@cf/cloudflare/clef-omni`](https://developers.cloudflare.com/workers-ai/models/clef-omni/) | $0.150 per M input tokens | 64K tokens  
  
All Clef models convert image inputs to input tokens, and Clef-omni does the same for audio and video. For details on how each input type is tokenized, refer to the [Clef](https://developers.cloudflare.com/workers-ai/models/clef/), [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/), and [Clef-omni](https://developers.cloudflare.com/workers-ai/models/clef-omni/) model pages.

#### Clef is now faster

We optimized how Clef is served on Workers AI, so it now returns decisions up to 2x faster. The model weights are unchanged.

Input size | Before: median / p95 (ms) | Now: median / p95 (ms) | Median speedup  
---|---|---|---  
~800 tokens | 262 / 438 | 152 / 351 | 1.7x  
~3,400 tokens | 616 / 777 | 305 / 531 | 2.0x  
~16,000 tokens | 2,721 / 3,250 | 1,635 / 1,805 | 1.7x  
  
Part of this speedup comes from moving Clef to [SGLang ↗︎](https://github.com/sgl-project/sglang). Clef support is coming to SGLang in version 0.5.22 ([PR #42721 ↗︎](https://github.com/sgl-project/sglang/pull/42721)). If you self-host Clef, launch commands are available in the [Clef collection on Hugging Face ↗︎](https://huggingface.co/collections/Cloudflare/clef).

#### Get started

Clef-omni follows the same System One API as Clef and Clef-flash, and works with [AI Gateway](https://developers.cloudflare.com/ai-gateway/). To try it, change the model ID to `@cf/cloudflare/clef-omni` and set the `model` selector to `clef-omni`.

For more information, refer to the [Clef-omni model page](https://developers.cloudflare.com/workers-ai/models/clef-omni/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

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

## [Monetization Gateway closed beta](https://developers.cloudflare.com/changelog/post/2026-09-30-closed-beta/)

[Monetization Gateway](https://developers.cloudflare.com/monetization-gateway/)

Monetization Gateway is now available in closed beta. Sellers can use it to charge agents for access to APIs, Model Context Protocol (MCP) tools, sites, and datasets.

Sellers (domain owners) define which requests require payment, the cost, and where the payment should be sent. Buyers receive the payment instructions, sign an authorization, and receive the resource after the payment has been settled. The Monetization Gateway uses the x402 protocol to handle payment authorization within the HTTP request flow.

To learn more, request access in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/monetize/monetization-gateway), review the [Monetization Gateway documentation](https://developers.cloudflare.com/monetization-gateway/), or read the [blog ↗︎](https://blog.cloudflare.com/monetization-gateway-beta/).

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

Sep 28, 2026

## [Browser Run adds WebMCP to Kitesurf and moves to document.modelContext](https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/) now works in [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) sessions as well as [Lab sessions](https://developers.cloudflare.com/browser-run/features/webmcp/#get-started). Both backends use the `document.modelContext` API from the [WebMCP Community Group draft ↗︎](https://webmachinelearning.github.io/webmcp/). Lab sessions no longer expose `navigator.modelContextTesting`.

To list and run page tools:

  * **Chrome DevTools** : Use the **Application** > **WebMCP** panel in the live view of a Lab session or in the [Kitesurf playground ↗︎](https://kitesurf.dev/).
  * **AI agents** : Start [Chrome DevTools MCP](https://developers.cloudflare.com/browser-run/features/webmcp/#using-an-ai-agent) with the `--category-experimental-webmcp` flag to add the `list_webmcp_tools` and `execute_webmcp_tool` tools.
  * **CDP clients** : Use the `WebMCP` CDP domain.



Sep 25, 2026

## [Subscribe to Browser Run crawl events](https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/)

[Browser Run](https://developers.cloudflare.com/browser-run/)[Queues](https://developers.cloudflare.com/queues/)

[Browser Run crawl jobs](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) can publish lifecycle events to [Cloudflare Queues](https://developers.cloudflare.com/queues/). Subscribe to started, updated, and finished events to track progress or trigger downstream processing without polling.

To create an account-level subscription, run the following command:

npmyarnpnpm
    
    
    npx wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
    
    
    yarn wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
    
    
    pnpm wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished

For payload examples, refer to the [Browser Run event schemas](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/#browser-run).

Sep 21, 2026

## [Browser Run adds session and DevTools methods to browser bindings](https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Run](https://developers.cloudflare.com/browser-run/) browser bindings now provide typed methods for session management and DevTools operations. You can acquire a session, connect a browser client, create Live View URLs, manage targets, and close sessions without constructing HTTP requests.

The new `acquire()` and `launch()` methods also accept [`outboundByHost`](https://developers.cloudflare.com/browser-run/features/outbound-workers/). This lets you route requests for selected hostnames through another Worker, including a Worker that adds authentication or reaches a private service.
    
    
    const connection = await env.BROWSER.launch({
    	outboundByHost: {
    		"private.example.test": env.OUTBOUND,
    	},
    });
    
    
    const connection = await env.BROWSER.launch({
    	outboundByHost: {
    		"private.example.test": env.OUTBOUND,
    	},
    });

Use `connectSession(sessionId)` when you need to acquire and connect in separate steps. The method returns a session-pinned `webSocket` Fetcher for a CDP client.

The binding also includes session methods for Live View, active sessions, session history, limits, session details, and cleanup. The nested `devtools` binding provides typed methods for browser version information, protocol descriptions, and target operations such as listing, creating, activating, and closing targets.

Refer to the [Browser binding API documentation](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/) for method signatures and the [outbound Worker feature guide](https://developers.cloudflare.com/browser-run/features/outbound-workers/) for routing examples.

Sep 18, 2026

## [Inspect logs, network requests, and DOM in Session Recordings](https://developers.cloudflare.com/changelog/post/2026-09-18-browser-run-session-recording-inspect/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Run Session Recordings](https://developers.cloudflare.com/browser-run/features/session-recording/) now include an **Inspect** panel, giving you more context to understand what happened during a browser session without having to reproduce it.

![Inspecting logs, network requests, and the DOM in a Browser Run Session Recording](https://developers.cloudflare.com/images/browser-run/session-recording-inspect.gif)

The **Logs** tab lets you search captured console output and filter messages by level. The **Network** tab shows each request's method, status, headers, payload, response, and timing waterfall, with the option to download the session's network activity as a HAR file.

You can also [retrieve recorded network activity via API](https://developers.cloudflare.com/browser-run/features/session-recording/#retrieve-network-activity-via-api) as raw JSON or a HAR file for use in your own debugging and analysis workflows.

The **DOM** tab provides an expandable view of the page structure at the end of the recording and lets you copy the reconstructed HTML. For sessions with multiple browser tabs, the Inspect panel updates to show data for the tab selected in the recording viewer.

To get started, enable recording when launching a browser session. After the session closes, open **Browser Run** > **Runs** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/browser-run/runs) and select the recording icon next to the session.

Refer to the [Session recording documentation](https://developers.cloudflare.com/browser-run/features/session-recording/) for setup instructions and current limits.

Sep 17, 2026

## [Reject busy synchronous inference requests](https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

The `rejectIfBusy` option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue.

Pass the option as the third argument to the Workers AI binding:
    
    
    const response = await env.AI.run(
    	"@cf/google/gemma-4-26b-a4b-it",
    	{
    		messages: [{ role: "user", content: "Explain capacity queues." }],
    	},
    	{ rejectIfBusy: true },
    );
    
    
    const response = await env.AI.run(
    	"@cf/google/gemma-4-26b-a4b-it",
    	{
    		messages: [{ role: "user", content: "Explain capacity queues." }],
    	},
    	{ rejectIfBusy: true },
    );

For the native REST API, add the option to the request body:
    
    
    curl --request POST \
      --url "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "messages": [{ "role": "user", "content": "Explain capacity queues." }],
        "options": { "rejectIfBusy": true }
      }'

Refer to [Reject busy requests](https://developers.cloudflare.com/workers-ai/features/reject-if-busy/) for OpenAI-compatible usage and error behavior.

Sep 14, 2026

## [Prevent Unified Billing fallback for BYOK third-party providers](https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway can now require credentials for third-party provider requests. Credentials must accompany the request or be stored on the gateway. This setting prevents fallback to Unified Billing with Cloudflare-managed credentials.

Turn on **Require provider credentials** in your gateway settings. To use the API, set `byok_only` to `true` in the request body of a [`PUT` request to update the gateway](https://developers.cloudflare.com/api/resources/ai_gateway/methods/update/):
    
    
    {
    	"byok_only": true
    }

To require provider credentials for one third-party request, set the `cf-aig-no-wholesale` header to `true`. This header cannot relax the gateway setting.

Requests without applicable credentials then return an HTTP `400` response. Workers AI requests remain allowed, and the setting does not change their configured billing mode.

For configuration details and request-level controls, refer to [Prevent Unified Billing fallback for BYOK third-party providers](https://developers.cloudflare.com/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers).

Sep 14, 2026

## [Control which hostnames Browser Run sessions can access](https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/)

[Browser Run](https://developers.cloudflare.com/browser-run/)

[Browser Run](https://developers.cloudflare.com/browser-run/) now supports [guardrails](https://developers.cloudflare.com/browser-run/features/guardrails/), which limit a browser session's HTTP and HTTPS requests to permitted hostnames.

Use guardrails when you need to:

  * Keep a browser workflow limited to a specific website and its subdomains.
  * Load only known third-party APIs, scripts, images, and fonts.
  * Generate a screenshot or PDF from HTML you provide while preventing it from loading external content.



Set guardrails when starting a session with Puppeteer, Playwright, or the REST API. With a browser binding named `MYBROWSER`, pass `guardrails` when launching Puppeteer:
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    export async function startGuardedSession(env) {
    	return puppeteer.launch(env.MYBROWSER, {
    		guardrails: {
    			allowedDomains: ["example.com", "*.example.com"],
    		},
    	});
    }
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    interface Env {
    	MYBROWSER: Fetcher;
    }
    
    export async function startGuardedSession(env: Env) {
    	return puppeteer.launch(env.MYBROWSER, {
    		guardrails: {
    			allowedDomains: ["example.com", "*.example.com"],
    		},
    	});
    }

In addition to session guardrails, Browser Run now supports a read-only mode for [Live View](https://developers.cloudflare.com/browser-run/features/live-view/). Live View lets you watch and interact with an active Browser Run session in real time. A read-only link lets someone watch without clicking, typing, navigating, or running JavaScript.

To create a read-only link, set `{ mode: "readonly" }` when generating the Live View URL. This setting affects only the person using that link. The session's hostname restrictions remain unchanged.

Refer to the [guardrails documentation](https://developers.cloudflare.com/browser-run/features/guardrails/) for more information.

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

Sep 11, 2026

## [AI Search supports extensionless R2 objects with Content-Type metadata](https://developers.cloudflare.com/changelog/post/2026-09-11-extensionless-r2-content-type/)

[AI Search](https://developers.cloudflare.com/ai-search/)

AI Search can index R2 objects without filename extensions when they include supported `Content-Type` metadata. This supports object keys that do not include file extensions while preserving file-type validation during indexing.

For supported file types and Content-Type requirements, refer to [R2 data sources](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/).

Sep 9, 2026

## [AI Gateway custom costs support cache tokens](https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers.

Add `per_cache_read_token` or `per_cache_write_token` to the `cf-aig-custom-cost` header:
    
    
    {
    	"per_token_in": 0.000001,
    	"per_token_out": 0.000002,
    	"per_cache_read_token": 0.0000001,
    	"per_cache_write_token": 0.0000005
    }

Cache-token pricing activates when either cache rate is present. An omitted cache rate defaults to `per_token_in`. If both cache rates are omitted, AI Gateway preserves the existing input and output calculation.

Providers can include cache tokens within input tokens or report them separately. AI Gateway automatically accounts for these differences and prevents double-counting.

For more information, refer to [Custom costs](https://developers.cloudflare.com/ai-gateway/configuration/custom-costs/).

Sep 2, 2026

## [Run Cursor Cloud Agents on Cloudflare via self-hosted machines](https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/)

[Sandboxes](https://developers.cloudflare.com/sandbox/)

[Cursor self-hosted machines ↗︎](https://cursor.com/docs/cloud-agent/self-hosted) let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by [Cloudflare Containers](https://developers.cloudflare.com/containers/).

![Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3308,height=1916,format=webp/_astro/cursor-cloud-agents-self-hosted-pool.XNeWCXB2.png)

Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source [Cursor Cloudflare Workers template ↗︎](https://github.com/anysphere/cloudflare-workers) deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.

To get started, refer to [Run Cursor Cloud Agents on Cloudflare via self-hosted machines](https://developers.cloudflare.com/sandbox/coding-agents/cursor/).

Sep 1, 2026

## [AI Gateway consolidates monthly usage invoice line items and standardizes model names](https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway monthly usage invoices, issued at the beginning of each month for the previous month's usage, now show a single total cost for each model. These invoices no longer break out input and output token quantities and unit prices into separate line items. This change does not apply to invoices for AI Gateway credit purchases.

For example, an invoice that previously included these separate line items:

  * `anthropic claude-haiku-4-5-20251001 Input Tokens`: 40,000 tokens at $0.000001 ($0.04)
  * `anthropic claude-haiku-4-5-20251001 Output Tokens`: 24,000 tokens at $0.000005 ($0.12)



The updated invoice includes one line item: `anthropic/claude-haiku-4.5`: $0.16.

AI Gateway has also standardized model names across invoices and logs. Model variants that previously appeared with provider-specific version suffixes now use a consistent `provider/model` identifier.

For more information, refer to the [Unified Billing documentation](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) and [AI Gateway logging documentation](https://developers.cloudflare.com/ai-gateway/observability/logging/).

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/ai/2/)…[8](https://developers.cloudflare.com/changelog/product-group/ai/8/)

[Next →](https://developers.cloudflare.com/changelog/product-group/ai/2/)
