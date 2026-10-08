---
url: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/hash-origin-steering/
title: Hash steering \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:07.381412+00:00
---

# Hash steering · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/hash-origin-steering/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

Concepts[Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/)

  4. /[Local traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/)
  5. /Hash



# Hash

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/hash-origin-steering/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLimitation when using Workers Workaround

**Hash steering** guides Cloudflare to send requests to endpoints based on a combination of [endpoint weights](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights) and previous requests from that IP address. Ensures requests from the same IP address will hit the same endpoint, but actual traffic distribution may differ from endpoint weights.

## Limitation when using Workers

Hash Steering relies on the `x-forwarded-for` header to determine the originating IP address of a request. However, when a [Cloudflare Worker](https://developers.cloudflare.com/workers/) is used in front of a load balancer, this can affect how Hash Steering functions.

When a request originates from a browser, it lacks an `x-forwarded-for` header, but if a Worker proxies the request to a load balancer, the header is populated with the Worker's IP instead of the original client IP. Since the Worker's IP — often a Cloudflare public IP — can change between requests, Hash Steering may direct the same client's requests to different endpoints, leading to inconsistent traffic routing.

### Workaround

To ensure Hash Steering works correctly when using a Worker in front of a Load Balancer, manually set the `x-forwarded-for` header in the Worker to the client's original IP address. By manually setting `x-forwarded-for` to `CF-Connecting-IP`, Hash Steering will function as expected, ensuring traffic consistency for end users.

[PreviousRandom](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/random-origin-steering/)[NextLeast Outstanding Requests](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/least-outstanding-requests-pools/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/traffic-steering/origin-level-steering/hash-origin-steering.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
