---
url: https://developers.cloudflare.com/api-shield/security/jwt-validation/transform-rules/
title: Enhance Request Header Transform Rules with JWT claims \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:18.905948+00:00
---

# Enhance Request Header Transform Rules with JWT claims · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/security/jwt-validation/transform-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /…

[Security](https://developers.cloudflare.com/api-shield/security/)

  4. /[JSON Web Tokens validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/)
  5. /Enhance Request Header Transform Rules



# Enhance Request Header Transform Rules

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/security/jwt-validation/transform-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a Request Header Transform Rule

You can forward verified claims from a [JSON Web Token (JWT)](https://developers.cloudflare.com/api-shield/security/jwt-validation/) to your origin in a header by creating a [Request Header Transform Rule](https://developers.cloudflare.com/rules/transform/request-header-modification/).

Verified claims are available to Request Header Transform Rules through the `http.request.jwt.claims` fields. They are not available to [URL Rewrite Rules](https://developers.cloudflare.com/rules/transform/url-rewrite/).

For example, the following expression will extract the user claim from a token processed by the token configuration with `TOKEN_CONFIGURATION_ID`:
    
    
    lookup_json_string(http.request.jwt.claims["<TOKEN_CONFIGURATION_ID>"][0], "claim_name")

Refer to [Configure JWT validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/) for more information about creating a token configuration.

## Create a Request Header Transform Rule

As an example, create a Request Header Transform Rule to send the `x-send-jwt-claim-user` request header to the origin:

  1. In the Cloudflare dashboard, go to the **Rules overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview)
  2. Select **Create rule** > **Request Header Transform Rules**.

  3. Enter a rule name and a filter expression, if applicable.

  4. Choose **Set dynamic**.

  5. Set the header name to `x-send-jwt-claim-user`.

  6. Set the value to:
         
         lookup_json_string(http.request.jwt.claims["<TOKEN_CONFIGURATION_ID>"][0], "claim_name")

`<TOKEN_CONFIGURATION_ID>` is your token configuration ID found in JWT validation and `claim_name` is the JWT claim you want to add to the header.




[PreviousConfigure the Worker](https://developers.cloudflare.com/api-shield/security/jwt-validation/jwt-worker/)[NextOverview](https://developers.cloudflare.com/api-shield/security/mtls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/security/jwt-validation/transform-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
