---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/
title: Zero Trust Network Session Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:13.857407+00:00
---

# Zero Trust Network Session Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Zero Trust Network Session Logs



# Zero Trust Network Session Logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccountIDBytesReceivedBytesSentClientTCPHandshakeDurationMsClientTLSCipherClientTLSHandshakeDurationMsClientTLSVersionConnectionCloseReasonConnectionReuseDestinationReplicaIDDestinationTunnelIDDetectedProtocolDeviceIDDeviceNameEgressColoNameEgressIPEgressPortEgressRuleIDEgressRuleNameEmailIngressColoNameInitialOriginIPOfframpOnrampTypeOriginIPOriginPortOriginTLSCertificateIssuerOriginTLSCertificateValidationResultOriginTLSCipherOriginTLSHandshakeDurationMsOriginTLSVersionProtocolRegistrationIDResolvedFQDNRuleEvaluationDurationMsSNISessionEndTimeSessionIDSessionStartTimeSourceIDSourceIPSourceInternalIPSourceNameSourcePortTenantIDUserIDVirtualNetworkID

Network session logs are generated for all traffic proxied through Cloudflare Gateway across all supported [on-ramps](https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/), such as the Cloudflare One Client (WARP), proxy endpoints (PAC files), Browser Isolation, and Cloudflare Tunnel.

The descriptions below detail the fields available for `zero_trust_network_sessions`.

## AccountID

Type: `string`

Cloudflare account ID.

## BytesReceived

Type: `int`

The number of bytes sent from the origin to the client during the network session.

## BytesSent

Type: `int`

The number of bytes sent from the client to the origin during the network session.

## ClientTCPHandshakeDurationMs

Type: `int`

Duration of handshaking the TCP connection between the client and Cloudflare in milliseconds.

## ClientTLSCipher

Type: `string`

TLS cipher suite used in the connection between the client and Cloudflare.

## ClientTLSHandshakeDurationMs

Type: `int`

Duration of handshaking the TLS connection between the client and Cloudflare in milliseconds.

## ClientTLSVersion

Type: `string`

TLS protocol version used in the connection between the client and Cloudflare.

## ConnectionCloseReason

Type: `string`

The reason for closing the connection, only applicable for TCP.   
Possible values are _CLIENT_CLOSED_ | _CLIENT_IDLE_TIMEOUT_ | _CLIENT_TLS_ERROR_ | _CLIENT_ERROR_ | _ORIGIN_CLOSED_ | _ORIGIN_TLS_ERROR_ | _ORIGIN_ERROR_ | _ORIGIN_UNREACHABLE_ | _ORIGIN_UNROUTABLE_ | _PROXY_CONN_REFUSED_ | _EGRESS_PORT_ALLOCATION_ERROR_ | _UNKNOWN_ | _MISMATCHED_IP_VERSIONS_ | _TOO_MANY_ACTIVE_SESSIONS_FOR_ACCOUNT_ | _TOO_MANY_ACTIVE_SESSIONS_FOR_USER_ | _TOO_MANY_NEW_SESSIONS_FOR_ACCOUNT_ | _TOO_MANY_NEW_SESSIONS_FOR_USER_.

## ConnectionReuse

Type: `bool`

Whether the TCP connection was reused for multiple HTTP requests.

## DestinationReplicaID

Type: `string`

Identifier of the physical replica that served the session, such as a WARP device for Mesh or a cloudflared replica for Cloudflare Tunnel.

## DestinationTunnelID

Type: `string`

Identifier of the Cloudflare One connector to which the network session was routed to, if any, such as Cloudflare Tunnel or WARP device.

## DetectedProtocol

Type: `string`

Detected traffic protocol of the network session.

## DeviceID

Type: `string`

Identifier of the client device which initiated the network session, if applicable, (for example, WARP Device ID).

## DeviceName

Type: `string`

Name of the client device which initiated the network session, if applicable, (for example, WARP Device ID).

## EgressColoName

Type: `string`

The name of the Cloudflare data center from which traffic egressed to the origin.

## EgressIP

Type: `string`

Source IP used when egressing traffic from Cloudflare to the origin.

## EgressPort

Type: `int`

Source port used when egressing traffic from Cloudflare to the origin.

## EgressRuleID

Type: `string`

Identifier of the egress rule that was applied by the Secure Web Gateway, if any.

## EgressRuleName

Type: `string`

The name of the egress rule that was applied by the Secure Web Gateway, if any.

## Email

Type: `string`

Email address associated with the user identity which initiated the network session.

## IngressColoName

Type: `string`

The name of the Cloudflare data center to which traffic ingressed.

## InitialOriginIP

Type: `string`

The IP used to correlate existing FQDN matching policy between Gateway DNS and Gateway proxy.

## Offramp

Type: `string`

The type of destination to which the network session was routed.   
Possible values are _INTERNET_ | _MAGIC_ | _CFD_TUNNEL_ | _WARP_ | _MESH_.

## OnrampType

Type: `string`

The type of on-ramp through which the network session entered Cloudflare One.   
Possible values are _OTHER_ | _CF1_CLIENT_ | _MESH_ | _WORKERS_VPC_ | _MAGIC_.

## OriginIP

Type: `string`

The IP of the destination ("origin") for the network session.

## OriginPort

Type: `int`

The port of the destination origin for the network session.

## OriginTLSCertificateIssuer

Type: `string`

The issuer of the origin TLS certificate.

## OriginTLSCertificateValidationResult

Type: `string`

The result of validating the TLS certificate of the origin.   
Possible values are _VALID_ | _EXPIRED_ | _REVOKED_ | _HOSTNAME_MISMATCH_ | _NONE_ | _UNKNOWN_.

## OriginTLSCipher

Type: `string`

TLS cipher suite used in the connection between Cloudflare and the origin.

## OriginTLSHandshakeDurationMs

Type: `int`

Duration of handshaking the TLS connection between Cloudflare and the origin in milliseconds.

## OriginTLSVersion

Type: `string`

TLS protocol version used in the connection between Cloudflare and the origin.

## Protocol

Type: `string`

Network protocol used for this network session.   
Possible values are _TCP_ | _UDP_ | _ICMP_ | _ICMPV6_.

## RegistrationID

Type: `string`

Identifier of the client registration which initiated the network session, if applicable (for example, WARP Registration ID).

## ResolvedFQDN

Type: `string`

The fully qualified domain name of the destination.

## RuleEvaluationDurationMs

Type: `int`

The duration taken by Secure Web Gateway applying applicable Network, HTTP, and Egress rules to the network session in milliseconds.

## SNI

Type: `string`

The server name indication (SNI) value from the TLS handshake, if applicable.

## SessionEndTime

Type: `int or string`

The network session end timestamp with nanosecond precision.

## SessionID

Type: `string`

The identifier of this network session.

## SessionStartTime

Type: `int or string`

The network session start timestamp with nanosecond precision.

## SourceID

Type: `string`

Stable identifier of the Worker or Durable Object that initiated the network session. Only available for Workers VPC sessions.

## SourceIP

Type: `string`

Source IP of the network session.

## SourceInternalIP

Type: `string`

Internal IP of the device. For Cloudflare One Client (WARP) traffic, this is the WARP CGNAT address. For GRE/IPsec on-ramps, this is the source IP behind the tunnel.

## SourceName

Type: `string`

Name of the Worker script that initiated the network session. Only available for Workers VPC sessions.

## SourcePort

Type: `int`

Source port of the network session.

## TenantID

Type: `string`

The tenant ID of the network session, if exists.

## UserID

Type: `string`

User identity where the network session originated from. Only applicable for WARP device clients.

## VirtualNetworkID

Type: `string`

Identifier of the virtual network configured for the client.

[PreviousWorkers Trace Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events/)[NextCMB support by dataset ↗︎](https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
