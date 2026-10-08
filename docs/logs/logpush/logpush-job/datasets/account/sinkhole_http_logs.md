---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs/
title: Sinkhole HTTP Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:12.961175+00:00
---

# Sinkhole HTTP Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Sinkhole HTTP Logs



# Sinkhole HTTP Logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccountIDBodyBodyLengthDestAddrHeadersHostMethodPasswordR2PathReferrerSinkholeIDSrcAddrTimestampURIURLUserAgentUsername

The descriptions below detail the fields available for `sinkhole_http_logs`.

## AccountID

Type: `string`

The Account ID.

## Body

Type: `string`

The request body.

## BodyLength

Type: `int`

The length of request body.

## DestAddr

Type: `string`

The destination IP address of the request.

## Headers

Type: `string`

The request headers. If a header has multiple values, the values are comma separated. Each header is separated by the escaped newline character (\n).

## Host

Type: `string`

The host the request was sent to.

## Method

Type: `string`

The request method.

## Password

Type: `string`

The request password.

## R2Path

Type: `string`

The path to the object within the R2 bucket linked to this sinkhole that stores overflow body and header data. Blank if neither headers nor body was larger than 256 bytes.

## Referrer

Type: `string`

The referrer of the request.

## SinkholeID

Type: `string`

The ID of the Sinkhole that logged the HTTP Request.

## SrcAddr

Type: `string`

The sender's IP address.

## Timestamp

Type: `int or string`

The date and time the sinkhole HTTP request was logged.

## URI

Type: `string`

The request Uniform Resource Identifier.

## URL

Type: `string`

The request Uniform Resource Locator.

## UserAgent

Type: `string`

The request user agent.

## Username

Type: `string`

The request username.

[PreviousNetwork Analytics Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/network_analytics_logs/)[NextSSH Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
