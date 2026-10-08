---
url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/
title: TLS 1.3 \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:38.792889+00:00
---

# TLS 1.3 · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /Additional options
  5. /TLS 1.3



# TLS 1.3

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is TLS 1.3?AvailabilityEnable TLS 1.3 TroubleshootingLimitations

TLS 1.3 enables the latest version of the TLS protocol (when supported) for improved security and performance.

## What is TLS 1.3?

TLS 1.3 is the newest, fastest, and most secure version of the [TLS protocol](https://developers.cloudflare.com/ssl/reference/protocols/).

By turning on the TLS 1.3 feature, traffic to and from your website will be served over the TLS 1.3 protocol when supported by clients. TLS 1.3 protocol has improved latency over older versions, has several new features, and is currently supported in all updated major browsers.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
## Enable TLS 1.3

TLS 1.3 can be activated in the Cloudflare dashboard or through the API:

To enable TLS 1.3 in the dashboard:

  1. In the Cloudflare dashboard, go to the **Edge Certificates** page.

[ Go to **Edge Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates)
  2. For **TLS 1.3** , switch the toggle to **On**.




To adjust your TLS 1.3 settings with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `tls_1_3` as the setting name in the URI path, and set the `value` parameter to your desired setting (`"on"`, `"zrt"` or `"off"`). `zrt` refers to [Zero Round Trip Time Resumption (0-RTT) ↗︎](https://blog.cloudflare.com/introducing-0-rtt/).

### Troubleshooting

Since TLS 1.3 implementations are relatively new, some failures may occur. If you experience errors, submit a Cloudflare Support ticket with the following information:

  * Steps to replicate the issue (if possible)
  * Client build version
  * Client diagnostic information
  * Packet captures



Chrome users should submit a [net-internals trace ↗︎](https://dev.chromium.org/for-testers/providing-network-details) to Google. Firefox users should [report bugs to Mozilla ↗︎](https://bugzilla.mozilla.org/home).

## Limitations

You cannot set specific TLS 1.3 ciphers. Instead, you can enable [TLS 1.3](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/#enable-tls-13) for your entire zone and Cloudflare will use [all applicable TLS 1.3 cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/). In combination with this, you can still [disable weak cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/) for TLS 1.0-1.2.

[PreviousCertificate Signing Requests (CSRs)](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-signing-requests/)[NextMinimum TLS Version](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/additional-options/tls-13.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
