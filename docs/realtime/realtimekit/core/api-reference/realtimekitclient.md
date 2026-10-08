---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/realtimekitclient/
title: RealtimeKitClient \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:54.546301+00:00
---

# RealtimeKitClient · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/realtimekitclient/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RealtimeKitClient



# RealtimeKitClient

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/realtimekitclient/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.participants meeting.self meeting.meta meeting.ai meeting.plugins meeting.chat meeting.polls meeting.connectedMeetings meeting.__internals__ meeting.join() meeting.leave() meeting.initMedia([options], [skipAwaits], [cachedUserDetails]) meeting.init(options)

The RealtimeKitClient class is the main class of the web core library. An object of the RealtimeKitClient class can be created using `await RealtimeKitClient.init({ ... })`. Typically, an object of `RealtimeKitClient` is named `meeting`.

  * RealtimeKitClient
    * _instance_
      * .participants
      * .self
      * .meta
      * .ai
      * .plugins
      * .chat
      * .polls
      * .connectedMeetings
      * .**internals**
      * .join()
      * .leave()
    * _static_
      * .initMedia([options], [skipAwaits], [cachedUserDetails])
      * .init(options)



### meeting.participants

The `participants` object consists of 4 maps of participants, `waitlisted`, `joined`, `active`, `pinned`. The maps are indexed by `peerId`s, and the values are the corresponding participant objects.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.self

The `self` object can be used to manipulate audio and video settings, and other configurations for the local participant. This exposes methods to enable and disable media tracks, share the user's screen, etc.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.meta

The `room` object stores information about the current meeting, such as chat messages, polls, room name, etc.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.ai

The `ai` object is used to interface with AI features. You can obtain the live meeting transcript and use other meeting AI features such as summary, and agenda using this object.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.plugins

The `plugins` object stores information about the plugins available in the current meeting. It exposes methods to activate and deactivate them.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.chat

The chat object stores the chat messages that were sent in the meeting. This includes text messages, images, and files.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.polls

The polls object stores the polls that were initiated in the meeting. It exposes methods to create and vote on polls.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.connectedMeetings

The connectedMeetings object stores the connected meetings states. It exposes methods to create/read/update/delete methods for connected meetings.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.__internals__

The **internals** object exposes the internal tools & utilities such as features and logger so that client can utilise the same to build their own feature based UI. Logger (**internals**.logger) can be used to send logs to servers to inform of issues, if any, proactively.

**Kind** : instance property of `RealtimeKitClient`  


### meeting.join()

The `join()` method can be used to join the meeting. A `roomJoined` event is emitted on `self` when the room is joined successfully.

**Kind** : instance method of `RealtimeKitClient`  


### meeting.leave()

The `leave()` method can be used to leave a meeting.

**Kind** : instance method of `RealtimeKitClient`  


### meeting.initMedia([options], [skipAwaits], [cachedUserDetails])

**Kind** : static method of `RealtimeKitClient`

Param | Type | Default  
---|---|---  
[options] | `Object` |   
[options.video] | `boolean` |   
[options.audio] | `boolean` |   
[options.constraints] | `MediaConstraints` |   
[skipAwaits] | `boolean` | `false`  
[cachedUserDetails] | `CachedUserDetails` |   
  
### meeting.init(options)

The `init` method can be used to instantiate the RealtimeKitClient class. This returns an instance of RealtimeKitClient, which can be used to perform actions on the meeting.

**Kind** : static method of `RealtimeKitClient`

Param | Description  
---|---  
options | The options object.  
options.authToken | The authorization token received using the API.  
options.baseURI | The base URL of the API.  
options.defaults | The default audio and video settings.  
  
[PreviousMedia Acquisition Approaches](https://developers.cloudflare.com/realtime/realtimekit/core/media-acquisition-approaches/)[NextRTKAi](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RealtimeKitClient.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
