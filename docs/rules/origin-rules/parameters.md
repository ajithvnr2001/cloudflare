---
url: https://developers.cloudflare.com/rules/origin-rules/parameters/
title: Origin Rules API parameter reference \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:52.156236+00:00
---

# Origin Rules API parameter reference · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/origin-rules/parameters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Origin Rules](https://developers.cloudflare.com/rules/origin-rules/)
  4. /API parameter reference



# Origin Rules API parameter reference

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/origin-rules/parameters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHost header override parametersSNI override parametersDNS record override and destination port override parametersConfiguring several overrides in the same rule

Create [different overrides](https://developers.cloudflare.com/rules/origin-rules/features/) by including different action parameters in the `action_parameters` field:

Override type | What to include  
---|---  
Host header override | `host_header` parameter  
SNI override | `sni` object  
DNS record override / Destination port override | `origin` object  
  
Note

The same origin rule can have different types of overrides. Refer to Configuring several overrides in the same rule for a syntax example.

## Host header override parameters

The full syntax of the `action_parameters` field for overriding the HTTP `Host` header is the following:
    
    
    "action_parameters": {
      "host_header": "<HOST_HEADER_VALUE>"
    }

## SNI override parameters

The full syntax of the `action_parameters` field for overriding the SNI value of incoming requests is the following:
    
    
    "action_parameters": {
      "sni": {
        "value": "<SNI_VALUE>"
      }
    }

## DNS record override and destination port override parameters

The full syntax of the `action_parameters` field for overriding both the hostname and the destination port of incoming requests is the following:
    
    
    "action_parameters": {
      "origin": {
        "host": "<HOSTNAME>",
        "port": <PORT>
      }
    }

If you are only overriding the hostname or the port, omit the `port` or `host` parameter, respectively.

## Configuring several overrides in the same rule

The same origin rule can have different types of overrides. For example, a single origin rule can perform an HTTP `Host` header override and a destination port override. The syntax of such a rule would be the following:
    
    
    "action_parameters": {
      "host_header": "<HOST_HEADER_VALUE>",
      "origin": {
        "port": <PORT>
      }
    }

[PreviousAvailable settings](https://developers.cloudflare.com/rules/origin-rules/features/)[NextFAQ](https://developers.cloudflare.com/rules/origin-rules/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/origin-rules/parameters.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
