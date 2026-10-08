---
url: https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/
title: Request timeouts and retries with AI Gateway \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:02.521530+00:00
---

# Request timeouts and retries with AI Gateway · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 6, 2025

## Request timeouts and retries with AI Gateway

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-05-aig-request-handling/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway adds additional ways to handle requests - [Request Timeouts](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-timeouts) and [Request Retries](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries), making it easier to keep your applications responsive and reliable.

Timeouts and retries can be used on both the [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) or directly to a [supported provider](https://developers.cloudflare.com/ai-gateway/usage/providers/).

**Request timeouts** A [request timeout](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-timeouts) allows you to trigger [fallbacks](https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/) or a retry if a provider takes too long to respond.

To set a request timeout directly to a provider, add a `cf-aig-request-timeout` header.

Provider-specific endpoint examplebash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/workers-ai/@cf/meta/llama-3.1-8b-instruct \
     --header 'Authorization: Bearer {cf_api_token}' \
     --header 'Content-Type: application/json' \
     --header 'cf-aig-request-timeout: 5000'
     --data '{"prompt": "What is Cloudflare?"}'

**Request retries** A [request retry](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries) automatically retries failed requests, so you can recover from temporary issues without intervening.

To set up request retries directly to a provider, add the following headers:

  * cf-aig-max-attempts (number)
  * cf-aig-retry-delay (number)
  * cf-aig-backoff ("constant" | "linear" | "exponential)


