---
url: https://developers.cloudflare.com/workers/languages/python/basics/
title: Learn the basics of Python Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:31.374716+00:00
---

# Learn the basics of Python Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/languages/python/basics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Languages](https://developers.cloudflare.com/workers/languages/)

  4. /[Python Workers](https://developers.cloudflare.com/workers/languages/python/)
  5. /The Basics



# The Basics

Last updated Jun 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/languages/python/basics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFetch HandlerThe Request InterfaceReturn JSON responsesThe env AttributeModulesTypes and AutocompletionUpgrading pywranglerNext Up

## Fetch Handler

As mentioned in the [introduction to Python Workers](https://developers.cloudflare.com/workers/languages/python/), a Python Worker can be as simple as four lines of code:
    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            return Response("Hello World!")

Similar to other Workers, the main entry point for a Python worker is the [`fetch` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch) which handles incoming requests sent to the Worker.

In a Python Worker, this handler is placed in a `Default` class that extends the `WorkerEntrypoint` class (which you can import from the `workers` SDK module).

## The `Request` Interface

The `request` parameter passed to your `fetch` handler is a JavaScript Request object, exposed via the [foreign function interface (FFI)](https://developers.cloudflare.com/workers/languages/python/ffi), allowing you to access it directly from your Python code.

Let's try editing the worker to accept a POST request. We know from the [documentation for `Request`](https://developers.cloudflare.com/workers/runtime-apis/request) that we can call `await request.json()` within an `async` function to parse the request body as JSON.

In a Python Worker, you would write:
    
    
    from workers import WorkerEntrypoint, Response
    from hello import hello
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            body = await request.json()
            name = body["name"]
            return Response(hello(name))

Many other JavaScript APIs are available in Python Workers via the FFI, so you can call other methods in a similar way.

Once you edit the `src/entry.py`, Wrangler will automatically restart the local development server.

Now, if you send a POST request with the appropriate body, your Worker will respond with a personalized message.
    
    
    curl --header "Content-Type: application/json" \
      --request POST \
      --data '{"name": "Python"}' http://localhost:8787
    
    
    Hello, Python!

## Return JSON responses

To return JSON from a Python Worker, use `Response.json()`:
    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            data = {"message": "Hello", "status": "ok"}
            return Response.json(data)

## The `env` Attribute

The `env` attribute on the `WorkerEntrypoint` can be used to access [environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/), [secrets](https://developers.cloudflare.com/workers/configuration/secrets/), and [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/).

For example, let us try setting and using an environment variable in a Python Worker. First, add the environment variable to your Worker's [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "hello-python-worker",
    	"main": "src/entry.py",
    	"compatibility_flags": [
    		"python_workers"
    	],
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"vars": {
    		"API_HOST": "example.com"
    	}
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "hello-python-worker"
    main = "src/entry.py"
    compatibility_flags = [ "python_workers" ]
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [vars]
    API_HOST = "example.com"

Then, you can access the `API_HOST` environment variable via the `env` parameter:
    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            return Response(self.env.API_HOST)

## Modules

Python workers can be split across multiple files.

Let's create a new Python file, called `src/hello.py`:
    
    
    def hello(name):
        return "Hello, " + name + "!"

Now, we can modify `src/entry.py` to make use of the new module.
    
    
    from hello import hello
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            return Response(hello("World"))

Once you edit `src/entry.py`, [`pywrangler`](https://developers.cloudflare.com/workers/languages/python/#the-pywrangler-cli-tool) will automatically detect the change and reload your Worker.

## Types and Autocompletion

The `workers-runtime-sdk` package provides the runtime SDK for Python Workers. This package is automatically installed and included in your worker when you use `pywrangler`, but you can also install it manually to take advantage of type hints and autocompletion in your IDE.

To enable them, add the `workers-runtime-sdk` package to your `pyproject.toml` file.
    
    
    dependencies = [
      "workers-runtime-sdk"
    ]

Additionally, you can generate types based on your Worker configuration using `uv run pywrangler types`

This includes `Env` types based on your bindings, module rules, and runtime types based on the `compatibility_date` and `compatibility_flags` in your config file. See

## Upgrading `pywrangler`

To upgrade to the latest version of [`pywrangler`](https://developers.cloudflare.com/workers/languages/python/#the-pywrangler-cli-tool) globally, run the following command:
    
    
    uv tool upgrade workers-py

To upgrade to the latest version of `pywrangler` in a specific project, run the following command:
    
    
    uv lock --upgrade-package workers-py

## Next Up

  * Learn details about local development, deployment, and [how Python Workers work](https://developers.cloudflare.com/workers/languages/python/how-python-workers-work).
  * Explore the [package](https://developers.cloudflare.com/workers/languages/python/packages) docs for instructions on how to use packages with Python Workers.
  * Understand which parts of the [Python Standard Library](https://developers.cloudflare.com/workers/languages/python/stdlib) are supported in Python Workers.
  * Learn about Python Workers' [foreign function interface (FFI)](https://developers.cloudflare.com/workers/languages/python/ffi), and how to use it to work with [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings) and [Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/).



[PreviousOverview](https://developers.cloudflare.com/workers/languages/python/)[NextHow Python Workers Work](https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/languages/python/basics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
