---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/
title: RTKStage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:57.308170+00:00
---

# RTKStage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKStage



# RTKStage

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.stage.peerId meeting.stage.getAccessRequests() meeting.stage.requestAccess() meeting.stage.cancelRequestAccess() meeting.stage.grantAccess() meeting.stage.denyAccess() meeting.stage.join() meeting.stage.leave() meeting.stage.kick(userIds)

The RTKStage module represents a class to mange the RTKStage of the meeting RTKStage refers to a virtual area, where participants stream are visible to other participants. When a participant is off stage, they are not producing media but only consuming media from participants who are on RTKStage

  * RTKStage
    * .peerId
    * .getAccessRequests()
    * .requestAccess()
    * .cancelRequestAccess()
    * .grantAccess()
    * .denyAccess()
    * .join()
    * .leave()
    * .kick(userIds)



### meeting.stage.peerId

Returns the peerId of the current user

**Kind** : instance property of `RTKStage`  


### meeting.stage.getAccessRequests()

Method to fetch all RTKStage access requests from viewers

**Kind** : instance method of `RTKStage`  


### meeting.stage.requestAccess()

Method to send a request to privileged users to join the stage

**Kind** : instance method of `RTKStage`  


### meeting.stage.cancelRequestAccess()

Method to cancel a previous RTKStage join request

**Kind** : instance method of `RTKStage`  


### meeting.stage.grantAccess()

Method to grant access to RTKStage. This can be in response to a RTKStage Join request but it can be called on other users as well

`permissions.acceptStageRequests` privilege required

**Kind** : instance method of `RTKStage`  


### meeting.stage.denyAccess()

Method to deny access to RTKStage. This should be called in response to a RTKStage Join request

**Kind** : instance method of `RTKStage`  


### meeting.stage.join()

Method to join the stage Users either need to have the permission in the preset or must be accepted by a privileged user to call this method

**Kind** : instance method of `RTKStage`  


### meeting.stage.leave()

Method to leave the stage Users must either be on the stage already or be accepted to join the stage to call this method

**Kind** : instance method of `RTKStage`  


### meeting.stage.kick(userIds)

Method to kick a user off the stage

`permissions.acceptStageRequests` privilege required

**Kind** : instance method of `RTKStage`

Param | Type  
---|---  
userIds | `Array.<string>`  
  
[PreviousRTKSelfMedia](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkselfmedia/)[NextRTKStore](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstore/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKStage.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
