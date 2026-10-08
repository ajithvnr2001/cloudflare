---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-http-ports/
title: Require specific HTTP ports \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:39.263496+00:00
---

# Require specific HTTP ports · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-http-ports/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Require specific HTTP ports



# Require specific HTTP ports

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-http-ports/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

By default, Cloudflare allows requests on a [number of different HTTP ports](https://developers.cloudflare.com/fundamentals/reference/network-ports/).

You can target requests based on their HTTP port with the [`cf.edge.server_port`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.server_port/) field. Use the `in` [comparison operator](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#comparison-operators) to target a set of ports.

This example [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) blocks requests to `www.example.com` that are not on ports `80` or `443`:

  * **When incoming requests match** :

Use the expression editor:  
`(http.host eq "www.example.com" and not cf.edge.server_port in {80 443})`

  * **Then take action** : _Block_




Open server ports and blocked traffic

Due to the nature of Cloudflare's anycast network, ports other than `80` and `443` will be open so that Cloudflare can serve traffic for other customers on these ports. In general, Cloudflare makes available several different products on [Cloudflare IPs ↗︎](https://www.cloudflare.com/ips), so you can expect tools like Netcat and security scanners to report these non-standard ports as open in specific conditions. If you have questions on security compliance, review [Cloudflare's certifications and compliance resources ↗︎](https://www.cloudflare.com/en-gb/trust-hub/compliance-resources/) and contact your Cloudflare enterprise account manager for more information.

Custom rules and WAF Managed Rules can block traffic at the application layer (layer 7 in the [OSI model ↗︎](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)), preventing HTTP/HTTPS requests over non-standard ports from reaching the origin server.

[PreviousRequire specific HTTP headers](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/)[NextStop R-U-Dead-Yet? (R.U.D.Y.) attacks](https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/require-specific-http-ports.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
