---
url: https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/
title: Error page types \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:48.652668+00:00
---

# Error page types · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/)

  4. /Reference
  5. /Error page types



# Error page types

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Page type | Description | API identifier  
---|---|---  
WAF block | The page displayed when visitors are blocked by a [Web Application Firewall](https://developers.cloudflare.com/waf/) rule. This page returns a `403` status code. | `waf_block`  
IP/Country block | The page displayed when a request originates from a [blocked IP address or country](https://developers.cloudflare.com/waf/tools/ip-access-rules/). This page returns a `403` status code. | `ip_block`  
IP/Country challenge | Presents a challenge to visitors from specified IP addresses or countries. This page returns a `403` status code. For more information, refer to [IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/). | `country_challenge`  
500 class errors | 500 class error pages are displayed when a web server is unable to process a request. For more information, refer to [Cloudflare 5xx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/). | `500_errors`  
1000 class errors | 1000 class error pages are displayed when a domain’s configuration, security settings, or origin setup prevents Cloudflare from completing a request. For more information, refer to [Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/). | `1000_errors`  
Managed challenge / I'm Under Attack Mode | Presents different types of challenges to a visitor depending on the nature of their request and your security settings. This page returns a `403` status code. For more information, refer to [Under Attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/). | `managed_challenge`  
Rate limiting block | Displayed to visitors when they have been blocked by a [rate limiting rule](https://developers.cloudflare.com/waf/rate-limiting-rules/). This page returns a `429` status code. | `ratelimit_block`  
  
[PreviousError tokens](https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/)[NextTroubleshooting](https://developers.cloudflare.com/rules/custom-errors/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/custom-errors/reference/error-page-types.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
