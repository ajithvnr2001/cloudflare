---
url: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/
title: Supported fields and operators \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:03.792630+00:00
---

# Supported fields and operators · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)

  4. /[Custom load balancing rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/)
  5. /Supported fields and operators



# Supported fields and operators

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExpression Builder field setsFields supported regardless of proxyProxied-only fieldsUnproxied-only fieldsOperators and grouping symbols

The fields that are supported by load balancing rules depend on whether Cloudflare proxies the traffic going through your load balancer or not.

If you use the wrong set of fields, you might see unexpected behaviors. For best results, use the fields associated with your traffic's [proxy status](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/).

Also, some Load Balancing rules fields are available on the Expression Builder - as described in [Load Balancing expressions](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#working-with-expressions) \- while others can only be configured manually, via API or [Expression Editor](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor)

## Expression Builder field sets

Consider the following table to know how the fields available in the [Expression Builder](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-builder) are grouped.

Field Set | Section in Expression Builder | Description  
---|---|---  
Fields supported regardless of proxy | `BOTH` | Values that are always accessible regardless of the load balancer proxy status.  
Proxied-only fields | `PROXIED ONLY` | Values accessible only when the load balancer is proxied.  
Unproxied-only fields | `NON-PROXIED ONLY` | Values accessible only when the load balancer is not proxied (DNS-only traffic).  
  
![Choose load balancer fields based on the proxy status header](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=437,height=423,format=webp/_astro/proxy-status.DIPDmp1m.png)

## Fields supported regardless of proxy

Regardless of your traffic [proxy status](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/), Load Balancing rules can access values for the following fields:

Field| Name in Expression Builder| Description  
---|---|---  
`cf.load_balancer.name`  
`Bytes`| `Load Balancer Name`| Represents the name of the load balancer executing these rules.Example value:  
`lb.example.com`  
`cf.load_balancer.region`  
`Bytes`| `Load Balancer Region`| Provides the [region name](https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/#list-of-load-balancer-regions) of the data center processing the request.Example value:  
`ENAM`  
`ip.src`  
`IP address`| `IP Source Address`| If proxied, this field provides the client TCP IP address, which may be adjusted to reflect the actual address of the client by using HTTP headers such as `X-Forwarded-For` or `X-Real-IP` .If unproxied (DNS-only), this field provides the ECS source address, if available. If not available, it provides the client resolver IP address.**Deprecation Warning:** In the future, this field will always be set to the client resolver IP address for unproxied requests. To check for the presence of ECS and use the ECS IP, see the fields `dns.rr.opt.client` and `dns.rr.opt.client.addr`, respectively.Example value:  
`1.2.3.4`  
`ip.src.asnum`  
`Number`| `AS Number`| The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address.Example value:  
`13335`  
  
## Proxied-only fields

If your traffic is proxied through Cloudflare, you have access to all the fields listed under Fields supported regardless of proxy in addition to the following fields:

Many of these fields are referenced from the [Rules language documentation](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).

Field| Name in Expression Builder| Description  
---|---|---  
[`http.cookie`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.cookie/)  
`String`| ([Manual entry only](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor))| Represents the entire cookie as a string.Example value:   
`session=8521F670545D7865F79C3D7BEDC29CCE;-background=light`  
[`http.host`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.host/)  
`String`| ([Manual entry only](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor))| Represents the hostname used in the full request URI.Example value:   
`[www.example.org ↗︎](http://www.example.org)`  
[`http.referer`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.referer/)  
`String`| ([Manual entry only](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor))| Represents the HTTP Referer request header, which contains the address of the web page that linked to the currently requested page.Example value:   
`Referer: htt­ps://developer.example.org/en-US/docs/Web/JavaScript`  
[`http.request.headers`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/)  
`Map<Array<String>>`| `Header`| Represents HTTP request headers as a Map (or associative array).The keys of the associative array are the names of HTTP request headers **converted to lowercase**.When there are repeating headers, the array includes them in the order they appear in the request.__Decoding:__ no decoding performed   
_Whitespace:_ preserved   
_Non-ASCII:_ preservedExample:   
`any(http.request.headers["content-type"][*] == "application/json")`Example value:   
``{"content-type": ["application/json"]}``  
[`http.request.method`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.method/)  
`String`| `Request Method`| Represents the HTTP method, returned as a string of uppercase characters.Example value:   
`GET`  
[`http.request.timestamp.sec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/)  
`Integer`| `Timestamp`| Represents the timestamp when Cloudflare received the request, expressed as Unix time in seconds. This value is 10 digits long.Example value:   
`1484063137`  
[`http.request.uri`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri/)  
`String`| `URI`| Represents the URI path and query string of the request.Example value:   
`/articles/index?section=539061&expand=comments`  
[`http.request.uri.args`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/)  
`Map<Array<String>>`| ([Manual entry only](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor))| Represents the HTTP URI arguments associated with a request as a Map (associative array).When an argument repeats, then the array contains multiple items in the order they appear in the request.The values are not pre-processed and retain the original case used in the request._Decoding:_ no decoding performed   
_Non-ASCII:_ preservedExample:   
`any(http.request.uri.args["search"][*] == "red+apples")`Example value:   
``{"search": ["red+apples"]}``  
[`http.request.uri.args.names`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.names/)  
`Array<String>`| ([Manual entry only](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor))| Represents the names of the arguments in the HTTP URI query string. The names are not pre-processed and retain the original case used in the request.When a name repeats, the array contains multiple items in the order that they appear in the request._Decoding:_ no decoding performed   
_Non-ASCII:_ preservedExample:   
`any(http.request.uri.args.names[*] == "search")`Example value:   
`["search"]`  
[`http.request.uri.args.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.values/)  
`Array<String>`| ([Manual entry only](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor))| Represents the values of arguments in the HTTP URI query string. The values are not pre-processed and retain the original case used in the request. They are in the same order as in the request.Duplicated values are listed multiple times._Decoding:_ no decoding performed   
_Non-ASCII:_ preservedExample:   
`any(http.request.uri.args.values[*] == "red+apples")`Example value:   
`["red+apples"]`  
[`http.request.uri.path`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path/)  
`String`| `URI Path`| Represents the URI path of the request.Example value:   
`/articles/index`  
[`http.request.uri.query`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.query/)  
`String`| `URI Query`| Represents the entire query string, without the `?` delimiter.Example value:   
`section=539061&expand=comments`  
[`http.request.version`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.version/)  
`String`| `HTTP Version`| Represents the version of the HTTP protocol used. Use this field when you require different checks for different versions.Example Values:

  * `HTTP/1.1`
  * `HTTP/3`

  
  
## Unproxied-only fields

If your traffic is not proxied through Cloudflare, you have access to all the fields listed under Fields supported regardless of proxy in addition to the following fields:

Field| Name in Expression Builder| Description  
---|---|---  
`dns.qry.name`  
`Bytes`| `Query Name`| Represents the query name asked.Example value:  
`example.com.`  
`dns.qry.name.len`  
`Integer`| `Query Name Length`| Represents the length in bytes of the query name.Example value:  
`123`  
`dns.qry.qu`  
`Boolean`| `Question`| When `true`, this field indicates that the received DNS message was a question.  
`dns.qry.type`  
`Integer`| `Query Type`| Represents the numeric value of the [DNS query type](https://en.wikipedia.org/wiki/List_of_DNS_record_types).Example Values:

  * `1` (A record)
  * `28` (AAAA record)

  
`dns.rr.opt.client`  
`Boolean`| ([Manual entry only](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor))| When `true`, this field indicates that the EDNS Client Subnet (ECS) address was sent with the DNS request.  
`dns.rr.opt.client.addr`  
`String`| ([Manual entry only](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor))| If present, this field represents the ECS address sent with the DNS request.Example value:  
`1.2.3.0`  
  
## Operators and grouping symbols

  * **Comparison operators** specify how values defined in an expression must relate to the actual HTTP request value for the expression to return true.

  * **Logical operators** combine two expressions to form a compound expression and use order of precedence to determine how an expression is evaluated.

  * **Grouping symbols** allow you to organize expressions, enforce operator precedence, and nest expressions.




For examples and usage, refer to [Operators and grouping symbols](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/) in the Rules language documentation.

[PreviousActions](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/)[NextIntegrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/load-balancing-rules/reference.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
