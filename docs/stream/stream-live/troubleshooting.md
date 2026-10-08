---
url: https://developers.cloudflare.com/stream/stream-live/troubleshooting/
title: Troubleshooting a live stream \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:49.565712+00:00
---

# Troubleshooting a live stream · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/stream-live/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Stream live video](https://developers.cloudflare.com/stream/stream-live/)
  4. /Troubleshooting a live stream



# Troubleshooting a live stream

Last updated Jul 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/stream-live/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBuffering, freezing, and latencyEncoder failing to connect or keeps disconnectingConnecting but the player says "Stream has not started yet"

In addition to following the live stream troubleshooting steps in this guide, make sure that your video settings align with [Cloudflare live stream recommendations](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#recommendations-requirements-and-limitations). If you use OBS, you can also check these [OBS-specific recommendations](https://developers.cloudflare.com/stream/examples/obs-from-scratch/#6-optional-optimize-settings).

## Buffering, freezing, and latency

If your live stream is buffering, freezing, experiencing latency issues, or having other similar issues, try these troubleshooting steps:

  1. In the Cloudflare dashboard, go to the **Live inputs** page.

[ Go to **Live inputs** ↗ ](https://dash.cloudflare.com/?to=/:account/stream/inputs)
  2. For the live input in use, select the **Metrics** tab.

  3. Look at your **Keyframe Interval** chart.

It should be a consistent flat line that stays between 2s and 8s. If you see an inconsistent or wavy line, or a line that is consistently below 2s or above 8s, adjust the keyframe interval (also called GOP size) in your software or service used to send the stream to Cloudflare. The exact steps for editing those settings will depend on your platform.

     * Start by setting the keyframe interval to 4s. If playback is stable but latency is still too high, lower it to 2s. If you are experiencing buffering or freezing in playback, increase it to 8s.

     * If the keyframe interval is "variable" or "automatic", change it to a specific number instead, like 4s.

What is a keyframe interval?

The keyframe interval (also called GOP size) is a measurement of how often keyframes are sent to Stream. A shorter keyframe interval requires more Internet bandwidth on the broadcast side, but can reduce glass-to-glass latency. A longer keyframe requires less Internet bandwidth and can reduce buffering and freezing, but can increase glass-to-glass latency.

  4. Look at your **Upload-to-Duration Ratio** chart.

It should be a consistent flat line below 90%. If you see an inconsistent or wavy line, or a line that is consistently above 100%, try the following troubleshooting steps:

     * [Check that your Internet upload speed ↗︎](https://speed.cloudflare.com/) is at least 20 Mbps. If it is below 20 Mbps, use common troubleshooting steps such as restarting your router, using an Ethernet connection instead of Wi-Fi, or contacting your Internet service provider.

     * Check the video bitrate setting in the software or service you use to send the stream to Cloudflare.

       * If it is "variable", change it to "constant" with a specific number, like 8 Mbps.
       * If it is above 15 Mbps, lower it to 8 Mbps or 70% of your Internet speed, whichever is lower.
     * Follow the steps above (the keyframe interval steps) to _increase_ the keyframe interval in the software or service you use to send the stream to Cloudflare.

What is the upload-to-duration ratio?

The upload-to-duration ratio is a measurement of how long it takes to upload a part of the stream compared to how long that part would take to play. A ratio of less than 100% means that the stream is uploading at least as fast as it would take to play, so most users should not experience buffering or freezing. A ratio of 100% or more means that your video is uploading slower than it would take to play, so it is likely that most users will experience buffering and freezing.




## Encoder failing to connect or keeps disconnecting

If your encoder shows a connection error such as "Failed to connect to server" or repeatedly disconnects shortly after starting, try the following:

  * Verify that your RTMPS URL, stream key, and encoder software are copied correctly into your broadcasting software.

  * If the connection fails, check whether the live input is [disabled](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#enable-or-disable-a-live-input) or its [broadcast keys have been rotated](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#rotate-broadcast-keys).

  * If you use [Live Webhooks](https://developers.cloudflare.com/stream/stream-live/webhooks/), check for a `live_input.errored` event. The webhook payload includes an [error code](https://developers.cloudflare.com/stream/stream-live/webhooks/#error-codes) that can help you troubleshoot the specific cause.




## Connecting but the player says "Stream has not started yet"

If your encoder is connected and the dashboard shows a green **Connected** status with valid metrics, but the player preview says `Stream has not started yet`, try the following:

  * Wait thirty seconds. There is a brief delay between when your encoder connects and the stream becomes playable.

  * Restart the stream to clear any bad state from the initial connection.

  * Verify that your encoder is sending [AAC audio](https://developers.cloudflare.com/stream/stream-live/start-stream-live/#recommendations-requirements-and-limitations). If it is not, set your encoder's settings to AAC explicitly.

  * Verify that your encoder is sending keyframes at a fixed interval between two and eight seconds. If the keyframe interval is set to _variable_ or _automatic_ , change it to a specific value such as four seconds. For more details, refer to the keyframe information in Buffering, freezing, and latency.




[PreviousReceive Live Webhooks](https://developers.cloudflare.com/stream/stream-live/webhooks/)[NextDVR for Live](https://developers.cloudflare.com/stream/stream-live/dvr-for-live/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/stream-live/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
