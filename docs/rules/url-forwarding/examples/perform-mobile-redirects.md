---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/
title: Perform mobile redirects \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:59.779641+00:00
---

# Perform mobile redirects · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Perform mobile redirects



# Perform mobile redirects

Create a redirect rule to redirect visitors using mobile devices to a different hostname.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRedirect mobile users dropping the original URI pathRedirect mobile users keeping the original path

The following examples will redirect visitors using mobile devices — based on the request user agent string — to a different hostname.

## Redirect mobile users dropping the original URI path

This example static redirect will redirect requests for the current zone (`example.com`) from mobile users to `m.example.com` without preserving the URI path in the original HTTP request.

**When incoming requests match**

  * Enter the following expression in the [Expression Editor](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor):  
`not http.host in {"m.example.com"} and (http.user_agent contains "mobi" or http.user_agent contains "Mobi")`



**Then**

  * **Type:** _Static_
  * **URL:** `m.example.com`
  * **Status code:** _301_



Notes about this example:

  * The `not http.host in {"m.example.com"}` condition prevents redirect loops.
  * The user agent condition follows [Mozilla's recommendation ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent/Firefox#device-specific_user_agent_strings) for identifying mobile devices.
  * The **Then** > **URL** value should be the same as the one you entered in the `http.host` condition of the rule's filter expression.
  * You can redirect users to other zones on Cloudflare or to other hostnames not on Cloudflare.



## Redirect mobile users keeping the original path

This example single redirect will redirect requests for the current zone (`example.com`) from mobile users to `m.example.com`, keeping the URI path of the original HTTP request.

**When incoming requests match**

  * Enter the following expression in the [Expression Editor](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor):  
`not http.host in {"m.example.com"} and (http.user_agent contains "mobi" or http.user_agent contains "Mobi")`



**Then**

  * **Type:** _Dynamic_
  * **Expression:** `concat("https://m.example.com", http.request.uri.path)`
  * **Status code:** _301_



Notes about this example:

  * The `not http.host in {"m.example.com"}` condition prevents redirect loops.
  * The user agent condition follows [Mozilla's recommendation ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent/Firefox#device-specific_user_agent_strings) for identifying mobile devices.
  * The hostname in **Then** > **Expression** should be the same as the one you entered in the `http.host` condition of the rule's filter expression.
  * Depending on your use case, you may want to enable **Then** > **Preserve query string** to also keep the query string of the original request.
  * You can redirect users to other zones on Cloudflare or to other hostnames not on Cloudflare.



[PreviousOverview](https://developers.cloudflare.com/rules/url-forwarding/examples/)[NextRedirect admin area requests to HTTPS](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/perform-mobile-redirects.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
