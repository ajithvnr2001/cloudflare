---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/
title: Programmable Flow Protection API - JSON objects \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:44.975036+00:00
---

# Programmable Flow Protection API - JSON objects · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systemsAPI configuration

  4. /[Programmable Flow Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/)
  5. /JSON objects



# JSON objects

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProgramRule Scope Mode Expression

This page contains examples of the JSON objects used in the Programmable Flow Protection API.

## Program
    
    
    {
      "id": "31c70c65-9f81-4669-94ed-1e1e041e7b06",
      "name": "rate-limiter",
      "status": "success",
      "created_on": "2024-01-01T13:06:04.721954+01:00",
      "modified_on": "2024-01-01T13:06:04.721954+01:00"
    }

Field | Description  
---|---  
`id` | Unique identifier for the program.  
`name` | Name of the program, derived from the uploaded filename.  
`status` | Compilation and verification status. One of `success` or `failed`. Programs with `failed` status are automatically deleted after 30 days of inactivity.  
`created_on` | Timestamp when the program was created.  
`modified_on` | Timestamp when the program was last modified.  
  
## Rule
    
    
    {
      "id": "20b99eb6-8b48-48dd-a5b9-a995a0843b57",
      "program_id": "31c70c65-9f81-4669-94ed-1e1e041e7b06",
      "scope": "region",
      "name": "WEUR",
      "mode": "enabled",
      "expression": "ip.dst in { 192.0.2.0/24 }",
      "created_on": "2024-01-01T13:10:38.762503+01:00",
      "modified_on": "2024-01-01T13:10:38.762503+01:00"
    }

Field | Description  
---|---  
`id` | Unique identifier for the rule.  
`program_id` | The ID of the program this rule executes.  
`scope` | The scope of the rule. Must be one of `global`, `region`, or `datacenter`.  
`name` | For `global` scope, use `global`. For `region` or `datacenter` scope, provide the region code or datacenter code.  
`mode` | The rule mode. Must be one of `enabled`, `disabled`, or `monitoring`.  
`expression` | A [Rules language expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/) to filter which packets the rule applies to. Optional.  
`created_on` | Timestamp when the rule was created.  
`modified_on` | Timestamp when the rule was last modified.  
  
### Scope

The `scope` field determines where the rule executes:

  * `global` — The rule executes at all Cloudflare locations. You can only create one global rule per account.
  * `region` — The rule executes at all Cloudflare locations within the specified region.
  * `datacenter` — The rule executes only at the specified Cloudflare datacenter.



When multiple rules match a packet, the rule with the most specific scope executes. A datacenter-scoped rule takes precedence over a region-scoped rule, which takes precedence over a global rule.

### Mode

The `mode` field determines how the rule behaves:

  * `enabled` — The program runs and its verdict (pass or drop) is applied to packets.
  * `disabled` — The rule is inactive and the program does not run.
  * `monitoring` — The program runs but packets are never dropped, regardless of the program's verdict. Use this mode to test a program before enabling it.



### Expression

The `expression` field is a [Rules language expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/) up to 8,192 characters. The expression filters which packets the rule applies to. Only packets matching the expression are processed by the program.

Supported fields:

  * `ip.src`
  * `ip.dst`
  * `udp.srcport`
  * `udp.dstport`



If the expression is empty or omitted, the rule applies to all UDP packets within its scope.

For more information on rule settings, refer to [Rule settings](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#rule-settings).

[PreviousCommon API calls](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples/)[NextTroubleshooting Advanced TCP Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
