---
url: https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/
title: sFlow DDoS attack rule \u00b7 Cloudflare Network Flow docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:24.017238+00:00
---

# sFlow DDoS attack rule · Cloudflare Network Flow docs

> Source: https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Flow](https://developers.cloudflare.com/network-flow/)
  3. /[Rules](https://developers.cloudflare.com/network-flow/rules/)
  4. /sFlow DDoS attack rule



# sFlow DDoS attack rule

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSend sFlow data from your network to CloudflareRule configuration fieldsAPI documentationTune the sFlow DDoS alert thresholds

An sFlow DDoS attack rule (beta) alerts you when a DDoS attack is detected in your network traffic. Network Flow (formerly Magic Network Monitoring) uses the same DDoS detection rules that protect Cloudflare's global network to identify these attacks.

To use sFlow DDoS attack rules, you must send sFlow data to Cloudflare. You can only configure these rules through the [Network Flow Rules API](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/) — they are not available in the dashboard.

## Send sFlow data from your network to Cloudflare

To send sFlow data to Cloudflare, your router must support sFlow exports. Refer to [Supported routers](https://developers.cloudflare.com/network-flow/routers/supported-routers/) to verify compatibility, and [Configure sFlow](https://developers.cloudflare.com/network-flow/routers/sflow-config/) for setup instructions.

## Rule configuration fields

Field | Description  
---|---  
**Rule name** | Must be unique and cannot contain spaces. Supports characters `A-Z`, `a-z`, `0-9`, underscore (`_`), dash (`-`), period (`.`), and tilde (`~`). Maximum of 256 characters.  
**Rule type** | advanced_ddos  
**Prefix Match** | The field `prefix_match` determines how IP matches are handled.   
  
**Subnet** (recommended): Automatically advertise if the attacked IPs are within a subnet of a public IP prefix that can be advertised by Magic Transit.  
  
**Exact** : Automatically advertise if the attacked IPs are an exact match with a public IP prefix that can be advertised by Magic Transit.  
  
**Supernet** : Automatically advertise if the attacked IPs are a supernet of a public IP prefix that can be advertised by Magic Transit.  
**Auto-advertisement** | If you are a [Magic Transit On Demand](https://developers.cloudflare.com/magic-transit/on-demand) customer, you can enable this feature to automatically enable Magic Transit if the rule's dynamic threshold is triggered. To learn more, refer to [Auto-advertisement](https://developers.cloudflare.com/network-flow/rules/#rule-auto-advertisement).  
**Rule IP prefix** | The IP prefix associated with the rule for monitoring traffic volume. Must be a CIDR range such as `160.168.0.1/24`. The maximum is 5,000 unique CIDR entries. To learn more and see an example, refer to [Rule IP prefixes](https://developers.cloudflare.com/network-flow/rules/#rule-ip-prefixes).  
  
## API documentation

Refer to the [Rules API documentation](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/) to review an example API configuration call using CURL and the expected output for a successful response.

## Tune the sFlow DDoS alert thresholds

You can tune the thresholds of your sFlow DDoS alerts in the dashboard and via the Cloudflare API by following the [Network-layer DDoS Attack Protection managed ruleset](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/) guide.

[PreviousDynamic threshold rule](https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/)[NextConfigure rule notifications](https://developers.cloudflare.com/network-flow/rules/rule-notifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-flow/rules/s-flow-ddos-attack.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
