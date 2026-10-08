---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/indicator-feeds/
title: Use indicator feeds to improve security policies \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:58.112079+00:00
---

# Use indicator feeds to improve security policies · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/indicator-feeds/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Understand and streamline policy creation](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/)
  5. /Use indicator feeds to improve security policies



# Use indicator feeds to improve security policies

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/indicator-feeds/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSubscribe to indicator feeds

When building DNS, network, or HTTP policies to block malicious activity for your organization, you can use external indicator feeds supplied by Cloudflare and other third-party providers.

## Subscribe to indicator feeds

Cloudflare threat intelligence data consists of a data exchange between providers and subscribers.

A provider is an organization that has a set of data that they are interested in sharing with other Cloudflare organizations. Any organization can be a provider. Examples of current providers are Government Cyber Defense groups.

Subscribers can be any Cloudflare customer that wants to secure their environment further by creating rules based on provider datasets. Subscribers must be authorized by a provider. Authorization is granted using the [Grant permission to indicator feed endpoint](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/subresources/permissions/methods/create/).

To subscribe to an indicator feed, contact your account team. For more information, refer to [Custom Indicator Feeds](https://developers.cloudflare.com/security-center/indicator-feeds/).

[PreviousCreate a list of IPs or domains](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/create-list/)[NextOverview](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/understand-policies/indicator-feeds.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
