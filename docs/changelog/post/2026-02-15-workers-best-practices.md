---
url: https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/
title: New Best Practices guide for Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:37.160865+00:00
---

# New Best Practices guide for Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 15, 2026

## New Best Practices guide for Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-15-workers-best-practices/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new [Workers Best Practices](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/) guide provides opinionated recommendations for building fast, reliable, observable, and secure Workers. The guide draws on production patterns, Cloudflare internal usage, and best practices observed from developers building on Workers.

Key guidance includes:

  * **Keep your compatibility date current and enable`nodejs_compat`** — Ensure you have access to the latest runtime features and Node.js built-in modules.


    
    
    {
    	"name": "my-worker",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"compatibility_flags": ["nodejs_compat"],
    }
    
    
    name = "my-worker"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "nodejs_compat" ]

  * **Generate binding types with`wrangler types`** — Never hand-write your `Env` interface. Let Wrangler generate it from your actual configuration to catch mismatches at compile time.
  * **Stream request and response bodies** — Avoid buffering large payloads in memory. Use `TransformStream` and `pipeTo` to stay within the 128 MB memory limit and improve time-to-first-byte.
  * **Use bindings, not REST APIs** — Bindings to KV, R2, D1, Queues, and other Cloudflare services are direct, in-process references with no network hop and no authentication overhead.
  * **Use Queues and Workflows for background work** — Move long-running or retriable tasks out of the critical request path. Use Queues for simple fan-out and buffering, and Workflows for multi-step durable processes.
  * **Enable Workers Logs and Traces** — Configure observability before deploying to production so you have data when you need to debug.
  * **Avoid global mutable state** — Workers reuse isolates across requests. Storing request-scoped data in module-level variables causes cross-request data leaks.
  * **Always`await` or `waitUntil` your Promises** — Floating promises cause silent bugs and dropped work.
  * **Use Web Crypto for secure token generation** — Never use `Math.random()` for security-sensitive operations.



To learn more, refer to [Workers Best Practices](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/).
