---
url: https://developers.cloudflare.com/time-services/ntp/
title: Network Time Protocol \u00b7 Cloudflare Time Services docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:01.898331+00:00
---

# Network Time Protocol · Cloudflare Time Services docs

> Source: https://developers.cloudflare.com/time-services/ntp/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Time Services](https://developers.cloudflare.com/time-services/)
  3. /Network Time Protocol



# Network Time Protocol

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/time-services/ntp/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundNext steps

[Network Time Protocol ↗︎](https://tools.ietf.org/html/rfc1305) (NTP) is an Internet protocol designed to synchronize time between computer systems communicating over unreliable and variable-latency network paths. Cloudflare offers its version of NTP for free so you can use our [global anycast network ↗︎](https://www.cloudflare.com/network/) to synchronize time from our closest server.

## Background

NTP works by having a client send a query packet out to an NTP server that then responds with its clock time. The client then computes an estimate of the difference between its clock and the remote clock and attempts to compensate for any network delay. The NTP client then queries multiple servers and implements algorithms to select the best estimate.

Cloudflare does not implement leap smearing: NTP includes a Leap Indicator field [spec ↗︎](https://tools.ietf.org/html/rfc5905#section-7.3) and the kernel will apply the leap second correction at the appropriate time. This is the behavior servers in `pool.ntp.org` share. Using servers that smear time along with servers that do not may lead to unpredictable and anomalous results.

## Next steps

For more background information about NTP, refer to the [introductory blog ↗︎](https://blog.cloudflare.com/secure-time/).

To enable NTP on your device, refer to our [Usage guide](https://developers.cloudflare.com/time-services/ntp/usage/).

[PreviousOverview](https://developers.cloudflare.com/time-services/)[NextUser Guide](https://developers.cloudflare.com/time-services/ntp/usage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/time-services/ntp/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
