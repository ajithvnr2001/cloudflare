---
url: https://developers.cloudflare.com/realtime/sfu/platform/pricing/
title: Pricing \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:37.507994+00:00
---

# Pricing · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)

  4. /[Platform](https://developers.cloudflare.com/realtime/sfu/platform/)
  5. /Pricing



# Pricing

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/platform/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSFUWebSocket adapterTURN

Realtime billing is based on data sent from Cloudflare to your application. The SFU and TURN services cost $0.05 per GB of egress.

The first 1,000 GB each month is free. SFU and TURN share this allowance; they do not have independent free tiers. Realtime usage appears as a single line item on your Cloudflare bill.

## SFU

Traffic from Cloudflare to clients incurs egress charges. Traffic published into Cloudflare is free, including when no client subscribes to that publication.

## WebSocket adapter

WebSocket adapter usage is tracked in Realtime billing. Traffic from Cloudflare to your WebSocket endpoint follows the Realtime egress rate and shares the Realtime free tier. Audio ingested from a WebSocket endpoint into the SFU is not charged as ingress.

The adapter close response's `bytesProcessed` field is an operational statistic. It is not the authoritative billed-usage total.

Workers, Durable Objects, Containers, and AI services used by an application have their own pricing.

## TURN

Traffic between Realtime TURN and Realtime SFU or Cloudflare Stream WHIP/WHEP is not charged twice. Refer to the [TURN FAQ](https://developers.cloudflare.com/realtime/turn/faq/) for the traffic paths measured for TURN billing.

[PreviousOverview](https://developers.cloudflare.com/realtime/sfu/platform/)[NextLimits, timeouts, and quotas](https://developers.cloudflare.com/realtime/sfu/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
