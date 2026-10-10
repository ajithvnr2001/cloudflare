---
url: https://developers.cloudflare.com/changelog/post/2026-07-31-wrangler-startup-profile-summary/
title: Inspect Worker startup performance with Wrangler \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.948711+00:00
---

# Inspect Worker startup performance with Wrangler · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-31-wrangler-startup-profile-summary/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 31, 2026

## Inspect Worker startup performance with Wrangler

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`wrangler check startup` now reports your Worker's raw and compressed bundle sizes. It also summarizes local CPU activity during startup directly in your terminal.

Large bundles and costly startup work can introduce cold-start latency, so use this command to find code and large dependencies that slow your Worker before it handles requests.

The summary includes sampled, active, garbage collection, and idle time. Wrangler continues to save a `.cpuprofile` file for detailed flamegraph analysis in Chrome DevTools or VS Code.
    
    
    ⛅️ wrangler 4.116.0
    ───────────────────────────────────────────────
    ├ Building your Worker
    │ Worker Built! 🎉
    │
    ├ Analysing
    │ Startup phase analysed
    │
    │ Bundle: 7171.25 KiB / gzip: 2197.00 KiB
    │
    │ Local startup profile:
    │   Profile window: 70.3 ms
    │   Sampled time: 70.3 ms
    │   Active: 38.5 ms (including 3.7 ms garbage collection)
    │   Idle: 31.8 ms
    │   Samples: 36
    │
    │ CPU Profile has been written to worker-startup.cpuprofile. Load it into the Chrome DevTools profiler (or directly in VSCode) to view a flamegraph.
    │
    │ Note that the CPU Profile was measured on your Worker running locally on your machine, which has a different CPU than when your Worker runs on Cloudflare.
    │
    │ As such, CPU Profile can be used to understand where time is spent at startup, but the overall startup time in the profile should not be expected to exactly match what your Worker's startup time will be when deploying to Cloudflare.

The profile runs locally, so its duration will differ from startup time on Cloudflare. For authoritative startup time, deploy your Worker or upload a version.

Available in Wrangler version 4.116.0 or later. For more information, refer to [`wrangler check startup`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#startup).
