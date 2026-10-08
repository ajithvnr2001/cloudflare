---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/
title: Gateway Network \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:12.874322+00:00
---

# Gateway Network · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Gateway Network



# Gateway Network

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccountIDActionApplicationIDsApplicationNamesCategoryIDsCategoryNamesDatetimeDestinationIPDestinationIPContinentCodeDestinationIPCountryCodeDestinationPortDetectedProtocolDeviceIDDeviceNameEmailIsIsolatedOfframpOnrampOverrideIPOverridePortPolicyIDPolicyNameProxyEndpointRegistrationIDSNISessionIDSourceIPSourceIPContinentCodeSourceIPCountryCodeSourceInternalIPSourcePortTenantIDTransport (deprecated)TransportProtocolUserIDVirtualNetworkIDVirtualNetworkName

The descriptions below detail the fields available for `gateway_network`.

## AccountID

Type: `string`

Cloudflare account tag.

## Action

Type: `string`

Action performed by gateway on the session.

## ApplicationIDs

Type: `array[int]`

IDs of the applications that matched the session parameters.

## ApplicationNames

Type: `array[string]`

Names of the applications that matched the session parameters.

## CategoryIDs

Type: `array[int]`

IDs of the categories that matched the session parameters.

## CategoryNames

Type: `array[string]`

Names of the categories that matched the session parameters.

## Datetime

Type: `int or string`

The date and time the corresponding network session was made (for example, '2021-07-27T00:01:07Z').

## DestinationIP

Type: `string`

Destination IP of the network session.

## DestinationIPContinentCode

Type: `string`

Continent code of the destination IP of the network session (for example, 'NA').

## DestinationIPCountryCode

Type: `string`

Country code of the destination IP of the network session (for example, 'US').

## DestinationPort

Type: `int`

Destination port of the network session.

## DetectedProtocol

Type: `string`

Detected traffic protocol of the network session.

## DeviceID

Type: `string`

UUID of the device where the network session originated from.

## DeviceName

Type: `string`

The name of the device where the HTTP request originated from (for example, 'Laptop MB810').

## Email

Type: `string`

Email associated with the user identity where the network session originated from.

## IsIsolated

Type: `bool`

Whether the network session originated from an isolated browser.

## Offramp

Type: `string`

Traffic destination type.

## Onramp

Type: `string`

Traffic source type.

## OverrideIP

Type: `string`

Overridden IP of the network session, if any.

## OverridePort

Type: `int`

Overridden port of the network session, if any.

## PolicyID

Type: `string`

Identifier of the policy/rule that was applied, if any.

## PolicyName

Type: `string`

The name of the gateway policy applied to the request, if any.

## ProxyEndpoint

Type: `string`

The proxy endpoint used on this network session, if any.

## RegistrationID

Type: `string`

The UUID of the device registration from which the network session originated.

## SNI

Type: `string`

Content of the SNI for the TLS network session, if any.

## SessionID

Type: `string`

The session identifier of this network session.

## SourceIP

Type: `string`

Source IP of the network session.

## SourceIPContinentCode

Type: `string`

Continent code of the source IP of the network session (for example, 'NA').

## SourceIPCountryCode

Type: `string`

Country code of the source IP of the network session (for example, 'US').

## SourceInternalIP

Type: `string`

Internal IP of the device. For Cloudflare One Client (WARP) traffic, this is the WARP CGNAT address. For GRE/IPsec on-ramps, this is the source IP behind the tunnel.

## SourcePort

Type: `int`

Source port of the network session.

## TenantID

Type: `string`

The tenant ID of the network session, if exists.

## Transport (deprecated)

Type: `string`

Transport protocol used for this session.   
Possible values are _tcp_ | _quic_ | _udp_. Deprecated, please use TransportProtocol instead.

## TransportProtocol

Type: `string`

Transport protocol used for this session.   
Possible values are _tcp_ | _quic_ | _udp_.

## UserID

Type: `string`

User identity where the network session originated from.

## VirtualNetworkID

Type: `string`

The identifier of the virtual network the device was connected to, if any.

## VirtualNetworkName

Type: `string`

The name of the virtual network the device was connected to, if any.

[PreviousGateway HTTP](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_http/)[NextIPSec Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/gateway_network.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
