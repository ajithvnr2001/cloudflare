---
url: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/
title: Override expressions for HTTP DDoS Attack Protection \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:53.479149+00:00
---

# Override expressions for HTTP DDoS Attack Protection · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Managed rulesets](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)[HTTP DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/)

  4. /[Overrides](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/)
  5. /Override expressions



# Override expressions

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable expression fields

Note

Only available to Enterprise customers with the Advanced DDoS Protection subscription.

Set an override expression for the HTTP DDoS Attack Protection managed ruleset to define a specific scope for [sensitivity level](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/#sensitivity-level) or [action](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/#action) adjustments.

For example, you can set different sensitivity levels for different request URI paths: a medium sensitivity level for URI path `A` and a low sensitivity level for URI path `B`.

## Available expression fields

You can use the following fields in override expressions:

  * `cf.bot_management.ja3_hash`
  * `cf.bot_management.ja4`
  * `cf.client.bot`
  * `cf.tls_cipher`
  * `cf.tls_client_auth.cert_verified`
  * `cf.tls_version`
  * `cf.verified_bot_category`
  * `http.cookie`
  * `http.host`
  * `http.referer`
  * `http.request.headers`
  * `http.request.headers.names`
  * `http.request.headers.truncated`
  * `http.request.headers.values`
  * `http.request.uri`
  * `http.request.uri.path`
  * `http.request.uri.path.extension`
  * `http.request.uri.query`
  * `http.request.full_uri`
  * `http.request.method`
  * `http.request.version`
  * `http.request.cookies`
  * `http.user_agent`
  * `http.x_forwarded_for`
  * `ip.src`
  * `ip.src.asnum`
  * `ip.src.continent`
  * `ip.src.country`
  * `ip.src.is_in_european_union`
  * `ssl`



Refer to the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) in the Rules language documentation for more information.

[PreviousConfigure using Terraform ↗︎](https://developers.cloudflare.com/terraform/additional-configurations/ddos-managed-rulesets/#example-configure-http-ddos-attack-protection)[NextOverride examples](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/managed-rulesets/http/http-overrides/override-expressions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
