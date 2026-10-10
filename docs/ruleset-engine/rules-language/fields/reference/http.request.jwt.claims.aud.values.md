---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.aud.values/
title: http.request.jwt.claims.aud.values \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:32.576338+00:00
---

# http.request.jwt.claims.aud.values · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.aud.values/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Jwt.Claims.Aud.Values



# http.request.jwt.claims.aud.values

`http.request.jwt.claims.aud.values``Array<String>`

The `aud` (audience) claim identifies the recipients that the JSON Web Token (JWT) is intended for.

Each principal intended to process the JWT must identify itself with a value in the audience claim. In the general case, the `aud` value is an array of case-sensitive strings, each containing a `StringOrURI` value. For details, refer to the [Registered Claim Names](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1) in RFC 7519.

Requires a Cloudflare Enterprise plan with a paid add-on.

For more information on validating JSON Web Tokens, refer to [JSON Web Tokens Validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) in the API Shield documentation.

Categories: 

  * Request
  * JWT validation



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
