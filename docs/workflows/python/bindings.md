---
url: https://developers.cloudflare.com/workflows/python/bindings/
title: Interact with a Workflow \u00b7 Cloudflare Workflows docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:16.078551+00:00
---

# Interact with a Workflow · Cloudflare Workflows docs

> Source: https://developers.cloudflare.com/workflows/python/bindings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workflows](https://developers.cloudflare.com/workflows/)
  3. /[Python Workflows SDK](https://developers.cloudflare.com/workflows/python/)
  4. /Interact with a Workflow



# Interact with a Workflow

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workflows/python/bindings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWorkflow create create_batch get send_eventREST API (HTTP)Command line (CLI)

Note

You must add both `python_workflows` and `python_workers` compatibility flags to your Wrangler config file.

Also, Python Workflows requires `compatibility_date = "2025-08-01"`, or later, to be set in your Wrangler config file.

The Python Workers platform leverages [FFI ↗︎](https://en.wikipedia.org/wiki/Foreign_function_interface) to access bindings to Cloudflare resources. Refer to the [bindings](https://developers.cloudflare.com/workers/languages/python/ffi/#using-bindings-from-python-workers) documentation for more information.

From the configuration perspective, enabling Python Workflows requires adding the `python_workflows` compatibility flag to your Wrangler configuration file.
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "workflows-starter",
    	"main": "src/index.py",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"compatibility_flags": ["python_workflows", "python_workers"],
    	"workflows": [
    		{
    			// name of your workflow
    			"name": "workflows-starter",
    			// binding name env.MY_WORKFLOW
    			"binding": "MY_WORKFLOW",
    			// this is class that extends the Workflow class in src/index.py
    			"class_name": "MyWorkflow",
    		}
    	]
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "workflows-starter"
    main = "src/index.py"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "python_workflows", "python_workers" ]
    
    [[workflows]]
    name = "workflows-starter"
    binding = "MY_WORKFLOW"
    class_name = "MyWorkflow"

And this is how you use the payload in your workflow:
    
    
    from workers import WorkflowEntrypoint
    
    class DemoWorkflowClass(WorkflowEntrypoint):
        async def run(self, event, step):
            @step.do('step-name')
            async def first_step():
                payload = event["payload"]
                return payload

## Workflow

The `Workflow` binding gives you access to the [Workflow](https://developers.cloudflare.com/workflows/build/workers-api/#workflow) class. All its methods are available on the binding.

### `create`

Create (trigger) a new instance of a given Workflow.

  * `create(options=None)`* `options` \- an **optional** dictionary of options to pass to the workflow instance. Should contain the same keys as the [WorkflowInstanceCreateOptions](https://developers.cloudflare.com/workflows/build/workers-api/#workflowinstancecreateoptions) type.


    
    
    from workers import WorkerEntrypoint, Response
    
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            event = {"foo": "bar"}
            await self.env.MY_WORKFLOW.create(params=event)
            return Response.json({"status": "success"})

The `create` method returns a [`WorkflowInstance`](https://developers.cloudflare.com/workflows/build/workers-api/#workflowinstance) object, which can be used to query the status of the workflow instance. Note that this is a Javascript object, and not a Python object.

### `create_batch`

Create (trigger) a batch of new workflow instances, up to 100 instances at a time. This is useful if you need to create multiple instances at once within the [instance creation limit](https://developers.cloudflare.com/workflows/reference/limits/).

  * `create_batch(batch)`* `batch` \- list of `WorkflowInstanceCreateOptions` to pass when creating an instance, including a user-provided ID and payload parameters.



Each element of the `batch` list is expected to include both `id` and `params` properties:
    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
    			# Create a new batch of 3 Workflow instances, each with its own ID and pass params to the Workflow instances
            instances = [
                {"id": "id-abc123", "params": {"hello": "world-0"}},
                {"id": "id-def456", "params": {"hello": "world-1"}},
                {"id": "id-ghi789", "params": {"hello": "world-2"}},
            ]
            await self.env.MY_WORKFLOW.create_batch(instances)
            return Response.json({"status": "success"})

### `get`

Get a workflow instance by ID.

  * `get(id)`* `id` \- the ID of the workflow instance to get.



Returns a [`WorkflowInstance`](https://developers.cloudflare.com/workflows/build/workers-api/#workflowinstance) object, which can be used to query the status of the workflow instance.
    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            instance = await self.env.MY_WORKFLOW.get("abc-123")
    
            # FFI methods available for WorkflowInstance
            await instance.status()
            await instance.pause()
            await instance.resume()
            await instance.restart()
            await instance.terminate()
            return Response.json({"status": "success"})

### `send_event`

Send an event to a workflow instance.

  * `send_event(type, payload)`* `type` \- the type of event to send to the workflow instance. * `payload` \- the payload to send to the workflow instance.


    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            await self.env.MY_WORKFLOW.send_event(type="my-event-type", payload={"foo": "bar"})
            return Response.json({"status": "success"})

## REST API (HTTP)

Refer to the [Workflows REST API documentation](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/create/).

## Command line (CLI)

Refer to the [CLI quick start](https://developers.cloudflare.com/workflows/get-started/guide/) to learn more about how to manage and trigger Workflows via the command-line.

[PreviousPython Workers API](https://developers.cloudflare.com/workflows/python/python-workers-api/)[NextDAG Workflows](https://developers.cloudflare.com/workflows/python/dag/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workflows/python/bindings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
