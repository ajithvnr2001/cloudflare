---
url: https://developers.cloudflare.com/ohttp-relay/
title: Overview \u00b7 Cloudflare OHTTP Relay docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:27.774860+00:00
---

# Overview · Cloudflare OHTTP Relay docs

> Source: https://developers.cloudflare.com/ohttp-relay/

  1. [Home](https://developers.cloudflare.com/)
  2. /Cloudflare OHTTP Relay



# Cloudflare OHTTP Relay

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ohttp-relay/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityFeatures

Implements the Oblivious HTTP IETF standard to improve client privacy.

Enterprise-only

[Cloudflare OHTTP Relay (formerly Privacy Gateway) ↗︎](https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/) is a managed service deployed on Cloudflare’s global network that implements part of the [Oblivious HTTP (OHTTP) IETF ↗︎](https://www.ietf.org/archive/id/draft-thomson-http-oblivious-01.html) standard. The goal of Cloudflare OHTTP Relay and Oblivious HTTP is to hide the client's IP address when interacting with an application backend.

OHTTP introduces a trusted third party between client and server, called a relay, whose purpose is to forward encrypted requests and responses between client and server. These messages are encrypted between client and server such that the relay learns nothing of the application data, beyond the length of the encrypted message and the server the client is interacting with.

* * *

## Availability

Cloudflare OHTTP Relay is currently in closed beta – available to select privacy-oriented companies and partners. If you are interested, [contact us ↗︎](https://www.cloudflare.com/lp/privacy-edge/).

* * *

## Features

[Get started](https://developers.cloudflare.com/ohttp-relay/get-started/)

Learn how to set up Cloudflare OHTTP Relay for your application.

Get started

[Legal](https://developers.cloudflare.com/ohttp-relay/reference/legal/)

Learn about the different parties and data shared in Cloudflare OHTTP Relay.

Learn more

[Metrics](https://developers.cloudflare.com/ohttp-relay/reference/metrics/)

Learn about how to query Cloudflare OHTTP Relay metrics.

Learn more

[NextGet started](https://developers.cloudflare.com/ohttp-relay/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ohttp-relay/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
