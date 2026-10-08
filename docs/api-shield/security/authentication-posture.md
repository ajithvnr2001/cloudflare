---
url: https://developers.cloudflare.com/api-shield/security/authentication-posture/
title: Authentication Posture \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:18.128069+00:00
---

# Authentication Posture · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/security/authentication-posture/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /[Security](https://developers.cloudflare.com/api-shield/security/)
  4. /Authentication Posture



# Authentication Posture

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/security/authentication-posture/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProcess Examine an endpoint's authentication details Stop unauthenticated traffic with CloudflareLimitationsAvailability

Authentication Posture detects API endpoints where all or some successful requests lack a configured session identifier and alerts you to potential misconfigurations.

For example, a security team member may expect that their API endpoints `/api/v1/users` and `/api/v1/orders` require authentication. However, bugs in origin API authentication policies can create broken authentication vulnerabilities — allowing unauthenticated access to protected resources. Authentication Posture does not validate credentials. Instead, it reports whether configured session identifiers are present on successful requests to help you identify potential misconfigurations.

Consider a typical e-commerce application. Users can browse items and prices without logging in. However, to retrieve order details via `GET /api/v1/orders/{order_id}`, users must log in and pass an Authorization HTTP header with all requests. Cloudflare alerts you via [Security Center Insights](https://developers.cloudflare.com/security/security-insights/) and [Endpoint labels](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/) if successful requests reach this endpoint or any other endpoint without a configured session identifier.

## Process

After configuring [session identifiers](https://developers.cloudflare.com/api-shield/get-started/#session-identifiers), API Shield scans successful requests for the presence of those identifiers and updates endpoint labels approximately once a day. The labeling methodology explains how API Shield assigns authentication posture labels.

Description | 2xx response codes | 4xx, 5xx response codes  
---|---|---  
If all successful requests lack a configured session identifier, Cloudflare applies the label: | `cf-risk-missing-auth` | Requests with these response codes are not used to apply the label.  
If some successful requests contain a configured session identifier and some lack one, Cloudflare applies the label: | `cf-risk-mixed-auth` | Requests with these response codes are not used to apply the label.  
  
### Examine an endpoint's authentication details

  1. In the Cloudflare dashboard, go to the **Web Assets** page.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Go to the **Operations** tab.

  3. Filter your endpoints by the `cf-risk-missing-auth` or `cf-risk-mixed-auth` labels.

  4. Select an endpoint to see its authentication posture details on the endpoint details page.

  5. Choose between the 24-hour and 7-day view options, and note any authentication changes over time.




The main authentication widget displays how many successful requests over the last seven days had session identifiers included with them, and which identifiers were included with the traffic.

The authentication-over-time chart shows a detailed breakdown over time of how clients successfully interacted with your API and which identifiers were used. A large increase in unauthenticated traffic may signal a security incident. Similarly, any successful unauthenticated traffic on an endpoint that is expected to be 100% authenticated can be a cause for concern.

Work with your development team to understand which authentication policies may need to be corrected on your API to stop unauthenticated traffic.

### Stop unauthenticated traffic with Cloudflare

In this context, an unauthenticated request is one that does not include a configured API Shield session identifier.

To block unauthenticated requests, create a [custom rule](https://developers.cloudflare.com/waf/custom-rules/) using the `cf.api_gateway.auth_id_present` field. This field evaluates to `true` when the configured API Shield session identifiers are present on a request. You can also match on absence to detect unauthenticated traffic. Add a host and path match to scope the rule to specific endpoints.

## Limitations

Authentication Posture can only apply when customers accurately set up session identifiers in API Shield. Session identifiers must uniquely identify authenticated users of your API. If you are unsure of your API's session identifier, consult with your development team.

## Availability

Authentication Posture is available for all Enterprise customers with an API Shield subscription.

[PreviousAPI](https://developers.cloudflare.com/api-shield/security/schema-validation/api/)[NextBOLA vulnerability detection](https://developers.cloudflare.com/api-shield/security/bola-vulnerability-detection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/security/authentication-posture.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
