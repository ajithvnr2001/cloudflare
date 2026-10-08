---
url: https://developers.cloudflare.com/network/grpc-connections/
title: gRPC connections \u00b7 Cloudflare Network settings docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:25.087340+00:00
---

# gRPC connections · Cloudflare Network settings docs

> Source: https://developers.cloudflare.com/network/grpc-connections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network](https://developers.cloudflare.com/network/)
  3. /gRPC connections



# gRPC connections

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network/grpc-connections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityLimitationsEnable gRPC Requirements Procedure

Cloudflare offers support for gRPC to protect your APIs on any [proxied gRPC endpoints](https://developers.cloudflare.com/dns/proxy-status/). The gRPC protocol helps build efficient APIs with smaller payloads for reduced bandwidth usage, decreased latency, and faster implementations.

Note

When gRPC is not enabled on a zone, Cloudflare will respond to gRPC requests with a `403 Forbidden` response.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
Charges may occur for gRPC traffic over add-on products such as [Argo Smart Routing](https://developers.cloudflare.com/argo-smart-routing/), [WAF](https://developers.cloudflare.com/waf/), and [Bot Management](https://developers.cloudflare.com/bots/).

## Limitations

Running gRPC traffic on Cloudflare is compatible with most Cloudflare products.

However, the following products have limited capabilities with gRPC requests:

  * The [Cloudflare WAF](https://developers.cloudflare.com/waf/) will only run for header inspection during the connection phase. WAF Managed Rules will not run on the content of a gRPC stream.
  * Cloudflare Tunnel supports gRPC traffic via [private subnet routing](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/). Public hostname deployments are not currently supported.

  * [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) does not support gRPC traffic sent through Cloudflare’s reverse proxy. gRPC traffic will be ignored by Access if gRPC is enabled in Cloudflare. We recommend disabling gRPC for any sensitive origin servers protected by Access or enabling another means of authenticating gRPC traffic to your origin servers.



## Enable gRPC

### Requirements

  * Your gRPC endpoint must listen on port 443.
  * Your gRPC endpoint must support TLS and HTTP/2.
  * HTTP/2 must be advertised over ALPN.
  * Use `application/grpc` or `application/grpc+<message type` (for example: `application/grpc+proto`) for the **Content-Type** header of gRPC requests.
  * Make sure that the hostname that hosts your gRPC endpoint: 
    * Is set to [proxied](https://developers.cloudflare.com/dns/proxy-status/)
    * Uses at least the [Full SSL/TLS encryption mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/).



### Procedure

To change the **gRPC** setting in the dashboard:

  1. Log in to your [Cloudflare account ↗︎](https://dash.cloudflare.com) and go to a specific domain.
  2. Go to **Network**.
  3. For **gRPC** , switch the toggle to **On**.



[PreviousOverview](https://developers.cloudflare.com/network/)[NextIP geolocation](https://developers.cloudflare.com/network/ip-geolocation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network/grpc-connections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
