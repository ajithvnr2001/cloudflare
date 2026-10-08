---
url: https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/
title: Diagnostics \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:53.023675+00:00
---

# Diagnostics · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)

  4. /Network visibility
  5. /Diagnostics



# Diagnostics

Last updated Apr 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSample packet capturesFull packet captures

Packet captures allow you to record raw network traffic data passing through Cloudflare's network so you can inspect it offline in tools like Wireshark. This is useful for diagnosing connectivity issues, verifying firewall rules, or investigating unexpected traffic patterns.

Cloudflare supports two types of packet captures: full and sample. Full packet captures are the default behavior.

Note

The maximum packet capture runtime is 24 hours for sample and full packet captures.

## Sample packet captures

Sample packet captures collect historical data on network traffic that has already passed through Cloudflare's network. They will not collect any new traffic sent to Cloudflare's network after the packet capture has started. All sample packet captures will complete immediately after they are started because they query historical traffic data.

Sample packet captures can be viewed in the Cloudflare dashboard. They only include the first 160 bytes of each packet, which is useful for capturing packet headers but will not provide detailed packet data. The sample data is collected across all Cloudflare's data centers to build a PCAP file. This allows you to get a global picture of traffic across all data centers.

You should use full packet captures if you need to collect data on packets that pass through your network less frequently.

## Full packet captures

Full packet captures actively monitor Cloudflare's network for packets that match the selected filters, and capture the complete packet data, including the payload. The matching packet data is saved to a cloud storage bucket that is owned and configured by you. You must [configure a bucket](https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/buckets/) before starting a full packet capture.

Full packet captures will collect new traffic sent to Cloudflare's network after the packet capture has started, and include the full packet data. This type of capture cannot be viewed in the Cloudflare dashboard. You can download them from a cloud storage bucket and analyze them in Wireshark or another packet capture tool.

Refer to the articles in this section to learn how to use packet captures.

  * [Packet captures](https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/)
  * [Buckets](https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/buckets/)



[PreviousTroubleshoot Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/troubleshooting/)[NextPacket captures](https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/network-visibility/diagnostics/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
