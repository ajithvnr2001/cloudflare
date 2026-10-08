---
url: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workflows-playground/
title: Dynamic Workflows Playground \u00b7 Cloudflare Dynamic Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:11.386921+00:00
---

# Dynamic Workflows Playground · Cloudflare Dynamic Workers docs

> Source: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workflows-playground/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/)
  3. /Examples
  4. /Dynamic Workflows Playground



# Dynamic Workflows Playground

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workflows-playground/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksWhat this playground includes

Try the [dynamic workflows playground ↗︎](https://github.com/cloudflare/dynamic-workflows/tree/main/examples/basic), write workflow logic in JavaScript, execute it from a Dynamic Worker, and log every step in real time.

This example shows you how to run [Cloudflare Workflows](https://developers.cloudflare.com/workflows/) from a [Dynamic Worker](https://developers.cloudflare.com/dynamic-workers/) to get full durable execution, including step retries, sleep, hibernation, and `waitForEvent`, for any workflow you need to run on demand.

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/dynamic-workflows/tree/main/examples/basic)

## How it works

There are two parts:

  * **Worker Loader** — The Worker that runs your platform logic. It receives a request, loads the user's workflow code as a Dynamic Worker, and gives it a Workflow binding so it can create and run workflows.
  * **Dynamic Worker** — This is where the workflow is defined. You write the workflow logic here, including which steps need to run, how long it sleeps, and what events it waits for.



The [`@cloudflare/dynamic-workflows` ↗︎](https://www.npmjs.com/package/@cloudflare/dynamic-workflows) library connects the two. When the Dynamic Worker creates a workflow, the library tags it with information about which Dynamic Worker created it. That tag is persisted by the Workflows engine, so when a workflow needs to resume after a sleep, a failure, or a server restart, the engine knows which Dynamic Worker to reload to continue execution.

For a full walkthrough of the library and how to set it up, refer to the [Dynamic Workflows guide](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/).

## What this playground includes

  * **Worker Loader and Dynamic Worker setup** — A full working example of a Worker Loader that loads workflow code at runtime and a Dynamic Worker that runs it with durable execution, using [`@cloudflare/dynamic-workflows` ↗︎](https://www.npmjs.com/package/@cloudflare/dynamic-workflows).
  * **Live log streaming** — Every `console.log()` and `console.warn()` from the Dynamic Worker is captured and streamed to the browser in real time, so you can see what is happening inside each step as it runs.
  * **Source persistence** — The workflow code is saved so that if the workflow pauses (for example, during a `step.sleep()`) and the server recycles the process, it can reload the same code and resume where it left off.



[PreviousCode Mode Example](https://developers.cloudflare.com/dynamic-workers/examples/codemode/)[NextAPI reference](https://developers.cloudflare.com/dynamic-workers/api-reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dynamic-workers/examples/dynamic-workflows-playground.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
