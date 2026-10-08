---
url: https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/
title: HTTP/3 inspection \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:11.829556+00:00
---

# HTTP/3 inspection · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

  4. /[HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/)
  5. /HTTP/3 inspection



# HTTP/3 inspection

Last updated Apr 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTurn on HTTP/3 inspection Application limitationsExempt HTTP/3 traffic from inspectionForce HTTP/2 traffic

HTTP/3 uses the QUIC protocol over UDP instead of TCP. Because Gateway's default proxy only handles TCP traffic, HTTP/3 inspection requires turning on the UDP proxy. Without it, HTTP/3 traffic bypasses HTTP inspection. [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) still apply to the underlying UDP traffic.

Gateway applies HTTP policies to HTTP/3 traffic last. For more information, refer to the [order of enforcement](https://developers.cloudflare.com/cloudflare-one/traffic-policies/order-of-enforcement/#http3-traffic).

## Turn on HTTP/3 inspection

Before you can inspect any HTTPS traffic, you must deploy a [user-side certificate](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/) to your devices and turn on [TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/). To inspect HTTP/3 traffic, you must also turn on the [Gateway proxy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/) for UDP.

To turn on the Gateway proxy for UDP and TLS decryption:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Traffic settings**.
  2. In **Proxy and inspection** , turn on **Allow Secure Web Gateway to proxy traffic**.
  3. Select **TCP** and **UDP**.
  4. Turn on **TLS decryption**.



### Application limitations

Gateway can inspect HTTP/3 traffic from Mozilla Firefox and Microsoft Edge by establishing an HTTP/3 proxy connection. Gateway will then terminate the HTTP/3 connection, decrypt and inspect the traffic, and connect to the destination server over HTTP/2. Gateway can also inspect other HTTP applications, such as cURL.

If both the UDP proxy and TLS decryption are turned on, Google Chrome will automatically cancel HTTP/3 connections and retry them over HTTP/2, which Gateway can inspect. If either the UDP proxy or TLS decryption is turned off, HTTP/3 traffic from Chrome bypasses inspection entirely.

Caution

If you do not turn on the UDP proxy, HTTP/3 traffic from browsers other than Chrome will bypass HTTP policy enforcement. Network policies still apply.

## Exempt HTTP/3 traffic from inspection

If you require HTTP/3 traffic with end-to-end encryption from the client to the origin while still using the Gateway proxy, you can create a [Do Not Inspect HTTP policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#do-not-inspect) to match the desired traffic. Using a Do Not Inspect policy allows HTTP/3 traffic to preserve proxy performance and end-to-end encryption by bypassing Gateway's TLS decryption and inspection.

## Force HTTP/2 traffic

To apply Gateway policies to HTTP traffic without turning on the UDP proxy, you must turn off QUIC in your users' browsers to ensure only HTTP/2 traffic reaches Gateway.

Google Chrome

  1. Go to `chrome://flags`
  2. Set **Experimental QUIC protocol** to _Disabled_.
  3. Relaunch Chrome.



Safari

You cannot turn off QUIC in Safari. All traffic will be sent over HTTP/3.

Firefox

  1. Go to `about:config`.
  2. If you receive a warning, select **Accept the Risk and Continue**.
  3. Set **network.http.http3.enable** to _false_.
  4. Relaunch Firefox.



Microsoft Edge

  1. Go to `edge://flags`
  2. Set **Experimental QUIC protocol** to _Disabled_.
  3. Relaunch Edge.



[PreviousTLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/)[NextApplication Granular Controls](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/granular-controls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-policies/http-policies/http3.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
