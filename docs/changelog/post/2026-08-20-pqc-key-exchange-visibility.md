---
url: https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/
title: Per-zone post-quantum visibility in Logpush and Log Explorer \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.480055+00:00
---

# Per-zone post-quantum visibility in Logpush and Log Explorer · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 20, 2026

## Per-zone post-quantum visibility in Logpush and Log Explorer

[Logs](https://developers.cloudflare.com/logs/)[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Radar ↗︎](https://radar.cloudflare.com/post-quantum) publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the [`http_requests`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) Logpush dataset — also queryable in [Log Explorer](https://developers.cloudflare.com/log-explorer/) — includes a new `ClientTLSKeyExchangeGroup` field.

The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as `X25519MLKEM768`, and classical connections appear as `X25519`, `P-256`, or another named group. A value of `UNK` means the group could not be determined, and `NONE` means either RSA key exchange was used or TLS was not used.

With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/).
