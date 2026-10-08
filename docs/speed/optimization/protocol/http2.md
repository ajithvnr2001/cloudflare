---
url: https://developers.cloudflare.com/speed/optimization/protocol/http2/
title: HTTP/2 \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:36.313991+00:00
---

# HTTP/2 · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/protocol/http2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

Settings

  4. /Protocol optimization
  5. /HTTP/2



# HTTP/2

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/protocol/http2/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityEnable HTTP/2Disable HTTP/2ERR_HTTP2_PROTOCOL_ERROR Malformed HTTP response headers Compression issues

HTTP/2 uses the TCP transport protocol and TLS to secure communications and improves page load times.

Note

For more background on HTTP/2, visit the [Learning Center ↗︎](https://www.cloudflare.com/learning/performance/http2-vs-http1.1/).

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Can customize | No | Yes | Yes | Yes  
  
## Enable HTTP/2

HTTP/2 is enabled by default for all plans (though it does require an [SSL certificate at Cloudflare’s edge network](https://developers.cloudflare.com/ssl/get-started/)).

## Disable HTTP/2

Domains on Free plans cannot disable Cloudflare's HTTP/2 setting.

To disable **HTTP/2** in the dashboard:

  1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com).
  2. Select your account and zone.
  3. Go to **Speed** > **Settings**.
  4. Go to **Protocol Optimization**.
  5. For **HTTP/2** , switch the toggle to **Off**.



To disable **HTTP/2** with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `http2` as the setting name in the URI path, and the `value` parameter set to `"off"`.

## ERR_HTTP2_PROTOCOL_ERROR

Requests proxied by Cloudflare may result in an error for visitors with the error code `ERR_HTTP2_PROTOCOL_ERROR` visible in the Developer Tools Console. These errors are usually due to an issue on the origin web server configuration, but might only materialize when requests are proxied by Cloudflare depending on the client browser's behavior. Some possible causes are:

### Malformed HTTP response headers

The origin web server may be sending improperly formatted HTTP response headers.

#### Resolution

Make a request directly to your origin web server and inspect its HTTP response headers for anomalies. Make sure that the field values respect the following requirements:

  * [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110.html#section-5.5)
  * [RFC 9113 ↗︎](https://www.rfc-editor.org/rfc/rfc9113.html#section-8.2.1)
  * [RFC 5234 ↗︎](https://www.rfc-editor.org/rfc/rfc5234#appendix-B.1)



### Compression issues

Examples of compression issues include the origin web server serving gzip encoded compressed content but failing to update the `Content-Length` header, or the origin web server serving broken gzip compressed content.

#### Resolution

You can try to disable compression at your origin web server and rely on Cloudflare to [compress content](https://developers.cloudflare.com/speed/optimization/content/compression/).

You can also review your origin server's compression settings to make sure the compression is working as expected.

[PreviousTurn off Auto Minify](https://developers.cloudflare.com/speed/optimization/content/troubleshooting/disable-auto-minify/)[NextHTTP/3 (with QUIC)](https://developers.cloudflare.com/speed/optimization/protocol/http3/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/protocol/http2.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
