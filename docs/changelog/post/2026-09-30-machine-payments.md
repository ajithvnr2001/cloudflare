---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/
title: Pay for AI inference with Machine Payments \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.016175+00:00
---

# Pay for AI inference with Machine Payments · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-machine-payments/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## Pay for AI inference with Machine Payments

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports Machine Payments in beta. With Machine Payments, clients can use the x402 protocol to pay for eligible inference requests directly from a stablecoin wallet instead of maintaining a prepaid credit balance.

Machine Payments is available for the `/ai/run` endpoint with select open models. To request x402 payment, authenticate with a Cloudflare API token and include the Cloudflare-specific `Payment-Method: x402` header:
    
    
    curl -iX POST "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Payment-Method: x402" \
      --header "Content-Type: application/json" \
      --data '{
        "model": "z-ai/glm-4.7-flash",
        "input": {
          "messages": [
            {
              "role": "user",
              "content": "What is Cloudflare?"
            }
          ]
        }
      }'

An x402-compatible client handles the payment challenge, signs an authorization from the client's wallet, and retries the request. Machine Payments currently requires customers to be based in the United States and have a credit card on file.

For prerequisites, eligible models, and transaction details, refer to [Machine Payments (x402)](https://developers.cloudflare.com/ai-gateway/features/machine-payments/).
