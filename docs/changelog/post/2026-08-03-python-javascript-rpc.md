---
url: https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/
title: Python and JavaScript Workers can now call each other via RPC \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.361761+00:00
---

# Python and JavaScript Workers can now call each other via RPC · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 3, 2026

## Python and JavaScript Workers can now call each other via RPC

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-python-javascript-rpc/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now call methods between Python and JavaScript Workers using [Workers RPC](https://developers.cloudflare.com/workers/runtime-apis/rpc/). This works through [Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/) without extra dependencies, schema definitions, or serialization code.

Cross-language RPC calls behave like ordinary function calls. Exceptions propagate to the call site. You can pass [structured cloneable types ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types) as parameters or return values, and Pyodide Foreign Function Interface (FFI) automatically converts types between languages.

#### Call a TypeScript Worker from Python

Define a method in a TypeScript Worker:

index.jsjs
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class RpcService extends WorkerEntrypoint {
    	async add(a, b) {
    		return a + b;
    	}
    }

index.tsts
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class RpcService extends WorkerEntrypoint {
    	async add(a: number, b: number): Promise<number> {
    		return a + b;
    	}
    }

Call it from a Python Worker through a Service binding:
    
    
    from workers import Response, WorkerEntrypoint
    
    class Default(WorkerEntrypoint):
    	async def fetch(self, request):
    		rpc = self.env.RPC
    		result = await rpc.add(42, 144)
    		return Response.json({"result": result})

Configure the Service binding in the Python Worker's Wrangler configuration:
    
    
    {
    	"services": [
    		{
    			"binding": "RPC",
    			"service": "ts-rpc-server",
    			"entrypoint": "RpcService"
    		}
    	]
    }
    
    
    [[services]]
    binding = "RPC"
    service = "ts-rpc-server"
    entrypoint = "RpcService"

#### Call a Python Worker from JavaScript

Define a method in a Python Worker:
    
    
    from workers import WorkerEntrypoint
    
    class Default(WorkerEntrypoint):
    	async def highlight_code(self, code: str, language: str) -> dict:
    		from pygments.formatters import HtmlFormatter
    		from pygments import highlight
    		from pygments.lexers import get_lexer_by_name
    
    		lexer = get_lexer_by_name(language, stripall=True)
    		formatter = HtmlFormatter(linenos=True, cssclass="highlight", style="monokai")
    		highlighted_html = highlight(code, lexer, formatter)
    		css = formatter.get_style_defs(".highlight")
    
    		return {
    			"html": highlighted_html,
    			"css": css
    		}

Call it from a JavaScript Worker through a Service binding:

index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const rpc = env.PYTHON_RPC;
    		const result = await rpc.highlight_code("print(42)", "python");
    		return Response.json(result);
    	},
    };

index.tsts
    
    
    export default {
    	async fetch(request, env) {
    		const rpc = env.PYTHON_RPC;
    		const result = await rpc.highlight_code("print(42)", "python");
    		return Response.json(result);
    	},
    };

Configure the Service binding in the JavaScript Worker's Wrangler configuration:
    
    
    {
    	"services": [
    		{
    			"binding": "PYTHON_RPC",
    			"service": "py-rpc-server"
    		}
    	]
    }
    
    
    [[services]]
    binding = "PYTHON_RPC"
    service = "py-rpc-server"

For more details on the announcement, read the [blog post ↗︎](https://blog.cloudflare.com/python-workers-rpc/).

For more information, refer to the [Workers RPC documentation](https://developers.cloudflare.com/workers/runtime-apis/rpc/) and the [Python Workers overview](https://developers.cloudflare.com/workers/languages/python/).
