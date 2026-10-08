---
url: https://developers.cloudflare.com/workers/testing/vitest-integration/
title: Vitest integration \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:57.559125+00:00
---

# Vitest integration · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/vitest-integration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Testing](https://developers.cloudflare.com/workers/testing/)
  4. /Vitest integration



# Vitest integration

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/vitest-integration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

For most users, Cloudflare recommends using the Workers Vitest integration for unit testing Workers and [Pages Functions](https://developers.cloudflare.com/pages/functions/) projects. [Vitest ↗︎](https://vitest.dev/) is a popular JavaScript testing framework featuring a fast watch mode, Jest compatibility, and default TypeScript support. Cloudflare provides the `@cloudflare/vitest-plugin` Vite plugin, which runs your Vitest tests inside the Workers runtime.

The Workers Vitest integration:

  * Supports both **unit tests** and **integration tests**.
  * Provides direct access to Workers runtime APIs and bindings.
  * Implements isolated per-test-file storage.
  * Runs tests fully-locally using [Miniflare ↗︎](https://miniflare.dev/).
  * Leverages Vitest's hot-module reloading for near instant reruns.
  * Supports projects with multiple Workers.

[Write your first test](https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/)

If you use `@cloudflare/vitest-pool-workers`, refer to [Migrate to Vitest plugin](https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/).

[PreviousOverview](https://developers.cloudflare.com/workers/testing/)[NextWrite your first test](https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/vitest-integration/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
