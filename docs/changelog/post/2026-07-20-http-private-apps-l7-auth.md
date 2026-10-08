---
url: https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/
title: Browser-based login for plaintext HTTP private applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:03.799007+00:00
---

# Browser-based login for plaintext HTTP private applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 20, 2026

## Browser-based login for plaintext HTTP private applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now uses the standard browser-based login flow for [private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) served over plaintext HTTP on port `80`.

Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an `Authentication required` pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access [application token](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/) on success.

This brings the HTTP experience in line with HTTPS apps (with [Gateway TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/) turned on). No configuration change is required. The Cloudflare One Client is still required to route traffic to the private network, but it no longer manages the Access session for HTTP apps.

Other non-HTTP protocols (SSH, RDP, arbitrary TCP/UDP) continue to use the Cloudflare One Client notification flow.
