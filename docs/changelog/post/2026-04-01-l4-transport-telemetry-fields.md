---
url: https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/
title: New L4 transport telemetry fields in Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:44.143515+00:00
---

# New L4 transport telemetry fields in Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 1, 2026

## New L4 transport telemetry fields in Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Three new properties are now available on `request.cf` in Workers that expose Layer 4 transport telemetry from the client connection. These properties let your Worker make decisions based on real-time connection quality signals — such as round-trip time and data delivery rate — without requiring any client-side changes.

Previously, this telemetry was only available via the `Server-Timing: cfL4` response header. These new properties surface the same data directly in the Workers runtime, so you can use it for routing, logging, or response customization.

#### New properties

Property | Type | Description  
---|---|---  
`clientTcpRtt` | number | undefined | The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for TCP connections (HTTP/1, HTTP/2). For example, `22`.  
`clientQuicRtt` | number | undefined | The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for QUIC connections (HTTP/3). For example, `42`.  
`edgeL4` | Object | undefined | Layer 4 transport statistics. Contains `deliveryRate` (number) — the most recent data delivery rate estimate for the connection, in bytes per second. For example, `123456`.  
  
#### Example: Log connection quality metrics
    
    
    export default {
      async fetch(request) {
        const cf = request.cf;
    
        const rtt = cf.clientTcpRtt ?? cf.clientQuicRtt ?? 0;
        const deliveryRate = cf.edgeL4?.deliveryRate ?? 0;
        const transport = cf.clientTcpRtt ? "TCP" : "QUIC";
    
        console.log(`Transport: ${transport}, RTT: ${rtt}ms, Delivery rate: ${deliveryRate} B/s`);
    
        const headers = new Headers(request.headers);
        headers.set("X-Client-RTT", String(rtt));
        headers.set("X-Delivery-Rate", String(deliveryRate));
    
        return fetch(new Request(request, { headers }));
      },
    };

For more information, refer to [Workers Runtime APIs: Request](https://developers.cloudflare.com/workers/runtime-apis/request/).
