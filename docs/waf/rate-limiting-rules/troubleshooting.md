---
url: https://developers.cloudflare.com/waf/rate-limiting-rules/troubleshooting/
title: Troubleshoot rate limiting rules \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:46.274380+00:00
---

# Troubleshoot rate limiting rules · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/rate-limiting-rules/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/)
  4. /Troubleshooting



# Troubleshoot rate limiting rules

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/rate-limiting-rules/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSome Workers subrequests are counted as separate requestsRate limiting rules with hostname conditions and Origin Rules ResolutionRate limiting fail-open behavior

## Some Workers subrequests are counted as separate requests

Cloudflare may count Workers subrequests on the same zone as separate requests, which will cause a rate limiting rule to trigger sooner than expected. This behavior happens when the rate limiting rule is configured with [**Also apply rate limiting to cached assets**](https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/#also-apply-rate-limiting-to-cached-assets) set to false.

To prevent this behavior, you must exclude any Workers subrequests coming from the same zone from your rate limiting rule using the [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field. For example, you could add the following sub-expression to your [rate limiting rule expression](https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/#when-incoming-requests-match):
    
    
    and (cf.worker.upstream_zone == "" or cf.worker.upstream_zone != "<YOUR_ZONE>")

The first condition (testing for an empty string) will match direct visitor requests, while the second condition will match subrequests not originating from your zone, effectively excluding subrequests from the same zone from the rate limiting rule.

## Rate limiting rules with hostname conditions and Origin Rules

If you use [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/) to rewrite the `Host` header and your rate limiting rule includes `http.host` in its expression or counting characteristics, the rule may match incoming requests but fail to increment its counter.

This happens because the rate limiting rule expression is evaluated in two phases:

  1. **Request phase** (rule matching): The expression is evaluated against the original request, where `http.host` contains the original hostname. The rule matches as expected.
  2. **Response phase** (counter increment): If the rule uses a [counting expression](https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/#increment-counter-when) or has **Also apply rate limiting to cached assets** turned off, the counter increment happens after the response. At this point, Origin Rules have already rewritten the `Host` header to the new value, so an expression containing the original hostname no longer matches.



As a result, the rule matches requests but never increments the counter, and the rate limit is never enforced.

### Resolution

To fix this, do one of the following:

  * Remove `http.host` conditions from the counting expression and use other fields (such as `http.request.uri.path`) to scope the counter.
  * Update the counting expression to use the rewritten hostname instead of the original hostname.
  * Add both the original and rewritten hostnames to the counting expression using an `or` condition.



## Rate limiting fail-open behavior

Cloudflare rate limiting rules operate in **fail-open mode** (allowing requests through rather than blocking them) during infrastructure overload. When the underlying infrastructure experiences high load, Cloudflare may skip rate counter updates and rate limit enforcement for affected requests rather than blocking legitimate traffic.

There is no customer-visible signal for fail-open events. If a rate limiting rule is not blocking traffic that it should be catching (a false negative) and the rule configuration is correct, infrastructure load at the affected data center may be a factor.

**Per-data-center counting:** Rate limiting counters are maintained per Cloudflare data center. Traffic distributed across many data centers may keep per-data-center rates below the threshold even when the aggregate rate exceeds it. Consider this when setting thresholds for globally distributed traffic.

[PreviousBest practices](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/)[NextOverview](https://developers.cloudflare.com/waf/managed-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/rate-limiting-rules/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
