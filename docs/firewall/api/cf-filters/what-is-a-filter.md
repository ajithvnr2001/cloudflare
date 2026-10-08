---
url: https://developers.cloudflare.com/firewall/api/cf-filters/what-is-a-filter/
title: What is a filter? \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:16.166748+00:00
---

# What is a filter? · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-filters/what-is-a-filter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/)
  5. /What is a filter?



# What is a filter?

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/what-is-a-filter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A filter is a way of saying:
    
    
    if (traffic matches certain criteria) then...

A filter contains an expression that would return `true` or `false` when evaluated against traffic passing through Cloudflare.

Filter expressions are human and machine readable, and you can compose complex logic to precisely match the traffic that you are interested in detecting and acting upon.

A filter object typically looks like the following:
    
    
    {
      "id": "<FILTER_ID>",
      "expression": "(http.request.uri.path ~ \"^.*wp-login.php$\" or http.request.uri.path ~ \"^.*xmlrpc.php$\") and ip.src ne 93.184.216.34",
      "description": "WordPress login paths via the login page or mobile RPC endpoint"
    }

The expression specified in this example filter is:
    
    
    (http.request.uri.path ~ "^.*wp-login.php$" or http.request.uri.path ~ "^.*xmlrpc.php$") and ip.src ne 93.184.216.34

This filter expression has a `(this or that) and not this` structure designed to:

  * Capture two WordPress paths that may be subject to brute force password attacks, and
  * Exclude traffic that comes from the IP address `93.184.216.34`.



Imagine that this is an IP for your office. This expression demonstrates a filter that might be used (in a firewall rule) to block access to the WordPress login when accessed outside the office network.

For more information on rule expressions, refer to [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/) in the Rules language documentation.

[PreviousOverview](https://developers.cloudflare.com/firewall/api/cf-filters/)[NextJSON object](https://developers.cloudflare.com/firewall/api/cf-filters/json-object/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-filters/what-is-a-filter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
