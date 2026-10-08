---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-421/
title: Error 421 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:54.589165+00:00
---

# Error 421 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-421/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 421



# Error 421

Last updated Sep 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-421/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview421 Misdirected Request Common use cases Cloudflare-specific information

## 421 Misdirected Request

The `421 Misdirected Request` status code indicates that the request was directed to a server that is not able to produce a response for the combination of scheme and authority included in the request URI.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.20).

### Common use cases

This error commonly occurs in HTTP/2 and HTTP/3 environments where connection reuse or alternative service selection is involved. A server may return a `421` response when:

  * The `Host` header value does not match the SNI (Server Name Indication) used during the TLS handshake, causing the server to reject the request as misdirected.
  * A single HTTP/2 connection is reused (coalesced) across multiple origins, but the server is not configured to respond for one of those origins.
  * The client selected an alternative service (via the `Alt-Svc` header) that cannot handle the request for that specific scheme and host combination.



Upon receiving a `421`, the client may retry the request on a new connection.

### Cloudflare-specific information

Cloudflare may generate or forward a `421` response in several scenarios:

  * **SNI mismatch** : The most common cause. If the SNI value used during the TLS handshake does not match the `Host` header in the HTTP request, Cloudflare returns `421` directly. Ensure your TLS certificate covers all hostnames you intend to serve — for example, use a wildcard or SAN certificate.
  * **Connection coalescing** : Cloudflare may coalesce HTTP/2 or HTTP/3 connections across multiple origins. If the origin is not configured to serve all coalesced hostnames, a `421` results. Verify that your origin correctly handles all domain names sharing a connection.
  * **Cloudflare Tunnel** : A `421` can occur if the tunnel ingress rule hostname does not match the request's `Host` header. Review your tunnel ingress configuration.
  * **R2 and Workers custom domains** : A mismatch between the custom domain TLS SNI and the requested hostname can produce a `421`. Verify that the custom domain is correctly configured and that the TLS certificate covers the relevant hostname.



If you receive a `421`, retry the request on a new connection with the correct SNI and host combination.

[PreviousError 417](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-417/)[NextError 429](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-429/)

Was this helpful?

YesNo
