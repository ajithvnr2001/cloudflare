---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkself/
title: RTKSelf \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:56.879374+00:00
---

# RTKSelf · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkself/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKSelf



# RTKSelf

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.self.peerId meeting.self.roomState meeting.self.permissions meeting.self.config meeting.self.roomJoined meeting.self.isPinned meeting.self.cleanupEvents() meeting.self.setName(name) meeting.self.setupTracks(options) meeting.self.enableAudio() meeting.self.enableVideo() meeting.self.updateVideoConstraints() meeting.self.enableScreenShare() meeting.self.updateScreenshareConstraints() meeting.self.disableAudio() meeting.self.disableVideo() meeting.self.disableScreenShare() meeting.self.getAllDevices() meeting.self.pin() meeting.self.unpin() meeting.self.hide() meeting.self.show() meeting.self.setDevice(device)

The RTKSelf module represents the current user, and allows to modify the state of the user in the meeting. The audio and video streams of the user can be retrieved from this module.

  * RTKSelf
    * .peerId
    * .roomState
    * .permissions
    * .config
    * .roomJoined
    * .isPinned
    * .cleanupEvents()
    * .setName(name)
    * .setupTracks(options)
    * .enableAudio()
    * .enableVideo()
    * .updateVideoConstraints()
    * .enableScreenShare()
    * .updateScreenshareConstraints()
    * .disableAudio()
    * .disableVideo()
    * .disableScreenShare()
    * .getAllDevices()
    * .pin()
    * .unpin()
    * .hide()
    * .show()
    * .setDevice(device)



### meeting.self.peerId

NOTE(ishita1805): Discussed with Ravindra, added a duplicate for consistency when using identifiers in Locker. We might want to look at deprecating the `id` sometime later.

**Kind** : instance property of `RTKSelf`  


### meeting.self.roomState

Returns the current state of room init - Initial State joined - User is in the meeting waitlisted - User is in the waitlist state rejected - User's was in the waiting room, but the entry was rejected kicked - A privileged user removed the user from the meeting left - User left the meeting ended - The meeting was ended

**Kind** : instance property of `RTKSelf`  


### meeting.self.permissions

Returns the current permission given to the user for the meeting.

**Kind** : instance property of `RTKSelf`  


### meeting.self.config

Returns configuration for the meeting.

**Kind** : instance property of `RTKSelf`  


### meeting.self.roomJoined

Returns true if the local participant has joined the meeting.

**Kind** : instance property of `RTKSelf`  


### meeting.self.isPinned

Returns true if the current user is pinned.

**Kind** : instance property of `RTKSelf`  


### meeting.self.cleanupEvents()

**Kind** : instance method of `RTKSelf`  


### meeting.self.setName(name)

The name of the user can be set by calling this method. This will get reflected to other participants ONLY if this method is called before the room is joined.

**Kind** : instance method of `RTKSelf`

Param | Type | Description  
---|---|---  
name | `string` | Name of the user.  
  
### meeting.self.setupTracks(options)

Sets up the local media tracks.

**Kind** : instance method of `RTKSelf`

Param | Type | Description  
---|---|---  
options | `Object` | The audio and video options.  
[options.video] | `boolean` | If true, the video stream is fetched.  
[options.audio] | `boolean` | If true, the audio stream is fetched.  
[options.forceReset] | `boolean` | If true, force resets tracks before re-acquiring.  
  
### meeting.self.enableAudio()

This method is used to unmute the local participant's audio.

**Kind** : instance method of `RTKSelf`  


### meeting.self.enableVideo()

This method is used to start streaming the local participant's video to the meeting.

**Kind** : instance method of `RTKSelf`  


### meeting.self.updateVideoConstraints()

This method is used to apply constraints to the current video stream.

**Kind** : instance method of `RTKSelf`  


### meeting.self.enableScreenShare()

This method is used to start sharing the local participant's screen to the meeting.

**Kind** : instance method of `RTKSelf`  


### meeting.self.updateScreenshareConstraints()

This method is used to apply constraints to the current screenshare stream.

**Kind** : instance method of `RTKSelf`  


### meeting.self.disableAudio()

This method is used to mute the local participant's audio.

**Kind** : instance method of `RTKSelf`  


### meeting.self.disableVideo()

This participant is used to disable the local participant's video.

**Kind** : instance method of `RTKSelf`  


### meeting.self.disableScreenShare()

This method is used to stop sharing the local participant's screen.

**Kind** : instance method of `RTKSelf`  


### meeting.self.getAllDevices()

Returns all media devices accessible by the local participant.

**Kind** : instance method of `RTKSelf`  


### meeting.self.pin()

Returns `self.id` if user has permission to pin participants.

**Kind** : instance method of `RTKSelf`  


### meeting.self.unpin()

Returns `self.id` if user has permission to unpin participants.

**Kind** : instance method of `RTKSelf`  


### meeting.self.hide()

Hide's user's tile in the UI (locally)

**Kind** : instance method of `RTKSelf`  


### meeting.self.show()

Show's user's tile in the UI if hidden (locally)

**Kind** : instance method of `RTKSelf`  


### meeting.self.setDevice(device)

Change the current media device that is being used by the local participant.

**Kind** : instance method of `RTKSelf`

Param | Type | Description  
---|---|---  
device | `MediaDeviceInfo` | The device that is to be used. A device of the same `kind` will be replaced. the primary stream.  
  
[PreviousRTKRecording](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkrecording/)[NextRTKSelfMedia](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkselfmedia/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKSelf.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
