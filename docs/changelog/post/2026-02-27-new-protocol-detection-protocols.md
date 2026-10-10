---
url: https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/
title: New protocols added for Gateway Protocol Detection (Beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.087550+00:00
---

# New protocols added for Gateway Protocol Detection (Beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 27, 2026

## New protocols added for Gateway Protocol Detection (Beta)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Gateway [Protocol Detection](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/) now supports seven additional protocols in beta:

Protocol | Notes  
---|---  
IMAP | Internet Message Access Protocol — email retrieval  
POP3 | Post Office Protocol v3 — email retrieval  
SMTP | Simple Mail Transfer Protocol — email sending  
MYSQL | MySQL database wire protocol  
RSYNC-DAEMON | rsync daemon protocol  
LDAP | Lightweight Directory Access Protocol  
NTP | Network Time Protocol  
  
These protocols join the existing set of detected protocols (HTTP, HTTP2, SSH, TLS, DCERPC, MQTT, and TPKT) and can be used with the _Detected Protocol_ selector in [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) to identify and filter traffic based on the application-layer protocol, without relying on port-based identification.

If protocol detection is enabled on your account, these protocols will automatically be logged when detected in your Gateway network traffic.

For more information on using Protocol Detection, refer to the [Protocol detection documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/protocol-detection/).
