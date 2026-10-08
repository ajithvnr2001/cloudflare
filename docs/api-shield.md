---
url: https://developers.cloudflare.com/api-shield/
title: Overview \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:17.343150+00:00
---

# Overview · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/

  1. [Home](https://developers.cloudflare.com/)
  2. /API Shield



# Cloudflare API Shield

Last updated Aug 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhy care about API security?FeaturesUse Schema ProfilesAvailabilityRelated products

Identify and address your API vulnerabilities.

Enterprise-only paid add-on

Note

Enterprise customers can preview this product as a [non-contract service](https://developers.cloudflare.com/billing/understand/preview-services/), which provides full access, free of metered usage fees, limits, and certain other restrictions.

## Why care about API security?

APIs have become the [backbone of popular web services ↗︎](https://blog.postman.com/intro-to-apis-history-of-apis/), helping the Internet become more accessible and useful.

As APIs have become more prevalent, however, so have their problems:

  * Many companies have [thousands of APIs](https://developers.cloudflare.com/api-shield/security/api-discovery/), including ones they do not even know about.
  * To support a large base of users, many APIs are protected by a negative security model that makes them vulnerable to credential-stuffing attacks and automated scanning tools.
  * With so many endpoints and users, it is difficult to recognize brute-force attacks against [specific endpoints](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/).
  * Sophisticated attacks are even harder to recognize, often because even development teams are unaware of common and uncommon [usage patterns](https://developers.cloudflare.com/api-shield/security/sequence-analytics/).



Refer to the [Get started](https://developers.cloudflare.com/api-shield/get-started/) guide to set up API Shield.

## Features

[Security features](https://developers.cloudflare.com/api-shield/security/)

Secure your APIs using API Shield's security features.

Use Security features

[Management, monitoring, and more](https://developers.cloudflare.com/api-shield/management-and-monitoring/)

Monitor the health of your API endpoints.

Use Management, monitoring, and more

## Use Schema Profiles

[Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/) provides a shared detection, analytics, and mitigation model. Schema Profile is its only current profile type.

API Shield provides two Schema Profile sources. [Schema Learning](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/) learns from traffic, while [Schema Validation](https://developers.cloudflare.com/api-shield/security/schema-validation/) uses uploaded OpenAPI schemas.

Use API Shield for API inventory, OpenAPI governance, profile export, automation, and higher-scale API workflows. Use the WAF Application Profiles pages for Profile Analysis and Custom Rule enforcement.

## Availability

Cloudflare API Security products are available to Enterprise customers only. Anyone can set up [Mutual TLS](https://developers.cloudflare.com/api-shield/security/mtls/) with a Cloudflare-managed certificate authority.

The full API Shield security suite is available as an Enterprise paid add-on. Refer to [API Shield plans](https://developers.cloudflare.com/api-shield/plans/) for feature-specific availability.

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed beta access does not imply future plan availability or pricing.

Note

API Shield currently does not work for JDCloud customers.

## Related products

[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)

Cloudflare DDoS protection secures websites, applications, and entire networks while ensuring the performance of legitimate traffic is not compromised.

[NextGet started](https://developers.cloudflare.com/api-shield/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
