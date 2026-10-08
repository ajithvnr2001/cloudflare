---
url: https://developers.cloudflare.com/byoip/concepts/prefix-delegations/
title: Prefix delegations \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.974578+00:00
---

# Prefix delegations · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/concepts/prefix-delegations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /Concepts
  4. /Prefix delegations



# Prefix delegations

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/concepts/prefix-delegations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCDNSpectrumAPI calls for prefix delegationsConfigure prefix delegations

Prefix delegations allow a prefix owner (Account A) to grant another Cloudflare account (Account B) permission to use all or part of their BYOIP prefix. The original prefix remains managed by Account A, but Account B can use the delegated IPs with CDN services (including Cloudflare for SaaS) or Spectrum. Refer to [service bindings](https://developers.cloudflare.com/byoip/service-bindings/) for more information on the services an IP can be bound to.

## CDN

CDN delegations allow you to use the IP(s) with [Address Maps](https://developers.cloudflare.com/byoip/address-maps/) or [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) customers.

Address Maps allows you to assign IPs either at the account level or zone level.

In the Cloudflare for SaaS example, Account A is using BYOIP + CDN and Cloudflare for SaaS. Account A can validate and serve traffic for a custom hostname on any of the IPs in its prefix. If Account A delegates some or all of the prefix to Account B, Account B may also validate and serve traffic for custom hostnames on those IPs as well. This is very useful if you use Cloudflare for SaaS but manage different configurations in different accounts. All the accounts can use the IPs through a delegation.

## Spectrum

If Account A delegates use of part or all of a prefix to Account B via a prefix delegation, Account B can also use the [Spectrum API](https://developers.cloudflare.com/spectrum/about/byoip/) with the IPs it was delegated access to.

**Example:** Account A is the primary owner of prefix 1.2.3.0/24. Account A delegates the use of 1.2.3.0/32 to Account B. Account B can now use the Spectrum API to create a Spectrum app with 1.2.3.0/32.

## API calls for prefix delegations

API calls for delegations can be found at [Prefix Delegations](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/delegations/methods/list/).

Note

The dashboard only supports delegation of an entire prefix. If you want to delegate less than the entire prefix, use the API.

To bind an IP from one service to another, use the API.

## Configure prefix delegations

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select your account.
  2. Go to **IP Addresses** > **BYOIP Prefixes**.
  3. Select **Edit** to modify a prefix. **Edit IP Prefixes** displays.
  4. At the bottom of the page, select **Add Delegation**. Other accounts that your user is a part of will auto-load when you create the delegation.
  5. Select **Save**.
  6. Bind IPs to a service via the [Service Bindings API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/) as needed.



[PreviousLetter of Agency](https://developers.cloudflare.com/byoip/concepts/loa/)[NextStatic IPs](https://developers.cloudflare.com/byoip/concepts/static-ips/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/concepts/prefix-delegations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
