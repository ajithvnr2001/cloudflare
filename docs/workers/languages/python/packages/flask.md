---
url: https://developers.cloudflare.com/workers/languages/python/packages/flask/
title: Flask \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:32.464248+00:00
---

# Flask · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/languages/python/packages/flask/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Languages](https://developers.cloudflare.com/workers/languages/)[Python Workers](https://developers.cloudflare.com/workers/languages/python/)

  4. /[Packages](https://developers.cloudflare.com/workers/languages/python/packages/)
  5. /Flask



# Flask

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/languages/python/packages/flask/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a Flask WorkerServe a frontendMore examples

[Flask ↗︎](https://flask.palletsprojects.com/) is supported in Python Workers.

Flask applications rely on a protocol called the Web Server Gateway Interface (WSGI). This means that Flask never directly reads or writes to a socket, instead relying on the WSGI server to communicate.

Python Workers include a [WSGI server ↗︎](https://github.com/cloudflare/workers-py/blob/main/packages/runtime-sdk/src/workers/wsgi.py) which you can use with Flask applications.

## Create a Flask Worker

Use this quick start to run a minimal Flask application.

  1. Create `src/worker.py` with your flask application:

src/worker.pypython
         
         from flask import Flask
         from workers import wsgi
         
         app = Flask(__name__)
         
         @app.get("/")
         def index():
             return {"message": "Hello from Flask"}
         
         Default = wsgi.entrypoint(app)

  2. In the project root, create `wrangler.jsonc`:
         
         {
           "$schema": "node_modules/wrangler/config-schema.json",
           "name": "my-flask-worker",
           "main": "src/worker.py",
           // Set this to today's date
           "compatibility_date": "2026-10-08",
           "compatibility_flags": ["python_workers"]
         }
         
         "$schema" = "node_modules/wrangler/config-schema.json"
         name = "my-flask-worker"
         main = "src/worker.py"
         # Set this to today's date
         compatibility_date = "2026-10-08"
         compatibility_flags = [ "python_workers" ]

  3. Create a `pyproject.toml` to declare dependencies:

pyproject.tomltoml
         
         [project]
         name = "flask-worker"
         version = "0.1.0"
         requires-python = ">=3.12"
         dependencies = [
             "flask",
         ]
         
         [dependency-groups]
         dev = [
             "workers-py",
             "workers-runtime-sdk",
         ]

  4. Start the local development server:
         
         uv run pywrangler dev

  5. In another terminal, send a request to the Worker:
         
         curl http://localhost:8787/

The Worker returns:
         
         {"message":"Hello from Flask"}




## Serve a frontend

You can serve any static frontend alongside your flask backend by using [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/). Using Static Assets means your frontend files are not bundled inside the Worker itself, keeping the bundle small.

Place your static files in a directory such as `./public/`. Then configure your Wrangler file with an `assets` block that includes a `binding` and sets `run_worker_first` to `true`. This ensures every request reaches your Flask Worker first, so your API routes take priority over static files.
    
    
    {
      "$schema": "node_modules/wrangler/config-schema.json",
      "name": "my-flask-worker",
      "main": "src/worker.py",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "compatibility_flags": ["python_workers"],
      "assets": {
        "directory": "./public/",
        "binding": "ASSETS",
        "run_worker_first": true
      }
    }
    
    
    "$schema" = "node_modules/wrangler/config-schema.json"
    name = "my-flask-worker"
    main = "src/worker.py"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "python_workers" ]
    
    [assets]
    directory = "./public/"
    binding = "ASSETS"
    run_worker_first = true

The following Worker handles an API route before forwarding other requests. The catch-all handlers return each asset's body, status, and headers:

src/worker.pypython
    
    
    from flask import Flask, Response, request
    from pyodide.ffi import run_sync
    from workers import wsgi
    
    
    app = Flask(__name__)
    
    
    @app.get("/api/hello")
    def api_hello():
        return {"message": "Hello from the API"}
    
    
    @app.get("/")
    @app.get("/<path:path>")
    def frontend(path=""):
        assets = request.environ["workers.env"].ASSETS
        asset_response = run_sync(assets.fetch(f"https://assets.local/{path}"))
        body = run_sync(asset_response.bytes())
        return Response(
            body,
            status=asset_response.status,
            headers=asset_response.headers,
        )
    
    
    Default = wsgi.entrypoint(app)

`run_sync` bridges both asynchronous asset operations into Flask's synchronous handler. API routes take priority, and unmatched paths are served from `./public/`.

## More examples

Clone the `cloudflare/python-workers-examples` repository and run the flask-todo example there:
    
    
    git clone https://github.com/cloudflare/python-workers-examples
    cd python-workers-examples/flask-todo
    #  See README.md for instructions

[PreviousFastAPI ↗︎](https://developers.cloudflare.com/workers/languages/python/packages/fastapi/)[NextHono ↗︎](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/languages/python/packages/flask.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
