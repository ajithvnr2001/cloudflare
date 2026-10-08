---
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/
title: Recording \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:05.910426+00:00
---

# Recording · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /Recording



# Recording

Last updated Sep 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow composite recording worksWorkflow

Learn how RealtimeKit records meetings as a single composite file or as separate participant audio tracks.

Visit the following pages to learn more about recording meetings:

  * [Start Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/)
  * [Stop Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/)
  * [Monitor Recording Status](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/monitor-status/)
  * [Configure Video Settings](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/)
  * [Set Audio Configurations](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/)
  * [Add Watermark](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/)
  * [Disable Upload to RealtimeKit Bucket](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/)
  * [Track recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/)
  * [Create Custom Recording App Using Recording SDKs](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/create-record-app-using-sdks/)
  * [Interactive Recordings with Timed Metadata](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/interactive-recording/)
  * [Manage Recording Config Precedence Order](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/)
  * [Upload Recording to Your Cloud](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/)



RealtimeKit can record the audio and video of multiple users in a meeting, as well as interactions with RealtimeKit plugins, in a single file using composite recording mode. RealtimeKit can also record separate participant audio tracks using [track recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/).

## How composite recording works

Composite recordings are powered by anonymous virtual bot users who join your meeting, record it, and then upload it to RealtimeKit's Cloudflare R2 bucket. For video files, we currently support the [H.264 ↗︎](https://en.wikipedia.org/wiki/Advanced_Video_Coding) and [VP8 ↗︎](https://en.wikipedia.org/wiki/VP8) codecs.

  1. When the recording is finished, it is stored in RealtimeKit's Cloudflare R2 bucket.

  2. RealtimeKit generates a downloadable link from which the recording can be downloaded. You can get the download URL using the [Fetch details of a recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/) or from the Developer Portal.

You can receive notifications of recording status in any of the following ways:

     * Using the `recording.statusUpdate` webhook. RealtimeKit uses webhooks to notify your application when an event happens.
     * Using the [Fetch active recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings/).
     * You can also view the states of recording from the Developer Portal.
  3. Download the recording from the download url and store it to your cloud storage. The file is kept on RealtimeKit's server for seven days before being deleted.

You can get the download URL using the [Fetch active recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings/) or from the Developer Portal.

We support transferring recordings to AWS, Azure, and DigitalOcean storage buckets. You can also choose to preconfigure the storage configurations using the Developer Portal or the [Start recording a meeting API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).




## Workflow

A typical workflow for recording a meeting involves the following steps:

  1. Start a recording using the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/) or client side SDK.
  2. Manage the recording using the [Pause, resume, or stop recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/pause_resume_stop_recording/) or client side SDK.
  3. Fetch the download URL for downloading the recording using the [Fetch details of a recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/), webhook, or from the Developer Portal.



For separate participant audio files, refer to [Track recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/).

[PreviousMessage Broadcast APIs](https://developers.cloudflare.com/realtime/realtimekit/broadcast-apis/)[NextStart Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/recording-guide/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
