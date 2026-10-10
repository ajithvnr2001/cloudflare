---
url: https://developers.cloudflare.com/changelog/post/2026-03-17-collect-log-payload-header/
title: Log AI Gateway request metadata without storing payloads \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.289126+00:00
---

# Log AI Gateway request metadata without storing payloads · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-17-collect-log-payload-header/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 17, 2026

## Log AI Gateway request metadata without storing payloads

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports the `cf-aig-collect-log-payload` header, which controls whether request and response bodies are stored in logs. By default, this header is set to `true` and payloads are stored alongside metadata. Set this header to `false` to skip payload storage while still logging metadata such as token counts, model, provider, status code, cost, and duration.

This is useful when you need usage metrics but do not want to persist sensitive prompt or response data.
    
    
    curl https://gateway.ai.cloudflare.com/v1/$ACCOUNT_ID/$GATEWAY_ID/openai/chat/completions \
      --header "Authorization: Bearer $TOKEN" \
      --header 'Content-Type: application/json' \
      --header 'cf-aig-collect-log-payload: false' \
      --data '{
        "model": "gpt-4o-mini",
        "messages": [
          {
            "role": "user",
            "content": "What is the email address and phone number of user123?"
          }
        ]
      }'

For more information, refer to [Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/#collect-log-payload-cf-aig-collect-log-payload).
