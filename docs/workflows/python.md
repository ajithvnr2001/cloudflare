---
url: https://developers.cloudflare.com/workflows/python/
title: Python Workflows SDK \u00b7 Cloudflare Workflows docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:16.015608+00:00
---

# Python Workflows SDK · Cloudflare Workflows docs

> Source: https://developers.cloudflare.com/workflows/python/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workflows](https://developers.cloudflare.com/workflows/)
  3. /Python Workflows SDK



# Python Workflows SDK

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workflows/python/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet Started

Workflow entrypoints can be declared using Python. To achieve this, you can export a `WorkflowEntrypoint` that runs on the Cloudflare Workers platform. Refer to [Python Workers](https://developers.cloudflare.com/workers/languages/python) for more information about Python on the Workers runtime.

## Get Started

The main entrypoint for a Python workflow is the [`WorkflowEntrypoint`](https://developers.cloudflare.com/workflows/build/workers-api/#workflowentrypoint) class. Your workflow logic should exist inside the [`run`](https://developers.cloudflare.com/workflows/build/workers-api/#run) handler.
    
    
    from workers import WorkflowEntrypoint
    
    class MyWorkflow(WorkflowEntrypoint):
        async def run(self, event, step):
            # steps here

For example, a Workflow may be defined as:
    
    
    from workers import Response, WorkflowEntrypoint, WorkerEntrypoint
    
    class PythonWorkflowStarter(WorkflowEntrypoint):
        async def run(self, event, step):
    
            @step.do('step1')
            async def step_1():
                # does stuff
                print('executing step1')
    
            @step.do('step2')
            async def step_2():
                # does stuff
                print('executing step2')
    
            await step_1()
            await step_2()
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            await self.env.MY_WORKFLOW.create()
            return Response("Hello world!")

You must add both `python_workflows` and `python_workers` compatibility flags to your Wrangler configuration file.
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "hello-python",
    	"main": "src/entry.py",
    	"compatibility_flags": [
    		"python_workers",
    		"python_workflows"
    	],
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"workflows": [
    		{
    			"name": "workflows-demo",
    			"binding": "MY_WORKFLOW",
    			"class_name": "PythonWorkflowStarter"
    		}
    	]
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "hello-python"
    main = "src/entry.py"
    compatibility_flags = [ "python_workers", "python_workflows" ]
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[workflows]]
    name = "workflows-demo"
    binding = "MY_WORKFLOW"
    class_name = "PythonWorkflowStarter"

To run a Python Workflow locally, use [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the CLI for Cloudflare Workers:
    
    
    npx wrangler@latest dev

To deploy a Python Workflow to Cloudflare, run [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy):
    
    
    npx wrangler@latest deploy

Join the #python-workers channel in the [Cloudflare Developers Discord ↗︎](https://discord.cloudflare.com/) and let us know what you would like to see next.

[PreviousMetrics and analytics](https://developers.cloudflare.com/workflows/observability/metrics-analytics/)[NextPython Workers API](https://developers.cloudflare.com/workflows/python/python-workers-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workflows/python/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
