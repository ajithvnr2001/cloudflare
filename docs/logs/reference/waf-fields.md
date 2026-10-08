---
url: https://developers.cloudflare.com/logs/reference/waf-fields/
title: WAF fields \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:17.157452+00:00
---

# WAF fields · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/reference/waf-fields/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Reference](https://developers.cloudflare.com/logs/reference/)
  4. /WAF fields



# WAF fields

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/reference/waf-fields/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWAF ActionDeprecated fields for internal Cloudflare use

The Web Application Firewall (WAF) contains rules managed by Cloudflare to block requests that contain malicious content.

## WAF Action

Value | Action | Description  
---|---|---  
`0` | Unknown | Take no other action.  
`1` | Allow | Bypass all subsequent WAF rules.  
`2` | Drop | Block with an HTTP 403 response.  
`3` | Challenge Allow | Issue a Managed Challenge.  
`4` | Challenge Drop | Unused.  
`5` | Log | Take no action other than logging the event.  
  
## Deprecated fields for internal Cloudflare use

The values of these fields are subject to change by Cloudflare at any time and are irrelevant for customer data analysis:

  * WAFFlags
  * WAFMatchedVar



[PreviousSecurity fields](https://developers.cloudflare.com/logs/reference/security-fields/)[NextClientRequestSource field](https://developers.cloudflare.com/logs/reference/clientrequestsource/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/reference/waf-fields.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
