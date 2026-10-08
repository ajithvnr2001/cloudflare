---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/
title: Node.js compatibility \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:44.969998+00:00
---

# Node.js compatibility · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)
  4. /Node.js compatibility



# Node.js compatibility

Last updated Aug 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet StartedSupported Node.js APIs Non-functional stub modules Node.js API PolyfillsEnable only AsyncLocalStorage

When you write a Worker, you may need to import packages from [npm ↗︎](https://www.npmjs.com/). Many npm packages rely on APIs from the [Node.js runtime ↗︎](https://nodejs.org/en/about), and will not work unless these Node.js APIs are available.

Cloudflare Workers provides a subset of Node.js APIs in two forms:

  1. As built-in APIs provided by the Workers Runtime. Most of these APIs are full implementations of the corresponding Node.js APIs, while a few are partially supported.
  2. As polyfill shim implementations that [Wrangler](https://developers.cloudflare.com/workers/wrangler/) adds to your Worker's code, allowing it to import the module, but calling API methods will throw errors.



## Get Started

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. Built-in Node.js APIs and polyfills are available without additional configuration.

For these compatibility dates, `nodejs_compat` and `nodejs_compat_v2` are not used because the compatibility date enables the same behavior. Existing projects do not need to remove these flags when updating their compatibility date. Omit them from new configurations.

For compatibility dates from `2024-09-23` through `2026-08-03`, add the `nodejs_compat` compatibility flag to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in:
    
    
    {
    	"compatibility_date": "2026-08-03",
    	"compatibility_flags": ["nodejs_compat"]
    }
    
    
    compatibility_date = "2026-08-03"
    compatibility_flags = [ "nodejs_compat" ]

To turn off Node.js compatibility completely with a compatibility date of `2026-08-04` or later, remove the positive flags if present. Then add both `no_nodejs_compat` and `no_nodejs_compat_v2`. For configuration examples, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

## Supported Node.js APIs

The runtime APIs from Node.js listed in this section with the status "🟢 supported" are currently natively supported in the Workers Runtime. Items listed as "🟡 partially supported" include usable APIs, but do not implement the complete Node.js API surface.

[Deprecated or experimental APIs from Node.js ↗︎](https://nodejs.org/docs/latest/api/documentation.html#stability-index), and APIs that do not fit in a serverless context, are not included in the supported API list in this section. Some import-only stubs for these APIs are listed separately in Non-functional stub modules.

API Name | Natively supported by the Workers Runtime  
---|---  
[Assertion testing](https://developers.cloudflare.com/workers/runtime-apis/nodejs/assert/) | 🟢 supported  
[Asynchronous context tracking](https://developers.cloudflare.com/workers/runtime-apis/nodejs/asynclocalstorage/) | 🟢 supported  
[Buffer](https://developers.cloudflare.com/workers/runtime-apis/nodejs/buffer/) | 🟢 supported  
[Console ↗︎](https://nodejs.org/docs/latest/api/console.html) | 🟡 partially supported  
[Crypto](https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/) | 🟢 supported  
[Debugger](https://developers.cloudflare.com/workers/observability/dev-tools/) | 🟢 supported via [Chrome DevTools integration](https://developers.cloudflare.com/workers/observability/dev-tools/)  
[Diagnostics Channel](https://developers.cloudflare.com/workers/runtime-apis/nodejs/diagnostics-channel/) | 🟢 supported  
[DNS](https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/) | 🟡 partially supported  
Errors | 🟢 supported  
[Events](https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/) | 🟢 supported  
[File system](https://developers.cloudflare.com/workers/runtime-apis/nodejs/fs/) | 🟢 supported  
Globals | 🟢 supported  
[HTTP](https://developers.cloudflare.com/workers/runtime-apis/nodejs/http/) | 🟢 supported  
[HTTPS](https://developers.cloudflare.com/workers/runtime-apis/nodejs/https/) | 🟢 supported  
[Module ↗︎](https://nodejs.org/docs/latest/api/module.html) | 🟡 partially supported  
[Net](https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/) | 🟢 supported  
[OS ↗︎](https://nodejs.org/docs/latest/api/os.html) | 🟡 partially supported  
[Path](https://developers.cloudflare.com/workers/runtime-apis/nodejs/path/) | 🟢 supported  
[Performance hooks ↗︎](https://nodejs.org/docs/latest/api/perf_hooks.html) | 🟡 partially supported  
[Process](https://developers.cloudflare.com/workers/runtime-apis/nodejs/process/) | 🟢 supported  
[Punycode ↗︎](https://nodejs.org/docs/latest/api/punycode.html) (deprecated) | 🟢 supported  
[Query strings ↗︎](https://nodejs.org/docs/latest/api/querystring.html) | 🟢 supported  
[Stream](https://developers.cloudflare.com/workers/runtime-apis/nodejs/streams/) | 🟢 supported  
[String decoder](https://developers.cloudflare.com/workers/runtime-apis/nodejs/string-decoder/) | 🟢 supported  
[Test runner](https://developers.cloudflare.com/workers/runtime-apis/nodejs/test/) | 🟡 partially supported  
[Timers](https://developers.cloudflare.com/workers/runtime-apis/nodejs/timers/) | 🟢 supported  
[TLS/SSL](https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/) | 🟡 partially supported  
[URL](https://developers.cloudflare.com/workers/runtime-apis/nodejs/url/) | 🟢 supported  
[Utilities](https://developers.cloudflare.com/workers/runtime-apis/nodejs/util/) | 🟢 supported  
[Web Crypto API](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/) | 🟢 supported  
[Web Streams API](https://developers.cloudflare.com/workers/runtime-apis/streams/) | 🟢 supported  
[Zlib](https://developers.cloudflare.com/workers/runtime-apis/nodejs/zlib/) | 🟢 supported  
  
Unless otherwise specified, native implementations of Node.js APIs in Workers are intended to match the implementation in the [Current release of Node.js ↗︎](https://github.com/nodejs/release#release-schedule).

If an API you wish to use is missing and you want to suggest that Workers support it, please add a post or comment in the [Node.js APIs discussions category ↗︎](https://github.com/cloudflare/workerd/discussions/categories/node-js-apis) on GitHub.

### Non-functional stub modules

Some Node.js modules are available as non-functional stubs. A stub can be imported or required, but does not provide a working implementation of the underlying Node.js API. These stubs exist so packages that check for the presence of a module can load in Workers, but they are not suitable for direct use in application code.

The following stubs are enabled automatically only when the `nodejs_compat` compatibility flag is enabled and your Worker's compatibility date is on or after the date shown. To enable one earlier, add the corresponding enable flag. To keep one unavailable after that date, add the corresponding disable flag.

Stub module | Enabled with `nodejs_compat` on or after | Enable flag | Disable flag  
---|---|---|---  
[`node:http2` ↗︎](https://nodejs.org/docs/latest/api/http2.html) | `2025-09-01` | `enable_nodejs_http2_module` | `disable_nodejs_http2_module`  
[`node:vm` ↗︎](https://nodejs.org/docs/latest/api/vm.html) | `2025-10-01` | `enable_nodejs_vm_module` | `disable_nodejs_vm_module`  
[`node:cluster` ↗︎](https://nodejs.org/docs/latest/api/cluster.html) | `2025-12-04` | `enable_nodejs_cluster_module` | `disable_nodejs_cluster_module`  
[`node:domain` ↗︎](https://nodejs.org/docs/latest/api/domain.html) | `2025-12-04` | `enable_nodejs_domain_module` | `disable_nodejs_domain_module`  
[`node:trace_events` ↗︎](https://nodejs.org/docs/latest/api/tracing.html) | `2025-12-04` | `enable_nodejs_trace_events_module` | `disable_nodejs_trace_events_module`  
[`node:wasi` ↗︎](https://nodejs.org/docs/latest/api/wasi.html) | `2025-12-04` | `enable_nodejs_wasi_module` | `disable_nodejs_wasi_module`  
`node:_stream_wrap` | `2026-01-29` | `enable_nodejs_stream_wrap_module` | `disable_nodejs_stream_wrap_module`  
[`node:dgram` ↗︎](https://nodejs.org/docs/latest/api/dgram.html) | `2026-01-29` | `enable_nodejs_dgram_module` | `disable_nodejs_dgram_module`  
[`node:inspector` ↗︎](https://nodejs.org/docs/latest/api/inspector.html) | `2026-01-29` | `enable_nodejs_inspector_module` | `disable_nodejs_inspector_module`  
[`node:sqlite` ↗︎](https://nodejs.org/docs/latest/api/sqlite.html) | `2026-01-29` | `enable_nodejs_sqlite_module` | `disable_nodejs_sqlite_module`  
[`node:child_process` ↗︎](https://nodejs.org/docs/latest/api/child_process.html) | `2026-03-17` | `enable_nodejs_child_process_module` | `disable_nodejs_child_process_module`  
[`node:readline` ↗︎](https://nodejs.org/docs/latest/api/readline.html) | `2026-03-17` | `enable_nodejs_readline_module` | `disable_nodejs_readline_module`  
[`node:repl` ↗︎](https://nodejs.org/docs/latest/api/repl.html) | `2026-03-17` | `enable_nodejs_repl_module` | `disable_nodejs_repl_module`  
[`node:tty` ↗︎](https://nodejs.org/docs/latest/api/tty.html) | `2026-03-17` | `enable_nodejs_tty_module` | `disable_nodejs_tty_module`  
[`node:v8` ↗︎](https://nodejs.org/docs/latest/api/v8.html) | `2026-03-17` | `enable_nodejs_v8_module` | `disable_nodejs_v8_module`  
[`node:worker_threads` ↗︎](https://nodejs.org/docs/latest/api/worker_threads.html) | `2026-03-17` | `enable_nodejs_worker_threads_module` | `disable_nodejs_worker_threads_module`  
  
### Node.js API Polyfills

Node.js APIs that are not yet supported in the Workers runtime are polyfilled via [Wrangler](https://developers.cloudflare.com/workers/wrangler/), which uses [unenv ↗︎](https://github.com/unjs/unenv). If the `nodejs_compat` [compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/) is enabled, and your Worker's [compatibility date](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) is 2024-09-23 or later, Wrangler will automatically inject polyfills into your Worker's code.

Adding polyfills maximizes compatibility with existing npm packages by providing modules with mocked methods. Calling these mocked methods will either noop or will throw an error with a message like:
    
    
    [unenv] <method name> is not implemented yet!

This allows you to import packages that use these Node.js modules, even if certain methods are not supported.

## Enable only AsyncLocalStorage

If you need to enable only the Node.js `AsyncLocalStorage` API, you can enable the `nodejs_als` compatibility flag:
    
    
    {
    	"compatibility_flags": ["nodejs_als"],
    }
    
    
    compatibility_flags = [ "nodejs_als" ]

[PreviousMessageChannel](https://developers.cloudflare.com/workers/runtime-apis/messagechannel/)[Nextassert](https://developers.cloudflare.com/workers/runtime-apis/nodejs/assert/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
