---
url: https://developers.cloudflare.com/time-services/nts/
title: Network Time Security \u00b7 Cloudflare Time Services docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:02.071128+00:00
---

# Network Time Security · Cloudflare Time Services docs

> Source: https://developers.cloudflare.com/time-services/nts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Time Services](https://developers.cloudflare.com/time-services/)
  3. /Network Time Security



# Network Time Security

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/time-services/nts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundNext steps

[Network Time Security ↗︎](https://datatracker.ietf.org/doc/html/rfc8915) (NTS) provides cryptographic security for the client-server mode of the Network Time Protocol (NTP). This allows users to obtain time in an authenticated manner.

## Background

The NTS protocol is divided into two phases:

  1. **NTS Key Exchange** : Establishes the necessary key material between the NTP client and the server, using a [Transport Layer Security (TLS) handshake ↗︎](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) (the same public key infrastructure as the web). Once the keys are exchanged, the TLS channel is closed and the protocol enters the second phase.
  2. **NTS Extension Fields for NTPv4** : Authenticates NTP time synchronization packets using previously established key material. For more information, refer to [RFC 8915 ↗︎](https://tools.ietf.org/html/rfc8915).



## Next steps

NTS is gaining support in many NTP implementations, including [Chrony ↗︎](https://chrony-project.org/documentation.html), [NTPsec ↗︎](https://www.ntpsec.org/), and [ntpd-rs ↗︎](https://github.com/pendulum-project/ntpd-rs). Read the relevant documentation for guidance on setting them up to point to our time service, `time.cloudflare.com`. Also see [Netnod's documentation ↗︎](https://www.netnod.se/netnod-time/how-to-use-nts) for configuring NTS clients.

[PreviousUser Guide](https://developers.cloudflare.com/time-services/ntp/usage/)[NextOverview](https://developers.cloudflare.com/time-services/roughtime/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/time-services/nts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
