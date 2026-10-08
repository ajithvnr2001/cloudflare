---
url: https://developers.cloudflare.com/network/onion-routing/
title: Onion Routing and Tor support \u00b7 Cloudflare Network settings docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:25.190547+00:00
---

# Onion Routing and Tor support · Cloudflare Network settings docs

> Source: https://developers.cloudflare.com/network/onion-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network](https://developers.cloudflare.com/network/)
  3. /Onion Routing and Tor support



# Onion Routing and Tor support

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network/onion-routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityHow it worksEnable Onion Routing

Improve the Tor user experience by enabling Onion Routing, which enables Cloudflare to serve your website’s content directly through the Tor network and without requiring exit nodes.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
## How it works

Onion Routing helps improve Tor browsing as follows:

  * Tor users no longer access your site via exit nodes, which can sometimes be compromised, and may snoop on user traffic.
  * Human Tor users and bots can be distinguished by our Onion services, such that interactive challenges are only served to malicious bot traffic.



[Tor Browser ↗︎](https://tb-manual.torproject.org/about/) users receive an [alt-svc header ↗︎](https://httpwg.org/specs/rfc7838.html#alt-svc) as part of the response to the first request to your website. The browser then creates a Tor Circuit to access this website using the `.onion` TLD service provided by this header.

You should note that the visible domain in the user interface remains unchanged, as the host header and the SNI are preserved. However, the underlying connection changes to be routed through Tor, as the [UI denotes on the left of the address bar ↗︎](https://tb-manual.torproject.org/managing-identities/#managing-identities) with a Tor Circuit. Cloudflare does not provide a certificate for the `.onion` domain provided as part of alt-svc flow, which therefore cannot be accessed via HTTPS.

## Enable Onion Routing

To enable **Onion Routing** in the dashboard:

  1. In the Cloudflare dashboard, go to the **Network** page.

[ Go to **Network** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/network)
  2. For **Onion Routing** , switch the toggle to **On**.




To enable **Onion Routing** with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `opportunistic_onion` as the setting name in the URI path, and the `value` parameter set to `"on"`.

[PreviousMaximum upload size ↗︎](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#upload-limits)[NextPseudo IPv4](https://developers.cloudflare.com/network/pseudo-ipv4/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network/onion-routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
