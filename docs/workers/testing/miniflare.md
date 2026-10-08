---
url: https://developers.cloudflare.com/workers/testing/miniflare/
title: Miniflare \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:54.687558+00:00
---

# Miniflare · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Testing](https://developers.cloudflare.com/workers/testing/)
  4. /Miniflare



# Miniflare

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Caution

This documentation describes the Miniflare API, which is only relevant for advanced use cases. Instead, most users should use [Wrangler](https://developers.cloudflare.com/workers/wrangler) to build, run & deploy their Workers locally

**Miniflare** is a simulator for developing and testing [**Cloudflare Workers** ↗︎](https://workers.cloudflare.com/). It's written in TypeScript, and runs your code in a sandbox implementing Workers' runtime APIs.

  * 🎉 **Fun:** develop Workers easily with detailed logging, file watching and pretty error pages supporting source maps.
  * 🔋 **Full-featured:** supports most Workers features, including KV, Durable Objects, WebSockets, modules and more.
  * ⚡ **Fully-local:** test and develop Workers without an Internet connection. Reload code on change quickly.

[Get Started](https://developers.cloudflare.com/workers/testing/miniflare/get-started) [GitHub](https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare) [NPM](https://npmjs.com/package/miniflare)

* * *

These docs primarily cover Miniflare specific things. For more information on runtime APIs, refer to the [Cloudflare Workers docs](https://developers.cloudflare.com/workers).

If you find something that doesn't behave as it does in the production Workers environment (and this difference isn't documented), or something's wrong in these docs, please [open a GitHub issue ↗︎](https://github.com/cloudflare/workers-sdk/issues/new/choose).

  * [Get Started](https://developers.cloudflare.com/workers/testing/miniflare/get-started/): Install and configure the Miniflare API to dispatch events and test Cloudflare Workers locally.
  * [Writing tests](https://developers.cloudflare.com/workers/testing/miniflare/writing-tests/): Write integration tests against Workers using Miniflare.
  * [Core](https://developers.cloudflare.com/workers/testing/miniflare/core/): Core Miniflare features for testing Cloudflare Workers, including fetch events and compatibility settings.
  * [Developing](https://developers.cloudflare.com/workers/testing/miniflare/developing/): Development tools for Miniflare, including debugger support and live reload for Cloudflare Workers.
  * [Migrations](https://developers.cloudflare.com/workers/testing/miniflare/migrations/): Review migration guides for specific versions of Miniflare.
  * [Storage](https://developers.cloudflare.com/workers/testing/miniflare/storage/): Configure and manage local storage simulators in Miniflare for Workers bindings like KV, R2, and D1.



[PreviousIntegrations](https://developers.cloudflare.com/workers/testing/test-harness/integrations/)[NextGet Started](https://developers.cloudflare.com/workers/testing/miniflare/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
