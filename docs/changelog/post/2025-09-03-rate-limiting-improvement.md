---
url: https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/
title: Introducing new headers for rate limiting on Cloudflare's API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.272670+00:00
---

# Introducing new headers for rate limiting on Cloudflare's API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 3, 2025

## Introducing new headers for rate limiting on Cloudflare's API

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's API now supports rate limiting headers using the pattern developed by the [IETF draft on rate limiting ↗︎](https://ietf-wg-httpapi.github.io/ratelimit-headers/draft-ietf-httpapi-ratelimit-headers.html). This allows API consumers to know how many more calls are left until the rate limit is reached, as well as how long you will need to wait until more capacity is available.

Our SDKs automatically work with these new headers, backing off when rate limits are approached. There is no action required for users of the latest Cloudflare SDKs to take advantage of this.

As always, if you need any help with rate limits, please contact Support.

#### Changes

#### New Headers

**Headers that are always returned:**

  * `Ratelimit`: List of service limit items, composed of the limit name, the remaining quota (`r`) and the time next window resets (`t`). For example: `"default";r=50;t=30`
  * `Ratelimit-Policy`: List of quota policy items, composed of the policy name, the total quota (`q`) and the time window the quota applies to (`w`). For example: `"burst";q=100;w=60`



**Returned only when a rate limit has been reached (error code: 429):**

  * Retry-After: Number of Seconds until more capacity is available, rounded up



#### SDK Back offs

  * All of Cloudflare's latest SDKs will automatically respond to the headers, instituting a backoff when limits are approached.



#### GraphQL and Edge APIs

These new headers and back offs are only available for Cloudflare REST APIs, and will not affect GraphQL.

#### For more information

  * [Rate limits at Cloudflare ↗︎](https://developers.cloudflare.com/fundamentals/api/reference/limits/)


