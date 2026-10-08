---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/
title: RTKConnectedMeetings \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:55.130528+00:00
---

# RTKConnectedMeetings · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKConnectedMeetings



# RTKConnectedMeetings

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.connectedMeetings.getConnectedMeetings() meeting.connectedMeetings.createMeetings(request) meeting.connectedMeetings.updateMeetings(request) meeting.connectedMeetings.deleteMeetings(meetingIds) meeting.connectedMeetings.moveParticipants(sourceMeetingId, destinationMeetingId, participantIds) meeting.connectedMeetings.moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)

This consists of the methods to facilitate connected meetings

  * RTKConnectedMeetings
    * .getConnectedMeetings()
    * .createMeetings(request)
    * .updateMeetings(request)
    * .deleteMeetings(meetingIds)
    * .moveParticipants(sourceMeetingId, destinationMeetingId, participantIds)
    * .moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)



### meeting.connectedMeetings.getConnectedMeetings()

get connected meeting state

**Kind** : instance method of `RTKConnectedMeetings`  


### meeting.connectedMeetings.createMeetings(request)

create connected meetings

**Kind** : instance method of `RTKConnectedMeetings`

Param | Type  
---|---  
request | `Array.<{title: string}>`  
  
### meeting.connectedMeetings.updateMeetings(request)

update meeting title

**Kind** : instance method of `RTKConnectedMeetings`

Param | Type  
---|---  
request | `Array.<{id: string, title: string}>`  
  
### meeting.connectedMeetings.deleteMeetings(meetingIds)

delete connected meetings

**Kind** : instance method of `RTKConnectedMeetings`

Param | Type  
---|---  
meetingIds | `Array.<string>`  
  
### meeting.connectedMeetings.moveParticipants(sourceMeetingId, destinationMeetingId, participantIds)

Trigger event to move participants

**Kind** : instance method of `RTKConnectedMeetings`

Param | Type | Description  
---|---|---  
sourceMeetingId | `string` | id of source meeting  
destinationMeetingId | `string` | id of destination meeting  
participantIds | `Array.<string>` | list of id of the participants  
  
### meeting.connectedMeetings.moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)

Trigger event to move participants with custom preset

**Kind** : instance method of `RTKConnectedMeetings`

Param | Type | Description  
---|---|---  
sourceMeetingId | `string` | id of source meeting  
destinationMeetingId | `string` | id of destination meeting  
participants | `Array.<{id: string, presetId: string}>` |   
  
[PreviousRTKChat](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/)[NextRTKLivestream](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKConnectedMeetings.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
