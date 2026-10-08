---
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/monitor-status/
title: Monitor Recording Status \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:07.129864+00:00
---

# Monitor Recording Status · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/monitor-status/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)
  5. /Monitor Recording Status



# Monitor Recording Status

Last updated Jun 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/monitor-status/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRecording statesFetching the state Using the recording.statusUpdate webhook By polling HTTP APIs

## Recording states

The recording of a meeting can have the following states:

Name | Description  
---|---  
INVOKED | RealtimeKit backend servers have received the recording request, and the master is looking for a ready worker to assign the recording job.  
RECORDING | The meeting is currently being recorded by a worker; note that this will also hold true if the meeting is being live streamed.  
UPLOADING | The recording has been stopped and the file is being uploaded to the cloud storage. If you have not specified storage details, then the files will be uploaded only to RealtimeKit's server. Any RTMP and livestreaming link will also stop at this stage.  
UPLOADED | The recording file upload is complete and the status webhook is also triggered.  
ERRORED | There was an irrecoverable error while recording the meeting and the file will not be available.  
  
## Fetching the state

There are two ways you can track what state a recording is in or view more details about a recording:

### Using the `recording.statusUpdate` webhook

RealtimeKit sends a `recording.statusUpdate` webhook when the recording transitions between states during its lifecycle. Add `recording.statusUpdate` to your webhook's `events` array to receive these notifications.
    
    
    curl --request POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Recording status webhook",
        "url": "https://example.com/webhook",
        "events": ["recording.statusUpdate"],
        "enabled": true
      }'

The webhook payload includes the current recording status, recording metadata, and associated meeting details. When the status is `UPLOADED`, the payload can include `downloadUrl`, `audioDownloadUrl`, and `downloadUrlExpiry` fields for accessing the uploaded files.

For setup, signature verification, retry behavior, and a full payload example, refer to [RealtimeKit webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/#recordingstatusupdate).

### By polling HTTP APIs

Alternatively, you can also use the following APIs:

  * [List recordings](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_recordings/): This endpoint gets all past and ongoing recordings linked to a meeting.
  * [Fetch active recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings/): This endpoint gets all ongoing recordings of a meeting.
  * [Fetch details of a recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/): This endpoint gets a specific recording using a recording ID.



[PreviousStop Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/)[NextConfigure Video Settings](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/recording-guide/monitor-status.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
