---
url: https://developers.cloudflare.com/changelog/product/sandbox/
title: Sandboxes Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:49.160036+00:00
---

# Sandboxes Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/sandbox/

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

Sep 2, 2026

## [Run Cursor Cloud Agents on Cloudflare via self-hosted machines](https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/)

[Sandboxes](https://developers.cloudflare.com/sandbox/)

[Cursor self-hosted machines ↗︎](https://cursor.com/docs/cloud-agent/self-hosted) let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by [Cloudflare Containers](https://developers.cloudflare.com/containers/).

![Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3308,height=1916,format=webp/_astro/cursor-cloud-agents-self-hosted-pool.XNeWCXB2.png)

Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source [Cursor Cloudflare Workers template ↗︎](https://github.com/anysphere/cloudflare-workers) deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.

To get started, refer to [Run Cursor Cloud Agents on Cloudflare via self-hosted machines](https://developers.cloudflare.com/sandbox/coding-agents/cursor/).

Jul 21, 2026

## [Run Devin on Cloudflare using Devin Outposts](https://developers.cloudflare.com/changelog/post/2026-07-21-devin-outposts/)

[Sandboxes](https://developers.cloudflare.com/sandbox/)

[Devin Outposts ↗︎](https://docs.devin.ai/onboard-devin/outposts) lets you run Devin agents on Cloudflare. Each Devin session runs in its own isolated sandbox backed by [Cloudflare Containers](https://developers.cloudflare.com/containers/), so agents can execute code and use development tooling in an isolated environment.

Use Devin Outposts when you want Devin sessions to run on Cloudflare managed infrastructure, with each session isolated from the others.

![Devin interface showing Cloudflare selected as an Outposts virtual environment](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1712,height=914,format=webp/_astro/devin-outposts.B3xjmfR5.jpg)

To get started, refer to [Run Devin on Cloudflare using Devin Outposts](https://developers.cloudflare.com/sandbox/coding-agents/devin/).

Jun 9, 2026

## [Deprecating Sandbox SDK features](https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/)

[Sandboxes](https://developers.cloudflare.com/sandbox/)

Sandbox SDK 1.0 preview

A preview of **Sandbox SDK 1.0** is available on `@cloudflare/sandbox@next`. For new projects, or to move past these deprecations in one migration, refer to the [Sandbox SDK 1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) and [Migrate](https://developers.cloudflare.com/sandbox/1-0-preview/migrate/).

Today we are announcing the deprecation of several features from the Sandbox SDK. The SDK has grown and matured substantially since it first launched. As agent workflows have developed, we have shipped many new features and experiments so developers can easily integrate secure, isolated code execution into their workflows.

We want the SDK to continue providing a stable foundation for agentic workflows while we iterate quickly on the codebase. These deprecated features have either been superseded by newer capabilities or seen low adoption. Do not build new work on them. Migrate using the [2026 deprecation migration guide](https://developers.cloudflare.com/sandbox/guides/2026-deprecation/), or move to the [Sandbox SDK 1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) when you can.

#### HTTP and WebSocket transports

In April 2026, we released the new RPC transport and deprecated the WebSocket transport. This setting governs how the sandbox container talks to the Workers ecosystem. The RPC transport removes the limitations of both the HTTP and WebSocket transports. As of this announcement, RPC is the recommended default. HTTP and WebSocket transports are deprecated and will not ship in future Sandbox SDK majors.

To migrate, update the `SANDBOX_TRANSPORT` variable to `rpc` or set the `transport` option when calling `getSandbox()`. For more information, refer to the [transport configuration documentation](https://developers.cloudflare.com/sandbox/configuration/transport/).

#### Desktop

The desktop feature ran a full Linux desktop inside the sandbox (display server, desktop environment, and VNC/noVNC) so agents and apps could drive a GUI with screenshots, mouse, and keyboard — the same _computer-use_ shape other sandbox products expose for UI automation. Adoption stayed low, and we removed it in `0.10.2`. If you need that capability again, you can build it on top of the sandbox with [extensions](https://developers.cloudflare.com/sandbox/1-0-preview/extensions/) rather than a built-in `sandbox.desktop` API.

#### Expose ports

We recently released support for Cloudflare Tunnel in the Sandbox SDK. This provides a robust API for exposing services running in your sandbox to the public internet. It fixes issues many were facing with local development and deployment to `workers.dev` domains. To migrate from `exposePort()` to tunnels, refer to the [tunnels API documentation](https://developers.cloudflare.com/sandbox/api/tunnels/) and the [expose services guide](https://developers.cloudflare.com/sandbox/guides/expose-services/).

#### Default sessions

By default, the `exec()` method in the Sandbox SDK maintains a default session across all calls, so a `cd` in one call is honored in the next. This convenience helped developers writing `exec` statements by hand, but confused agents and caused hard-to-trace bugs. As of `0.10.3`, we have introduced the [`enableDefaultSession`](https://developers.cloudflare.com/sandbox/configuration/sandbox-options/) flag on the `getSandbox()` interface to turn this off. Default sessions as a concept — and the flag — will be removed in an upcoming release.

We recommend setting `enableDefaultSession: false` today and using the [`sandbox.createSession()` API](https://developers.cloudflare.com/sandbox/api/sessions/) when you need the previous behavior.

#### Other changes

We are also consolidating all APIs that buffer data to support streaming by default. This includes [`readFile`, `writeFile`](https://developers.cloudflare.com/sandbox/api/files/), and [`exec`](https://developers.cloudflare.com/sandbox/api/commands/). The stream equivalents will be removed.

We are exploring moving non-core features like the [code interpreter](https://developers.cloudflare.com/sandbox/guides/code-execution/), [terminal](https://developers.cloudflare.com/sandbox/api/terminal/), and [git APIs](https://developers.cloudflare.com/sandbox/guides/git-workflows/) into helpers. These features will retain their existing APIs, so migration should be simple.

#### Next steps

If you use any of these features on the **current stable** package, refer to the [2026 deprecation migration guide](https://developers.cloudflare.com/sandbox/guides/2026-deprecation/). Coding agents can use the **`sandbox-stable`** skill for stable-package work and that guide for cleanup ([Agent setup](https://developers.cloudflare.com/agent-setup/) · [Cloudflare Skills ↗︎](https://github.com/cloudflare/skills)).

If you are moving to **Sandbox SDK 1.0** (`@next`), use the [1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) and [Migrate](https://developers.cloudflare.com/sandbox/1-0-preview/migrate/) guides instead — or the **`sandbox-migrate-to-next`** skill after installing Cloudflare Skills. New projects should prefer **`sandbox-next`** on `@next`.

For any questions, ask in the [Cloudflare Developers Discord ↗︎](https://discord.gg/cloudflaredev).
