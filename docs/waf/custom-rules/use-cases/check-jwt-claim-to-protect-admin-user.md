---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/
title: Issue challenge for admin user in JWT claim based on attack score \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:38.920353+00:00
---

# Issue challenge for admin user in JWT claim based on attack score · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Issue challenge for admin user in JWT claim based on attack score



# Issue challenge for admin user in JWT claim based on attack score

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

To use claims inside a JSON Web Token (JWT), you must first set up a [token validation configuration](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/) in API Shield.

This example configures additional protection for requests with a JSON Web Token (JWT) with a user claim of `admin`, based on the request's [attack score](https://developers.cloudflare.com/waf/detections/attack-score/).

[Create a custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) that issues a Managed Challenge if the user claim in a JWT is `admin` and the attack score is below 40.

  * **When incoming requests match**

Use the expression editor:  
`(lookup_json_string(http.request.jwt.claims["<TOKEN_CONFIGURATION_ID>"][0], "user") eq "admin" and cf.waf.score < 40)`

  * **Then take action** : _Managed Challenge_




In this example, `<TOKEN_CONFIGURATION_ID>` is your [token configuration ID](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/) found in JWT Validation and `user` is the JWT claim.

[PreviousExempt partners from Hotlink Protection](https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/)[NextRequire a specific cookie](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
