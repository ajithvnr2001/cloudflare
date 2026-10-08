---
url: https://developers.cloudflare.com/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/
title: Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:06.244729+00:00
---

# Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 13, 2025

## Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now debug your Workers tests with our [Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/) by running the following command:
    
    
    vitest --inspect --no-file-parallelism

Attach a debugger to the port 9229 and you can start stepping through your Workers tests. This is available with `@cloudflare/vitest-pool-workers` v0.7.5 or later.

Learn more in our [documentation](https://developers.cloudflare.com/workers/testing/vitest-integration/debugging/).
