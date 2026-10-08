---
url: https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/
title: AI Gateway adds DeepSeek as a Provider \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:01.634524+00:00
---

# AI Gateway adds DeepSeek as a Provider · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 2, 2025

## AI Gateway adds DeepSeek as a Provider

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-07-aig-provider-deepseek/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**AI Gateway**](https://developers.cloudflare.com/ai-gateway/) now supports [**DeepSeek**](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/), including their cutting-edge DeepSeek-V3 model. With this addition, you have even more flexibility to manage and optimize your AI workloads using AI Gateway. Whether you're leveraging DeepSeek or other providers, like OpenAI, Anthropic, or [Workers AI](https://developers.cloudflare.com/workers-ai/), AI Gateway empowers you to:

  * **Monitor** : Gain actionable insights with analytics and logs.
  * **Control** : Implement caching, rate limiting, and fallbacks.
  * **Optimize** : Improve performance with feedback and evaluations.

![AI Gateway adds DeepSeek as a provider](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=131,format=webp/_astro/deepseek.hirkr3rv.png)

To get started, simply update the base URL of your DeepSeek API calls to route through AI Gateway. Here's how you can send a request using cURL:

Example fetch requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \
     --header 'content-type: application/json' \
     --header 'Authorization: Bearer DEEPSEEK_TOKEN' \
     --data '{
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": "What is Cloudflare?"
            }
        ]
    }'

For detailed setup instructions, see our [DeepSeek provider documentation](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/).
