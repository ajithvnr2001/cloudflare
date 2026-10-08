---
url: https://developers.cloudflare.com/changelog/product/containers/
title: Containers Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:44.179477+00:00
---

# Containers Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/containers/

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

Sep 10, 2026

## [Use Cloudflare Containers with Codex via the OpenAI Agents API](https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/)

[Containers](https://developers.cloudflare.com/containers/)

The OpenAI Agents API gives your application access to Codex through an OpenAI-managed API.

OpenAI manages sessions, orchestration, context compaction, and recovery while your application provides tools and uses Cloudflare Containers as the execution environment.

Cloudflare Containers can now provide self-hosted execution environments for the OpenAI Agents API. The open-source [OpenAI Agents API Workers template ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api) provides a reference implementation. The Worker maintains a Cloudflare Container for each Codex session, keeps active work running, reconnects on follow-up input, and shuts down automatically when idle.

You can configure the reference implementation to meet your needs by extending the Container to provide controlled access to data and the network or by integrating it with other Cloudflare products.

To get started, refer to [Run Codex on Cloudflare using the OpenAI Agents API](https://developers.cloudflare.com/sandbox/tutorials/openai-agents-api/).

Sep 8, 2026

## [Configure observability per container application](https://developers.cloudflare.com/changelog/post/2026-09-08-per-container-observability/)

[Containers](https://developers.cloudflare.com/containers/)

You can now configure observability for each container application when you deploy [Containers](https://developers.cloudflare.com/containers/) with [Wrangler](https://developers.cloudflare.com/workers/wrangler/). This lets you change logging for one container without changing the rest of your Worker.

If you omit `containers[].observability`, Wrangler uses the top-level `observability` setting for that container. If you set it, the container setting overrides the top-level setting.

Use `target_instance_percentage` or `target_instance_count` to apply an observability change to a subset of running instances.
    
    
    {
    	"observability": {
    		"enabled": false,
    	},
    	"containers": [
    		{
    			"class_name": "MyContainer",
    			"image": "./Dockerfile",
    			"observability": {
    				"enabled": true,
    				"target_instance_percentage": 25,
    			},
    		},
    	],
    }
    
    
    [observability]
    enabled = false
    
    [[containers]]
    class_name = "MyContainer"
    image = "./Dockerfile"
    
      [containers.observability]
      enabled = true
      target_instance_percentage = 25

For more information about Workers Logs, refer to [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/).

Aug 20, 2026

## [Use FUSE in local Containers development](https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/)

[Containers](https://developers.cloudflare.com/containers/)

Miniflare now automatically grants local Containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to `wrangler dev`, the Cloudflare Vite plugin, and direct Miniflare use.

Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM). This includes Docker engines on macOS and through Windows Subsystem for Linux (WSL). On Linux, Miniflare grants the privileges for local rootless Docker when `/dev/fuse` is available.

Rootful Docker on Linux does not support FUSE by default during local development. Miniflare does not grant FUSE privileges when the Docker daemon does not meet these conditions or cannot be inspected.

For requirements and troubleshooting, refer to [FUSE support during local development](https://developers.cloudflare.com/containers/guides/local-dev/#fuse-support). For a complete example, refer to [Mount R2 buckets with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/).

Jul 1, 2026

## [Use Google Artifact Registry images with Containers](https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/)

[Containers](https://developers.cloudflare.com/containers/)

Containers now support [Google Artifact Registry ↗︎](https://cloud.google.com/artifact-registry) images. After you configure credentials, you can use a fully qualified Google Artifact Registry image reference in your [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) instead of first pushing the image to Cloudflare Registry.

Provide the service account email with `--gar-email` and pipe the service account JSON key through `stdin`:
    
    
    cat <PATH_TO_KEY> | npx wrangler containers registries configure <REGION>-docker.pkg.dev --gar-email=<SERVICE_ACCOUNT_EMAIL> --secret-name=<SECRET_NAME>
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "containers": [
        {
          "image": "<REGION>-docker.pkg.dev/<PROJECT_ID>/<REPOSITORY>/<IMAGE>:<TAG>"
        }
      ]
    }
    
    
    # Example: us-central1-docker.pkg.dev/my-project/my-repo/my-image:latest
    [[containers]]
    image = "<REGION>-docker.pkg.dev/<PROJECT_ID>/<REPOSITORY>/<IMAGE>:<TAG>"

Only `*-docker.pkg.dev` hosts are supported. To configure credentials, refer to [Use private Google Artifact Registry images](https://developers.cloudflare.com/containers/guides/image-management/#use-private-google-artifact-registry-images).

For more information, refer to [Image management](https://developers.cloudflare.com/containers/guides/image-management/).

Jun 18, 2026

## [exec() is now available for Containers](https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/)

[Containers](https://developers.cloudflare.com/containers/)

`exec()` is now available for [Containers](https://developers.cloudflare.com/containers/). Use `this.ctx.container.exec()` to start processes inside a running Container, stream standard input and output, inspect exit codes, and signal each process.

Call `exec()` from a class extending `Container`, or from another Durable Object through `this.ctx.container`. The associated Container must already be running.

This example starts the Container when needed, then reads its Node.js version:

src/index.jsjs
    
    
    import { Container } from "@cloudflare/containers";
    
    export class MyContainer extends Container {
    	async readVersion() {
    		if (!this.ctx.container.running) {
    			await this.start();
    		}
    
    		const process = await this.ctx.container.exec(["node", "--version"]);
    		const output = await process.output();
    		const decoder = new TextDecoder();
    
    		return {
    			exitCode: output.exitCode,
    			stdout: decoder.decode(output.stdout),
    			stderr: decoder.decode(output.stderr),
    		};
    	}
    }

src/index.tsts
    
    
    import { Container } from "@cloudflare/containers";
    
    export class MyContainer extends Container {
    	async readVersion() {
    		if (!this.ctx.container.running) {
    			await this.start();
    		}
    
    		const process = await this.ctx.container.exec(["node", "--version"]);
    		const output = await process.output();
    		const decoder = new TextDecoder();
    
    		return {
    			exitCode: output.exitCode,
    			stdout: decoder.decode(output.stdout),
    			stderr: decoder.decode(output.stderr),
    		};
    	}
    }

The command array starts an executable directly, without an implicit shell. Invoke a shell explicitly for pipes, redirects, or variable expansion.

One RPC method can coordinate multiple `exec()` calls in one caller-to-Durable Object round trip. It can also pass byte-oriented `ReadableStream` input or return streamed output with flow control.

For options and streaming examples, refer to [Execute commands](https://developers.cloudflare.com/containers/guides/execute-commands/).

Jun 4, 2026

## [Billable usage and budget alerts now in product sidebars](https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)[D1](https://developers.cloudflare.com/d1/)[R2](https://developers.cloudflare.com/r2/)[KV](https://developers.cloudflare.com/kv/)[Queues](https://developers.cloudflare.com/queues/)[Vectorize](https://developers.cloudflare.com/vectorize/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Containers](https://developers.cloudflare.com/containers/)

Pay-as-you-go customers can now view billable usage and create [budget alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) directly from the product overview pages for [Workers & Pages](https://developers.cloudflare.com/workers/), [D1](https://developers.cloudflare.com/d1/), [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Queues](https://developers.cloudflare.com/queues/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Containers](https://developers.cloudflare.com/containers/). A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.

The widget pulls from the same data as the [Billable Usage dashboard](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.

![Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1614,format=webp/_astro/2026-06-04-billable-usage-product-sidebar.BUuIokn_.png)

Selecting **Create budget alert** opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.

For more information, refer to the [Usage-based billing documentation](https://developers.cloudflare.com/billing/).

May 28, 2026

## [Wrangler supports SSH ProxyCommand for Containers](https://developers.cloudflare.com/changelog/post/2026-05-28-ssh-proxy-command/)

[Containers](https://developers.cloudflare.com/containers/)

[Wrangler](https://developers.cloudflare.com/workers/wrangler/) supports using `wrangler containers ssh` as an OpenSSH `ProxyCommand` for [Containers](https://developers.cloudflare.com/containers/). This lets your local SSH client connect to a running Container through Wrangler.
    
    
    ssh -o ProxyCommand="wrangler containers ssh %h" cloudchamber@<INSTANCE_ID>

When standard input and output are piped, Wrangler forwards data to the SSH server in the Container. You can also pass `--stdio` to force this mode.

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).

May 12, 2026

## [SSH through Wrangler is now enabled by default for Containers](https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/)

[Containers](https://developers.cloudflare.com/containers/)

SSH through Wrangler is now enabled by default for [Containers](https://developers.cloudflare.com/containers/). Previously, you had to set `ssh.enabled` to `true` in your Container configuration before you could connect.

This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through [`wrangler containers ssh`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-ssh), which authenticates against your Cloudflare account. You also need to add an `ssh-ed25519` public key to `authorized_keys` before anyone can connect, so enabling SSH alone does not grant access.

To connect, add a public key to your Container configuration and run `wrangler containers ssh <INSTANCE_ID>`:
    
    
    {
    	"containers": [
    		{
    			"authorized_keys": [
    				{
    					"name": "<NAME>",
    					"public_key": "<YOUR_PUBLIC_KEY_HERE>",
    				},
    			],
    		},
    	],
    }
    
    
    [[containers]]
    [[containers.authorized_keys]]
    name = "<NAME>"
    public_key = "<YOUR_PUBLIC_KEY_HERE>"

To disable SSH, set `ssh.enabled` to `false` in your Container configuration:
    
    
    {
    	"containers": [
    		{
    			"ssh": {
    				"enabled": false,
    			},
    		},
    	],
    }
    
    
    [[containers]]
    [containers.ssh]
    enabled = false

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).

Apr 21, 2026

## [Container logs page now includes relevant Worker and Durable Object logs](https://developers.cloudflare.com/changelog/post/2026-04-21-correlated-worker-durable-object-logs/)

[Containers](https://developers.cloudflare.com/containers/)

The Container logs page now displays related [Worker](https://developers.cloudflare.com/workers/) and [Durable Object](https://developers.cloudflare.com/durable-objects/) logs alongside container logs. This co-locates all relevant log events for a container application in one place, making it easier to trace requests and debug issues.

![Container logs page showing Worker and Durable Object logs alongside container logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1682,height=926,format=webp/_astro/container-worker-logs.BBQ7NRse.png)

You can filter to a single source when you need to isolate Container, Worker, or Durable Object output.

For information on configuring container logging, refer to [How do Container logs work?](https://developers.cloudflare.com/containers/faq/#how-do-container-logs-work).

Apr 13, 2026

## [Containers and Sandboxes are now generally available](https://developers.cloudflare.com/changelog/post/2026-04-13-containers-sandbox-ga/)

[Containers](https://developers.cloudflare.com/containers/)

Cloudflare [Containers](https://developers.cloudflare.com/containers/) and [Sandboxes](https://developers.cloudflare.com/sandbox/) are now generally available.

Containers let you run more workloads on the Workers platform, including resource-intensive applications, different languages, and CLI tools that need full Linux environments.

Since the initial launch of Containers, there have been significant improvements to Containers' performance, stability, and feature set. Some highlights include:

  * [Higher limits](https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/) allow you to run thousands of containers concurrently.
  * [Active-CPU pricing](https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/) means that you only pay for used CPU cycles.
  * [Easy connections to Workers and other bindings](https://developers.cloudflare.com/changelog/post/2026-03-26-outbound-workers/) via hostnames help you extend your Containers with additional functionality.
  * [Docker Hub support](https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/) makes it easy to use your existing images and registries.
  * [SSH support](https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/) helps you access and debug issues in live containers.



The [Sandbox SDK](https://developers.cloudflare.com/sandbox/) provides isolated environments for running untrusted code securely, with a simple TypeScript API for executing commands, managing files, and exposing services. This makes it easier to secure and manage your agents at scale. Some additions since launch include:

  * [Live preview URLs](https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/) so agents can run long-lived services and verify in-flight changes.
  * [Persistent code interpreters](https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/) for Python, JavaScript, and TypeScript, with rich structured outputs.
  * [Interactive PTY terminals](https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/) for real browser-based terminal access with multiple isolated shells per sandbox.
  * [Backup and restore APIs](https://developers.cloudflare.com/changelog/post/2026-02-23-sandbox-backup-restore-api/) to snapshot a workspace and quickly restore an agent's coding session without repeating expensive setup steps.
  * [Real-time filesystem watching](https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/) so apps and agents can react immediately to file changes inside a sandbox.



For more information, refer to [Containers](https://developers.cloudflare.com/containers/) and [Sandbox SDK](https://developers.cloudflare.com/sandbox/) documentation.

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

Apr 5, 2026

## [Control where your Containers run with regional and jurisdictional placement](https://developers.cloudflare.com/changelog/post/2026-04-05-regional-placement/)

[Containers](https://developers.cloudflare.com/containers/)

You can now specify placement constraints to control where your [Containers](https://developers.cloudflare.com/containers/) run.

Constraint | Values | Use case  
---|---|---  
`regions` | `ENAM`, `WNAM`, `EEUR`, `WEUR` | Geographic placement  
`jurisdiction` | `eu`, `fedramp` | Compliance boundaries  
  
Use `regions` to limit placement to specific geographic areas. Use `jurisdiction` to restrict containers to compliance boundaries — `eu` maps to European regions (EEUR, WEUR) and `fedramp` maps to North American regions (ENAM, WNAM).

Refer to [Containers placement](https://developers.cloudflare.com/containers/concepts/placement/) for more details.

Mar 26, 2026

## [Easily connect Containers and Sandboxes to Workers](https://developers.cloudflare.com/changelog/post/2026-03-26-outbound-workers/)

[Containers](https://developers.cloudflare.com/containers/)

[Containers](https://developers.cloudflare.com/containers/) and [Sandboxes](https://developers.cloudflare.com/sandbox/) now support connecting directly to Workers over HTTP. This allows you to call Workers functions and [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/), like [KV](https://developers.cloudflare.com/kv) or [R2](https://developers.cloudflare.com/r2/), from within the container at specific hostnames.

#### Run Worker code

Define an `outbound` handler to capture any HTTP request or use `outboundByHost` to capture requests to individual hostnames and IPs.
    
    
    export class MyApp extends Sandbox {}
    
    MyApp.outbound = async (request, env, ctx) => {
    	// you can run arbitrary functions defined in your Worker on any HTTP request
    	return await someWorkersFunction(request.body);
    };
    
    MyApp.outboundByHost = {
    	"my.worker": async (request, env, ctx) => {
    		return await anotherFunction(request.body);
    	},
    };

In this example, requests from the container to `http://my.worker` will run the function defined within `outboundByHost`, and any other HTTP requests will run the `outbound` handler. These handlers run entirely inside the Workers runtime, outside of the container sandbox.

#### Access Workers bindings

Each handler has access to `env`, so it can call any binding set in [Wrangler config](https://developers.cloudflare.com/workers/wrangler/configuration/#bindings). Code inside the container makes a standard HTTP request to that hostname and the outbound Worker translates it into a binding call.
    
    
    export class MyApp extends Sandbox {}
    
    MyApp.outboundByHost = {
    	"my.kv": async (request, env, ctx) => {
    		const key = new URL(request.url).pathname.slice(1);
    		const value = await env.KV.get(key);
    		return new Response(value ?? "", { status: value ? 200 : 404 });
    	},
    	"my.r2": async (request, env, ctx) => {
    		const key = new URL(request.url).pathname.slice(1);
    		const object = await env.BUCKET.get(key);
    		return new Response(object?.body ?? "", { status: object ? 200 : 404 });
    	},
    };

Now, from inside the container sandbox, `curl http://my.kv/some-key` will access [Workers KV](https://developers.cloudflare.com/kv) and `curl http://my.r2/some-object` will access [R2](https://developers.cloudflare.com/r2/).

#### Access Durable Object state

Use `ctx.containerId` to reference the container's automatically provisioned [Durable Object](https://developers.cloudflare.com/durable-objects).
    
    
    export class MyContainer extends Container {}
    
    MyContainer.outboundByHost = {
    	"get-state.do": async (request, env, ctx) => {
    		const id = env.MY_CONTAINER.idFromString(ctx.containerId);
    		const stub = env.MY_CONTAINER.get(id);
    		return stub.getStateForKey(request.body);
    	},
    };

This provides an easy way to associate state with any container instance, and includes a [built-in SQLite database](https://developers.cloudflare.com/durable-objects/get-started/#2-write-a-durable-object-class-using-sql-api).

#### Get Started Today

Upgrade to `@cloudflare/containers` version 0.2.0 or later, or `@cloudflare/sandbox` version 0.8.0 or later to use outbound Workers.

Refer to [Containers outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/) and [Sandboxes outbound traffic](https://developers.cloudflare.com/sandbox/guides/outbound-traffic/) for more details and examples.

Mar 24, 2026

## [Use Docker Hub images with Containers](https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/)

[Containers](https://developers.cloudflare.com/containers/)

Containers now support [Docker Hub ↗︎](https://hub.docker.com/) images. You can use a fully qualified Docker Hub image reference in your [Wrangler configuration ↗︎](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) instead of first pushing the image to Cloudflare Registry.
    
    
    {
    	"containers": [
    		{
    			// Example: docker.io/cloudflare/sandbox:0.7.18
    			"image": "docker.io/<NAMESPACE>/<REPOSITORY>:<TAG>",
    		},
    	],
    }
    
    
    [[containers]]
    image = "docker.io/<NAMESPACE>/<REPOSITORY>:<TAG>"

Containers also support private Docker Hub images. To configure credentials, refer to [Use private Docker Hub images](https://developers.cloudflare.com/containers/guides/image-management/#use-private-docker-hub-images).

For more information, refer to [Image management](https://developers.cloudflare.com/containers/guides/image-management/).

Mar 12, 2026

## [SSH into running Container instances](https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/)

[Containers](https://developers.cloudflare.com/containers/)

You can now SSH into running Container instances using Wrangler. This is useful for debugging, inspecting running processes, or executing one-off commands inside a Container.

To connect, enable `wrangler_ssh` in your Container configuration and add your `ssh-ed25519` public key to `authorized_keys`:
    
    
    {
    	"containers": [
    		{
    			"wrangler_ssh": {
    				"enabled": true
    			},
    			"authorized_keys": [
    				{
    					"name": "<NAME>",
    					"public_key": "<YOUR_PUBLIC_KEY_HERE>"
    				}
    			]
    		}
    	]
    }
    
    
    [[containers]]
    [containers.wrangler_ssh]
    enabled = true
    
    [[containers.authorized_keys]]
    name = "<NAME>"
    public_key = "<YOUR_PUBLIC_KEY_HERE>"

Then connect with:
    
    
    wrangler containers ssh <INSTANCE_ID>

You can also run a single command without opening an interactive shell:
    
    
    wrangler containers ssh <INSTANCE_ID> -- ls -al

Use `wrangler containers instances <APPLICATION>` to find the instance ID for a running Container.

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).

Mar 12, 2026

## [List Container instances with `wrangler containers instances`](https://developers.cloudflare.com/changelog/post/2026-03-12-wrangler-containers-instances/)

[Containers](https://developers.cloudflare.com/containers/)

A new [`wrangler containers instances`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-instances) command lists all instances for a given Container application. This mirrors the instances view in the Cloudflare dashboard.

The command displays each instance's ID, name, state, location, version, and creation time:
    
    
    wrangler containers instances <APPLICATION_ID>

Use the `--json` flag for machine-readable output, which is also the default format in non-interactive environments such as CI pipelines.

For the full list of options, refer to the [`containers instances` command reference](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-instances).

Feb 25, 2026

## [Run 15x more Containers with higher resource limits](https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/)

[Containers](https://developers.cloudflare.com/containers/)

You can now run more [Containers](https://developers.cloudflare.com/containers/) concurrently with significantly higher limits on memory, vCPU, and disk.

Limit | Previous Limit | New Limit  
---|---|---  
Memory for concurrent live Container instances | 400GiB | 6TiB  
vCPU for concurrent live Container instances | 100 | 1,500  
Disk for concurrent live Container instances | 2TB | 30TB  
  
This 15x increase enables larger-scale workloads on Containers. You can now run 15,000 instances of the `lite` instance type, 6,000 instances of `basic`, over 1,500 instances of `standard-1`, or over 1,000 instances of `standard-2` concurrently.

Refer to [Limits](https://developers.cloudflare.com/containers/platform/limits/) for more details on the available instance types and limits.

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

Feb 17, 2026

## [Docker-in-Docker support added to Containers and Sandboxes](https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/)

[Containers](https://developers.cloudflare.com/containers/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) and [Containers](https://developers.cloudflare.com/containers/) now support running Docker for "Docker-in-Docker" setups. This is particularly useful when your end users or [agents](https://developers.cloudflare.com/agents) want to run a full sandboxed development environment.

This allows you to:

  * Develop containerized applications with your Sandbox
  * Run isolated test environments for images
  * Build container images as part of CI/CD workflows
  * Deploy arbitrary images supplied at runtime within a container



For [Sandbox SDK](https://developers.cloudflare.com/sandbox/) users, see the [Docker-in-Docker guide](https://developers.cloudflare.com/sandbox/guides/docker-in-docker/) for instructions on combining Docker with the SandboxSDK. For general Containers usage, see the [Containers FAQ](https://developers.cloudflare.com/containers/faq/#can-i-run-docker-inside-a-container-docker-in-docker).

Jan 5, 2026

## [Custom container instance types now available for all users](https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/)

[Containers](https://developers.cloudflare.com/containers/)

Custom instance types are now enabled for all [Cloudflare Containers](https://developers.cloudflare.com/containers) users. You can now specify specific vCPU, memory, and disk amounts, rather than being limited to pre-defined [instance types](https://developers.cloudflare.com/containers/platform/limits/#instance-types). Previously, only select Enterprise customers were able to customize their instance type.

To use a custom instance type, specify the `instance_type` property as an object with `vcpu`, `memory_mib`, and `disk_mb` fields in your Wrangler configuration:
    
    
    [[containers]]
    image = "./Dockerfile"
    instance_type = { vcpu = 2, memory_mib = 6144, disk_mb = 12000 }

Individual limits for custom instance types are based on the `standard-4` instance type (4 vCPU, 12 GiB memory, 20 GB disk). You must allocate at least 1 vCPU for custom instance types. For workloads requiring less than 1 vCPU, use the predefined instance types like `lite` or `basic`.

See the [limits documentation](https://developers.cloudflare.com/containers/platform/limits/#custom-instance-types) for the full list of constraints on custom instance types. See the [getting started guide](https://developers.cloudflare.com/containers/get-started/) to deploy your first Container,

Nov 21, 2025

## [Mount R2 buckets in Containers](https://developers.cloudflare.com/changelog/post/2025-11-21-fuse-support-in-containers/)

[Containers](https://developers.cloudflare.com/containers/)[R2](https://developers.cloudflare.com/r2/)

[Containers](https://developers.cloudflare.com/containers/) now support mounting R2 buckets as FUSE (Filesystem in Userspace) volumes, allowing applications to interact with [R2](https://developers.cloudflare.com/r2/) using standard filesystem operations.

Common use cases include:

  * Bootstrapping containers with datasets, models, or dependencies for [sandboxes](https://developers.cloudflare.com/sandbox/) and [agent](https://developers.cloudflare.com/agents/) environments
  * Persisting user configuration or application state without managing downloads
  * Accessing large static files without bloating container images or downloading at startup



FUSE adapters like [tigrisfs ↗︎](https://github.com/tigrisdata/tigrisfs), [s3fs ↗︎](https://github.com/s3fs-fuse/s3fs-fuse), and [gcsfuse ↗︎](https://github.com/GoogleCloudPlatform/gcsfuse) can be installed in your container image and configured to mount buckets at startup.
    
    
    FROM alpine:3.20
    
    # Install FUSE and dependencies
    RUN apk update && \
        apk add --no-cache ca-certificates fuse curl bash
    
    # Install tigrisfs
    RUN ARCH=$(uname -m) && \
        if [ "$ARCH" = "x86_64" ]; then ARCH="amd64"; fi && \
        if [ "$ARCH" = "aarch64" ]; then ARCH="arm64"; fi && \
        VERSION=$(curl -s https://api.github.com/repos/tigrisdata/tigrisfs/releases/latest | grep -o '"tag_name": "[^"]*' | cut -d'"' -f4) && \
        curl -L "https://github.com/tigrisdata/tigrisfs/releases/download/${VERSION}/tigrisfs_${VERSION#v}_linux_${ARCH}.tar.gz" -o /tmp/tigrisfs.tar.gz && \
        tar -xzf /tmp/tigrisfs.tar.gz -C /usr/local/bin/ && \
        rm /tmp/tigrisfs.tar.gz && \
        chmod +x /usr/local/bin/tigrisfs
    
    # Create startup script that mounts bucket
    RUN printf '#!/bin/sh\n\
        set -e\n\
        mkdir -p /mnt/r2\n\
        R2_ENDPOINT="https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com"\n\
        /usr/local/bin/tigrisfs --endpoint "${R2_ENDPOINT}" -f "${BUCKET_NAME}" /mnt/r2 &\n\
        sleep 3\n\
        ls -lah /mnt/r2\n\
        ' > /startup.sh && chmod +x /startup.sh
    
    CMD ["/startup.sh"]

See the [Mount R2 buckets with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/) example for a complete guide on mounting R2 buckets and/or other S3-compatible storage buckets within your containers.

Nov 21, 2025

## [New CPU Pricing for Containers and Sandboxes](https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/)

[Containers](https://developers.cloudflare.com/containers/)

[Containers](https://developers.cloudflare.com/containers/) and [Sandboxes](https://developers.cloudflare.com/sandbox/) pricing for CPU time is now based on active usage only, instead of provisioned resources.

This means that you now pay less for Containers and Sandboxes.

#### An Example Before and After

Imagine running the `standard-2` instance type for one hour, which can use up to 1 vCPU, but on average you use only 20% of your CPU capacity.

CPU-time is priced at _$0.00002 per vCPU-second_.

Previously, you would be charged for the CPU allocated to the instance multiplied by the time it was active, in this case 1 hour.

CPU cost would have been: **$0.072** — 1 vCPU * 3600 seconds * $0.00002

Now, since you are only using 20% of your CPU capacity, your CPU cost is cut to 20% of the previous amount.

CPU cost is now: **$0.0144** — 1 vCPU * 3600 seconds * $0.00002 * 20% utilization

This can significantly reduce costs for Containers and Sandboxes.

Note

Memory cost and disk pricing remain unchanged, and is still calculated based on _provisioned_ resources.

See the documentation to learn more about [Containers](https://developers.cloudflare.com/containers/get-started/), [Sandboxes](https://developers.cloudflare.com/sandbox/), and [associated pricing](https://developers.cloudflare.com/containers/platform/pricing).

← Prev

1[2](https://developers.cloudflare.com/changelog/product/containers/2/)

[Next →](https://developers.cloudflare.com/changelog/product/containers/2/)
