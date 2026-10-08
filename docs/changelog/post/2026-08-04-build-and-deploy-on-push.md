---
url: https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/
title: Build and deploy Artifacts repos on every push \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.478787+00:00
---

# Build and deploy Artifacts repos on every push · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 4, 2026

## Build and deploy Artifacts repos on every push

[Artifacts](https://developers.cloudflare.com/artifacts/)[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-build-and-deploy-on-push/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
