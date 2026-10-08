---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/
title: Allow traffic from search engine bots and other verified bots \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:38.101032+00:00
---

# Allow traffic from search engine bots and other verified bots · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Allow traffic from search engine bots



# Allow traffic from search engine bots

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOther resources

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) challenges requests from a list of countries, but allows traffic from search engine bots — such as Googlebot and Bingbot — and from other [verified bots](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/).

The rule expression uses the [`cf.client.bot`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.client.bot/) field to determine if the request originated from a known good bot or crawler.

  * **When incoming requests match** :

Field | Operator | Value | Logic  
---|---|---|---  
Country | is in | `Mexico`, `United States` | And  
Known Bots | equals | `false` |   
  
If you are using the expression editor:  
`(ip.src.country in {"US" "MX"} and not cf.client.bot)`

  * **Then take action** : _Managed Challenge_




## Other resources

  * [Use case: Challenge bad bots](https://developers.cloudflare.com/waf/custom-rules/use-cases/challenge-bad-bots/)
  * [Cloudflare bot solutions](https://developers.cloudflare.com/bots/)
  * [Troubleshooting: Bing's Site Scan blocked by a WAF managed rule](https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/)
  * [Learning Center: What is a web crawler? ↗︎](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/)



[PreviousAllow traffic from IP addresses in allowlist only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/)[NextAllow traffic from specific countries only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/allow-traffic-from-verified-bots.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
