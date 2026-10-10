---
url: https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/
title: Reject busy synchronous inference requests \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.023293+00:00
---

# Reject busy synchronous inference requests · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 17, 2026

## Reject busy synchronous inference requests

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `rejectIfBusy` option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue.

Pass the option as the third argument to the Workers AI binding:
    
    
    const response = await env.AI.run(
    	"@cf/google/gemma-4-26b-a4b-it",
    	{
    		messages: [{ role: "user", content: "Explain capacity queues." }],
    	},
    	{ rejectIfBusy: true },
    );
    
    
    const response = await env.AI.run(
    	"@cf/google/gemma-4-26b-a4b-it",
    	{
    		messages: [{ role: "user", content: "Explain capacity queues." }],
    	},
    	{ rejectIfBusy: true },
    );

For the native REST API, add the option to the request body:
    
    
    curl --request POST \
      --url "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "messages": [{ "role": "user", "content": "Explain capacity queues." }],
        "options": { "rejectIfBusy": true }
      }'

Refer to [Reject busy requests](https://developers.cloudflare.com/workers-ai/features/reject-if-busy/) for OpenAI-compatible usage and error behavior.
