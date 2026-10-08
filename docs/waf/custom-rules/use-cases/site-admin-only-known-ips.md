---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/
title: Require known IP addresses in site admin area \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:39.463160+00:00
---

# Require known IP addresses in site admin area · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Require known IP addresses in site admin area



# Require known IP addresses in site admin area

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOther resources

If an attack compromises the administrative area of your website, the consequences can be severe. With custom rules, you can protect your site's admin area by blocking requests for access to admin paths that do not come from a known IP address.

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) limits access to the WordPress admin area, `/wp-admin/`, by blocking requests that do not originate from a specified set of IP addresses:

  * **When incoming requests match** :

Field | Operator | Value | Logic  
---|---|---|---  
IP Source Address | is not in | `10.20.30.40` `192.168.1.0/24` | And  
URI Path | wildcard | `/wp-admin/*` |   
  
If you are using the expression editor:  
`(not ip.src in {10.20.30.40 192.168.1.0/24} and http.request.uri.path wildcard "/wp-admin/*")`

  * **Then take action** : _Block_




## Other resources

  * [Use case: Allow traffic from IP addresses in allowlist only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/)



[PreviousRequire a specific cookie](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/)[NextRequire specific HTTP headers](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/site-admin-only-known-ips.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
