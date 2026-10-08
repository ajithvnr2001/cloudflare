---
url: https://developers.cloudflare.com/realtime/turn/custom-domains/
title: Custom TURN domains \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:38.075921+00:00
---

# Custom TURN domains · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/turn/custom-domains/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[TURN Service](https://developers.cloudflare.com/realtime/turn/)
  4. /Custom TURN domains



# Custom TURN domains

Last updated Sep 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/turn/custom-domains/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetting up a CNAME record

Cloudflare Realtime TURN service supports using custom domains for UDP, and TCP - but not TLS protocols. Custom domains do not affect any of the performance of Cloudflare Realtime TURN and is set up via a simple CNAME DNS record on your domain.

Protocol | Custom domains | Primary port | Alternate port  
---|---|---|---  
STUN over UDP | ✅ | 3478/udp |   
TURN over UDP | ✅ | 3478/udp | 443/udp  
TURN over TCP | ✅ | 3478/tcp | 80/tcp  
TURN over TLS | No | 5349/tcp | 443/tcp  
  
## Setting up a CNAME record

To use custom domains for TURN, you must create a CNAME DNS record pointing to `turn.cloudflare.com`.

Caution

Do not resolve the address of `turn.cloudflare.com` or `stun.cloudflare.com` or use an IP address as the value you input to your DNS record. Only CNAME records are supported.

Any DNS provider, including Cloudflare DNS can be used to set up a CNAME for custom domains.

Note

If Cloudflare's authoritative DNS service is used, the record must be set to [DNS-only or "grey cloud" mode](https://developers.cloudflare.com/dns/proxy-status/#dns-only-records).`

There is no additional charge to using a custom hostname with Cloudflare Realtime TURN.

[PreviousGenerate Credentials](https://developers.cloudflare.com/realtime/turn/generate-credentials/)[NextReplacing existing TURN servers](https://developers.cloudflare.com/realtime/turn/replacing-existing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/turn/custom-domains.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
