---
url: https://developers.cloudflare.com/workers/languages/python/packages/
title: Python packages supported in Cloudflare Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:32.139780+00:00
---

# Python packages supported in Cloudflare Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/languages/python/packages/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Languages](https://developers.cloudflare.com/workers/languages/)

  4. /[Python Workers](https://developers.cloudflare.com/workers/languages/python/)
  5. /Packages



# Packages

Last updated Sep 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/languages/python/packages/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported Libraries

[Pywrangler ↗︎](https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler) is a CLI tool for managing packages and Python Workers. It is meant as a wrapper for wrangler that sets up a full environment for you, including bundling your packages into your worker bundle on deployment.

To get started, create a pyproject.toml file with the following contents:
    
    
    [project]
    name = "YourProjectName"
    version = "0.1.0"
    description = "Add your description here"
    requires-python = ">=3.13"
    dependencies = [
        "fastapi"
    ]
    
    [dependency-groups]
    dev = [
    	"workers-py",
    	"workers-runtime-sdk"
    ]

The above will allow your worker to depend on the [FastAPI ↗︎](https://fastapi.tiangolo.com/) package.

To run the worker locally:
    
    
    uv run pywrangler dev

To deploy your worker:
    
    
    uv run pywrangler deploy

Your dependencies will get bundled with your worker automatically on deployment.

The `pywrangler` CLI also supports all commands supported by the `wrangler` tool, for the full list of commands run `uv run pywrangler --help`.

## Supported Libraries

Python Workers support pure and [PyEmscripten ↗︎](https://peps.python.org/pep-0783/) Python packages on [PyPI ↗︎](https://pypi.org/). Additionally, Python Workers support packages that are included in [Pyodide ↗︎](https://pyodide.org/en/stable/usage/packages-in-pyodide.html).

WebAssembly support for Python packages is still in early stages, and some packages may not yet be available as PyEmscripten wheels on PyPI. If a package you would like to use is not yet available, we encourage you to reach out to the package maintainers and request PyEmscripten wheels. You can also start a thread in the [Python Packages Discussions ↗︎](https://github.com/cloudflare/workerd/discussions/categories/python-packages) on the Cloudflare Workers Runtime GitHub repository — we would be happy to help you communicate with package maintainers.

[PreviousExamples](https://developers.cloudflare.com/workers/languages/python/examples/)[NextDjango](https://developers.cloudflare.com/workers/languages/python/packages/django/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/languages/python/packages/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
