---
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/
title: Set Audio Configurations \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:06.818447+00:00
---

# Set Audio Configurations · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)
  5. /Set Audio Configurations



# Set Audio Configurations

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCodecChannelDownload Audio Files

Recording audio requires configuring the **codec** and **channel** parameters to guarantee optimal quality and compatibility with your application's demands. The codec determines the encoding format for the audio, and the channel specifies the number of audio channels for the recording. You can modify the following `audio_config` used for recording the audio:

## Codec

Codec determines the audio encoding format for recording, with MP3 and AAC being the supported formats.

  * AAC (default)
  * MP3



Note

If [VP8](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/) is selected for `video_config`, changing `audio_config` is not allowed. In this case, the codec in the `audio_config` is automatically set to `vorbis`.

## Channel

Audio signal pathway within an audio file that carries a specific sound source. The following channels are supported:

  * stereo (default)
  * mono



You can modify the configs by specifying it in the `audio_config` field in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/), for example:
    
    
    {
      "audio_config": {
        "codec": "AAC"
        "channel": "stereo"
      }
    }

## Download Audio Files

The audio file for your recording is generated only if you passed the `audio_config` parameters in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

When the recording is completed, you can use the `audio_download_url` provided in the response body of the [Fetch details of a recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/) to download and export the audio file.

[PreviousConfigure Video Settings](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/)[NextAdd Watermark](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/recording-guide/configure-audio-codec.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
