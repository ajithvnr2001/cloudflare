---
url: https://developers.cloudflare.com/privacy-proxy/
title: Privacy Proxy \u00b7 Cloudflare Privacy Proxy docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:37.746026+00:00
---

# Privacy Proxy · Cloudflare Privacy Proxy docs

> Source: https://developers.cloudflare.com/privacy-proxy/

  1. [Home](https://developers.cloudflare.com/)
  2. /Privacy Proxy



# Privacy Proxy

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/privacy-proxy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesRelated productsAvailability

A MASQUE-based forward proxy that protects user privacy while preserving geolocation accuracy.

Enterprise-only

Privacy Proxy is a managed proxy service that runs on Cloudflare's global network. It uses the [MASQUE ↗︎](https://datatracker.ietf.org/wg/masque/about/) protocol suite to proxy TCP and UDP traffic via HTTP CONNECT and CONNECT-UDP methods over HTTP/2 and HTTP/3.

Privacy Proxy separates user identity from user activity. Users authenticate to the proxy without revealing which destinations they visit, and destination servers see requests from Cloudflare IP addresses without learning who made them.

Privacy Proxy powers services like [Microsoft Edge Secure Network ↗︎](https://blog.cloudflare.com/cloudflare-now-powering-microsoft-edge-secure-network/) and serves as a second-hop relay for [iCloud Private Relay ↗︎](https://blog.cloudflare.com/icloud-private-relay/).

* * *

## Features

[Single-hop deployment](https://developers.cloudflare.com/privacy-proxy/concepts/deployment-models/#single-hop)

Deploy Privacy Proxy as a standalone proxy where Cloudflare handles authentication, proxying, and egress.

Use Single-hop deployment

[Double-hop deployment](https://developers.cloudflare.com/privacy-proxy/concepts/deployment-models/#double-hop)

Operate your own first-hop proxy to authenticate users, then relay traffic through Cloudflare for additional privacy separation.

Use Double-hop deployment

[Geolocation preservation](https://developers.cloudflare.com/privacy-proxy/concepts/geolocation/)

Maintain accurate geolocation for users without exposing their real IP addresses, ensuring location-relevant content and services work correctly.

Use Geolocation preservation

[Privacy Pass authentication](https://developers.cloudflare.com/privacy-proxy/concepts/authentication/)

Authenticate users with Privacy Pass tokens for production deployments, ensuring privacy-preserving access control.

Use Privacy Pass authentication

* * *

## Related products

[Cloudflare OHTTP Relay](https://developers.cloudflare.com/ohttp-relay/)

Cloudflare OHTTP Relay (formerly Privacy Gateway) implements the Oblivious HTTP (OHTTP) standard for request-level privacy, hiding client IP addresses from application backends.

[WARP Client](https://developers.cloudflare.com/warp-client/)

Cloudflare's consumer VPN application that uses similar privacy-preserving proxy technology.

* * *

## Availability

Privacy Proxy is available as a managed service for Enterprise customers. [Contact us ↗︎](https://www.cloudflare.com/lp/privacy-edge/) to discuss your use case and get started.

[NextGet started](https://developers.cloudflare.com/privacy-proxy/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/privacy-proxy/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
