---
url: https://developers.cloudflare.com/workers/testing/test-harness/
title: Integration test harness \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:56.661638+00:00
---

# Integration test harness · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/test-harness/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Testing](https://developers.cloudflare.com/workers/testing/)
  4. /Integration test harness



# Integration test harness

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/test-harness/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesGuides

[`createTestHarness()`](https://developers.cloudflare.com/workers/wrangler/api/#createtestharness) is a Wrangler API for integration testing from any Node.js test runner. It runs one or more Workers from [Wrangler](https://developers.cloudflare.com/workers/wrangler/) projects or Vite projects that use the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

[Get started](https://developers.cloudflare.com/workers/testing/test-harness/get-started/) [View complete example](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/create-test-harness-example)

## Features

  * Runs production build output from Wrangler or the Cloudflare Vite plugin
  * Dispatches requests and events to one or more Workers
  * Provides access to bindings and local storage from tests
  * Captures logs and diagnostic output from the Workers runtime



## Guides

### [Configure the test harness](https://developers.cloudflare.com/workers/testing/test-harness/configure/)

Configure Workers, test values, lifecycle hooks, and failure diagnostics.

### [Prepare test state](https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/)

Seed storage, mock outbound requests, and replace bindings.

### [Interact with Workers](https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/)

Test routes, dispatch events, control Workflows, and assert logs.

### [Integrations](https://developers.cloudflare.com/workers/testing/test-harness/integrations/)

Use the test harness with MSW and Playwright.

[PreviousMigrate from unstable_dev](https://developers.cloudflare.com/workers/testing/vitest-integration/migration-guides/migrate-from-unstable-dev/)[NextGet started](https://developers.cloudflare.com/workers/testing/test-harness/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/test-harness/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
