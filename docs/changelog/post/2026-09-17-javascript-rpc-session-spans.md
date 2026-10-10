---
url: https://developers.cloudflare.com/changelog/post/2026-09-17-javascript-rpc-session-spans/
title: Workers traces now automatically include JavaScript RPC session spans \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.008971+00:00
---

# Workers traces now automatically include JavaScript RPC session spans · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-17-javascript-rpc-session-spans/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 17, 2026

## Workers traces now automatically include JavaScript RPC session spans

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers traces can now follow JavaScript RPC calls across Worker boundaries and into Durable Objects. Previously, a trace stopped at the caller's RPC boundary. The dashboard now shows the caller-side session and method calls alongside the callee invocation, nested calls, and callbacks into another Worker.

A session span covers the lifetime of a caller-side session and groups calls that reuse it. Individual call spans show each method invocation. Execution colors distinguish the Workers or Durable Object entrypoints involved, while arrows mark outgoing and incoming calls. Together, these details show where time was spent, which calls reused a session, and how returned stubs and callbacks fit into the request.

![A Workers trace of a Worker-to-Worker RPC session, showing the session span, the caller's getCounter and increment call spans, and the callee's invocation and matching call spans](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2878,height=1576,format=webp/_astro/jsrpc-session-spans.DQuwQrpm.png)

Enable tracing with one setting in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/#observability):
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "observability": {
        "traces": {
          "enabled": true
        }
      }
    }
    
    
    [observability.traces]
    enabled = true

Cloudflare records these spans automatically. You do not need to change your application code or add an observability SDK.

For supported spans and attributes, refer to [Spans and attributes](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/).
