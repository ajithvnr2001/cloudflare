---
url: https://developers.cloudflare.com/time-services/roughtime/
title: Roughtime \u00b7 Cloudflare Time Services docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:02.139170+00:00
---

# Roughtime · Cloudflare Time Services docs

> Source: https://developers.cloudflare.com/time-services/roughtime/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Time Services](https://developers.cloudflare.com/time-services/)
  3. /Roughtime



# Roughtime

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/time-services/roughtime/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundNext steps

[Roughtime ↗︎](https://roughtime.googlesource.com/roughtime) is a simple, flexible, and secure authenticated time protocol developed by Google.

## Background

Endpoints on the Internet often synchronize their clocks using the [Network Time Protocol (NTP)](https://developers.cloudflare.com/time-services/ntp/). NTP provides precise synchronization, but is frequently deployed without a means of authentication. This is due to a [combination of issues ↗︎](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/dowling).

As a result, a man-in-the-middle attacker can easily influence a victim’s clock. By moving them back in time, the attacker can, for example, force a victim to accept an expired (and possibly compromised) TLS certificate or session ticket.

For many applications, _precise_ network time is not essential. It is sufficient to have _accurate_ time to mitigate these kinds of attacks, such as within 10 seconds of real time. This observation is the primary motivation behind Roughtime.

## Next steps

For more technical details on Roughtime, refer to the [introductory blog post ↗︎](https://blog.cloudflare.com/roughtime/).

To get started, refer to [Get the Roughtime](https://developers.cloudflare.com/time-services/roughtime/usage/). For more practical guidance on using the Roughtime, refer to our [how-to guide](https://developers.cloudflare.com/time-services/roughtime/recipes/).

[PreviousNetwork Time Security](https://developers.cloudflare.com/time-services/nts/)[NextGet the Roughtime](https://developers.cloudflare.com/time-services/roughtime/usage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/time-services/roughtime/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
