---
url: https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/
title: Cloudflare Tunnel now runs connectivity pre-checks at startup \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:54.594704+00:00
---

# Cloudflare Tunnel now runs connectivity pre-checks at startup · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 27, 2026

## Cloudflare Tunnel now runs connectivity pre-checks at startup

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting with [`cloudflared` version 2026.5.2 ↗︎](https://github.com/cloudflare/cloudflared/releases), [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) automates the entire [connectivity pre-checks workflow](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/) directly inside the binary. Previously, customers had to install `dig` and `netcat` and run those commands by hand to verify their environment. Now `cloudflared` does it natively at startup — and surfaces actionable remediation when something is blocked.

![cloudflared connectivity pre-checks output](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1012,format=webp/_astro/cloudflared-connectivity-prechecks.DRwN6tGe.gif)

On every `cloudflared tunnel run` (and `cloudflared tunnel diag`), the binary now natively checks:

  * **DNS resolution** — `region1.v2.argotunnel.com` and `region2.v2.argotunnel.com` resolve to valid Cloudflare IPs.
  * **Transport connectivity** — outbound `UDP (QUIC)` and `TCP (HTTP/2)` on port `7844`.
  * **Management API** — outbound `TCP/443` to `api.cloudflare.com` for software updates.



Results are printed in a scannable CLI table with three states:

  * ✅ **Pass** — the check succeeded.
  * ⚠️ **Warn** — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.
  * ❌ **Fail** — a blocking issue, with a specific remediation hint (for example, `Allow outbound UDP on port 7844`).



If DNS is unresolvable, or **both** UDP and TCP fail on port 7844, `cloudflared` exits early with the failure rather than looping on opaque `failed to dial` errors.

Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.

To get the new behavior, upgrade `cloudflared` to version `2026.5.2` or later. For more details, refer to the [Connectivity pre-checks documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/).
