---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/
title: RTKChat \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:54.985578+00:00
---

# RTKChat · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKChat



# RTKChat

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkchat/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.chat.messages meeting.chat.setMaxTextLimit(limit) meeting.chat.updateRateLimits(num, period) meeting.chat.sendTextMessage(message, [peerIds]) meeting.chat.sendCustomMessage(message, [peerIds]) meeting.chat.sendImageMessage(image, [peerIds]) meeting.chat.sendFileMessage(file, [peerIds]) meeting.chat.sendMessage(message, [participantIds]) meeting.chat.editTextMessage(messageId, message) meeting.chat.editImageMessage(messageId, image) meeting.chat.editFileMessage(messageId, file) meeting.chat.editMessage(messageId, message) meeting.chat.deleteMessage(messageId) meeting.chat.pin(id) meeting.chat.unpin(id) meeting.chat.fetchPublicMessages(options) meeting.chat.fetchPrivateMessages(options) meeting.chat.fetchPinnedMessages(options)

This is the chat module, which can be used to send and receive messages from the meeting.

  * RTKChat
    * ~~.messages~~
    * .setMaxTextLimit(limit)
    * .updateRateLimits(num, period)
    * .sendTextMessage(message, [peerIds])
    * .sendCustomMessage(message, [peerIds])
    * .sendImageMessage(image, [peerIds])
    * .sendFileMessage(file, [peerIds])
    * .sendMessage(message, [participantIds])
    * .editTextMessage(messageId, message)
    * .editImageMessage(messageId, image)
    * .editFileMessage(messageId, file)
    * .editMessage(messageId, message)
    * .deleteMessage(messageId)
    * .pin(id)
    * .unpin(id)
    * .fetchPublicMessages(options)
    * .fetchPrivateMessages(options)
    * .fetchPinnedMessages(options)



### ~~meeting.chat.messages~~

_**Deprecated**_

**Kind** : instance property of `RTKChat`  


### meeting.chat.setMaxTextLimit(limit)

Set the max character limit of a text message

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
limit | `number` | Max character limit for a text message.  
  
### meeting.chat.updateRateLimits(num, period)

**Kind** : instance method of `RTKChat`

Param | Type  
---|---  
num | `number`  
period | `number`  
  
### meeting.chat.sendTextMessage(message, [peerIds])

Sends a chat text message to the room.

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
message | `string` | The message that must be sent to the room.  
[peerIds] | `Array.<string>` | Peer ids to send the message to.  
  
### meeting.chat.sendCustomMessage(message, [peerIds])

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
message | `CustomMessagePayload` | Custom message payload.  
[peerIds] | `Array.<string>` | Peer ids to send the message to.  
  
### meeting.chat.sendImageMessage(image, [peerIds])

Sends an image message to the meeting.

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
image | `File` | `ReactNativeFile` | The image that is to be sent.  
[peerIds] | `Array.<string>` | Peer ids to send the message to.  
  
### meeting.chat.sendFileMessage(file, [peerIds])

Sends a file to the meeting.

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
file | `File` | `ReactNativeFile` | A File object.  
[peerIds] | `Array.<string>` | Peer ids to send the message to.  
  
### meeting.chat.sendMessage(message, [participantIds])

Sends a message to the meeting. This method can be used to send text, image, or file messages. The message type is determined by the key 'type' in `message` object.

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
message | `MessagePayload` | An object including the type and content of the message.  
[participantIds] | `Array.<string>` | An array including the userIds of the participants.  
  
### meeting.chat.editTextMessage(messageId, message)

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
messageId | `string` | Id of the message to edit.  
message | `string` | Updated text message.  
  
### meeting.chat.editImageMessage(messageId, image)

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
messageId | `string` | Id of the message to edit.  
image | `File` | `ReactNativeFile` | Updated image file.  
  
### meeting.chat.editFileMessage(messageId, file)

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
messageId | `string` | Id of the message to edit.  
file | `File` | `ReactNativeFile` | Updated file.  
  
### meeting.chat.editMessage(messageId, message)

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
messageId | `string` | Id of the message to edit.  
message | `MessagePayload` | Updated message payload.  
  
### meeting.chat.deleteMessage(messageId)

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
messageId | `string` | Id of the message to delete.  
  
### meeting.chat.pin(id)

Pins a chat message

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
id | `string` | ID of the message to be pinned  
  
### meeting.chat.unpin(id)

Unpins a chat message

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
id | `string` | ID of the message to be unpinned  
  
### meeting.chat.fetchPublicMessages(options)

Fetches messages from the chat with pagination.

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
options | `FetchMessageOptions` | Configuration options for fetching messages, including timestamp, limit, and direction for pagination.  
  
### meeting.chat.fetchPrivateMessages(options)

Fetches private messages between the current user and another participant with pagination.

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
options | `FetchPrivateMessagesOptions` | Configuration options for fetching private messages, including private RTKChat ID (User ID of the participant) and pagination settings.  
  
### meeting.chat.fetchPinnedMessages(options)

Fetches pinned messages with pagination.

**Kind** : instance method of `RTKChat`

Param | Type | Description  
---|---|---  
options | `FetchMessageOptions` | Configuration options for fetching pinned messages, including timestamp, limit, and direction.  
  
[PreviousRTKAi](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkai/)[NextRTKConnectedMeetings](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKChat.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
