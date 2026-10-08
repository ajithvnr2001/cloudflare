---
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/
title: Stop Recording \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:07.598790+00:00
---

# Stop Recording · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)
  5. /Stop Recording



# Stop Recording

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

RealtimeKit recordings can be stopped in any of the following ways:

  1. **Automatic Stop (Empty meeting)** : A RealtimeKit recording will automatically stop if the meeting has no participants for a duration of 1 minute or more. This wait time can be customized by contacting RealtimeKit's support team to configure a custom value for your app.
  2. **Automatic Stop (maxSeconds elapsed)** : A recording will automatically stop when it reaches the duration specified by the `max_seconds` parameter passed while starting the recording, regardless of whether participants are present in the meeting. If this parameter is not passed, it defaults to 24 hours (86400 seconds).
  3. **Using Stop Recording API** : A recording can also be stopped by passing the recording ID and `stop` action to the [Stop Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/).



When a recording is stopped, it transitions to the `UPLOADING` state and then to the `UPLOADED` state after it has been transferred to RealtimeKit's storage and any external storage that has been set up.

[PreviousStart Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/start-recording/)[NextMonitor Recording Status](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/monitor-status/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/recording-guide/stop-recording.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
