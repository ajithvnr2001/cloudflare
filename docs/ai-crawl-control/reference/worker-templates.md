---
url: https://developers.cloudflare.com/ai-crawl-control/reference/worker-templates/
title: Worker templates \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:28.121929+00:00
---

# Worker templates · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/reference/worker-templates/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /Reference
  4. /Worker templates



# Worker templates

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/reference/worker-templates/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewx402 Payment-Gated ProxyRelated

Use [AI Crawl Control analytics](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/) to identify which crawlers are accessing your site, then deploy Worker templates to customize how you handle that traffic.

## x402 Payment-Gated Proxy

The x402-proxy template implements payment-gated access using the [x402 protocol ↗︎](https://www.x402.org/) — an open payment standard built around HTTP 402 (Payment Required). Use it to monetize crawler access, paywall specific routes, or charge bots while letting humans through free.

For setup instructions and Bot Management integration examples, see the [template on GitHub ↗︎](https://github.com/cloudflare/templates/tree/main/x402-proxy-template).

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/x402-proxy-template)

## Related

  * [Bot reference](https://developers.cloudflare.com/ai-crawl-control/reference/bots/) — Detection IDs and user agents for common crawlers
  * [Cloudflare Workers](https://developers.cloudflare.com/workers/) — Build and deploy serverless applications
  * [Workers templates ↗︎](https://github.com/cloudflare/templates) — More templates on GitHub
  * [Pay Per Crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/) — Native Cloudflare integration for monetizing crawler access
  * [x402 payments](https://developers.cloudflare.com/agents/tools/payments/x402/) — Gate resources, charge for MCP tools, add payments to coding agents



[PreviousBot reference](https://developers.cloudflare.com/ai-crawl-control/reference/bots/)[NextGlossary](https://developers.cloudflare.com/ai-crawl-control/reference/glossary/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/reference/worker-templates.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
