---
url: https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/
title: Recommended sampling rate \u00b7 Cloudflare Network Flow docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:23.582533+00:00
---

# Recommended sampling rate · Cloudflare Network Flow docs

> Source: https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Flow](https://developers.cloudflare.com/network-flow/)
  3. /Routers
  4. /Recommended sampling rate



# Recommended sampling rate

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Your router samples the traffic that passes through it to create NetFlow or sFlow data. The sampling rate determines how frequently your router captures a packet — for example, a rate of 1 in 100 means your router captures one out of every 100 packets.

Sampling more frequently (lower ratios like 1 in 100) produces more accurate flow data but uses more router memory and CPU. Sampling less frequently (higher ratios like 1 in 4,000) reduces resource usage and is suitable for networks with larger traffic volumes.

The following table provides general recommendations based on your traffic volume. Test different sampling rates to find the best option for your network.

Traffic Volume | Router sampling recommendation  
---|---  
Low | Between 1 in 100 packets - 1 in 500 packets  
Medium | Between 1 in 1,000 - 1 in 2,000 packets  
High | Between 1 in 2,000 - 1 in 4,000 packets  
  
As a general rule, you may notice a loss in data accuracy (depending on your network volume) when your network flow sampling rate exceeds 1 in 5,000 packets.

[PreviousSupported routers](https://developers.cloudflare.com/network-flow/routers/supported-routers/)[NextNetflow/IPFIX configuration](https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-flow/routers/recommended-sampling-rate.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
