---
url: https://developers.cloudflare.com/changelog/post/2026-05-28-realtimekit-track-recording/
title: Record specific participant audio tracks in RealtimeKit \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.633777+00:00
---

# Record specific participant audio tracks in RealtimeKit · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-28-realtimekit-track-recording/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## Record specific participant audio tracks in RealtimeKit

[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now record specific participant audio tracks in RealtimeKit with [track recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/). Track recording creates separate WebM files for each participant instead of a single composite recording, which is useful for post-processing, transcription, and regulated or content-sensitive workflows.

To record specific participants, pass `user_ids` when starting a track recording:
    
    
    curl --request POST \
      --url https://api.cloudflare.com/client/v4/accounts/<account_id>/realtime/kit/<app_id>/recordings/track \
      --header 'Authorization: Bearer <api_token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "meeting_id": "97440c6a-140b-40a9-9499-b23fd7a3868a",
      "user_ids": ["user-123", "user-456"]
    }'

To pass `user_ids` for selective track recording, use the following minimum SDK versions:

  * Web Core: `@cloudflare/realtimekit` version `1.4.0` or later
  * Web UI Kit: `@cloudflare/realtimekit-ui`, `@cloudflare/realtimekit-react-ui`, or `@cloudflare/realtimekit-angular-ui` version `1.1.2` or later
  * Android Core or iOS Core: version `2.0.0` or later
  * Android UI Kit or iOS UI Kit: version `1.1.0` or later



[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/) provides SDKs and UI components so that you can build your own meeting experience on Cloudflare's [global WebRTC infrastructure](https://developers.cloudflare.com/realtime/#realtime-sfu). Teams today build products ranging from telehealth to education on RealtimeKit for global audiences. You can get started today with our [Quickstart](https://developers.cloudflare.com/realtime/realtimekit/quickstart/) or take a look at our [Cloudflare Meet repo ↗︎](https://github.com/cloudflare/meet) as a reference.
