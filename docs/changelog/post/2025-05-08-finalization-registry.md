---
url: https://developers.cloudflare.com/changelog/post/2025-05-08-finalization-registry/
title: Improved memory efficiency for WebAssembly Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.379571+00:00
---

# Improved memory efficiency for WebAssembly Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-08-finalization-registry/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 8, 2025

## Improved memory efficiency for WebAssembly Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[FinalizationRegistry ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry) is now available in Workers. You can opt-in using the [`enable_weak_ref`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref) compatibility flag.

This can reduce memory leaks when using WebAssembly-based Workers, which includes [Python Workers](https://developers.cloudflare.com/workers/languages/python/) and [Rust Workers](https://developers.cloudflare.com/workers/languages/rust/). The FinalizationRegistry works by enabling toolchains such as [Emscripten ↗︎](https://emscripten.org/) and [wasm-bindgen ↗︎](https://wasm-bindgen.github.io/wasm-bindgen/) to automatically free WebAssembly heap allocations. If you are using WASM and seeing Exceeded Memory errors and cannot determine a cause using [memory profiling](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/), you may want to enable the FinalizationRegistry.

For more information refer to the [`enable_weak_ref`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref) compatibility flag documentation.
