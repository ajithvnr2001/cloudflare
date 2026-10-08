---
url: https://developers.cloudflare.com/workflows/python/dag/
title: DAG Workflows \u00b7 Cloudflare Workflows docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:16.112869+00:00
---

# DAG Workflows · Cloudflare Workflows docs

> Source: https://developers.cloudflare.com/workflows/python/dag/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workflows](https://developers.cloudflare.com/workflows/)
  3. /[Python Workflows SDK](https://developers.cloudflare.com/workflows/python/)
  4. /DAG Workflows



# DAG Workflows

Last updated Apr 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workflows/python/dag/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Python Workflows SDK supports DAG workflows in a declarative way, using `step.do` and parameter names to define dependencies (other steps that must complete before a step can run).
    
    
    from workers import Response, WorkflowEntrypoint, WorkerEntrypoint
    
    class PythonWorkflowStarter(WorkflowEntrypoint):
        async def run(self, event, step):
            async def await_step(fn):
                try:
                    return await fn()
                except TypeError as e:
                    print(f"Successfully caught {type(e).__name__}: {e}")
    
            await step.sleep('demo sleep', '10 seconds')
    
            @step.do()
            async def dep_1():
                # does stuff
                print('executing dep1')
                return 'dep1'
    
            @step.do()
            async def dep_2():
                # does stuff
                print('executing dep2')
                return 'dep2'
    
            @step.do(concurrent=True)
            async def final_step(dep_1, dep_2):
                # does stuff
                print(f'{dep_1} {dep_2}')
    
            await await_step(final_step)
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            await self.env.MY_WORKFLOW.create()
            return Response("Hello world!")

In this example, `dep_1` and `dep_2` are run concurrently before execution of `final_step`, which depends on both of them.

Having `concurrent=True` allows dependencies to be resolved concurrently. If a dependency has already completed, it will be skipped and its return value will be reused.

Note

Older compatibility behavior supports explicit dependency lists with `depends=[...]`. For new workflows, use parameter names to express step dependencies.

This pattern is useful for diamond shaped workflows, where a step depends on two or more other steps that can run concurrently.

[PreviousInteract with a Workflow](https://developers.cloudflare.com/workflows/python/bindings/)[NextVideos](https://developers.cloudflare.com/workflows/videos/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workflows/python/dag.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
