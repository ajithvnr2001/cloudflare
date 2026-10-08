---
url: https://developers.cloudflare.com/api-shield/management-and-monitoring/session-identifiers/
title: Session identifiers \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:17.911714+00:00
---

# Session identifiers · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/management-and-monitoring/session-identifiers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /Management and Monitoring
  4. /Session identifiers



# Session identifiers

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/management-and-monitoring/session-identifiers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTo set up session identifiers

While not strictly required, it is recommended that you configure your session identifiers when getting started with API Shield. When Cloudflare inspects your API traffic for individual sessions, we can offer more tools for visibility, management, and control.

If you are unsure of the session identifiers that your API uses, consult with your development team.

Session identifiers should uniquely identify API clients. A common session identifier for API traffic is the `Authorization` header. When a [JSON Web Token (JWT)](https://developers.cloudflare.com/api-shield/security/jwt-validation/) is used by the API for client authentication, its value may change over time. You can use a claim value inside the JWT such as `sub` or `email` as a session identifier to uniquely identify the session over time.

If no session identifiers are configured and the `Authorization` header appears on more than 1% of eligible sampled client requests with `2xx` responses, Cloudflare automatically configures that header as the API Shield session identifier. Cloudflare does not overwrite an existing session identifier configuration.

Note

An API Shield subscription or eligible API Shield trial is required to configure session identifiers, including cookie-based identifiers. Configured identifiers can provide optional evidence for [API Discovery](https://developers.cloudflare.com/api-shield/security/api-discovery/), and are used by [Sequence Mitigation](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/), [rate limiting recommendations](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/), [Sequence Analytics](https://developers.cloudflare.com/api-shield/security/sequence-analytics/), and [Authentication Posture](https://developers.cloudflare.com/api-shield/security/authentication-posture/).

## To set up session identifiers

You can configure up to 10 session identifiers.

  1. In the Cloudflare dashboard, go to the **Security Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **API abuse**.

  3. On **Session identifiers** , select **Configure session identifiers**.

  4. Select **Manage identifiers**.

  5. Choose the type of session identifier (cookie, HTTP header, or JWT claim).

Note

The session identifier cookie must comply with RFC 6265. Otherwise, it will be rejected.

If you are using a JWT claim, choose the [Token Configuration](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/#token-configurations) that will verify the JWT, then specify the claim using a supported [RFC 9535 JSONPath ↗︎](https://www.rfc-editor.org/rfc/rfc9535.html) expression. Token Configurations are required to use JWT claims as session identifiers. Refer to [JWT Validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) for more information.

  6. Enter the name of the session identifier.

  7. Select **Save**.




API Shield generates rate limiting recommendations for eligible saved operations. Recommendations require API Shield access, a configured session identifier that matches operation traffic, sufficient data, and completed processing. After these requirements are met, you can view per-operation and per-session recommendations and create rate limiting rules.

Discovery can use configured session identifiers as one signal when identifying API traffic. Session identifiers also support session traffic analysis in [Sequence Analytics](https://developers.cloudflare.com/api-shield/security/sequence-analytics/).

[PreviousLabeling service](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/)[NextAPI Routing](https://developers.cloudflare.com/api-shield/management-and-monitoring/api-routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/management-and-monitoring/session-identifiers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
