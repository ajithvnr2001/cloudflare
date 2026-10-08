---
url: https://developers.cloudflare.com/changelog/post/2026-04-27-structured-responses-for-5xx-errors/
title: Structured error responses for Cloudflare 5xx errors \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:49.827116+00:00
---

# Structured error responses for Cloudflare 5xx errors · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-27-structured-responses-for-5xx-errors/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 27, 2026

## Structured error responses for Cloudflare 5xx errors

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-27-structured-responses-for-5xx-errors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare-generated 5xx error responses now return structured JSON and Markdown when agents request them, matching the format already available for 1xxx errors. Responses follow [RFC 9457 (Problem Details for HTTP APIs) ↗︎](https://www.rfc-editor.org/rfc/rfc9457) and include a `Retry-After` HTTP header on retryable codes.

#### Changes

**5xx coverage.** Ten Cloudflare-generated error codes (500, 502, 504, 520-526) now serve structured responses. These are errors Cloudflare itself generates when it cannot reach or understand the origin server. Origin-generated 5xx responses that Cloudflare passes through are not affected.

**Fault attribution.** The `error_category` field tells agents where the fault lies:

  * `origin` (502, 504, 520-524) — the origin server is responsible. Transient; retry with the backoff in `retry_after`.
  * `cloudflare` (500) — Cloudflare's fault, not the website or the request. Short retry.
  * `ssl` (525, 526) — the origin's TLS configuration is broken. Do not retry.



**Retry-After header.** Retryable codes (500, 502, 504, 520-524) include a `Retry-After` HTTP header matching the `retry_after` body field. Non-retryable codes (525, 526) do not include the header.

#### Negotiation behavior

Request header sent | Response format  
---|---  
`Accept: application/json` | JSON (`application/json` content type)  
`Accept: application/problem+json` | JSON (`application/problem+json` content type)  
`Accept: application/json, text/markdown;q=0.9` | JSON  
`Accept: text/markdown` | Markdown  
`Accept: text/markdown, application/json` | Markdown (equal `q`, first-listed wins)  
`Accept: */*` | HTML (default)  
  
#### Availability

Available now for all zones on all plans.

#### Get started

Get JSON response for error 522:
    
    
    curl -s --compressed -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/522" | jq .

Check presence of the `Retry-After` HTTP header associated with the JSON response for error 521:
    
    
    curl -s --compressed -D - -o /dev/null -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/521" | grep -i retry-after

References:

  * [RFC 9457 — Problem Details for HTTP APIs ↗︎](https://www.rfc-editor.org/rfc/rfc9457)
  * [Cloudflare 5xx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)


