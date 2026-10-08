---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/dns_logs/
title: DNS logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:14.069690+00:00
---

# DNS logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/dns_logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Zone-scoped datasets
  5. /DNS logs



# DNS logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/dns_logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewColoCodeEDNSSubnetEDNSSubnetLengthQueryNameQueryTypeResponseCachedResponseCodeSourceIPTimestamp

The descriptions below detail the fields available for `dns_logs`.

## ColoCode

Type: `string`

IATA airport code of the data center that received the request.

## EDNSSubnet

Type: `string`

IPv4 or IPv6 address information corresponding to the [EDNS Client Subnet (ECS)](https://developers.cloudflare.com/glossary/?term=ecs) forwarded by recursive resolvers. Not all resolvers send this information.

## EDNSSubnetLength

Type: `int`

Size of the [EDNS Client Subnet (ECS)](https://developers.cloudflare.com/glossary/?term=ecs) in bits. For example, if the last octet of an IPv4 address is omitted (`192.0.2.x.`), the subnet length will be 24.

## QueryName

Type: `string`

Name of the query that was sent.

## QueryType

Type: `int`

Integer value of query type. For more information refer to [Query type ↗︎](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).

## ResponseCached

Type: `bool`

Whether the response was cached or not.

## ResponseCode

Type: `int`

Integer value of response code. For more information refer to [Response code ↗︎](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6).

## SourceIP

Type: `string`

IP address of the client (IPv4 or IPv6).

## Timestamp

Type: `int or string`

Timestamp at which the query occurred.

[PreviousAccount Abuse Protection Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/account_abuse_protection_events/)[NextFirewall events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/zone/dns_logs.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
