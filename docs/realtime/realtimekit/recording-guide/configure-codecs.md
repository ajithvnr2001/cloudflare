---
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/
title: Configure Video Settings \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:06.232533+00:00
---

# Configure Video Settings · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)
  5. /Configure Video Settings



# Configure Video Settings

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure CodecsDownload Video Files

Video codecs are software programs that compress and decompress digital video data for transmission, storage, or playback. Configuring the appropriate video codec can help reduce file size, enhance video quality, and ensure compatibility with different playback devices.

## Configure Codecs

You can modify the codec which is used for recording the videos. We currently support the following codecs:

  * **H264 (default)** : Records video using the H.264 codec with 1280px × 720px resolution, and 384 kbps AAC audio in MP4 container.
  * **VP8** : Records video using the VP8 codec with 1280px × 720px resolution, and Vorbis codec audio in WebM container.



You can change the codec by specifying the codec in the `video_config` field in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/), for example:
    
    
    {
      "video_config": {
        "codec": "H264"
      }
    }

## Download Video Files

The video file for your recording is generated only if you passed the `video_config` parameters in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

When the recording is completed, you can use the `downloadUrl` provided in the response body of the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/) to download and export the video file.

[PreviousMonitor Recording Status](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/monitor-status/)[NextSet Audio Configurations](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/recording-guide/configure-codecs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
