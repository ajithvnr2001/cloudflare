---
url: https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/
title: Gateway policy expressions \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:09.664790+00:00
---

# Gateway policy expressions · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)
  4. /Gateway policy expressions



# Gateway policy expressions

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/expression-syntax/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExpression syntax Operators Logical operatorsArray handlingList handlingCommon field patternsExample expressions Block a domain in a DNS policy Block multiple content categories in an HTTP policy Allow traffic from a specific user group Block traffic to a destination IP range in a Network policy Combine identity and traffic conditionsGateway versus Ruleset EngineRelated resources

Gateway policies use a wirefilter-based expression language to match traffic against selectors (criteria). This syntax is similar to, but distinct from, the [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/) used by WAF, Rules, and other Cloudflare products. Refer to Gateway versus Ruleset Engine for details on the differences.

Important

The [Ruleset Engine documentation](https://developers.cloudflare.com/ruleset-engine/rules-language/) does not apply to Gateway policies. Gateway has its own set of selectors and fields specific to Zero Trust traffic filtering. For available selectors, refer to the documentation for each policy type:

  * [DNS policy selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/#selectors)
  * [HTTP policy selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#selectors)
  * [Network policy selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/#selectors)
  * [Egress policy selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#selectors)
  * [Resolver policy selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/#selectors)



## Expression syntax

Gateway expressions follow this pattern:
    
    
    <field> <operator> <value>

For example:
    
    
    dns.fqdn == "example.com"
    http.request.host == "api.example.com"
    identity.email == "user@company.com"

### Operators

Gateway supports the following operators:

Operator | Name | Example  
---|---|---  
`==` | Equals | `dns.fqdn == "example.com"`  
`!=` | Does not equal | `http.request.host != "blocked.com"`  
`in` | Value is in set | `net.dst.port in {80 443}`  
`matches` | Matches regular expression | `http.request.host matches ".*\\.example\\.com"`  
`>` | Greater than | `http.upload.file.size > 10`  
`>=` | Greater than or equal to | `http.download.file.size >= 100`  
`<` | Less than | `http.upload.file.size < 50`  
`<=` | Less than or equal to | `http.download.file.size <= 200`  
  
### Logical operators

Combine multiple conditions using logical operators:

Operator | Name | Example  
---|---|---  
`and` | Logical AND | `dns.fqdn == "example.com" and identity.email == "admin@company.com"`  
`or` | Logical OR | `net.dst.port == 80 or net.dst.port == 443`  
`not` | Logical NOT | `not(identity.email == "guest@company.com")`  
  
## Array handling

Some Gateway fields return arrays (multiple values). Use the `any()` function to match if any element in the array meets the condition:
    
    
    any(http.request.uri.content_category[*] in {17 85 102})
    
    
    any(identity.groups[*].name in {"Engineering" "Security"})
    
    
    any(http.request.domains[*] == "example.com")

The `[*]` notation indicates that the function should evaluate all elements in the array.

## List handling

You can reference [lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/) in your expressions using the list UUID:
    
    
    http.request.host in $<LIST_UUID>
    
    
    any(http.request.domains[*] in $<LIST_UUID>)

To find a list's UUID, go to **My Team** > **Lists** in Zero Trust and select the list. The UUID appears in the browser URL.

## Common field patterns

Each Gateway policy type has its own set of available fields. The following table shows the field prefixes used by each policy type:

Policy type | Field prefix | Example fields  
---|---|---  
DNS | `dns.` | `dns.fqdn`, `dns.content_category`, `dns.src_ip`  
HTTP | `http.` | `http.request.host`, `http.request.uri`, `http.request.domains`  
Network | `net.` | `net.dst.ip`, `net.dst.port`, `net.src.ip`  
Identity | `identity.` | `identity.email`, `identity.groups`, `identity.name`  
Device posture | `device_posture.` | `device_posture.checks.passed`  
  
For a complete list of available fields for each policy type, refer to the selectors documentation linked at the top of this page.

## Example expressions

### Block a domain in a DNS policy
    
    
    dns.fqdn == "example.com"

### Block multiple content categories in an HTTP policy
    
    
    any(http.request.uri.content_category[*] in {17 85 102})

### Allow traffic from a specific user group
    
    
    any(identity.groups[*].name in {"Engineering"})

### Block traffic to a destination IP range in a Network policy
    
    
    net.dst.ip in {10.0.0.0/8}

### Combine identity and traffic conditions
    
    
    http.request.host == "internal.example.com" and identity.email matches ".*@company.com"

## Gateway versus Ruleset Engine

The following table summarizes the key differences between the Rules language](/ruleset-engine/rules-language/) (supported by the Ruleset Engine) and Gateway policy expressions:

| Ruleset Engine | Gateway  
---|---|---  
**Products** | WAF, Transform Rules, Cache Rules, Configuration Rules | DNS, HTTP, Network, Egress, Resolver policies  
**Field examples** | `http.request.uri.path`, `cf.bot_management.score`, `ip.src` | `dns.fqdn`, `http.request.host`, `identity.email`  
**Identity fields** | Not available | Available (for example, `identity.email`, `identity.groups`)  
**DNS fields** | Not available | Available (for example, `dns.fqdn`, `dns.content_category`)  
**Documentation** | [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/) | [Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)  
  
Note

Do not reference the [Ruleset Engine fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/) when building Gateway policies. Gateway has its own field set documented on each policy type page.

## Related resources

  * [DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/)
  * [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/)
  * [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/)
  * [Identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/)
  * [Lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/)



[PreviousProxy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/)[NextGranular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-policies/expression-syntax.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
