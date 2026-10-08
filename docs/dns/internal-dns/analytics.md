---
url: https://developers.cloudflare.com/dns/internal-dns/analytics/
title: Analytics and logs \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:57.526970+00:00
---

# Analytics and logs · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/internal-dns/analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Internal DNS](https://developers.cloudflare.com/dns/internal-dns/)
  4. /Analytics and logs



# Analytics and logs

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/internal-dns/analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGraphQLLogs

Internal DNS leverages [Gateway analytics](https://developers.cloudflare.com/cloudflare-one/insights/analytics/gateway/). Below you can find information about specific fields and different methods you can use to access this data.

## GraphQL

For detailed metrics, use the [GraphQL API](https://developers.cloudflare.com/analytics/graphql-api/). Refer to the GraphQL Analytics API documentation for guidance on how to [get started](https://developers.cloudflare.com/analytics/graphql-api/getting-started/).

The [fields](https://developers.cloudflare.com/analytics/graphql-api/getting-started/querying-basics/) added to cover Internal DNS are the following:

  * `InternalDNSFallbackStrategy`: The fallback strategy applied to the internal DNS response. Empty if no fallback strategy was applied.
  * `InternalDNSRCode`: The response code sent back by the internal DNS service.
  * `InternalDNSViewID`: The view identifier that was sent to the internal DNS service.
  * `InternalDNSZoneID`: The internal zone identifier returned by the internal DNS service.



## Logs

Leverage Logpush jobs for [Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/#internaldnsfallbackstrategy). For help setting up Logpush, refer to [Logpush](https://developers.cloudflare.com/logs/logpush/) documentation.

You can also set up [Logpush filters](https://developers.cloudflare.com/logs/logpush/logpush-job/filters/) to only push logs related to a specific [internal zone](https://developers.cloudflare.com/dns/internal-dns/internal-zones/) or [view](https://developers.cloudflare.com/dns/internal-dns/dns-views/) ID.

[PreviousConnectivity](https://developers.cloudflare.com/dns/internal-dns/connectivity/)[NextOverview](https://developers.cloudflare.com/dns/dns-firewall/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/internal-dns/analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
