---
url: https://developers.cloudflare.com/waf/managed-rules/troubleshooting/
title: Troubleshoot managed rules \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:45.434688+00:00
---

# Troubleshoot managed rules · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)
  4. /Troubleshooting



# Troubleshoot managed rules

Last updated Sep 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTroubleshoot false positives Additional recommendationsTroubleshoot false negatives Additional recommendations

By default, WAF's managed rulesets are compatible with most websites and web applications. However, false positives and false negatives may occur:

  * **False positives** : Legitimate requests detected and mitigated as malicious.
  * **False negatives** : Malicious requests that were not mitigated and reached your origin server.



## Troubleshoot false positives

You can use [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/) to help you identify what caused legitimate requests to get blocked. Add filters and adjust the report duration as needed.

To get more detail about which part of a request matched a managed rule, enable [payload logging](https://developers.cloudflare.com/waf/managed-rules/payload-logging/) for the affected managed ruleset. Payload logging records the specific string that triggered each rule (encrypted with a key pair that you provide), which helps you confirm whether a match was a false positive. If you have not set it up yet, [configure payload logging](https://developers.cloudflare.com/waf/managed-rules/payload-logging/configure/) so that the matched payload is available the next time you investigate a false positive. Payload logging is available on Enterprise plans.

If you encounter a false positive caused by a managed rule, do one of the following:

  * **Add an exception** : [Exceptions](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/) allow you to skip the execution of WAF managed rulesets or some of their rules for certain requests.

  * **Adjust the OWASP managed ruleset** : A request blocked by the rule with ID ...843b323c and description `949110: Inbound Anomaly Score Exceeded` refers to the [Cloudflare OWASP Core Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/). To resolve the issue, [configure the OWASP managed ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/).

  * **Disable the corresponding managed rule(s)** : Create an override to disable specific rules. This may avoid false positives, but you will also reduce the overall site security. Refer to the [dashboard instructions](https://developers.cloudflare.com/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset) on configuring a managed ruleset, or to the [API instructions](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/) on creating an override.




Note

If you contact Cloudflare Support to verify whether a WAF managed rule triggers as expected, [provide a HAR file](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#generate-a-har-file) captured while sending the specific request of concern.

### Additional recommendations

  * If one specific rule causes false positives, disable that specific rule and not the entire ruleset.

  * For false positives with the administrator area of your website, add an [exception](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/) disabling a managed rule for the admin section of your site resources. You can use an expression similar to the following:

`http.host eq "example.com" and starts_with(http.request.uri.path, "/admin")`

  * WAF managed rulesets are designed to inspect standard HTTP request content. Requests that upload binary content (for example, file uploads) can resemble attack payloads and cause false positives. To scan file uploads for malicious content, use [Malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/) instead of relying on managed rules for that traffic.




## Troubleshoot false negatives

To identify false negatives, review the HTTP logs on your origin server.

To reduce false negatives, use the following checklist:

  * Are DNS records that serve HTTP traffic [proxied through Cloudflare](https://developers.cloudflare.com/dns/proxy-status/)?  
Cloudflare only mitigates requests in proxied traffic.

  * Have you deployed any of the [WAF managed rulesets](https://developers.cloudflare.com/waf/managed-rules/#available-managed-rulesets) in your zone?  
You must [deploy a managed ruleset](https://developers.cloudflare.com/waf/managed-rules/deploy-zone-dashboard/#deploy-a-managed-ruleset) to apply its rules.

  * Are Managed Rules being skipped via an [exception](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/)?  
Use [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/) to search for requests being skipped. If necessary, adjust the exception expression so that it matches the attack traffic that should have been blocked.

  * Have you enabled any necessary managed rules that are not enabled by default?  
Not all rules of WAF managed rulesets are enabled by default, so you should review individual managed rules.

    * For example, Cloudflare allows requests with empty user agents by default. To block requests with an empty user agent, enable the rule with ID ...0a6dbbd3 in the Cloudflare Managed Ruleset.
    * Another example: If you want to block unmitigated SQL injection (SQLi) attacks, make sure the relevant managed rules tagged with `sqli` are enabled in the Cloudflare Managed Ruleset.

For instructions, refer to [Configure a managed ruleset](https://developers.cloudflare.com/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset).

  * Is the attack traffic matching a custom rule [skipping all Managed Rules](https://developers.cloudflare.com/waf/custom-rules/skip/)?  
If necessary, adjust the custom rule expression so that it does not apply to the attack traffic.

  * Is the attack traffic matching an allowed ASN, IP range, or IP address in [IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)?  
Review your IP Access rules and make sure that any allow rules do not match the attack traffic.

  * Is the malicious traffic reaching your origin IP addresses directly, therefore bypassing Cloudflare protection?  
Block all traffic except from [Cloudflare's IP addresses](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/) at your origin server.




### Additional recommendations

If WAF's managed rulesets do not detect a specific attack pattern after verifying the above, consider the following:

  * Use [WAF attack score](https://developers.cloudflare.com/waf/detections/attack-score/) to complement signature-based managed rules with machine-learning detection. Attack score classifies each request with a score indicating the likelihood it is malicious, even when no managed rule matches.

  * Create a [custom rule](https://developers.cloudflare.com/waf/custom-rules/) to block the specific attack pattern. Use fields such as URI path, query string, or HTTP request headers to match the malicious requests.




[PreviousDeploy using Terraform ↗︎](https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/)[NextOverview](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
