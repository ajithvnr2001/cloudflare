---
url: https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/
title: JSON responses and RFC 9457 support for Cloudflare 1xxx errors \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.564806+00:00
---

# JSON responses and RFC 9457 support for Cloudflare 1xxx errors · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 11, 2026

## JSON responses and RFC 9457 support for Cloudflare 1xxx errors

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare-generated 1xxx errors now return structured JSON when clients send `Accept: application/json` or `Accept: application/problem+json`. JSON responses follow [RFC 9457 (Problem Details for HTTP APIs) ↗︎](https://www.rfc-editor.org/rfc/rfc9457), so any HTTP client that understands Problem Details can parse the base members without Cloudflare-specific code.

#### Breaking change

The Markdown frontmatter field `http_status` has been renamed to `status`. Agents consuming Markdown frontmatter should update parsers accordingly.

#### Changes

**JSON format.** Clients sending `Accept: application/json` or `Accept: application/problem+json` now receive a structured JSON object with the same operational fields as Markdown frontmatter, plus RFC 9457 standard members.

**RFC 9457 standard members (JSON only):**

  * `type` — URI pointing to Cloudflare documentation for the specific error code
  * `status` — HTTP status code (matching the response status)
  * `title` — short, human-readable summary
  * `detail` — human-readable explanation specific to this occurrence
  * `instance` — Ray ID identifying this specific error occurrence



**Field renames:**

  * `http_status` -> `status` (JSON and Markdown)
  * `what_happened` -> `detail` (JSON only — Markdown prose sections are unchanged)



**Content-Type mirroring.** Clients sending `Accept: application/problem+json` receive `Content-Type: application/problem+json; charset=utf-8` back; `Accept: application/json` receives `application/json; charset=utf-8`. Same body in both cases.

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

Available now for Cloudflare-generated 1xxx errors.

#### Get started
    
    
    curl -s --compressed -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/1015" | jq .
    
    
    curl -s --compressed -H "Accept: application/problem+json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/1015" | jq .

References:

  * [RFC 9457 — Problem Details for HTTP APIs ↗︎](https://www.rfc-editor.org/rfc/rfc9457)
  * [Cloudflare 1xxx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)


