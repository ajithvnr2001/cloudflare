---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/spectrum_events/
title: Spectrum events \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:14.396490+00:00
---

# Spectrum events · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/spectrum_events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Zone-scoped datasets
  5. /Spectrum events



# Spectrum events

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/spectrum_events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewApplicationClientAsnClientBytesClientCountryClientIPClientMatchedIpFirewallClientPortClientProtoClientTcpRttClientTlsCipherClientTlsClientHelloServerNameClientTlsProtocolClientTlsStatusColoCodeConnectTimestampDisconnectTimestampEventIpFirewallOriginBytesOriginIPOriginPortOriginProtoOriginTcpRttOriginTlsCipherOriginTlsFingerprintOriginTlsModeOriginTlsProtocolOriginTlsStatusProxyProtocolStatusTimestamp

The descriptions below detail the fields available for `spectrum_events`.

## Application

Type: `string`

The unique public ID of the application on which the event occurred.

## ClientAsn

Type: `int`

Client AS number.

## ClientBytes

Type: `int`

The number of bytes read from the client by the Spectrum service.

## ClientCountry

Type: `string`

Country of the client IP address.

## ClientIP

Type: `string`

Client IP address.

## ClientMatchedIpFirewall

Type: `string`

Whether the connection matched any IP Firewall rules. UNKNOWN = No match or Firewall not enabled for Spectrum; _UNKNOWN_ | _ALLOW_ | _BLOCK_ERROR_ | _BLOCK_IP_ | _BLOCK_COUNTRY_ | _BLOCK_ASN_ | _WHITELIST_IP_ | _WHITELIST_COUNTRY_ | _WHITELIST_ASN_.

## ClientPort

Type: `int`

Client port.

## ClientProto

Type: `string`

Transport protocol used by client; _tcp_ | _udp_ | _unix_.

## ClientTcpRtt

Type: `int`

The TCP round-trip time in nanoseconds between the client and Spectrum.

## ClientTlsCipher

Type: `string`

The cipher negotiated between the client and Spectrum. An unknown cipher is returned as "UNK."

## ClientTlsClientHelloServerName

Type: `string`

The server name in the Client Hello message from client to Spectrum.

## ClientTlsProtocol

Type: `string`

The TLS version negotiated between the client and Spectrum; _unknown_ | _none_ | _SSLv3_ | _TLSv1_ | _TLSv1.1_ | _TLSv1.2_ | _TLSv1.3_.

## ClientTlsStatus

Type: `string`

Indicates state of TLS session from the client to Spectrum; _UNKNOWN_ | _OK_ | _INTERNAL_ERROR_ | _INVALID_CONFIG_ | _INVALID_SNI_ | _HANDSHAKE_FAILED_ | _KEYLESS_RPC_.

## ColoCode

Type: `string`

IATA airport code of the data center that received the request.

## ConnectTimestamp

Type: `int or string`

Timestamp at which both legs of the connection (client/edge, edge/origin or nexthop) were established.

## DisconnectTimestamp

Type: `int or string`

Timestamp at which the connection was closed.

## Event

Type: `string`

_connect_ | _disconnect_ | _clientFiltered_ | _tlsError_ | _resolveOrigin_ | _originError_.

## IpFirewall

Type: `bool`

Whether IP Firewall was enabled at time of connection.

## OriginBytes

Type: `int`

The number of bytes read from the origin by Spectrum.

## OriginIP

Type: `string`

Origin IP address.

## OriginPort

Type: `int`

Origin port.

## OriginProto

Type: `string`

Transport protocol used by origin; _tcp_ | _udp_ | _unix_.

## OriginTcpRtt

Type: `int`

The TCP round-trip time in nanoseconds between Spectrum and the origin.

## OriginTlsCipher

Type: `string`

The cipher negotiated between Spectrum and the origin. An unknown cipher is returned as "UNK."

## OriginTlsFingerprint

Type: `string`

SHA256 hash of origin certificate. An unknown SHA256 hash is returned as an empty string.

## OriginTlsMode

Type: `string`

If and how the upstream connection is encrypted; _unknown_ | _off_ | _flexible_ | _full_ | _strict_.

## OriginTlsProtocol

Type: `string`

The TLS version negotiated between Spectrum and the origin; _unknown_ | _none_ | _SSLv3_ | _TLSv1_ | _TLSv1.1_ | _TLSv1.2_ | _TLSv1.3_.

## OriginTlsStatus

Type: `string`

The state of the TLS session from Spectrum to the origin; _UNKNOWN_ | _OK_ | _INTERNAL_ERROR_ | _INVALID_CONFIG_ | _INVALID_SNI_ | _HANDSHAKE_FAILED_ | _KEYLESS_RPC_.

## ProxyProtocol

Type: `string`

Which form of proxy protocol is applied to the given connection; _off_ | _v1_ | _v2_ | _simple_.

## Status

Type: `int`

A code indicating reason for connection closure.

## Timestamp

Type: `int or string`

Timestamp at which the event took place.

[PreviousPage Shield events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/)[NextWebSocket Analytics](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/zone/spectrum_events.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
