---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/
title: Require specific HTTP headers \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:39.145558+00:00
---

# Require specific HTTP headers · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Require specific HTTP headers



# Require specific HTTP headers

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample 1: Require presence of HTTP headerExample 2: Require HTTP header with a specific value

Many organizations qualify traffic based on the presence of specific HTTP request headers. Use the Rules language [HTTP request header fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/?field-category=Headers&search-term=http.request) to target requests with specific headers.

## Example 1: Require presence of HTTP header

This example custom rule uses the [`http.request.headers.names`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/) field to look for the presence of an `X-CSRF-Token` header. The [`lower()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#lower) transformation function converts the header name to lowercase so that the expression is case-insensitive.

When the `X-CSRF-Token` header is missing, Cloudflare blocks the request.

  * **When incoming requests match** :

Use the expression editor:  
`not any(lower(http.request.headers.names[*])[*] eq "x-csrf-token") and (http.request.full_uri eq "https://www.example.com/somepath")`

  * **Then take action** : _Block_




## Example 2: Require HTTP header with a specific value

This example custom rule uses the [`http.request.headers`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/) field to look for the presence of the `X-Example-Header` header and to get its value (if any). When the `X-Example-Header` header is missing or it does not have the value `example-value`, Cloudflare blocks the request.

  * **When incoming requests match** :

Use the expression editor:  
`not any(http.request.headers["x-example-header"][*] eq "example-value") and (http.request.uri.path eq "/somepath")`

  * **Then take action** : _Block_




The keys in the `http.request.headers` field, corresponding to HTTP header names, are in lowercase.

In this example the header name is case-insensitive, but the header value is case-sensitive.

[PreviousRequire known IP addresses in site admin area](https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/)[NextRequire specific HTTP ports](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-http-ports/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/require-specific-headers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
