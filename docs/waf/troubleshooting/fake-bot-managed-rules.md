---
url: https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/
title: Fake bot detection blocking legitimate requests \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:49.360136+00:00
---

# Fake bot detection blocking legitimate requests · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Troubleshooting
  4. /Fake bot detection blocking legitimate requests



# Fake bot detection blocking legitimate requests

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFake bot rulesCommon false positive scenariosResolution

The Cloudflare Managed Ruleset includes rules that detect requests impersonating well-known bots such as Googlebot and Bingbot. These rules compare the request's `User-Agent` header against known bot patterns and then verify the source using methods like reverse DNS lookup or IP validation. If the `User-Agent` matches a known bot but the source cannot be verified, the rule flags the request as a fake bot.

## Fake bot rules

The following table lists the fake bot detection rules in the Cloudflare Managed Ruleset:

Rule name | Rule ID  
---|---  
Anomaly:Header:User-Agent - Fake Google Bot | ...6aa0bef8  
Anomaly:Header:User-Agent - Fake Bing or MSN Bot | ...c12cf9c8  
  
## Common false positive scenarios

Fake bot rules may trigger false positives for legitimate services that share infrastructure or user agent patterns with known bots but use different IP ranges. Common examples include:

  * **Google Cloud services** : Services such as Google Cloud Workflows or Cloud Functions may send requests with a Google-related `User-Agent` header from IP addresses outside the standard Googlebot range. These requests fail the IP verification check and are flagged as fake Google bots.
  * **Bing Webmaster Tools Site Scan** : Site Scan does not use the same IP range as Bingbot, causing the fake Bing bot rule to trigger. For specific guidance on this scenario, refer to [Bing's Site Scan blocked by a managed rule](https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/).
  * **Monitoring and testing tools** : Third-party uptime monitors or automated testing tools that set a bot-like `User-Agent` header may also be flagged.



## Resolution

If a fake bot rule is blocking legitimate traffic, create an [exception](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/) to skip the specific managed rule for the affected requests.

When defining the exception expression, use request properties that identify the legitimate traffic without broadly disabling the rule. For example:

  * Filter by source IP address or IP range if the service uses a known set of addresses.
  * Filter by a specific URI path if the service only accesses certain endpoints.
  * Filter by ASN if the service originates from a specific network.



The exception must appear in the rules list before the rule that executes the Cloudflare Managed Ruleset, or it will have no effect.

For instructions on creating exceptions, refer to [Create exceptions](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/).

[PreviousBing's Site Scan blocked by a managed rule](https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/)[NextIssues sharing to Facebook](https://developers.cloudflare.com/waf/troubleshooting/facebook-sharing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/troubleshooting/fake-bot-managed-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
