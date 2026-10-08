---
url: https://developers.cloudflare.com/monetization-gateway/
title: Monetization Gateway \u00b7 Cloudflare Monetization Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:21.778565+00:00
---

# Monetization Gateway · Cloudflare Monetization Gateway docs

> Source: https://developers.cloudflare.com/monetization-gateway/

  1. [Home](https://developers.cloudflare.com/)
  2. /Monetization Gateway



# Monetization Gateway

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/monetization-gateway/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProtect resourcesUnderstand the payment flowContinue setup

Closed beta

Monetization Gateway is in closed beta. Request access in the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/monetize/monetization-gateway).

Monetization Gateway applies [x402](https://developers.cloudflare.com/agents/tools/payments/x402/) payment requirements to matching traffic. You define the shape of therequest to match, how much to charge for it, and the receiving wallet.

Use Monetization Gateway to protect APIs, Model Context Protocol (MCP) tools, sites, and datasets. Buyers and sellers must be based in the United States.

## Protect resources

You can match requests by URL, headers, query parameters, or caller attributes. For example, payment rules can charge every caller or only verified bots.

Payments happen within the HTTP request flow. Buyers simply sign a cryptographic payment authorization, no need for a checkout redirect or separate payment API call.

## Understand the payment flow

  1. A buyer requests a protected resource.
  2. Monetization Gateway returns payment requirements.
  3. The buyer signs an authorization and retries the request.
  4. Monetization Gateway verifies the authorized payment is valid.
  5. Your origin server receives the verified payment, produces a response.
  6. The gateway settles the payment through the Coinbase x402 Facilitator.
  7. The buyer receives the requested resource.



For fixed pricing, the gateway settles the authorized signed amount. For variable pricing, your origin reports the actual amount.

For request and response examples, refer to [x402 protocol](https://developers.cloudflare.com/monetization-gateway/x402/). To implement a buyer, refer to [x402 payments](https://developers.cloudflare.com/agents/tools/payments/x402/).

## Continue setup

  * [Eligibility](https://developers.cloudflare.com/monetization-gateway/eligibility/)
  * [Get started](https://developers.cloudflare.com/monetization-gateway/get-started/)
  * [x402 protocol](https://developers.cloudflare.com/monetization-gateway/x402/)
  * [Configuration](https://developers.cloudflare.com/monetization-gateway/configuration/)



[NextEligibility](https://developers.cloudflare.com/monetization-gateway/eligibility/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/monetization-gateway/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
