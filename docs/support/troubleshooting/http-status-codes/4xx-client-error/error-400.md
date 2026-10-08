---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-400/
title: Error 400 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.356350+00:00
---

# Error 400 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-400/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 400



# Error 400

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-400/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview400 Bad Request Common use cases Cloudflare-specific information

## 400 Bad Request

This error indicates that the client sent a request to the server that could not be understood or processed due to issues with the request itself.

For more information, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.1).

### Common use cases

A `400 Bad Request` error occurs due to client-side issues, such as malformed request syntax, invalid request content, message framing problems, or deceptive request routing. For example:

  * If the request contains a special character that is not properly [URL Encoded (or percent-encoded) ↗︎](https://en.wikipedia.org/wiki/Percent-encoding), an `HTTP Error 400` will be returned.
  * If the request contains both `Content Length` and `Transfer Encoding` chunked, these two framing methods contradict each other. `Content Length` declares a fixed size body, while chunked encoding declares a streamed body with no known size. [RFC 9112 section 6.3 ↗︎](https://www.rfc-editor.org/rfc/rfc9112#section-6.3) states that when `Transfer Encoding` is present, the `Content Length` header must be ignored and a request that includes both is considered malformed. This creates ambiguity in body framing and can enable request smuggling if different systems parse the boundary differently. Cloudflare follows the RFC and an `HTTP Error 400` will be returned.



### Cloudflare-specific information

If you encounter an HTTP error while using the [Cloudflare API](https://developers.cloudflare.com/api/), make sure that you are using the correct syntax, parameters, and body for your API call.

[PreviousOverview](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)[NextError 401](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-401/)

Was this helpful?

YesNo
