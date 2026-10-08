---
url: https://developers.cloudflare.com/privacy-proxy/reference/metrics/
title: Observability \u00b7 Cloudflare Privacy Proxy docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:38.314446+00:00
---

# Observability · Cloudflare Privacy Proxy docs

> Source: https://developers.cloudflare.com/privacy-proxy/reference/metrics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Privacy Proxy](https://developers.cloudflare.com/privacy-proxy/)
  3. /[Reference](https://developers.cloudflare.com/privacy-proxy/reference/)
  4. /Observability



# Observability

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/privacy-proxy/reference/metrics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewData privacy

Privacy Proxy provides two methods for accessing metrics and monitoring your proxy deployment. We recommend getting started with GraphQL as the default method for observability.

  * [GraphQL Analytics API](https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/)
  * [OpenTelemetry](https://developers.cloudflare.com/privacy-proxy/reference/metrics/opentelemetry/)



## Data privacy

Regardless of whether you use the GraphQL Analytics API or OpenTelemetry, Privacy Proxy observability data does not include:

  * User IP addresses
  * Request content or headers (beyond what is needed for metrics)
  * Destination URLs or hostnames (aggregated only)
  * Authentication tokens or credentials



Both methods export only operational metrics that help you monitor service health without compromising user privacy.

[PreviousProxy status reference](https://developers.cloudflare.com/privacy-proxy/reference/proxy-status/)[NextGraphQL Analytics API](https://developers.cloudflare.com/privacy-proxy/reference/metrics/graphql/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/privacy-proxy/reference/metrics/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
