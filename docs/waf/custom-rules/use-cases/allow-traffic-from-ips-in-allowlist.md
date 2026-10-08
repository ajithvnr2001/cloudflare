---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/
title: Allow traffic from IP addresses in allowlist only \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:37.701616+00:00
---

# Allow traffic from IP addresses in allowlist only · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Allow traffic from IP addresses in allowlist only



# Allow traffic from IP addresses in allowlist only

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOther resources

This example blocks incoming requests from IP addresses that are not present in an allowlist (defined using an [IP list](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#ip-lists)).

  1. [Create an IP list](https://developers.cloudflare.com/waf/tools/lists/create-dashboard/) with the IP addresses for which you want to allow access.  
For example, create an IP list named `allowed_ips` with one or more IP addresses. For more information on the accepted IP address formats, refer to [IP lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#ip-lists).

  2. [Create a custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocking any requests from IPs not present in the list you created (`allowed_ips` in the current example).

     * **When incoming requests match** :

Field | Operator | Value  
---|---|---  
IP Source Address | is not in list | `allowed_ips`  
  
If you are using the expression editor:  
`(not ip.src in $allowed_ips)`

     * **Then take action** : _Block_

  3. (Optional) Update your expression with any extra filters, like blocking non-allowlisted IPs only for specific URI paths:

Field | Operator | Value | Logic  
---|---|---|---  
IP Source Address | is not in list | `allowed_ips` | And  
URI Path | wildcard | `/admin/*` |   
  
If you are using the expression editor:  
`(not ip.src in $allowed_ips and http.request.uri.path wildcard "/admin/*")`




## Other resources

  * [Use case: Require known IP addresses in site admin area](https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/)
  * [Available skip options](https://developers.cloudflare.com/waf/custom-rules/skip/options/)



[PreviousSkip options](https://developers.cloudflare.com/waf/custom-rules/skip/options/)[NextAllow traffic from search engine bots](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
