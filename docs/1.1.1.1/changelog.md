---
url: https://developers.cloudflare.com/1.1.1.1/changelog/
title: Changelog \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:03.245895+00:00
---

# Changelog · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/changelog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /Changelog



# Changelog

Last updated Jul 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/changelog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/1.1.1.1.xml)

## 2026-09-24

  
**RFC 8509 root key trust anchor sentinel support**  


1.1.1.1 now supports [RFC 8509 ↗︎](https://datatracker.ietf.org/doc/html/rfc8509) root key trust anchor sentinels. They let you check whether the responding resolver trusts a DNSSEC root key ahead of a key rollover.

To check for KSK-2024 (key tag 38696), query DNSSEC-signed names in `dnstest.dev`:
    
    
    # On a sentinel-aware resolver that trusts KSK-2024:
    
    # Returns NOERROR with an A answer.
    dig @1.1.1.1 root-key-sentinel-is-ta-38696.dnstest.dev. A +noall +comments +answer
    
    # Returns SERVFAIL without an answer.
    dig @1.1.1.1 root-key-sentinel-not-ta-38696.dnstest.dev. A +noall +comments +answer
    
    # CD bypasses sentinel processing and returns the original A answer.
    dig @1.1.1.1 root-key-sentinel-not-ta-38696.dnstest.dev. A +cdflag +noall +comments +answer

For background on DNSSEC validation, refer to [DNSKEY](https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/).

## 2026-07-28

  
**Improved DoH JSON formatting for additional record types**  


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

[PreviousFAQ](https://developers.cloudflare.com/1.1.1.1/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/changelog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
