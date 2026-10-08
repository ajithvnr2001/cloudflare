---
url: https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/
title: Dynamic threshold rule \u00b7 Cloudflare Network Flow docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:24.882672+00:00
---

# Dynamic threshold rule · Cloudflare Network Flow docs

> Source: https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Flow](https://developers.cloudflare.com/network-flow/)
  3. /[Rules](https://developers.cloudflare.com/network-flow/rules/)
  4. /Dynamic threshold rule



# Dynamic threshold rule

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRule configuration fieldsAPI documentationHow the dynamic rule threshold is calculated

A dynamic threshold rule (beta) monitors your network traffic patterns and automatically adjusts the Distributed Denial of Service (DDoS) threshold based on traffic history. Network Flow (formerly Magic Network Monitoring) compares total traffic across all IP prefixes and addresses in the rule against the dynamic threshold, measured in bits or packets per second. If traffic exceeds the threshold, Network Flow sends an alert.

To use dynamic threshold rules, you must send NetFlow or sFlow data to Cloudflare. You can only configure dynamic threshold rules through the [Network Flow Rules API](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/) — they are not available in the dashboard.

## Rule configuration fields

Field | Description  
---|---  
**Rule name** | Must be unique and cannot contain spaces. Supports characters `A-Z`, `a-z`, `0-9`, underscore (`_`), dash (`-`), period (`.`), and tilde (`~`). Maximum of 256 characters.  
**Rule type** | zscore  
**Target** | Can be defined in either bits per second or packets per second.  
**Sensitivity** | Controls how easily traffic anomalies trigger alerts. Available values: low, medium, and high. Higher sensitivity triggers alerts on smaller deviations from normal traffic.  
**Auto-advertisement** | If you are a [Magic Transit On Demand](https://developers.cloudflare.com/magic-transit/on-demand) customer, you can enable this feature to automatically enable Magic Transit if the rule's dynamic threshold is triggered. Network Flow supports Magic Transit's supernet capability. To learn more refer to [Auto-Advertisement section](https://developers.cloudflare.com/network-flow/rules/#rule-auto-advertisement).  
**Rule IP prefix** | The IP prefix associated with the rule for monitoring traffic volume. Must be a CIDR range such as `160.168.0.1/24`. The maximum is 5,000 unique CIDR entries. To learn more and review an example, refer to the [Rule IP prefixes](https://developers.cloudflare.com/network-flow/rules/#rule-ip-prefixes) section.  
  
## API documentation

To review an example API configuration call using CURL and the expected output for a successful response, go to the [Rules](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/) section in the Network Flow API documentation.

## How the dynamic rule threshold is calculated

Z-score compares short-term traffic patterns (five-minute window) against long-term baselines (four-hour window) to detect anomalies. The threshold adjusts automatically as your traffic history grows.

Z-Score is calculated by using the following formula:
    
    
    Z = (X - μ) / σ

  * `X` = Current traffic value.
  * `μ` = Mean traffic value over the long window.
  * `σ` = Standard deviation over the long window.



[PreviousStatic threshold rule](https://developers.cloudflare.com/network-flow/rules/static-threshold/)[NextsFlow DDoS attack rule](https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-flow/rules/dynamic-threshold.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
