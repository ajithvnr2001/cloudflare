---
url: https://developers.cloudflare.com/stream/stream-live/custom-domains/
title: Add custom ingest domains \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:48.531473+00:00
---

# Add custom ingest domains · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/stream-live/custom-domains/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Stream live video](https://developers.cloudflare.com/stream/stream-live/)
  4. /Add custom ingest domains



# Add custom ingest domains

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/stream-live/custom-domains/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDelete a custom domain

With custom ingest domains, you can configure your RTMPS feeds to use an ingest URL that you specify instead of using `live.cloudflare.com.`

Note

Custom Ingest Domains cannot be configured for domains with [zone holds](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/) enabled.

  1. In the Cloudflare dashboard, go to the **Live inputs** page.

[ Go to **Live inputs** ↗ ](https://dash.cloudflare.com/?to=/:account/stream/inputs)
  2. Select **Settings** , above the list. The **Custom Input Domains** page displays.

  3. Under **Domain** , add your domain and select **Add domain**.

  4. At your DNS provider, add a CNAME record that points to `live.cloudflare.com`. If your DNS provider is Cloudflare, this step is done automatically.




If you are using Cloudflare for DNS, ensure the [**Proxy status**](https://developers.cloudflare.com/dns/proxy-status/) of your ingest domain is **DNS only** (grey-clouded).

## Delete a custom domain

  1. From the **Custom Input Domains** page under **Hostnames** , locate the domain.
  2. Select the menu icon under **Action**. Select **Delete**.



[PreviousStart a live stream](https://developers.cloudflare.com/stream/stream-live/start-stream-live/)[NextWatch a live stream](https://developers.cloudflare.com/stream/stream-live/watch-live-stream/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/stream-live/custom-domains.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
