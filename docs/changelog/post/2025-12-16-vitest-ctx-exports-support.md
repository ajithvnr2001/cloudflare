---
url: https://developers.cloudflare.com/changelog/post/2025-12-16-vitest-ctx-exports-support/
title: Support for ctx.exports in @cloudflare/vitest-pool-workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:32.011788+00:00
---

# Support for ctx.exports in @cloudflare/vitest-pool-workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-16-vitest-ctx-exports-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 16, 2025

## Support for ctx.exports in @cloudflare/vitest-pool-workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-16-vitest-ctx-exports-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [`@cloudflare/vitest-pool-workers`](https://developers.cloudflare.com/workers/testing/vitest-integration/) package now supports the [`ctx.exports` API](https://developers.cloudflare.com/workers/runtime-apis/context/#exports), allowing you to access your Worker's top-level exports during tests.

You can access `ctx.exports` in unit tests by calling `createExecutionContext()`:
    
    
    import { createExecutionContext } from "cloudflare:test";
    import { it, expect } from "vitest";
    
    it("can access ctx.exports", async () => {
      const ctx = createExecutionContext();
      const result = await ctx.exports.MyEntryPoint.myMethod();
      expect(result).toBe("expected value");
    });

Alternatively, you can import `exports` directly from `cloudflare:workers`:
    
    
    import { exports } from "cloudflare:workers";
    import { it, expect } from "vitest";
    
    it("can access imported exports", async () => {
      const result = await exports.MyEntryPoint.myMethod();
      expect(result).toBe("expected value");
    });

See the [context-exports fixture ↗︎](https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/context-exports) for a complete example.
