---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-worker-subrequests/
title: Block Worker subrequests from other zones \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:38.654735+00:00
---

# Block Worker subrequests from other zones · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-worker-subrequests/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Block Worker subrequests from other zones



# Block Worker subrequests from other zones

Last updated Oct 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-worker-subrequests/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Block subrequests from a specific zone Block all Worker subrequests except from your own zone

The [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field identifies the zone that spawned a [Workers subrequest](https://developers.cloudflare.com/workers/platform/limits/#subrequests). You can use this field in [custom rules](https://developers.cloudflare.com/waf/custom-rules/) to mitigate unwanted Worker traffic.

Caution

Do not use the [`CF-Worker`](https://developers.cloudflare.com/fundamentals/reference/http-headers/#cf-worker) request header in WAF rules. The header is added after rule evaluation, so it is not available when WAF rules run. Use the `cf.worker.upstream_zone` field instead, which holds the same value.

### Block subrequests from a specific zone

  * **When incoming requests match** :

If you are using the expression editor:  
`(cf.worker.upstream_zone eq "example.com")`

  * **Then take action** : _Block_




### Block all Worker subrequests except from your own zone

  * **When incoming requests match** :

If you are using the expression editor:  
`(not cf.worker.upstream_zone in {"" "your-zone.com"})`

  * **Then take action** : _Block_




The empty string matches requests that did not come from a Worker, so this expression only blocks subrequests from other zones. Direct visitor traffic is not affected.

[PreviousBlock traffic from specific countries](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/)[NextBuild a sequence rule within custom rules](https://developers.cloudflare.com/waf/custom-rules/use-cases/sequence-custom-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/block-worker-subrequests.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
