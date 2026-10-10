---
url: https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/
title: New TCP-based fields available in Rulesets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.329099+00:00
---

# New TCP-based fields available in Rulesets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2025

## New TCP-based fields available in Rulesets

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Build rules based on TCP transport and latency

Cloudflare now provides two new request fields in the Ruleset engine that let you make decisions based on whether a request used TCP and the measured TCP round-trip time between the client and Cloudflare. These fields help you understand protocol usage across your traffic and build policies that respond to network performance. For example, you can distinguish TCP from QUIC traffic or route high latency requests to alternative origins when needed.

* * *

#### New fields

Field | Type | Description  
---|---|---  
`cf.edge.client_tcp` | Boolean | Indicates whether the request used TCP. A value of true means the client connected using TCP instead of QUIC.  
`cf.timings.client_tcp_rtt_msec` | Number | Reports the smoothed TCP round-trip time between the client and Cloudflare in milliseconds. For example, a value of 20 indicates roughly twenty milliseconds of RTT.  
  
Example filter expression:
    
    
    cf.edge.client_tcp && cf.timings.client_tcp_rtt_msec < 100

More information can be found in the Rules language [fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).
