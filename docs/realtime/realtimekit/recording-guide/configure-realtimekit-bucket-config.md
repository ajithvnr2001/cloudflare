---
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/
title: Disable Upload to RealtimeKit Bucket \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:06.466729+00:00
---

# Disable Upload to RealtimeKit Bucket · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)
  5. /Disable Upload to RealtimeKit Bucket



# Disable Upload to RealtimeKit Bucket

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Once the recording is complete, by default, RealtimeKit uploads all recordings to RealtimeKit's Cloudflare R2 bucket. Additionally, a presigned URL is generated with a 7-day expiry. The recording can be accessed using the `downloadUrl` associated with each recording.

However, RealtimeKit provides users with the flexibility to choose whether or not to upload their recordings to RealtimeKit's R2 bucket. If you wish to disable uploads to RealtimeKit's bucket, you can set the `realtimekit_bucket_config` parameter to false in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

For example:
    
    
    {
    	"realtimekit_bucket_config": {
    		"enabled": false
    	}
    }

Note

If you haven't specified an external storage configuration and also disabled uploads to RealtimeKit's bucket, then the recording will not be uploaded to any location. It is considered as an invalid recording.

For more information on how to set your external storage configuration, see [Publish Recorded File to Your Cloud Provider](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/).

[PreviousAdd Watermark](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/add-watermark/)[NextTrack recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
