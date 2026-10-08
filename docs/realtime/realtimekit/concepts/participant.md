---
url: https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/
title: Participant \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:53.641896+00:00
---

# Participant · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Concepts](https://developers.cloudflare.com/realtime/realtimekit/concepts/)
  5. /Participant



# Participant

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Participant tokens Token validity and refresh Custom participant identifier Where to Go Next

Before a user can join a meeting through the RealtimeKit SDK, your backend must add that user as a participant to that meeting using the [Add Participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/). In RealtimeKit, a **participant** represents a user who is allowed to join a specific meeting.

You can think of this as enrolling a student into a classroom. The meeting is the classroom, and adding a participant is how you register a user so that they are allowed to attend.

When you add a participant, you also choose which [preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/) to apply. The preset defines the role, permissions, and meeting experience of that participant.

### Participant tokens

When you add a participant to a meeting using the [Add Participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) API endpoint, it returns:

  * A participant `id` that identifies this participant within the meeting.
  * An authentication `token` for that participant.



Your backend should make it available to your frontend application. When the user chooses to join the meeting, the frontend passes the token to the RealtimeKit SDK.

RealtimeKit uses the token to authenticate the participant and determine which meeting and which participant is joining. Without a valid authentication token, the SDK cannot join the meeting on behalf of that participant. As long as a participant has a valid authentication token, that participant can join multiple live sessions of the same meeting over time.

### Token validity and refresh

Participant authentication tokens are JSON Web Tokens (JWTs). The `meetingId` and `participantId` fields scope each token to one participant in one meeting.

A token becomes valid when issued and expires 100 days later. You cannot configure custom start or expiration dates. If you need scheduled access, enforce the schedule in your own system because RealtimeKit SDKs do not manage scheduling or duration logic.

Your backend can call the [Refresh Participant Token](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/refresh_participant_token/) endpoint before or after a token expires. The new token uses the existing participant record, including its participant `id` and preset. Refreshing does not invalidate previously issued tokens. Each token remains valid until its own expiration time.

To revoke all tokens for a participant in a meeting, call the [Delete Participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/delete_meeting_participant/) endpoint. First, use the [Kick Participants](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/kick_participants/) endpoint to safely remove the participant from any active session.

A participant cannot join a meeting with an expired or revoked token. The RealtimeKit UI and Core SDK report the token as invalid. RealtimeKit rejects the participant before they enter the [meeting stage](https://developers.cloudflare.com/realtime/realtimekit/core/stage-management/), so they are not billed.

### Custom participant identifier

When adding the participant, you can optionally provide a custom participant identifier, referred to as `custom_participant_id`. This value is purely for your use. RealtimeKit stores it and returns it in APIs, but does not use it to control access. It allows you to map your application's user to RealtimeKit participant and to correlate RealtimeKit session data, events or analytics with user information in your system.

Note

**Do not** use personal data such as email address, phone number, or any other personally identifiable information as `custom_participant_id`. Use a stable internal identifier from your own system, such as a numeric user id or UUID.

### Where to Go Next

After understanding participants, you can explore the following topics:

  * Learn how [Presets](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset) define roles and permissions for participants
  * [Get started with RealtimeKit SDKs](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)



[PreviousPreset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/)[NextSession Lifecycle](https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/concepts/participant.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
