---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipants/
title: RTKParticipants \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:58.240405+00:00
---

# RTKParticipants · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipants/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKParticipants



# RTKParticipants

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.participants.waitlisted meeting.participants.joined meeting.participants.active meeting.participants.videoSubscribed meeting.participants.audioSubscribed meeting.participants.pinned meeting.participants.all meeting.participants.pip meeting.participants.viewMode meeting.participants.currentPage meeting.participants.lastActiveSpeaker meeting.participants.selectedPeers meeting.participants.count meeting.participants.maxActiveParticipantsCount meeting.participants.pageCount meeting.participants.setMaxActiveParticipantsCount(limit) meeting.participants.acceptWaitingRoomRequest(id) meeting.participants.acceptAllWaitingRoomRequest(userIds) meeting.participants.rejectWaitingRoomRequest(id) meeting.participants.setViewMode(viewMode) meeting.participants.subscribe(peerIds, [kinds]) meeting.participants.unsubscribe(peerIds, [kinds]) meeting.participants.setPage(page) meeting.participants.disableAllAudio(allowUnmute) meeting.participants.disableAllVideo() meeting.participants.kickAll() meeting.participants.broadcastMessage(type, payload, target) meeting.participants.getAllJoinedPeers(searchQuery, limit, offset) meeting.participants.getParticipantsInMeetingPreJoin()

This module represents all the participants in the meeting (except the local user). It consists of 4 maps:

  * `joined`: A map of all participants that have joined the meeting.
  * `waitlisted`: A map of all participants that have been added to the waitlist.
  * `active`: A map of active participants who should be displayed in the meeting grid.
  * `pinned`: A map of pinned participants.


  * RTKParticipants
    * .waitlisted
    * .joined
    * .active
    * .videoSubscribed
    * .audioSubscribed
    * .pinned
    * .all
    * .pip
    * .viewMode
    * .currentPage
    * .lastActiveSpeaker
    * .selectedPeers
    * .count
    * .maxActiveParticipantsCount
    * .pageCount
    * .setMaxActiveParticipantsCount(limit)
    * .acceptWaitingRoomRequest(id)
    * .acceptAllWaitingRoomRequest(userIds)
    * .rejectWaitingRoomRequest(id)
    * .setViewMode(viewMode)
    * .subscribe(peerIds, [kinds])
    * .unsubscribe(peerIds, [kinds])
    * .setPage(page)
    * .disableAllAudio(allowUnmute)
    * .disableAllVideo()
    * .kickAll()
    * .broadcastMessage(type, payload, target)
    * .getAllJoinedPeers(searchQuery, limit, offset)
    * .getParticipantsInMeetingPreJoin()



### meeting.participants.waitlisted

Returns a list of participants waiting to join the meeting.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.joined

Returns a list of all participants in the meeting.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.active

Returns a list of participants whose streams are currently consumed.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.videoSubscribed

Returns a list of participants whose video streams are currently consumed.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.audioSubscribed

Returns a list of participants whose audio streams are currently consumed.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.pinned

Returns a list of participants who have been pinned.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.all

Returns all added participants irrespective of whether they are currently in the meeting or not

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.pip

Return the controls for Picture-in-Picture

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.viewMode

Indicates whether the meeting is in 'ACTIVE_GRID' mode or 'PAGINATED' mode.

In 'ACTIVE_GRID' mode, participants are populated in the participants.active map dynamically. The participants present in the map will keep changing when other participants unmute their audio or turn on their videos.

In 'PAGINATED' mode, participants are populated in the participants.active map just once, and the participants in the map will only change if the page number is changed by the user using setPage(page).

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.currentPage

This indicates the current page that has been set by the user in PAGINATED mode. If the meeting is in ACTIVE_GRID mode, this value will be 0.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.lastActiveSpeaker

This stores the `participantId` of the last participant who spoke in the meeting.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.selectedPeers

Keeps a list of all participants who have been present in the selected peers list.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.count

Returns the number of participants who are joined in the meeting.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.maxActiveParticipantsCount

Returns the maximum number of participants that can be present in the active map.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.pageCount

Returns the number of pages that are available in the meeting in PAGINATED mode. If the meeting is in ACTIVE_GRID mode, this value will be 0.

**Kind** : instance property of `RTKParticipants`  


### meeting.participants.setMaxActiveParticipantsCount(limit)

Updates the maximum number of participants that are populated in the active map.

**Kind** : instance method of `RTKParticipants`

Param | Type | Description  
---|---|---  
limit | `number` | Updated max limit  
  
### meeting.participants.acceptWaitingRoomRequest(id)

Accepts requests from waitlisted participants if user has appropriate permissions.

**Kind** : instance method of `RTKParticipants`

Param | Type | Description  
---|---|---  
id | `string` | peerId or userId of the waitlisted participant.  
  
### meeting.participants.acceptAllWaitingRoomRequest(userIds)

We need a new event for socket service events since if we send them all together, sequence of events can be unreliable

**Kind** : instance method of `RTKParticipants`

Param | Type  
---|---  
userIds | `Array.<string>`  
  
### meeting.participants.rejectWaitingRoomRequest(id)

Rejects requests from waitlisted participants if user has appropriate permissions.

**Kind** : instance method of `RTKParticipants`

Param | Type | Description  
---|---|---  
id | `string` | participantId of the waitlisted participant.  
  
### meeting.participants.setViewMode(viewMode)

Sets the view mode of the meeting to either ACTIVE_GRID or PAGINATED.

**Kind** : instance method of `RTKParticipants`

Param | Type | Description  
---|---|---  
viewMode | `ViewMode` | The mode in which the active map should be populated  
  
### meeting.participants.subscribe(peerIds, [kinds])

**Kind** : instance method of `RTKParticipants`

Param | Type  
---|---  
peerIds | `Array.<string>`  
[kinds] | `Array.<('audio'|'video'|'screenshareAudio'|'screenshareVideo')>`  
  
### meeting.participants.unsubscribe(peerIds, [kinds])

**Kind** : instance method of `RTKParticipants`

Param | Type  
---|---  
peerIds | `Array.<string>`  
[kinds] | `Array.<('audio'|'video'|'screenshareAudio'|'screenshareVideo')>`  
  
### meeting.participants.setPage(page)

Populates the active map with participants present in the page number indicated by the parameter `page` in PAGINATED mode. Does not do anything in ACTIVE_GRID mode.

**Kind** : instance method of `RTKParticipants`

Param | Type | Description  
---|---|---  
page | `number` | The page number to be set.  
  
### meeting.participants.disableAllAudio(allowUnmute)

Disables audio for all participants in the meeting.

**Kind** : instance method of `RTKParticipants`

Param | Type | Description  
---|---|---  
allowUnmute | `boolean` | Allow participants to unmute after they are muted.  
  
### meeting.participants.disableAllVideo()

Disables video for all participants in the meeting.

**Kind** : instance method of `RTKParticipants`  


### meeting.participants.kickAll()

Kicks all participants from the meeting.

**Kind** : instance method of `RTKParticipants`  


### meeting.participants.broadcastMessage(type, payload, target)

Broadcasts the message to participants

If no `target` is specified it is sent to all participants including `self`.

**Kind** : instance method of `RTKParticipants`

Param | Type | Description  
---|---|---  
type | `string` |   
payload | `BroadcastMessagePayload` |   
target | `BroadcastMessageTarget` | object containing a list of `participantIds` or object containing `presetName` \- every user with that preset will be sent the message  
  
### meeting.participants.getAllJoinedPeers(searchQuery, limit, offset)

Returns all peers currently present in the room If you are in a group call, use `meeting.participants.joined` instead

**Kind** : instance method of `RTKParticipants`

Param | Type  
---|---  
searchQuery | `string`  
limit | `number`  
offset | `number`  
  
### meeting.participants.getParticipantsInMeetingPreJoin()

Returns all peers currently in the room, is a non paginated call and should only be used if you are in a non room joined state, if in a joined group call, use `meeting.participants.joined`

**Kind** : instance method of `RTKParticipants`

[PreviousRTKParticipant](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipant/)[NextRTKPermissionsPreset](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpermissionspreset/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKParticipants.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
