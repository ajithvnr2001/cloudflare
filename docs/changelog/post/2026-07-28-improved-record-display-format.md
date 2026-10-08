---
url: https://developers.cloudflare.com/changelog/post/2026-07-28-improved-record-display-format/
title: Improved DoH JSON formatting for additional record types \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:05.048426+00:00
---

# Improved DoH JSON formatting for additional record types · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-28-improved-record-display-format/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 28, 2026

## Improved DoH JSON formatting for additional record types

[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-28-improved-record-display-format/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare is rolling out updated formatting for the `data` field in the 1.1.1.1 [DoH JSON API](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/) (`application/dns-json`). During the roll out responses may use either the old or new format.

Note

These are breaking changes. The DoH JSON format has no formal RFC and its schema is not guaranteed to be stable. If you need a stable format, use the [DoH wireformat](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-wireformat/) instead.

#### Human-readable display for additional record types

Several record types previously returned their `data` field in [RFC 3597 ↗︎](https://datatracker.ietf.org/doc/html/rfc3597) generic hex encoding (`\# <length> <hex>`). These now use standard presentation format:
    
    
    CAA:        0 issue "letsencrypt.org"
    NAPTR:      100 10 "s" "SIP+D2U" "" _sip._udp.example.com.
    RP:         admin.example.com. txt.example.com.
    IPSECKEY:   10 1 2 192.0.2.1 AwEA...
    SVCB:       1 target.example.com. alpn=h2
    HTTPS:      1 . alpn=h3,h2 ipv4hint=192.0.2.1
    TLSA:       3 1 1 aabbccdd...
    SSHFP:      1 2 aabbccdd...
    OPENPGPKEY: AwEA...

#### Numeric DNSSEC algorithm identifiers

DNSSEC-related records now use numeric algorithm identifiers as defined in [RFC 4034 ↗︎](https://datatracker.ietf.org/doc/html/rfc4034) instead of mnemonic names. This affects `RRSIG`, `DS`, `CDS`, `DNSKEY`, and `CDNSKEY` records. For example, `RSASHA256` becomes `8`, `ECDSAP256SHA256` becomes `13`, and `ED25519` becomes `15`. DS digest types also change from mnemonic to numeric: `SHA-256` becomes `2`.

Beforetxt
    
    
    RRSIG:  A RSASHA256 2 300 ...
    DS:     12345 RSASHA256 SHA-256 aabb...
    DNSKEY: 257 3 RSASHA256 AwEA...

Aftertxt
    
    
    RRSIG:  A 8 2 300 ...
    DS:     12345 8 2 aabb...
    DNSKEY: 257 3 8 AwEA...

#### Other formatting changes

`HINFO` character-strings are now individually quoted to remove ambiguity when values contain spaces:

Beforetxt
    
    
    "data": "Intel Xeon Linux"

Aftertxt
    
    
    "data": "\"Intel Xeon\" \"Linux\""
