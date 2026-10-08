---
url: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/
title: Custom rules \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:04.045055+00:00
---

# Custom rules · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)
  4. /Custom load balancing rules



# Custom load balancing rules

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow custom rules workAvailabilityLimitations

Custom load balancing rules let you customize the behavior of your load balancer based on the characteristics of a request.

For example, you can use URL-based routing, or create a rule that selects a pool based on the URI path of an HTTP request.

## How custom rules work

As with [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/), each load balancing custom rule is a combination of two elements: an [expression](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/) and an [action](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/). Expressions define the criteria for an HTTP request to trigger an action. The action tells Cloudflare how to handle the request.

You can [create Load Balancing rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/) whenever you create or edit a load balancer in **Load Balancing**.

When building expressions for Load Balancing rules, refer to [Supported fields and operators](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/) for definitions and usage.

## Availability

By default, non-Enterprise customers have **one** Load Balancing rule **per load balancer hostname**. For more rules, upgrade to [Enterprise ↗︎](https://www.cloudflare.com/enterprise/).

## Limitations

At the moment, you cannot use Load Balancing rules with [Cloudflare Spectrum](https://developers.cloudflare.com/spectrum/about/load-balancer/).

Custom rules can override [Geo steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/) pool mappings for matched requests. Specify different region, country, or data center pools in the rule. Changing only the steering policy does not disable Geo steering. Cloudflare still resolves pools from the configured topology before applying that policy.

Custom rules do work alongside [pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/). Cloudflare evaluates pool sets first, then applies custom rule overrides on top of the result. A pool set that returns a fixed response is the complete response, so custom rules are not evaluated for that request.

[PreviousCNAME flattening for endpoints](https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/)[NextCreate custom rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/load-balancing-rules/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
