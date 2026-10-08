---
url: https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/
title: Updating the WAF maximum payload values \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:30.932977+00:00
---

# Updating the WAF maximum payload values · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 5, 2025

## Updating the WAF maximum payload values

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-05-waf-max-payload-size-change/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are reinstating the maximum request-payload size the Cloudflare WAF inspects, with WAF on Enterprise zones inspecting up to 128 KB.

**Key Findings**

On [December 5, 2025](https://developers.cloudflare.com/changelog/2025-12-05-rcs-vuln/), we initially attempted to increase the maximum WAF payload limit to 1 MB across all plans. However, an automatic rollout for all customers proved impractical because the increase led to a surge in false positives for existing managed rules.

This issue was particularly notable within the Cloudflare Managed Ruleset and the Cloudflare OWASP Core Ruleset, impacting customer traffic.

**Impact**

Customers on paid plans can increase the limit to 1 MB for any of their zones by contacting Cloudflare Support. Free zones are already protected up to 1 MB and do not require any action.
