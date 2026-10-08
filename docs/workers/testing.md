---
url: https://developers.cloudflare.com/workers/testing/
title: Testing \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:53.915563+00:00
---

# Testing · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Testing



# Testing

Last updated Jul 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUnit testsIntegration tests

The Workers platform provides complementary tools for testing different parts of your application. For most projects, use the [Workers Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/) for unit tests and the [`createTestHarness()`](https://developers.cloudflare.com/workers/testing/test-harness/) API for integration tests.

## Unit tests

Use the [Workers Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/) for fast feedback while testing individual functions and modules. Tests run inside the Workers runtime, so your test code can access bindings and runtime APIs directly.

The Workers Vitest integration provides:

  * Fast feedback while testing individual functions and modules.
  * Direct assertions against binding state, such as values written to KV, R2, D1, or Durable Objects.
  * Direct calls to Durable Objects and other runtime APIs.



To set up unit tests, refer to [Write your first Vitest test](https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/).

## Integration tests

Use the [`createTestHarness()`](https://developers.cloudflare.com/workers/testing/test-harness/) API to exercise one or more Workers as a whole and test how they interact with each other and with external services.

The integration test harness provides:

  * Confidence from exercising production Worker builds.
  * Coverage through configured HTTP routes across Workers.
  * Compatibility with any Node.js test runner and tools such as Playwright or MSW.



To set up integration tests, refer to [Get started with the integration test harness](https://developers.cloudflare.com/workers/testing/test-harness/get-started/).

[PreviousSource maps and stack traces](https://developers.cloudflare.com/workers/observability/source-maps/)[NextOverview](https://developers.cloudflare.com/workers/testing/vitest-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
