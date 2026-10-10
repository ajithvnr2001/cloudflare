---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.nbf.sec/
title: http.request.jwt.claims.nbf.sec \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:32.128509+00:00
---

# http.request.jwt.claims.nbf.sec · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.nbf.sec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Jwt.Claims.Nbf.Sec



# http.request.jwt.claims.nbf.sec

`http.request.jwt.claims.nbf.sec``Map<Array<Integer>>`

The `nbf` (not before) claim identifies the time (number of seconds) before which the JWT must not be accepted for processing.

For details, refer to the [Registered Claim Names](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1) in RFC 7519.

Requires a Cloudflare Enterprise plan with a paid add-on.

For more information on validating JSON Web Tokens, refer to [JSON Web Tokens Validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) in the API Shield documentation.

Categories: 

  * Request
  * JWT validation



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
