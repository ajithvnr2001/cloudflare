---
url: https://developers.cloudflare.com/rules/origin-rules/faq/
title: Origin Rules FAQ \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:49.719475+00:00
---

# Origin Rules FAQ · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/origin-rules/faq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Origin Rules](https://developers.cloudflare.com/rules/origin-rules/)
  4. /FAQ



# Origin Rules FAQ

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/origin-rules/faq/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat happens if I use both an origin rule and a page rule to perform a Host header/DNS record override?Will Cloudflare automatically migrate my Page Rules with Host header and DNS record overrides to origin rules?What happens if more than one origin rule matches the current request?

Below you will find answers to the most commonly asked questions regarding Origin Rules.

## What happens if I use both an origin rule and a page rule to perform a Host header/DNS record override?

In this situation the origin rule parameters will override the [page rule](https://developers.cloudflare.com/rules/page-rules/) parameters.

Consider the following example scenarios:

  * A page rule defines a Host header override, but not a resolve override (or DNS record override). An origin rule defines a DNS record override, but not a Host header override. The resulting request will have the `Host` header defined by the page rule and the origin hostname defined by the origin rule.
  * A page rule defines a Host header override, and an origin rule also defines a Host header override. The resulting request will have the `Host` header defined by the origin rule.



## Will Cloudflare automatically migrate my Page Rules with Host header and DNS record overrides to origin rules?

Yes. Refer to the [Page Rules migration guide](https://developers.cloudflare.com/rules/reference/page-rules-migration/) for any updates on the migration process.

## What happens if more than one origin rule matches the current request?

If two or more origin rules match a request, the configuration of those rules is merged. While merging two configurations, the settings of later rules will override the settings defined in previous rules, updating or adding configuration properties. The final configuration applied by Cloudflare will be this merged version.

For example, if you configure the following two [origin rules](https://developers.cloudflare.com/rules/origin-rules/) and both rules match, Cloudflare will use the destination port set by the first rule, and the DNS hostname override and `Host` header value set by the second rule.

**Origin rule #1**

Parameter | Value  
---|---  
Set `Host` header | `example.com`  
Set destination port | `8081`  
  
**Origin rule #2**

Parameter | Value  
---|---  
Set `Host` header | `example.net`  
Set DNS hostname | `example.net`  
  
JSON example for API users

When [using the API](https://developers.cloudflare.com/rules/origin-rules/create-api/), you configure origin rule parameters in an `action_parameters` object.
    
    
    {
    	"rules": [
    		{
    			"expression": "http.request.uri.query contains \"/eu/\"",
    			"description": "Origin rule #1",
    			"action": "route",
    			"action_parameters": {
    				"host_header": "example.com",
    				"origin": {
    					"port": 8081
    				}
    			}
    		},
    		{
    			"expression": "http.request.uri.query contains \"/eu/\"",
    			"description": "Origin rule #2",
    			"action": "route",
    			"action_parameters": {
    				"host_header": "example.net",
    				"origin": {
    					"host": "example.net"
    				}
    			}
    		}
    	]
    }

The merged configuration to apply would be the following:

Parameter | Value  
---|---  
Set `Host` header | `example.net`  
Set destination port | `8081`  
Set DNS hostname | `example.net`  
  
If you also configured a destination port in rule #2, that value would override the `8081` destination port defined in rule #1.

[PreviousAPI parameter reference](https://developers.cloudflare.com/rules/origin-rules/parameters/)[NextCache Rules ↗︎](https://developers.cloudflare.com/cache/how-to/cache-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/origin-rules/faq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
