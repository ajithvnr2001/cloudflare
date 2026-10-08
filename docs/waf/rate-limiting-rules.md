---
url: https://developers.cloudflare.com/waf/rate-limiting-rules/
title: Rate limiting rules \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:45.378116+00:00
---

# Rate limiting rules · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/rate-limiting-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Rate limiting rules



# Rate limiting rules

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/rate-limiting-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Rate limiting rules allow you to define rate limits for requests matching an expression, and the action to perform when those rate limits are reached. Use rate limiting rules to prevent abuse of your websites and APIs — for example, to protect a login endpoint from brute-force attacks or to cap how many API calls a single client can make in a given time window.

Were you blocked from accessing a website?

If you are a visitor who received an error while trying to access a website, please refer to the [error 1015 documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015).

In the [new security dashboard](https://developers.cloudflare.com/security/), rate limiting rules are one of the available types of [security rules](https://developers.cloudflare.com/security/rules/). Security rules perform security-related actions on incoming requests that match specified filters.

Some Enterprise customers can create [rate limiting rulesets](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/) at the account level that they can deploy to multiple Enterprise zones.

## Rule parameters

Like other rules evaluated by Cloudflare's [Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/), rate limiting rules have the following basic parameters:

  * An [expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/) that specifies the criteria you are matching traffic on using the [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/).
  * An [action](https://developers.cloudflare.com/ruleset-engine/rules-language/actions/) that specifies what to perform when there is a match for the rule and any additional conditions are met. In the case of rate limiting rules, the action occurs when the rate reaches the specified limit.



Besides these two parameters, rate limiting rules require the following additional parameters:

  * **Characteristics** : The set of parameters that define how Cloudflare tracks the rate for this rule.
  * **Period** : The period of time to consider (in seconds) when evaluating the rate.
  * **Requests per period** : The number of requests over the period of time that will trigger the rate limiting rule.
  * **Duration** (or mitigation timeout): Once the rate is reached, the rate limiting rule blocks further requests for the period of time defined in this field.
  * **Action behavior** : By default, Cloudflare will apply the rule action for the configured duration (or mitigation timeout), regardless of the request rate during this period. Some Enterprise customers can configure the rule to [throttle requests](https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/#with-the-following-behavior) over the maximum rate, allowing incoming requests when the rate is lower than the configured limit.



Refer to [Rate limiting parameters](https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/) for more information on mandatory and optional parameters.

Refer to [How Cloudflare determines the request rate](https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/) to learn how Cloudflare uses the parameters above when determining the rate of incoming requests.

## Interaction with other app security features

If you are using several app security features like custom rules, Managed Rules, and Super Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to [Security features interoperability](https://developers.cloudflare.com/waf/feature-interoperability/) for more information.

## Important remarks

  * Rate limiting rules are evaluated in order, and some actions like _Block_ will stop the evaluation of other rules. For more details on actions and their behavior, refer to [Actions](https://developers.cloudflare.com/ruleset-engine/rules-language/actions/).

  * Rate limiting rules are not designed to allow a precise number of requests to reach your origin server. There may be a delay of up to a few seconds between detecting a request and updating rate counters. Due to this delay, excess requests could still reach the origin before Cloudflare enforces a mitigation action such as blocking or challenging. For more information on how counters work, including their per-data-center scope, refer to [Request rate calculation](https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/).

  * Applying rate limiting rules to verified bots might affect Search Engine Optimization (SEO). For more information, refer to [Improve SEO](https://developers.cloudflare.com/fundamentals/performance/improve-seo/).




* * *

## Availability

Feature | Free | Pro | Business | Enterprise with app security | Enterprise with Advanced Rate Limiting  
---|---|---|---|---|---  
Available fields  
in rule expression | Path, [Verified Bot](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.verified_bot/) | Host, URI, Path, Full URI, Query, Verified Bot | Host, URI, Path, Full URI, Query, Method, Source IP, User Agent, Verified Bot | General request fields, request header fields, Verified Bot, Bot Management fields1 | General request fields, request header fields, Verified Bot, Bot Management fields1, request body fields2  
Cache exclusion | No | No | Yes | Yes | Yes  
Counting characteristics | IP | IP | IP, IP with NAT support | IP, IP with NAT support | IP, IP with NAT support, Query, Host, Headers, Cookie, ASN, Country, Path, JA3/JA4 Fingerprint1, JSON field value2, Body2, Form input value2, Custom  
Custom counting expression | No | No | Yes | Yes | Yes  
Available fields  
in counting expression | N/A | N/A | All rule expression fields, Response code, Response headers | All rule expression fields, Response code, Response headers | All rule expression fields, Response code, Response headers  
Counting model | Number of requests | Number of requests | Number of requests | Number of requests | Number of requests, [complexity score](https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/#complexity-based-rate-limiting)  
Rate limiting  
action behavior | Perform action during mitigation period | Perform action during mitigation period | Perform action during mitigation period | Perform action during mitigation period, Throttle requests above rate with block action | Perform action during mitigation period, Throttle requests above rate with block action  
Counting periods | 10 s | All supported values up to 1 min3 | All supported values up to 10 min3 | All supported values up to 65,535 s3 | All supported values up to 65,535 s3  
Mitigation timeout periods | 10 s | All supported values up to 1 h3 | All supported values up to 1 day3 | All supported values up to 1 day3 4 | All supported values up to 1 day3 4  
Number of rules | 1 | 2 | 5 | 1005 | 100  
  
Footnotes

1: Only available to Enterprise customers who have purchased [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/).

2: Availability depends on your WAF plan.

3: List of supported counting/mitigation period values in seconds:  
10, 15, 20, 30, 40, 45, 60 (1 min), 90, 120 (2 min), 180 (3 min), 240 (4 min), 300 (5 min), 480, 600 (10 min), 900, 1200 (20 min), 1800, 2400, 3600 (1 h), 65535, 86400 (1 day).  
Not all values are available on all plans.

4: Enterprise customers can specify a custom mitigation timeout period via API.

5: Enterprise customers must have application security on their contract to get access to rate limiting rules. The number of rules depends on the exact contract terms.

## Footnotes

  1. Only available to Enterprise customers who have purchased [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/). ↩ ↩2 ↩3

  2. Availability depends on your WAF plan. ↩ ↩2 ↩3 ↩4

  3. Supported period values in seconds:  
10, 15, 20, 30, 40, 45, 60 (1 min), 90, 120 (2 min), 180 (3 min), 240 (4 min), 300 (5 min), 480, 600 (10 min), 900, 1200 (20 min), 1800, 2400, 3600 (1 h), 65535, 86400 (1 day). ↩ ↩2 ↩3 ↩4 ↩5 ↩6 ↩7 ↩8

  4. Enterprise customers can specify a custom mitigation timeout period via API. ↩ ↩2

  5. Enterprise customers must have application security on their contract to get access to rate limiting rules. The number of rules depends on the exact contract terms. ↩




Note

Enterprise customers can preview this product as a [non-contract service](https://developers.cloudflare.com/billing/understand/preview-services/), which provides full access, free of metered usage fees, limits, and certain other restrictions.

## Next steps

Refer to the following resources:

  * [Create a rate limiting rule in the dashboard for a zone](https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/)
  * [Create a rate limiting rule via API for a zone](https://developers.cloudflare.com/waf/rate-limiting-rules/create-api/)



For Terraform examples, refer to [Rate limiting rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/).

* * *

## Related resources

  * [Learning Center: What is rate limiting? ↗︎](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)

  * [Cloudflare Rate Limiting (previous version, no longer available)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/): Documentation for the previous version of rate limiting rules (billed based on usage).




[PreviousCustom rulesets](https://developers.cloudflare.com/waf/custom-rules/custom-rulesets/)[NextRequest rate calculation](https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/rate-limiting-rules/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
