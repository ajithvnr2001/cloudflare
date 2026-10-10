---
url: https://developers.cloudflare.com/changelog/product/workers-ai/
title: Workers AI Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:02.905110+00:00
---

# Workers AI Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/workers-ai/

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

Aug 28, 2026

## [Z.ai GLM-5.3 now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-08-28-glm-5.3-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/zai-org/glm-5.3`](https://developers.cloudflare.com/workers-ai/models/glm-5.3/) is now available on Workers AI. It is Z.ai's flagship agentic coding model, built for long-running, tool-driven development workflows rather than single-turn chat.

GLM-5.3 uses the same base model as GLM-5.2, with every gain coming from post-training. The results are substantial on coding and agentic benchmarks: [Z.ai reports ↗︎](https://huggingface.co/zai-org/GLM-5.3) a 50% improvement over GLM-5.2 on its in-house Z.ai Code Bench, and calls GLM-5.3 the most capable open-weights model for coding. On public benchmarks, it scores 88.2 on Terminal Bench 2.1 (up from 81.0), 28.3 on Terminal Bench 3.0 — open-source state of the art, up from 4.6 — 66.9 on DeepSWE (up from 46.2), 78.1 on FrontierSWE (up from 67.5), and 42.5 on SWE-Marathon (up from 19.4). It is also the top-scoring model in Z.ai's comparisons on CyberGym for vulnerability discovery (84.5) and on long-horizon automation tasks like AutomationBench (48.2).

The price-to-performance ratio is the compelling part. On Workers AI, GLM-5.3 costs the same as GLM-5.2 — $1.40 per M input tokens, $0.26 per M cached input tokens, and $4.40 per M output tokens — while roughly doubling GLM-5.2's scores on long-horizon benchmarks like SWE-Marathon, and improving them by more than 6x on Terminal Bench 3.0.

GLM-5.3 requires the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use GLM-5.3 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [GLM-5.3 model page](https://developers.cloudflare.com/workers-ai/models/glm-5.3/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Aug 26, 2026

## [Z.ai GLM-5.3 Flash now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/zai-org/glm-5.3-flash`](https://developers.cloudflare.com/workers-ai/models/glm-5.3-flash/) is now available on Workers AI. It is the first natively multimodal model in the GLM-5 series, built on a Mixture-of-Experts architecture with 320B total parameters and 18B active per token.

GLM-5.3 Flash is the first GLM-family model on Workers AI to support multimodal inputs. It outperforms GLM-5.2 across benchmarks and real-world workloads at a lower price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.

GLM-5.3 Flash requires the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use GLM-5.3 Flash through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [GLM-5.3 Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-5.3-flash/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Aug 17, 2026

## [Qwen 3.8 27B now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-08-17-qwen-3.8-27b-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/qwen/qwen3.8-27b`](https://developers.cloudflare.com/workers-ai/models/qwen3.8-27b/) is now available on Workers AI.

Qwen 3.8 27B is a 27-billion-parameter instruction-tuned vision language model from Alibaba's Qwen family. It processes images and text together, with reasoning and function calling for agentic workflows.

**Key capabilities:**

  * **Vision** : Accept image and text inputs and generate text responses.
  * **Reasoning** : Support thinking mode for complex, step-by-step problem-solving.
  * **Function calling** : Build agents that invoke tools and APIs across multiple conversation turns.
  * **262,144 token context window** : Retain long conversations and multimodal inputs across extended agent sessions.



Use Qwen 3.8 27B through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`) or the REST API at `/ai/run`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with these endpoints.

For more information, refer to the [Qwen 3.8 27B model page](https://developers.cloudflare.com/workers-ai/models/qwen3.8-27b/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Aug 14, 2026

## [DeepSeek V4 Flash and Pro now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-08-14-deepseek-v4-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/deepseek-ai/deepseek-v4-pro-0813`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-pro-0813/) and [`@cf/deepseek-ai/deepseek-v4-flash-0731`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/) are now available on Workers AI.

DeepSeek V4 Flash and DeepSeek V4 Pro are the first Workers AI models with a full **one million (1,048,576) token context window**. Use them for long-horizon agentic workflows, large codebases, and multi-step reasoning that exceed the context limits of every other model hosted on the platform.

DeepSeek V4 Flash is the faster, lower-cost sibling. This release supersedes the preview version with substantially enhanced agentic capabilities.

**Key capabilities:**

  * **Reasoning** : Both models support thinking mode for complex, step-by-step problem-solving.
  * **Function calling** : Build agents that invoke tools and APIs across multiple conversation turns.
  * **Long context** : Both models support a full 1,048,576 token context window.



Both models require the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/).

Use these models through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [DeepSeek V4 Pro model page](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-pro-0813/), the [DeepSeek V4 Flash model page](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/), and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Aug 7, 2026

## [Workers AI and AI Gateway unify model access and billing](https://developers.cloudflare.com/changelog/post/2026-08-07-workers-ai-unified-billing/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Workers AI](https://developers.cloudflare.com/workers-ai/)

Workers AI and AI Gateway now provide a unified path for accessing models and managing inference traffic. Use the same AI binding and REST API to call models hosted on Workers AI or by supported third-party providers, with AI Gateway providing observability, logging, caching, security, and billing controls.

#### Unified entrypoints and observability

The [AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/) supports both Workers AI and third-party models through `env.AI.run()`. The [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) provides shared `/ai/` endpoints with Cloudflare authentication across providers.

Route a Workers AI request through AI Gateway by specifying a gateway ID. Use `default` to automatically create a gateway on the first authenticated request, or specify an existing gateway to separate applications and workloads:
    
    
    const response = await env.AI.run(
    	"@cf/zai-org/glm-5.2",
    	{
    		messages: [{ role: "user", content: "What is the capital of France?" }],
    	},
    	{
    		gateway: { id: "default" },
    	},
    );
    
    
    const response = await env.AI.run(
    	"@cf/zai-org/glm-5.2",
    	{
    		messages: [{ role: "user", content: "What is the capital of France?" }],
    	},
    	{
    		gateway: { id: "default" },
    	},
    );

Requests routed through AI Gateway can be logged and included in analytics for request volume, errors, latency, token usage, and costs. You can also configure controls such as caching, rate limiting, and request retries on the gateway.

#### Unified billing and higher rate limits

You can now use prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) to pay for Workers AI inference. This provides one credit balance for Workers AI and supported third-party model providers. To use credits for Workers AI, set the gateway's [Workers AI billing setting](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing) to **Unified billing**. Workers AI requests routed through that gateway deduct from your credit balance in real time.

Prepaid credits also provide access to the following Workers AI frontier models without requiring the Workers Paid plan. Each frontier Workers AI model has a rate limit of 50 requests per minute per account, per model when billed with AI Gateway credits, compared to 20 requests per minute through standard Workers AI billing:

  * [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/)
  * [`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/)
  * [`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/)



These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.

For details, refer to [Workers AI limits](https://developers.cloudflare.com/workers-ai/platform/limits/), [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/), [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), and the [AI Gateway model catalog](https://developers.cloudflare.com/ai/models/).

Jul 28, 2026

## [Select models now require the Workers Paid plan](https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We are limiting Workers Free plan access to a few resource-intensive models so we can prioritize capacity for the broader Workers AI user base. This helps everyone get a more reliable inference experience, with fewer `429` and `3040` (Out of Capacity) errors.

The following models now require the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers):

  * [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/)
  * [`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/)
  * [`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/)



On the Workers Free plan, requests to these models now return a `403` HTTP error ([internal error `5035`](https://developers.cloudflare.com/workers-ai/platform/errors/)) prompting you to upgrade. The Workers Paid plan starts at $5 per month and still includes the 10,000 free Neurons per day allocation, with usage beyond that billed at each [model's pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Many models remain available on the Workers Free plan, including:

  * [`@cf/zai-org/glm-4.7-flash`](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/)
  * [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/)
  * [`@cf/nvidia/nemotron-3-120b-a12b`](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/)



For the full list, refer to the [Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/).

Jul 10, 2026

## [Plain text output for Markdown Conversion](https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-conversion-text-output/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

The [Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) service now supports a new `output` conversion option that controls the format of the converted content.

Set `output.format` to `text` to receive plain text with Markdown syntax removed. The default value is `markdown`, so existing conversions are unchanged.

Use the [`env.AI`](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/) binding:
    
    
    await env.AI.toMarkdown(
    	{ name: "page.html", blob: new Blob([html]) },
    	{
    		conversionOptions: {
    			output: { format: "text" },
    		},
    	},
    );
    
    
    await env.AI.toMarkdown(
    	{ name: "page.html", blob: new Blob([html]) },
    	{
    		conversionOptions: {
    			output: { format: "text" },
    		},
    	},
    );

Or call the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \
      -H 'Authorization: Bearer {API_TOKEN}' \
      -F 'files=@index.html' \
      -F 'conversionOptions={"output": {"format": "text"}}'

When you request text output, the `format` field of each result is set to `text`. For more details, refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/#output).

Jul 8, 2026

## [Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion](https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)[AI Search](https://developers.cloudflare.com/ai-search/)

Workers AI [Markdown conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) (`toMarkdown`) now supports `.gif` and `.bmp` image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.

GIF and BMP files run through the same [image pipeline](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/#images) as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.

[AI Search](https://developers.cloudflare.com/ai-search/) uses `toMarkdown` automatically to process the files it ingests, so any `.gif` and `.bmp` files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.

Learn more about [Markdown conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) and the full list of [AI Search's supported file types](https://developers.cloudflare.com/ai-search/configuration/data-source/#supported-file-types).

Jul 8, 2026

## [Moondream 3.1 now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-07-08-moondream3.1-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Partnering with [Moondream ↗︎](https://moondream.ai/) to bring their latest model [`@cf/moondream/moondream3.1-9B-A2B`](https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/) to Workers AI. Moondream 3.1 is a fast vision language model built on a mixture-of-experts architecture with 9B total parameters and 2B active, delivering frontier-level visual reasoning while retaining fast, cost-efficient inference.

Moondream 3.1 is designed for real-world vision tasks, with a 32K token context window for handling complex queries and structured outputs.

#### Key capabilities

  * **Query** — ask open-ended questions about an image, with an optional reasoning parameter
  * **Caption** — generate short, normal, or long descriptions of an image
  * **Point** — return coordinates for objects matching a target phrase
  * **Detect** — return bounding boxes for objects matching a target phrase



#### Real-time vision at the edge

Vision workloads like live camera feeds, robotics, content moderation, and interactive agents need answers in milliseconds, not seconds. Moondream 3.1's small active footprint (2B active parameters) pairs well with Workers AI's serverless, globally distributed inference: requests run close to your users, and streaming responses start returning tokens almost immediately.

In our testing, first tokens streamed back in roughly 20–30 ms, and results were fast across every task. The example end-to-end times below (client-observed median, including network round trip) are for a simple, single-subject image. Actual latency depends heavily on the image and how much detail you ask for.

Task | End-to-end (p50)  
---|---  
`query` | ~770 ms  
`caption` | ~480 ms  
`point` | ~145 ms  
`detect` | ~160 ms  
  
At these speeds you can call the model inline while handling a request rather than pushing the work to a background queue or a separate service. That opens up use cases where a slow response breaks the experience: moderating user-uploaded images before they are stored, locating an object in a video frame to drive a live overlay, extracting fields from a document during a form submission, or letting an agent inspect a screenshot and decide its next step within a single turn.

#### Get started

Use Moondream 3.1 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`) or the REST API at `/ai/run`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with these endpoints.

For more information, refer to the [Moondream 3.1 model page](https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

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

Jun 12, 2026

## [Moonshot AI Kimi K2.7 Code now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.

#### Improved coding and agent performance

K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:

  * **+21.8%** on Kimi Code Bench v2
  * **+11.0%** on Program Bench
  * **+31.5%** on MLS Bench Lite



#### Reasoning efficiency

K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.

#### Key capabilities

  * **262.1k token context window** for retaining full conversation history, tool definitions, and codebases across long-running agent sessions
  * **Long-horizon coding** with improved instruction following and higher end-to-end coding task success rates
  * **Vision inputs** for processing images alongside text
  * **Thinking mode** with configurable reasoning depth via `chat_template_kwargs.thinking`
  * **Multi-turn tool calling** for building agents that invoke tools across multiple conversation turns
  * **Structured outputs** with JSON schema support



#### Differences from Kimi K2.6

If you are migrating from Kimi K2.6, note the following:

  * K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency
  * Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)
  * API usage is identical — no parameter changes required



#### Get started

Use Kimi K2.7 Code through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/ai/run`, or the OpenAI-compatible endpoint at `/v1/chat/completions`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with any of these endpoints.

For more information, refer to the [Kimi K2.7 Code model page](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

May 8, 2026

## [Planned model deprecations on Workers AI](https://developers.cloudflare.com/changelog/post/2026-05-08-planned-model-deprecations/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We are refreshing the Workers AI model catalog to make room for newer releases. Please update your apps to remove references to the models listed below before the deprecation date.

#### Recommended replacements

  * [`@cf/zai-org/glm-4.7-flash`](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) — fast multilingual model with multi-turn tool calling and coding capabilities.
  * [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/) — efficient open model with vision and tool calling.
  * [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/) — capable tool-calling and vision model for agentic workloads and coding.



For pricing, refer to the [Workers AI pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

#### Kimi K2.5

We originally stated Kimi K2.5 would be deprecated on May 10, 2026, however we have extended the deprecation date to May 30, 2026. Requests will be automatically aliased to Kimi K2.6 on May 30, 2026, which has a higher price. Please review the [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/) pricing and model capabilities prior to May 30, 2026 to ensure that the model suits your needs.

#### Models deprecated on May 30, 2026

  * `@cf/moonshotai/kimi-k2.5` \--> `@cf/moonshotai/kimi-k2.6`
  * `@hf/meta-llama/meta-llama-3-8b-instruct`
  * `@cf/meta/llama-3-8b-instruct`
  * `@cf/meta/llama-3-8b-instruct-awq`
  * `@cf/meta/llama-3.1-8b-instruct`
  * `@cf/meta/llama-3.1-8b-instruct-awq`
  * `@cf/meta/llama-3.1-70b-instruct`
  * `@cf/meta/llama-2-7b-chat-int8`
  * `@cf/meta/llama-2-7b-chat-fp16`
  * `@cf/mistral/mistral-7b-instruct-v0.1`
  * `@hf/mistral/mistral-7b-instruct-v0.2`
  * `@hf/google/gemma-7b-it`
  * `@cf/google/gemma-3-12b-it`
  * `@hf/nousresearch/hermes-2-pro-mistral-7b`
  * `@cf/microsoft/phi-2`
  * `@cf/defog/sqlcoder-7b-2`
  * `@cf/unum/uform-gen2-qwen-500m`
  * `@cf/facebook/bart-large-cnn`



#### Variants that remain active

The `-fast` and `-lora` variants of models will remain active, including:

  * `@cf/meta/llama-3.3-70b-instruct-fp8-fast`
  * `@cf/meta/llama-3.1-8b-instruct-fast`
  * `@cf/google/gemma-7b-it-lora`
  * `@cf/google/gemma-2b-it-lora`
  * `@cf/mistral/mistral-7b-instruct-v0.2-lora`
  * `@cf/meta-llama/llama-2-7b-chat-hf-lora`



LoRA models may be deprecated in the future. We will be adding more LoRA capabilities to the catalog, and will communicate when new LoRA models come online to give users time to train new LoRAs before we deprecate old ones.

For the full list of available models, refer to the [Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/).

Apr 20, 2026

## [Moonshot AI Kimi K2.6 now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-04-20-kimi-k2-6-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/) is now available on Workers AI, in partnership with Moonshot AI for Day 0 support. Kimi K2.6 is a native multimodal agentic model from Moonshot AI that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.

Built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token, Kimi K2.6 delivers frontier-scale intelligence with efficient inference. It scores competitively against GPT-5.4 and Claude Opus 4.6 on agentic and coding benchmarks, including BrowseComp (83.2), SWE-Bench Verified (80.2), and Terminal-Bench 2.0 (66.7).

#### Key capabilities

  * **262.1k token context window** for retaining full conversation history, tool definitions, and codebases across long-running agent sessions
  * **Long-horizon coding** with significant improvements on complex, end-to-end coding tasks across languages including Rust, Go, and Python
  * **Coding-driven design** that transforms simple prompts and visual inputs into production-ready interfaces and full-stack workflows
  * **Agent swarm orchestration** scaling horizontally to 300 sub-agents executing 4,000 coordinated steps for complex autonomous tasks
  * **Vision inputs** for processing images alongside text
  * **Thinking mode** with configurable reasoning depth
  * **Multi-turn tool calling** for building agents that invoke tools across multiple conversation turns



#### Differences from Kimi K2.5

If you are migrating from Kimi K2.5, note the following API changes:

  * K2.6 uses `chat_template_kwargs.thinking` to control reasoning, replacing `chat_template_kwargs.enable_thinking`
  * K2.6 returns reasoning content in the `reasoning` field, replacing `reasoning_content`



#### Get started

Use Kimi K2.6 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/ai/run`, or the OpenAI-compatible endpoint at `/v1/chat/completions`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with any of these endpoints.

For more information, refer to the [Kimi K2.6 model page](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Apr 4, 2026

## [Google Gemma 4 26B A4B now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We are partnering with Google to bring [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/) to Workers AI. Gemma 4 26B A4B is a Mixture-of-Experts (MoE) model built from Gemini 3 research, with 26B total parameters and only 4B active per forward pass. By activating a small subset of parameters during inference, the model runs almost as fast as a 4B-parameter model while delivering the quality of a much larger one.

Gemma 4 is Google's most capable family of open models, designed to maximize intelligence-per-parameter.

#### Key capabilities

  * **Mixture-of-Experts architecture** with 8 active experts out of 128 total (plus 1 shared expert), delivering frontier-level performance at a fraction of the compute cost of dense models
  * **256,000 token context window** for retaining full conversation history, tool definitions, and long documents across extended sessions
  * **Built-in thinking mode** that lets the model reason step-by-step before answering, improving accuracy on complex tasks
  * **Vision understanding** for object detection, document and PDF parsing, screen and UI understanding, chart comprehension, OCR (including multilingual), and handwriting recognition, with support for variable aspect ratios and resolutions
  * **Function calling** with native support for structured tool use, enabling agentic workflows and multi-step planning
  * **Multilingual** with out-of-the-box support for 35+ languages, pre-trained on 140+ languages
  * **Coding** for code generation, completion, and correction



Use Gemma 4 26B A4B through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, or the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/).

For more information, refer to the [Gemma 4 26B A4B model page](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/).

Mar 19, 2026

## [Moonshot AI Kimi K2.5 now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-03-19-kimi-k2-5-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Workers AI is officially in the big models game. [`@cf/moonshotai/kimi-k2.5`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.5/) is the first frontier-scale open-source model on our AI inference platform — a large model with a full 256k context window, multi-turn tool calling, vision inputs, and structured outputs. By bringing a frontier-scale model directly onto the Cloudflare Developer Platform, you can now run the entire agent lifecycle on a single, unified platform.

The model has proven to be a fast, efficient alternative to larger proprietary models without sacrificing quality. As AI adoption increases, the volume of inference is skyrocketing — now you can access frontier intelligence at a fraction of the cost.

#### Key capabilities

  * **256,000 token context window** for retaining full conversation history, tool definitions, and entire codebases across long-running agent sessions
  * **Multi-turn tool calling** for building agents that invoke tools across multiple conversation turns
  * **Vision inputs** for processing images alongside text
  * **Structured outputs** with JSON mode and JSON Schema support for reliable downstream parsing
  * **Function calling** for integrating external tools and APIs into agent workflows



#### Prefix caching and session affinity

When an agent sends a new prompt, it resends all previous prompts, tools, and context from the session. The delta between consecutive requests is usually just a few new lines of input. Prefix caching avoids reprocessing the shared context, saving time and compute from the prefill stage. This means faster Time to First Token (TTFT) and higher Tokens Per Second (TPS) throughput.

Workers AI has done prefix caching, but we are now surfacing cached tokens as a usage metric and offering a discount on cached tokens compared to input tokens (pricing is listed on the [model page](https://developers.cloudflare.com/workers-ai/models/kimi-k2.5/)).
    
    
    curl -X POST \
      "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/moonshotai/kimi-k2.5" \
      -H "Authorization: Bearer {api_token}" \
      -H "Content-Type: application/json" \
      -H "x-session-affinity: ses_12345678" \
      -d '{
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful assistant."
          },
          {
            "role": "user",
            "content": "What is prefix caching and why does it matter?"
          }
        ],
        "max_tokens": 2400,
        "stream": true
      }'

Some clients like [OpenCode ↗︎](https://opencode.ai) implement session affinity automatically. The [Agents SDK ↗︎](https://github.com/cloudflare/agents) starter also sets up the wiring for you.

#### Redesigned asynchronous API

For volumes of requests that exceed synchronous rate limits, you can submit batches of inferences to be completed asynchronously. We have revamped the [Asynchronous Batch API](https://developers.cloudflare.com/workers-ai/features/batch-api/) with a pull-based system that processes queued requests as soon as capacity is available. With internal testing, async requests usually execute within 5 minutes, but this depends on live traffic.

The async API is the best way to avoid capacity errors in durable workflows. It is ideal for use cases that are not real-time, such as code scanning agents or research agents.

To use the asynchronous API, pass `queueRequest: true`:
    
    
    // 1. Push a batch of requests into the queue
    const res = await env.AI.run(
    	"@cf/moonshotai/kimi-k2.5",
    	{
    		requests: [
    			{
    				messages: [{ role: "user", content: "Tell me a joke" }],
    			},
    			{
    				messages: [{ role: "user", content: "Explain the Pythagoras theorem" }],
    			},
    		],
    	},
    	{ queueRequest: true },
    );
    
    // 2. Grab the request ID
    const requestId = res.request_id;
    
    // 3. Poll for the result
    const result = await env.AI.run("@cf/moonshotai/kimi-k2.5", {
    	request_id: requestId,
    });
    
    if (result.status === "queued" || result.status === "running") {
    	// Retry by polling again
    } else {
    	return Response.json(result);
    }

You can also set up [event notifications](https://developers.cloudflare.com/workers-ai/platform/event-subscriptions/) to know when inference is complete instead of polling.

#### Get started

Use Kimi K2.5 through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, [AI Gateway](https://developers.cloudflare.com/ai-gateway/), or via the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/).

For more information, refer to the [Kimi K2.5 model page](https://developers.cloudflare.com/workers-ai/models/kimi-k2.5/), [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/), and [prompt caching](https://developers.cloudflare.com/workers-ai/features/prompt-caching/).

Mar 11, 2026

## [NVIDIA Nemotron 3 Super now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We're excited to partner with NVIDIA to bring [`@cf/nvidia/nemotron-3-120b-a12b`](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/) to Workers AI. NVIDIA Nemotron 3 Super is a Mixture-of-Experts (MoE) model with a hybrid Mamba-transformer architecture, 120B total parameters, and 12B active parameters per forward pass.

The model is optimized for running many collaborating agents per application. It delivers high accuracy for reasoning, tool calling, and instruction following across complex multi-step tasks.

**Key capabilities:**

  * **Hybrid Mamba-transformer architecture** delivers over 50% higher token generation throughput compared to leading open models, reducing latency for real-world applications
  * **Tool calling** support for building AI agents that invoke tools across multiple conversation turns
  * **Multi-Token Prediction (MTP)** accelerates long-form text generation by predicting several future tokens simultaneously in a single forward pass
  * **32,000 token context window** for retaining conversation history and plan states across multi-step agent workflows



Prompt caching

For optimal performance with multi-turn conversations, send the `x-session-affinity` header with a unique session identifier to enable prompt caching. This routes requests to the same model instance, reducing latency and inference costs. For details, refer to [Prompt caching](https://developers.cloudflare.com/workers-ai/features/prompt-caching/).

Use Nemotron 3 Super through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, or the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/).

For more information, refer to the [Nemotron 3 Super model page](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/).

Mar 6, 2026

## [Real-time transcription in RealtimeKit now supports 10 languages with regional variants](https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)[Realtime](https://developers.cloudflare.com/realtime/)

[Real-time transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) in RealtimeKit now supports 10 languages with regional variants, powered by [Deepgram Nova-3](https://developers.cloudflare.com/workers-ai/models/nova-3/) running on [Workers AI](https://developers.cloudflare.com/workers-ai/).

During a meeting, participant audio is routed through [AI Gateway](https://developers.cloudflare.com/ai-gateway/) to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.

Set the language when [creating a meeting](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/) via `ai_config.transcription.language`:
    
    
    {
    	"ai_config": {
    		"transcription": {
    			"language": "fr"
    		}
    	}
    }

Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like `en-AU`, `en-GB`, `en-IN`, `en-NZ`, `es-419`, `fr-CA`, `de-CH`, `pt-BR`, and `pt-PT`. Use `multi` for automatic multilingual detection.

If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.

  * [Transcription docs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)
  * [Nova-3 model page](https://developers.cloudflare.com/workers-ai/models/nova-3/)
  * [Workers AI](https://developers.cloudflare.com/workers-ai/)
  * [AI Gateway](https://developers.cloudflare.com/ai-gateway/)



Mar 4, 2026

## [New conversion options for Markdown Conversion](https://developers.cloudflare.com/changelog/post/2026-03-04-new-markdown-conversion-options/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

You can now customize how the [Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) service processes different file types by passing a `conversionOptions` object.

Available options:

  * **Images** : Set the language for AI-generated image descriptions
  * **HTML** : Use CSS selectors to extract specific content, or provide a hostname to resolve relative links
  * **PDF** : Exclude metadata from the output



Use the [`env.AI`](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/) binding:
    
    
    await env.AI.toMarkdown(
    	{ name: "page.html", blob: new Blob([html]) },
    	{
    		conversionOptions: {
    			html: { cssSelector: "article.content" },
    			image: { descriptionLanguage: "es" },
    		},
    	},
    );
    
    
    await env.AI.toMarkdown(
    	{ name: "page.html", blob: new Blob([html]) },
    	{
    		conversionOptions: {
    			html: { cssSelector: "article.content" },
    			image: { descriptionLanguage: "es" },
    		},
    	},
    );

Or call the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \
      -H 'Authorization: Bearer {API_TOKEN}' \
      -F 'files=@index.html' \
      -F 'conversionOptions={"html": {"cssSelector": "article.content"}}'

For more details, refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/).

Feb 19, 2026

## [AI dashboard experience improvements](https://developers.cloudflare.com/changelog/post/2026-02-19-ai-dashboard-experience-improvements/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Workers AI](https://developers.cloudflare.com/workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/) and [AI Gateway](https://developers.cloudflare.com/ai-gateway/) have received a series of dashboard improvements to help you get started faster and manage your AI workloads more easily.

**Navigation and discoverability**

AI now has its own top-level section in the Cloudflare dashboard sidebar, so you can find AI features without digging through menus.

![AI sidebar navigation in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2328,height=1140,format=webp/_astro/sidebar-navigation.BQNFBmAk.png)_The new top-level AI section in the dashboard sidebar._

**Onboarding and getting started**

[Getting started](https://developers.cloudflare.com/ai-gateway/get-started/) with AI Gateway is now simpler. When you create your first gateway, we now show your gateway's OpenAI-compatible endpoint and step-by-step guidance to help you configure it. The Playground also includes helpful prompts, and usage pages have clear next steps if you have not made any requests yet.

![AI Gateway onboarding flow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1232,format=webp/_astro/onboarding-flow.DZ7aMcHa.png)_The first-run setup experience for new gateways._

We've also combined the previously separate code example sections into one view with dropdown selectors for API type, provider, SDK, and authentication method so you can now customize the exact code snippet you need from one place.

**Dynamic Routing**

  * The [route builder](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) is now more performant and responsive.
  * You can now copy route names to your clipboard with a single click.
  * Code examples use the [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) format, making it easier to integrate routes into your application.



**Observability and analytics**

  * Small monetary values now display correctly in [cost analytics](https://developers.cloudflare.com/ai-gateway/observability/costs/) charts, so you can accurately track spending at any scale.



**Accessibility**

  * Improvements to keyboard navigation within the AI Gateway, specifically when exploring usage by [provider](https://developers.cloudflare.com/ai-gateway/usage/providers/).
  * Improvements to sorting and filtering components on the [Workers AI](https://developers.cloudflare.com/workers-ai/models/) models page.



For more information, refer to the [AI Gateway documentation](https://developers.cloudflare.com/ai-gateway/).

Feb 13, 2026

## [Introducing GLM-4.7-Flash on Workers AI, @cloudflare/tanstack-ai, and workers-ai-provider v3.1.1](https://developers.cloudflare.com/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/)

[Workers](https://developers.cloudflare.com/workers/)[Agents](https://developers.cloudflare.com/agents/)[Workers AI](https://developers.cloudflare.com/workers-ai/)

We're excited to announce **GLM-4.7-Flash** on Workers AI, a fast and efficient text generation model optimized for multilingual dialogue and instruction-following tasks, along with the brand-new [**@cloudflare/tanstack-ai** ↗︎](https://www.npmjs.com/package/@cloudflare/tanstack-ai) package and [**workers-ai-provider v3.1.1** ↗︎](https://www.npmjs.com/package/workers-ai-provider).

You can now run AI agents entirely on Cloudflare. With GLM-4.7-Flash's multi-turn tool calling support, plus full compatibility with TanStack AI and the Vercel AI SDK, you have everything you need to build agentic applications that run completely at the edge.

#### GLM-4.7-Flash — Multilingual Text Generation Model

[`@cf/zai-org/glm-4.7-flash`](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) is a multilingual model with a 131,072 token context window, making it ideal for long-form content generation, complex reasoning tasks, and multilingual applications.

**Key Features and Use Cases:**

  * **Multi-turn Tool Calling for Agents** : Build AI agents that can call functions and tools across multiple conversation turns
  * **Multilingual Support** : Built to handle content generation in multiple languages effectively
  * **Large Context Window** : 131,072 tokens for long-form writing, complex reasoning, and processing long documents
  * **Fast Inference** : Optimized for low-latency responses in chatbots and virtual assistants
  * **Instruction Following** : Excellent at following complex instructions for code generation and structured tasks



Use GLM-4.7-Flash through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API at `/run` or `/v1/chat/completions`, [AI Gateway](https://developers.cloudflare.com/ai-gateway/), or via [workers-ai-provider](https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/) for the Vercel AI SDK.

Pricing is available on the [model page](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) or [pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

#### @cloudflare/tanstack-ai v0.1.1 — TanStack AI adapters for Workers AI and AI Gateway

We've released `@cloudflare/tanstack-ai`, a new package that brings Workers AI and AI Gateway support to [TanStack AI ↗︎](https://tanstack.com/ai). This provides a framework-agnostic alternative for developers who prefer TanStack's approach to building AI applications.

**Workers AI adapters** support four configuration modes — plain binding (`env.AI`), plain REST, AI Gateway binding (`env.AI.gateway(id)`), and AI Gateway REST — across all capabilities:

  * **Chat** (`createWorkersAiChat`) — Streaming chat completions with tool calling, structured output, and reasoning text streaming.
  * **Image generation** (`createWorkersAiImage`) — Text-to-image models.
  * **Transcription** (`createWorkersAiTranscription`) — Speech-to-text.
  * **Text-to-speech** (`createWorkersAiTts`) — Audio generation.
  * **Summarization** (`createWorkersAiSummarize`) — Text summarization.



**AI Gateway adapters** route requests from third-party providers — OpenAI, Anthropic, Gemini, Grok, and OpenRouter — through Cloudflare AI Gateway for caching, rate limiting, and unified billing.

To get started:
    
    
    npm install @cloudflare/tanstack-ai @tanstack/ai

#### workers-ai-provider v3.1.1 — transcription, speech, reranking, and reliability

The Workers AI provider for the [Vercel AI SDK ↗︎](https://ai-sdk.dev) now supports three new capabilities beyond chat and image generation:

  * **Transcription** (`provider.transcription(model)`) — Speech-to-text with automatic handling of model-specific input formats across binding and REST paths.
  * **Text-to-speech** (`provider.speech(model)`) — Audio generation with support for voice and speed options.
  * **Reranking** (`provider.reranking(model)`) — Document reranking for RAG pipelines and search result ordering.


    
    
    import { createWorkersAI } from "workers-ai-provider";
    import {
    	experimental_transcribe,
    	experimental_generateSpeech,
    	rerank,
    } from "ai";
    
    const workersai = createWorkersAI({ binding: env.AI });
    
    const transcript = await experimental_transcribe({
    	model: workersai.transcription("@cf/openai/whisper-large-v3-turbo"),
    	audio: audioData,
    	mediaType: "audio/wav",
    });
    
    const speech = await experimental_generateSpeech({
    	model: workersai.speech("@cf/deepgram/aura-1"),
    	text: "Hello world",
    	voice: "asteria",
    });
    
    const ranked = await rerank({
    	model: workersai.reranking("@cf/baai/bge-reranker-base"),
    	query: "What is machine learning?",
    	documents: ["ML is a branch of AI.", "The weather is sunny."],
    });

This release also includes a comprehensive reliability overhaul (v3.0.5):

  * **Fixed streaming** — Responses now stream token-by-token instead of buffering all chunks, using a proper `TransformStream` pipeline with backpressure.
  * **Fixed tool calling** — Resolved issues with tool call ID sanitization, conversation history preservation, and a heuristic that silently fell back to non-streaming mode when tools were defined.
  * **Premature stream termination detection** — Streams that end unexpectedly now report `finishReason: "error"` instead of silently reporting `"stop"`.
  * **AI Search support** — Added `createAISearch` as the canonical export (renamed from AutoRAG). `createAutoRAG` still works with a deprecation warning.



To upgrade:
    
    
    npm install workers-ai-provider@latest ai

#### Resources

  * [@cloudflare/tanstack-ai on npm ↗︎](https://www.npmjs.com/package/@cloudflare/tanstack-ai)
  * [workers-ai-provider on npm ↗︎](https://www.npmjs.com/package/workers-ai-provider)
  * [GitHub repository ↗︎](https://github.com/cloudflare/ai)



Jan 28, 2026

## [Launching FLUX.2 [klein] 9B on Workers AI](https://developers.cloudflare.com/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We have partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 9B model to Workers AI. This distilled model offers enhanced quality compared to the 4B variant, while maintaining cost-effective pricing. With a fixed 4-step inference process, Klein 9B is ideal for rapid prototyping and real-time applications where both speed and quality matter.

Read the [BFL blog ↗︎](https://bfl.ai/blog) to learn more about the model itself, or try it out yourself on our [multi modal playground ↗︎](https://multi-modal.ai.cloudflare.com/).

Pricing documentation is available on the [model page](https://developers.cloudflare.com/workers-ai/models/flux-2-klein-9b/) or [pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

#### Workers AI platform specifics

The model hosted on Workers AI is optimized for speed with a **fixed 4-step inference process** and supports up to 4 image inputs. Since this is a distilled model, the `steps` parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev] and FLUX.2 [klein] 4B, this image model uses multipart form data inputs, even if you just have a prompt.

With the REST API, the multipart form data input looks like this:
    
    
    curl --request POST \
      --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b' \
      --header 'Authorization: Bearer {TOKEN}' \
      --header 'Content-Type: multipart/form-data' \
      --form 'prompt=a sunset at the alps' \
      --form width=1024 \
      --form height=1024

With the Workers AI binding, you can use it as such:
    
    
    const form = new FormData();
    form.append("prompt", "a sunset with a dog");
    form.append("width", "1024");
    form.append("height", "1024");
    
    // FormData doesn't expose its serialized body or boundary. Passing it to a
    // Request (or Response) constructor serializes it and generates the Content-Type
    // header with the boundary, which is required for the server to parse the multipart fields.
    const formResponse = new Response(form);
    const formStream = formResponse.body;
    const formContentType = formResponse.headers.get('content-type');
    
    const resp = await env.AI.run("@cf/black-forest-labs/flux-2-klein-9b", {
    	multipart: {
    		body: formStream,
    		contentType: formContentType,
    	},
    });

The parameters you can send to the model are detailed here:

JSON Schema for Model**Required Parameters**

  * `prompt` (string) - Text description of the image to generate



**Optional Parameters**

  * `input_image_0` (string) - Binary image
  * `input_image_1` (string) - Binary image
  * `input_image_2` (string) - Binary image
  * `input_image_3` (string) - Binary image
  * `guidance` (float) - Guidance scale for generation. Higher values follow the prompt more closely
  * `width` (integer) - Width of the image, default `1024` Range: 256-1920
  * `height` (integer) - Height of the image, default `768` Range: 256-1920
  * `seed` (integer) - Seed for reproducibility



**Note:** Since this is a distilled model, the `steps` parameter is fixed at 4 and cannot be adjusted.

#### Multi-reference images

The FLUX.2 klein-9b model supports generating images based on reference images, just like FLUX.2 [dev] and FLUX.2 [klein] 4B. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.

For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.

You must name the input parameter as `input_image_0`, `input_image_1`, `input_image_2`, `input_image_3` for it to work correctly. All input images must be smaller than 512x512.
    
    
    curl --request POST \
      --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b' \
      --header 'Authorization: Bearer {TOKEN}' \
      --header 'Content-Type: multipart/form-data' \
      --form 'prompt=take the subject of image 1 and style it like image 0' \
      --form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png \
      --form input_image_1=@/Users/johndoe/Desktop/me.png \
      --form width=1024 \
      --form height=1024

Through Workers AI Binding:
    
    
    //helper function to convert ReadableStream to Blob
    async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
      const reader = stream.getReader();
      const chunks = [];
    
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        chunks.push(value);
      }
    
      return new Blob(chunks, { type: contentType });
    }
    
    const image0 = await fetch("http://image-url");
    const image1 = await fetch("http://image-url");
    const form = new FormData();
    
    const image_blob0 = await streamToBlob(image0.body, "image/png");
    const image_blob1 = await streamToBlob(image1.body, "image/png");
    form.append('input_image_0', image_blob0)
    form.append('input_image_1', image_blob1)
    form.append('prompt', 'take the subject of image 1 and style it like image 0')
    
    // FormData doesn't expose its serialized body or boundary. Passing it to a
    // Request (or Response) constructor serializes it and generates the Content-Type
    // header with the boundary, which is required for the server to parse the multipart fields.
    const formResponse = new Response(form);
    const formStream = formResponse.body;
    const formContentType = formResponse.headers.get('content-type');
    
    const resp = await env.AI.run("@cf/black-forest-labs/flux-2-klein-9b", {
        multipart: {
            body: formStream,
            contentType: formContentType
        }
    })

Jan 15, 2026

## [Launching FLUX.2 [klein] 4B on Workers AI](https://developers.cloudflare.com/changelog/post/2026-01-15-flux-2-klein-4b-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

We've partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 4B model to Workers AI! This distilled model offers faster generation and cost-effective pricing, while maintaining great output quality. With a fixed 4-step inference process, Klein 4B is ideal for rapid prototyping and real-time applications where speed matters.

Read the [BFL blog ↗︎](https://bfl.ai/blog) to learn more about the model itself, or try it out yourself on our [multi modal playground ↗︎](https://multi-modal.ai.cloudflare.com/).

Pricing documentation is available on the [model page](https://developers.cloudflare.com/workers-ai/models/flux-2-klein-4b/) or [pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

#### Workers AI Platform specifics

The model hosted on Workers AI is optimized for speed with a **fixed 4-step inference process** and supports up to 4 image inputs. Since this is a distilled model, the `steps` parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev], this image model uses multipart form data inputs, even if you just have a prompt.

With the REST API, the multipart form data input looks like this:
    
    
    curl --request POST \
      --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b' \
      --header 'Authorization: Bearer {TOKEN}' \
      --header 'Content-Type: multipart/form-data' \
      --form 'prompt=a sunset at the alps' \
      --form width=1024 \
      --form height=1024

With the Workers AI binding, you can use it as such:
    
    
    const form = new FormData();
    form.append("prompt", "a sunset with a dog");
    form.append("width", "1024");
    form.append("height", "1024");
    
    // FormData doesn't expose its serialized body or boundary. Passing it to a
    // Request (or Response) constructor serializes it and generates the Content-Type
    // header with the boundary, which is required for the server to parse the multipart fields.
    const formResponse = new Response(form);
    const formStream = formResponse.body;
    const formContentType = formResponse.headers.get('content-type');
    
    const resp = await env.AI.run("@cf/black-forest-labs/flux-2-klein-4b", {
    	multipart: {
    		body: formStream,
    		contentType: formContentType,
    	},
    });

The parameters you can send to the model are detailed here:

JSON Schema for Model**Required Parameters**

  * `prompt` (string) - Text description of the image to generate



**Optional Parameters**

  * `input_image_0` (string) - Binary image
  * `input_image_1` (string) - Binary image
  * `input_image_2` (string) - Binary image
  * `input_image_3` (string) - Binary image
  * `guidance` (float) - Guidance scale for generation. Higher values follow the prompt more closely
  * `width` (integer) - Width of the image, default `1024` Range: 256-1920
  * `height` (integer) - Height of the image, default `768` Range: 256-1920
  * `seed` (integer) - Seed for reproducibility



**Note:** Since this is a distilled model, the `steps` parameter is fixed at 4 and cannot be adjusted.
    
    
    ## Multi-Reference Images
    
    The FLUX.2 klein-4b model supports generating images based on reference images, just like FLUX.2 [dev]. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.
    
    For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.
    
    Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2`, `input_image_3` for it to work correctly. All input images must be smaller than 512x512.
    
    ```bash
    curl --request POST \
      --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b' \
      --header 'Authorization: Bearer {TOKEN}' \
      --header 'Content-Type: multipart/form-data' \
      --form 'prompt=take the subject of image 1 and style it like image 0' \
      --form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png \
      --form input_image_1=@/Users/johndoe/Desktop/me.png \
      --form width=1024 \
      --form height=1024

Through Workers AI Binding:
    
    
    //helper function to convert ReadableStream to Blob
    async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
      const reader = stream.getReader();
      const chunks = [];
    
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        chunks.push(value);
      }
    
      return new Blob(chunks, { type: contentType });
    }
    
    const image0 = await fetch("http://image-url");
    const image1 = await fetch("http://image-url");
    const form = new FormData();
    
    const image_blob0 = await streamToBlob(image0.body, "image/png");
    const image_blob1 = await streamToBlob(image1.body, "image/png");
    form.append('input_image_0', image_blob0)
    form.append('input_image_1', image_blob1)
    form.append('prompt', 'take the subject of image 1 and style it like image 0')
    
    // FormData doesn't expose its serialized body or boundary. Passing it to a
    // Request (or Response) constructor serializes it and generates the Content-Type
    // header with the boundary, which is required for the server to parse the multipart fields.
    const formResponse = new Response(form);
    const formStream = formResponse.body;
    const formContentType = formResponse.headers.get('content-type');
    
    const resp = await env.AI.run("@cf/black-forest-labs/flux-2-klein-4b", {
        multipart: {
            body: formStream,
            contentType: formContentType
        }
    })

← Prev

1[2](https://developers.cloudflare.com/changelog/product/workers-ai/2/)

[Next →](https://developers.cloudflare.com/changelog/product/workers-ai/2/)
