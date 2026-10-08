---
url: https://developers.cloudflare.com/realtime/realtimekit/webinar/
title: Set up a webinar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:33.785603+00:00
---

# Set up a webinar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/webinar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /Set up a webinar



# Set up a webinar

Last updated Sep 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/webinar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWebinar rolesBefore you beginSet up a webinarManage stage requestsVerify the webinarPricingNext steps

In a RealtimeKit webinar, presenters publish audio and video from the [stage](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#stage). Viewers watch and can request to join the stage.

This guide sets up a webinar using the default webinar [presets](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/) and renders it with [RealtimeKit UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/). To build a custom interface instead, use [RealtimeKit Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) with [stage management](https://developers.cloudflare.com/realtime/realtimekit/core/stage-management/).

## Webinar roles

Every RealtimeKit app includes two default presets for webinars. Assign one of these presets to each participant, modify them, or create your own preset to fit your application.

Role | Default preset | Stage behavior | Can accept stage requests  
---|---|---|---  
Presenter | `webinar_presenter` | Can join the stage and publish audio and video | Yes  
Viewer | `webinar_viewer` | Can request to join the stage | No  
  
## Before you begin

Before you set up a webinar, make sure that you have:

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com) with a RealtimeKit app.
  * An API token with Realtime Admin permissions. Keep it server-side. Do not expose it in frontend code.
  * A backend that can call the RealtimeKit REST API to create meetings and add participants.
  * A frontend application ready to integrate [RealtimeKit UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/).



If you have not completed these requirements, refer to [Quickstart](https://developers.cloudflare.com/realtime/realtimekit/quickstart/).

## Set up a webinar

  1. In the [RealtimeKit dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/realtime/kit), go to **Presets** and review the default `webinar_presenter` and `webinar_viewer` presets. Both presets have **Meeting Type** set to **Video (WebRTC)** and **Manage Stage (Webinar)** turned on under **Configuration** > **Stage & Media**.
  2. Create a meeting using the [Create Meeting API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/). Save the returned meeting `id` for the next step.
  3. Add each presenter and viewer to the meeting using the [Add Participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/). Assign `webinar_presenter` to presenters and `webinar_viewer` to viewers.
  4. Deliver each participant's returned `authToken` only to the frontend session for that specific user.
  5. Initialize [RealtimeKit UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/) with the participant's `authToken`. UI Kit renders the webinar interface, including stage controls, based on the participant's preset.



Configure presets with the API

If you manage presets programmatically instead of through the dashboard, use the [Create Preset API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/create/) with the following fields:

  * `config.view_type` set to `WEBINAR`.
  * `permissions.stage_enabled` set to `true` for both presets.
  * `permissions.can_accept_production_requests` set to `true` for participants who moderate stage requests.



Set `permissions.stage_access`, `permissions.media.audio.can_produce`, `permissions.media.video.can_produce`, and `permissions.media.screenshare.can_produce` to the same value, based on the stage behavior you want:

Stage behavior | Applies to | Value  
---|---|---  
_Allowed to join_ | Presenters | `ALLOWED`  
_Can request to join_ | Viewers who can request to join the stage | `CAN_REQUEST`  
_Can only view_ | View-only viewers | `NOT_ALLOWED`  
  
For the complete request schema, refer to [Presets](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/).

## Manage stage requests

A viewer whose preset has **Behaviour** set to **Can request to join** can request access to the stage from the UI Kit interface. A presenter whose preset has **Accept Requests** turned on receives the request and can accept or reject it.

Once accepted, the viewer joins the stage and can publish audio and video like a presenter. RealtimeKit UI Kit handles this by default. To build a custom interface, implement the same behavior with the stage management APIs in [Stage Management](https://developers.cloudflare.com/realtime/realtimekit/core/stage-management/).

## Verify the webinar

  1. Join the meeting as a presenter and confirm that you can publish audio and video.
  2. Join the meeting as a viewer and confirm that you cannot publish audio or video by default.
  3. As the viewer, request to join the stage.
  4. As the presenter, accept the request and confirm that the viewer can now publish audio and video.



## Pricing

Both presenters and viewers are billed as Audio/Video Participants. For detailed pricing information, refer to [Pricing](https://developers.cloudflare.com/realtime/realtimekit/pricing/).

## Next steps

  * Customize the webinar interface with a [custom control bar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/custom-controlbar/) or [UI Kit addons](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/addons/).
  * Review [video and simulcast recommendations](https://developers.cloudflare.com/realtime/realtimekit/best-practices/video-and-simulcast/#webinar-audience-is-view-only) for presenter and viewer media quality.
  * [Record the webinar](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/) and store the recording in your own storage.
  * Use [webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/) to track webinar lifecycle events in your backend.



[PreviousBuild your own plugins](https://developers.cloudflare.com/realtime/realtimekit/custom-plugins/build-your-own-plugins/)[NextAudio Only Calls](https://developers.cloudflare.com/realtime/realtimekit/audio-calls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/webinar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
