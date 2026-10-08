---
url: https://developers.cloudflare.com/workers/languages/python/stdlib/
title: Standard Library provided to Python Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:32.551518+00:00
---

# Standard Library provided to Python Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/languages/python/stdlib/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Languages](https://developers.cloudflare.com/workers/languages/)

  4. /[Python Workers](https://developers.cloudflare.com/workers/languages/python/)
  5. /Standard Library



# Standard Library

Last updated Jun 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/languages/python/stdlib/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExcluded modulesModules with limited functionalityIn-memory filesystem

Workers written in Python are executed by [Pyodide ↗︎](https://pyodide.org/en/stable/index.html).

Pyodide is a port of CPython to WebAssembly — for the most part it behaves identically to [CPython ↗︎](https://github.com/python) (the reference implementation of Python — commonly referred to as just "Python"). The majority of the CPython test suite passes when run against Pyodide. For the most part, you shouldn't need to worry about differences in behavior.

The full [Python Standard Library ↗︎](https://docs.python.org/3/library/index.html) is available in Python Workers, with the following exceptions:

## Excluded modules

The following modules are not available in Python Workers:

  * curses
  * dbm
  * ensurepip
  * fcntl
  * grp
  * idlelib
  * lib2to3
  * msvcrt
  * pwd
  * resource
  * syslog
  * termios
  * tkinter
  * turtle.py
  * turtledemo
  * venv
  * winreg
  * winsound



The following modules can be imported, but are not functional due to the limitations of the WebAssembly VM.

  * multiprocessing
  * threading



The following are present but cannot be imported due to a dependency on the termios package which has been removed:

  * pty
  * tty



## Modules with limited functionality

  * `decimal`: The decimal module has C (_decimal) and Python (_pydecimal) implementations with the same functionality. Only the C implementation is available (compiled to WebAssembly)
  * `pydoc`: Help messages for Python builtins are not available
  * `webbrowser`: The original webbrowser module is not available.



## In-memory filesystem

Python Workers have access to an ephemeral, in-memory filesystem. You can read and write files using standard Python file I/O (for example, `open()`, `pathlib.Path`), but all data is **lost when the Worker isolate is destroyed**. The filesystem is not shared between different isolate instances.

This can be useful for temporary file operations, but should not be relied upon for persistent storage. Use [KV](https://developers.cloudflare.com/kv/), [R2](https://developers.cloudflare.com/r2/), or [Durable Objects](https://developers.cloudflare.com/durable-objects/) for durable storage.

[PreviousForeign Function Interface (FFI)](https://developers.cloudflare.com/workers/languages/python/ffi/)[NextExamples](https://developers.cloudflare.com/workers/languages/python/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/languages/python/stdlib.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
