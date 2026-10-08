---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/
title: Stop R-U-Dead-Yet? (R.U.D.Y.) attacks \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:39.557124+00:00
---

# Stop R-U-Dead-Yet? (R.U.D.Y.) attacks · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Stop R-U-Dead-Yet? (R.U.D.Y.) attacks



# Stop R-U-Dead-Yet? (R.U.D.Y.) attacks

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

R-U-Dead-Yet (R.U.D.Y.) attacks accomplish denial of service (DoS) by submitting long form fields. Use custom rules to stop these attacks by blocking requests that do not have a legitimate session cookie.

This example combines three expressions to target HTTP `POST` requests that do not contain a legitimate authenticated session cookie:

  * The first expression uses the [`http.request.uri.path`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path/) field to target the paths to secure from R.U.D.Y.:
        
        http.request.uri.path matches "(comment|conversation|event|poll)/create"

  * The second uses a regular expression to match the format of a legitimate `auth_session` cookie. The `not` operator targets requests where that cookie is not formatted correctly:
        
        not http.cookie matches "auth_session=[0-9a-zA-Z]{32}-[0-9]{10}-[0-9a-z]{6}"

  * The third expression targets HTTP `POST` requests:
        
        http.request.method eq "POST"




To generate the final [custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) expression for this example, the three expressions are combined into a compound expression using the `and` operator. When an HTTP `POST` request to any of the specified URIs does not contain a properly formatted `auth_session` cookie, Cloudflare blocks the request:

  * **When incoming requests match** :

Use the expression editor:  
`(http.request.method eq "POST" and http.request.uri.path matches "(comment|conversation|event|poll)/create" and not http.cookie matches "auth_session=[0-9a-zA-Z]{32}-[0-9]{10}-[0-9a-z]{6}")`

  * **Then take action** : _Block_




Note

The [`matches`](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#comparison-operators) operator requires a Cloudflare Business or Enterprise plan.

[PreviousRequire specific HTTP ports](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-http-ports/)[NextUpdate custom rules for customers or partners](https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/stop-rudy-attacks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
