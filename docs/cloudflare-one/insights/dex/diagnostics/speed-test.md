---
url: https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/speed-test/
title: Speed test \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:49.101432+00:00
---

# Speed test · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/speed-test/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Digital experience](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

  4. /[Diagnostics](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/)
  5. /Speed test



# Speed test

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/speed-test/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSpeed test metrics Internet speed Latency Network quality score

Speed tests allow administrators to remotely measure network performance from end-user devices running the [Cloudflare One client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/). Each test runs from the client to Cloudflare's network edge and reports metrics for internet speed, latency, and network quality.

Speed tests help IT teams:

  * Objectively measure network performance with the Cloudflare One client turned on.
  * Identify performance bottlenecks affecting specific users, devices, or locations.
  * Respond to user reports of slow connectivity with concrete data.



Feature compatibility

Feature availability

  * All Cloudflare One plans



Supported client modes

  * Traffic and DNS mode
  * Traffic only mode



Supported operating systems:

System | Support  
---|---  
Windows | ✅  
macOS | ✅  
Linux | ✅  
iOS | ❌  
Android | ❌  
ChromeOS | ❌  
  
To run a speed test from a device:

  1. In [Zero Trust ↗︎](https://dash.cloudflare.com/one), go to **Insights** > **Digital experience** > **Diagnostics**.
  2. Select **Run diagnostics**.
  3. Search for a device by user email, device name, or device ID.
  4. Select the device, then select **Device speed test**.



The test runs in the background on the selected device. Results appear in the diagnostics view once the test completes.

## Speed test metrics

Each speed test reports the following metrics:

### Internet speed

Metric | Description  
---|---  
Download throughput | The rate at which data is received by the device from Cloudflare's network edge, measured in Mbps.  
Upload throughput | The rate at which data is sent from the device to Cloudflare's network edge, measured in Mbps.  
  
### Latency

Metric | Description  
---|---  
Download latency | The round-trip time measured during an active download, reflecting latency under load.  
Upload latency | The round-trip time measured during an active upload, reflecting latency under load.  
Unloaded latency | The baseline round-trip time measured when no significant data transfer is occurring. This reflects the inherent latency of the connection.  
Jitter | The variation in latency over time. High jitter can cause inconsistent performance in real-time applications.  
  
### Network quality score

Network quality scores estimate the end-user experience for common application types based on the measured speed and latency values.

Score | Description  
---|---  
Video streaming | Rates the connection quality for video streaming applications based on throughput and latency.  
Video streaming | Estimates the connection quality for video streaming applications based on throughput and latency.  
Web chat / RTC | Estimates the connection quality for real-time communication applications such as video calls and VoIP.  
  
[PreviousClient packet capture](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/)[NextNotifications](https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/dex/diagnostics/speed-test.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
