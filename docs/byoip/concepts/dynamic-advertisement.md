---
url: https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/
title: Dynamic advertisement \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.791014+00:00
---

# Dynamic advertisement · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /Concepts
  4. /Dynamic advertisement



# Dynamic advertisement

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Dynamic advertisement allows you to control when Cloudflare announces your IP prefixes via BGP. When a prefix is advertised, Cloudflare announces it to the Internet so that traffic destined for those IPs can be routed to Cloudflare. When a prefix is withdrawn, Cloudflare stops announcing it — traffic will then follow whatever other BGP routes exist for that prefix.

You can advertise and withdraw prefixes on demand using the [Cloudflare API](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/#via-the-api) or the [IP Prefixes page](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/#via-the-cloudflare-dashboard) in the Cloudflare dashboard. Enabling advertisement typically takes two to seven minutes, and disabling advertisement takes approximately 15 minutes.

When using the API, you can authorize the call with your email and API key or create a service token for this purpose. A successful API response indicates the service registered the request.

Both the API and the Cloudflare dashboard support [prefix delegations](https://developers.cloudflare.com/byoip/concepts/prefix-delegations/), which allow other Cloudflare accounts to interact with your prefix. The effect of a delegation is service-specific.

[PreviousGet started](https://developers.cloudflare.com/byoip/get-started/)[NextBest practices](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/concepts/dynamic-advertisement/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
