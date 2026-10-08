---
url: https://developers.cloudflare.com/changelog/product/artifacts/
title: Artifacts Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:41.094151+00:00
---

# Artifacts Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/artifacts/

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

Aug 13, 2026

## [Data localization support for Artifacts](https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/)

[Artifacts](https://developers.cloudflare.com/artifacts/)

Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.

Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "namespace": "my-eu-namespace",
        "jurisdiction": "eu"
      }'

Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.

For supported jurisdictions and usage details, refer to [Data localization](https://developers.cloudflare.com/artifacts/guides/data-localization/).

Aug 4, 2026

## [Build and deploy Artifacts repos on every push](https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/)

[Artifacts](https://developers.cloudflare.com/artifacts/)[Workflows](https://developers.cloudflare.com/workflows/)

You can now run your CI/CD pipeline on your [Artifacts](https://developers.cloudflare.com/artifacts/) repo by defining a CI [Workflow](https://developers.cloudflare.com/workflows/) with the [CI SDK ↗︎](https://github.com/cloudflare/ci), automatically triggered on Artifacts push events.

This allows you to:

  * Automatically build and deploy application code stored in Artifacts.
  * Run linting, type checking, tests, and other checks on every push.
  * Reuse dependencies when the lockfile (i.e. `pnpm-lock.yaml`) has not changed.
  * Stop deployment when a check or build fails.
  * Restrict API token access to the deployment step.
  * Deploy the output to a [Worker](https://developers.cloudflare.com/workers/) or a [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) User Worker.



Define your CI steps with `@cloudflare/ci`. Each `ci.runner()` spins up an isolated sandbox, and the `cache` option reuses installed dependencies across each sandboxed step in your CI job.

Point `cache.inputs` at your lockfile (i.e. `pnpm-lock.yaml`, `bun.lock`), and the install step only runs again when that lockfile changes:

src/index.jsjs
    
    
    const deps = await ci.runner({
    	name: "install",
    	command: "bun install --frozen-lockfile",
    	cache: { inputs: ["package.json", "bun.lock"] },
    });
    
    await Promise.all([
    	deps.runner({ name: "lint", command: "bun run lint" }),
    	deps.runner({ name: "test", command: "bun run test" }),
    	deps.runner({ name: "typecheck", command: "bun run typecheck" }),
    	deps.runner({ name: "build", command: "bun run build" }),
    ]);
    
    await deps.runner({ name: "deploy", command: "bun wrangler deploy" });

src/index.tsts
    
    
    const deps = await ci.runner({
    	name: "install",
    	command: "bun install --frozen-lockfile",
    	cache: { inputs: ["package.json", "bun.lock"] },
    });
    
    await Promise.all([
    	deps.runner({ name: "lint", command: "bun run lint" }),
    	deps.runner({ name: "test", command: "bun run test" }),
    	deps.runner({ name: "typecheck", command: "bun run typecheck" }),
    	deps.runner({ name: "build", command: "bun run build" }),
    ]);
    
    await deps.runner({ name: "deploy", command: "bun wrangler deploy" });

To start the Workflow automatically after each push, add a `cf.artifacts.repo.pushed` trigger to your Wrangler configuration:
    
    
    {
    	"triggers": {
    		"events": [
    			{
    				"type": "cf.artifacts.repo.pushed",
    				"filter": {
    					"namespace": "CI",
    					"repoName": "my-repo",
    				},
    				"target": {
    					"scriptName": "my-ci-worker",
    					"workflowName": "ci-workflow",
    				},
    			},
    		],
    	},
    }
    
    
    [[triggers.events]]
    type = "cf.artifacts.repo.pushed"
    
      [triggers.events.filter]
      namespace = "CI"
      repoName = "my-repo"
    
      [triggers.events.target]
      scriptName = "my-ci-worker"
      workflowName = "ci-workflow"

To learn more, refer to [Build and deploy Artifacts repos](https://developers.cloudflare.com/artifacts/guides/build-and-deploy-on-push/).

Jun 17, 2026

## [Manage Artifacts from the Cloudflare dashboard](https://developers.cloudflare.com/changelog/post/2026-06-17-dashboard-management/)

[Artifacts](https://developers.cloudflare.com/artifacts/)

You can now configure [Artifacts](https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/) namespaces, repos, and tokens directly from the Cloudflare dashboard.

Artifacts is Git-compatible storage that lets you store repos on Cloudflare and interact with them using standard Git workflows.

You can view and create [namespaces](https://developers.cloudflare.com/artifacts/concepts/namespaces/#use-namespaces-as-containers), which are top-level containers for repos:

![Artifacts namespaces dashboard showing namespace search and create namespace controls](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1804,height=598,format=webp/_astro/dashboard-namespaces.0BJelWZh.png)

You can view, create, fork, and search repos within a namespace:

![Artifacts repositories dashboard showing repo source, access, and created columns](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1874,height=592,format=webp/_astro/dashboard-repositories.M9P9JUL_.png)

You can open a repo to view its files and copy its Git remote URL.

![Artifacts repository overview showing files, commits, token management, and quick actions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2194,height=806,format=webp/_astro/dashboard-repo-overview.CSHxrCW2.png)

You can also provision tokens directly from the dashboard to scope Git access to a single repo, with read tokens for clone, fetch, and pull workflows, or write tokens when a client needs to push changes.

To get started, go to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select **Storage & databases** > **Artifacts**.

If you are enrolled in the Artifacts beta, you can use the dashboard to set up Artifacts. If you would like to join the beta, complete the [request form ↗︎](https://forms.gle/DwBoPRa3CWQ8ajFp7).

May 19, 2026

## [Event subscriptions for Artifacts lifecycle events](https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/)

[Artifacts](https://developers.cloudflare.com/artifacts/)[Queues](https://developers.cloudflare.com/queues/)

You can now receive [event notifications](https://developers.cloudflare.com/queues/event-subscriptions/) for [Artifacts](https://developers.cloudflare.com/artifacts/) repository changes and consume them from a Worker to build commit-driven automation.

This allows you to:

  * Run custom workflows when a repository is created or imported
  * Kick off a build and deploy a change when an agent pushes to a repo
  * Trigger a review agent on every push



Available events include:

  * **Account-level events** (`artifacts` source) — `repo.created`, `repo.deleted`, `repo.forked`, `repo.imported`
  * **Repository-level events** (`artifacts.repo` source) — `pushed`, `cloned`, `fetched`



To learn more, refer to [Artifacts documentation](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/).

May 18, 2026

## [Manage Artifacts namespaces and repos with Wrangler CLI](https://developers.cloudflare.com/changelog/post/2026-05-18-wrangler-support/)

[Artifacts](https://developers.cloudflare.com/artifacts/)

You can now manage [Artifacts](https://developers.cloudflare.com/artifacts/) namespaces, repos, and repo-scoped tokens directly from Wrangler CLI.

Available commands:

  * `wrangler artifacts namespaces list` — List Artifacts namespaces in your account.
  * `wrangler artifacts namespaces get` — Get metadata for a namespace.
  * `wrangler artifacts repos create` — Create a repo in a namespace.
  * `wrangler artifacts repos list` — List repos in a namespace.
  * `wrangler artifacts repos get` — Get metadata for a repo.
  * `wrangler artifacts repos delete` — Delete a repo.
  * `wrangler artifacts repos issue-token` — Issue a repo-scoped token for Git access.



To get started, refer to the [Wrangler Artifacts commands documentation](https://developers.cloudflare.com/workers/wrangler/commands/artifacts/).

Apr 16, 2026

## [Artifacts now in beta: versioned filesystem with Git access](https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/)

[Artifacts](https://developers.cloudflare.com/artifacts/)

[Artifacts](https://developers.cloudflare.com/artifacts/) is now in private beta. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. It provides a versioned filesystem for storing and exchanging file trees across Workers, the REST API, and any Git client, running locally or within an agent.

You can [read the announcement blog ↗︎](https://blog.cloudflare.com/artifacts-git-for-agents-beta/) to learn more about what Artifacts does, how it works, and how to create repositories for your agents to use.

Artifacts has three API surfaces:

  * Workers bindings (for creating and managing repositories)
  * REST API (for creating and managing repos from any other compute platform)
  * Git protocol (for interacting with repos)



As an example: you can use the Workers binding to create a repo and read back its remote URL:
    
    
    # Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user.
    const created = await env.PROD_ARTIFACTS.create("agent-007");
    const remote = (await created.repo.info())?.remote;

Or, use the REST API to create a repo inside a namespace from your agent(s) running on any platform:
    
    
    curl --request POST "https://artifacts.cloudflare.net/v1/api/namespaces/some-namespace/repos" --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" --header "Content-Type: application/json" --data '{"name":"agent-007"}'

Any Git client that speaks smart HTTP can use the returned remote URL:
    
    
    # Agents know git.
    # Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.
    git clone https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git

To learn more, refer to [Get started](https://developers.cloudflare.com/artifacts/get-started/), [Workers binding](https://developers.cloudflare.com/artifacts/api/workers-binding/), and [Git protocol](https://developers.cloudflare.com/artifacts/api/git-protocol/).
