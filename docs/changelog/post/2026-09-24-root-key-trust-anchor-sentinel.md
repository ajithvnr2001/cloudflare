---
url: https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/
title: RFC 8509 root key trust anchor sentinel support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:15.991779+00:00
---

# RFC 8509 root key trust anchor sentinel support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 24, 2026

## RFC 8509 root key trust anchor sentinel support

[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
