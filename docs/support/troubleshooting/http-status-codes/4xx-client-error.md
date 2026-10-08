---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/
title: 4xx Client Error \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.280200+00:00
---

# 4xx Client Error · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)

  4. /[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)
  5. /4xx Client Error



# 4xx Client Error

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLog Explorer400 Bad Request401 Unauthorized402 Payment Required403 Forbidden404 Not Found405 Method Not Allowed406 Not Acceptable407 Authentication Required408 Request Timeout409 Conflict410 Gone411 Length Required412 Precondition Failed413 Payload Too Large414 URI Too Long415 Unsupported Media Type416 Range Not Satisfiable417 Expectation Failed421 Misdirected Request429 Too Many Requests451 Unavailable For Legal Reason499 Client Close Request

`4xx` codes are error responses that indicate an issue on the client's end, potentially due to a network problem.

  * `4xx` codes can be used as a response to any request method.
  * The origin server should include an explanation, which should be displayed by the User-Agent, except in the case of a `HEAD` request.
  * [Custom rules](https://developers.cloudflare.com/waf/custom-rules/) can return any response code in the range of `400–499` on your HTML page if the site owner has created a rule with the _Block_ action and configured a custom response code. For more details, refer to [custom response](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests).



## Log Explorer

[Log Explorer](https://developers.cloudflare.com/log-explorer/) provides access to Cloudflare logs with all the context available within the Cloudflare platform. You can monitor security and performance issues with custom dashboards or investigate and troubleshoot issues with log search. Log explorer [allows you to build queries](https://developers.cloudflare.com/log-explorer/log-search/) filtering for a specific [Ray ID](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/), which can be useful to investigate HTTP Errors.

## 400 Bad Request

For a complete description of this error refer to the [Error 400](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-400/) page.

## 401 Unauthorized

For a complete description of this error refer to the [Error 401](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-401/) page.

## 402 Payment Required

The `402 Payment Required` status code is reserved for future use and is not yet implemented according to the standards outlined in [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5).

## 403 Forbidden

For a complete description of this error refer to the [Error 403](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/) page.

## 404 Not Found

For a complete description of this error refer to the [Error 404](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-404/) page.

## 405 Method Not Allowed

For a complete description of this error refer to the [Error 405](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-405/) page.

## 406 Not Acceptable

For a complete description of this error refer to the [Error 406](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-406/) page.

## 407 Authentication Required

For a complete description of this error refer to the [Error 407](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-407/) page.

## 408 Request Timeout

For a complete description of this error refer to the [Error 408](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-408/) page.

## 409 Conflict

For a complete description of this error refer to the [Error 409](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-409/) page.

## 410 Gone

For a complete description of this error refer to the [Error 410](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-410/) page.

## 411 Length Required

For a complete description of this error refer to the [Error 411](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-411/) page.

## 412 Precondition Failed

For a complete description of this error refer to the [Error 412](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-412/) page.

## 413 Payload Too Large

For a complete description of this error refer to the [Error 413](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-413/) page.

## 414 URI Too Long

For a complete description of this error refer to the [Error 414](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-414/) page.

## 415 Unsupported Media Type

For a complete description of this error refer to the [Error 415](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-415/) page.

## 416 Range Not Satisfiable

For a complete description of this error refer to the [Error 416](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-416/) page.

## 417 Expectation Failed

For a complete description of this error refer to the [Error 417](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-417/) page.

## 421 Misdirected Request

For a complete description of this error refer to the [Error 421](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-421/) page.

## 429 Too Many Requests

For a complete description of this error refer to the [Error 429](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-429/) page.

## 451 Unavailable For Legal Reason

For a complete description of this error refer to the [Error 451](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-451/) page.

## 499 Client Close Request

For a complete description of this error refer to the [Error 499](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/) page.

[Previous3xx Redirection](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/3xx-redirection/)[NextError 400](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-400/)

Was this helpful?

YesNo
