---
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/
title: Add Watermark \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:06.150970+00:00
---

# Add Watermark · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)
  5. /Add Watermark



# Add Watermark

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

RealtimeKit's watermark feature enables you to include an image as a watermark in your recording. To add watermark, configure the following parameters to video_config in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

**Parameter** | **Description**  
---|---  
URL | Specify the URL of the watermark image  
Position | Specify the placement of the watermark, you have the flexibility to choose between left top, right top, left bottom, or right bottom. The default position is set to left top.  
Size | Specify the height and width of the watermark in pixels.  
      
    
    {
      "video_config": {
        "watermark": {
          "url": "https://test.io/images/client-logos-6.webp",
          "position": "left top",
          "size": {
            "height": 20,
            "width": 100
          }
        }
      }
    }

[PreviousSet Audio Configurations](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/)[NextDisable Upload to RealtimeKit Bucket](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/recording-guide/add-watermark.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
