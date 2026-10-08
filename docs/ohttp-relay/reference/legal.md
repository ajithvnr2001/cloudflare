---
url: https://developers.cloudflare.com/ohttp-relay/reference/legal/
title: Legal \u00b7 Cloudflare OHTTP Relay docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:27.929158+00:00
---

# Legal · Cloudflare OHTTP Relay docs

> Source: https://developers.cloudflare.com/ohttp-relay/reference/legal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare OHTTP Relay](https://developers.cloudflare.com/ohttp-relay/)
  3. /[Reference](https://developers.cloudflare.com/ohttp-relay/reference/)
  4. /Legal



# Legal

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ohttp-relay/reference/legal/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat Cloudflare seesWhat Cloudflare storesWhat Cloudflare OHTTP Relay customers see

Cloudflare OHTTP Relay (formerly Privacy Gateway) is a managed gateway service deployed on Cloudflare’s global network that implements the Oblivious HTTP IETF standard to improve client privacy when connecting to an application backend.

OHTTP introduces a trusted third party (Cloudflare in this case), called a relay, between client and server. The relay’s purpose is to forward requests from client to server, and likewise to forward responses from server to client. These messages are encrypted between client and server such that the relay learns nothing of the application data, beyond the server the client is interacting with.

The Cloudflare OHTTP Relay service follows [Cloudflare’s privacy policy ↗︎](https://www.cloudflare.com/privacypolicy/).

## What Cloudflare sees

While Cloudflare will never see the contents of the encrypted application HTTP request proxied through the Cloudflare OHTTP Relay service – because the client will first connect to the OHTTP relay server operated in Cloudflare’s global network– Cloudflare will see the following information: the connecting device’s IP address, the application service they are using, including its DNS name and IP address, and metadata associated with the request, including the type of browser, device operating system, hardware configuration, and timestamp of the request ("Cloudflare OHTTP Relay Logs").

## What Cloudflare stores

Cloudflare retains the Cloudflare OHTTP Relay Logs information for the most recent quarter plus one month (approximately 124 days).

## What Cloudflare OHTTP Relay customers see

  * The application content of requests.
  * The IP address and associated metadata of the Cloudflare OHTTP Relay server the request came from.



[PreviousProduct compatibility](https://developers.cloudflare.com/ohttp-relay/reference/product-compatibility/)[NextLimitations](https://developers.cloudflare.com/ohttp-relay/reference/limitations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ohttp-relay/reference/legal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
