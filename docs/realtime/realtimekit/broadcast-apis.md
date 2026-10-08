---
url: https://developers.cloudflare.com/realtime/realtimekit/broadcast-apis/
title: Message Broadcast APIs \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:52.868499+00:00
---

# Message Broadcast APIs · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/broadcast-apis/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /Message Broadcast APIs



# Message Broadcast APIs

Last updated Sep 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/broadcast-apis/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Broadcasting a Message Subscribe to Messages Rate Limiting & Constraints Examples

The broadcast APIs allow a user to send custom messages to all other users in a meeting.

WebMobile

ReactWeb ComponentsAngular

### Broadcasting a Message

The Participants module on the meeting object allows you to broadcast messages to all other users in a meeting (or to other meetings in case of connected meetings) over the signaling channel.

Param | Type | Description | Required  
---|---|---|---  
`type` | `Exclude<string, 'spotlight'>` | Message type identifier used to distinguish different kinds of broadcasts. | Yes  
`payload` | `BroadcastMessagePayload` | Data sent with the message. Keys map to boolean, number, string, Date, or `ActiveTab`. | Yes  
`target` | `BroadcastMessageTarget` | Optional target filter for which participants or meetings receive the message. | No  
  
  * If target is omitted, the message is broadcast to all participants in the current meeting, including the local participant.
  * If `target.participantIds` is provided, the message is sent only to those participants in the current meeting.
  * If `target.presetNames` is provided, the message is sent to all participants whose preset name is in the list.
  * If `target.meetingIds` is provided, the message is broadcast to all specified meetings (multi‑meeting broadcast).


    
    
    const participants = useRealtimeKitSelector((m) => m.participants);
    participants.broadcastMessage(
      type: Exclude<string, 'spotlight'>,
      payload: BroadcastMessagePayload,
      target?: BroadcastMessageTarget,
    ): Promise<void>
    
    
    type BroadcastMessagePayload = {
    	[key: string]: boolean | number | string | Date | ActiveTab;
    };
    
    type BroadcastMessageTarget =
    	| { participantIds: string[] }
    	| { presetNames: string[] }
    	| { meetingIds: string[] };

Param | Type | Description | Required  
---|---|---|---  
`type` | `Exclude<string, 'spotlight'>` | Message type identifier used to distinguish different kinds of broadcasts. | Yes  
`payload` | `BroadcastMessagePayload` | Data sent with the message. Keys map to boolean, number, string, Date, or `ActiveTab`. | Yes  
`target` | `BroadcastMessageTarget` | Optional target filter for which participants or meetings receive the message. | No  
  
  * If target is omitted, the message is broadcast to all participants in the current meeting, including the local participant.
  * If `target.participantIds` is provided, the message is sent only to those participants in the current meeting.
  * If `target.presetNames` is provided, the message is sent to all participants whose preset name is in the list.
  * If `target.meetingIds` is provided, the message is broadcast to all specified meetings (multi‑meeting broadcast).


    
    
    meeting.participants.broadcastMessage(
      type: Exclude<string, 'spotlight'>,
      payload: BroadcastMessagePayload,
      target?: BroadcastMessageTarget,
    ): Promise<void>
    
    
    type BroadcastMessagePayload = {
    	[key: string]: boolean | number | string | Date | ActiveTab;
    };
    
    type BroadcastMessageTarget =
    	| { participantIds: string[] }
    	| { presetNames: string[] }
    	| { meetingIds: string[] };

Param | Type | Description | Required  
---|---|---|---  
`type` | `Exclude<string, 'spotlight'>` | Message type identifier used to distinguish different kinds of broadcasts. | Yes  
`payload` | `BroadcastMessagePayload` | Data sent with the message. Keys map to boolean, number, string, Date, or `ActiveTab`. | Yes  
`target` | `BroadcastMessageTarget` | Optional target filter for which participants or meetings receive the message. | No  
  
  * If target is omitted, the message is broadcast to all participants in the current meeting, including the local participant.
  * If `target.participantIds` is provided, the message is sent only to those participants in the current meeting.
  * If `target.presetNames` is provided, the message is sent to all participants whose preset name is in the list.
  * If `target.meetingIds` is provided, the message is broadcast to all specified meetings (multi‑meeting broadcast).


    
    
    meeting.participants.broadcastMessage(
      type: Exclude<string, 'spotlight'>,
      payload: BroadcastMessagePayload,
      target?: BroadcastMessageTarget,
    ): Promise<void>
    
    
    type BroadcastMessagePayload = {
    	[key: string]: boolean | number | string | Date | ActiveTab;
    };
    
    type BroadcastMessageTarget =
    	| { participantIds: string[] }
    	| { presetNames: string[] }
    	| { meetingIds: string[] };

### Subscribe to Messages

Use the `broadcastedMessage` event to listen for messages sent via `broadcastMessage` and handle them in your application.
    
    
    const participants = useRealtimeKitSelector((m) => m.participants);
    participants.on("broadcastedMessage", ({ type, payload, timestamp }) => {
    	// handle message
    });
    
    
    meeting.participants.on(
    	"broadcastedMessage",
    	({ type, payload, timestamp }) => {
    		// handle message
    	},
    );
    
    
    meeting.participants.on(
    	"broadcastedMessage",
    	({ type, payload, timestamp }) => {
    		// handle message
    	},
    );

### Rate Limiting & Constraints

  * The method is rate‑limited (server‑side + client‑side) to prevent abuse.
  * Default client‑side config in the deprecated module: maxInvocations = 5 per period = 1s.
  * The Participants module exposes a `rateLimitConfig` and `updateRateLimits(maxInvocations, period)` for tuning on the client, but server‑side limits may still apply.
  * The event type cannot be `spotlight`. This is reserved for internal use by the SDK.



### Examples

#### Broadcast to everyone in the meeting
    
    
    const participants = useRealtimeKitSelector((m) => m.participants);
    await participants.broadcastMessage("HAND_RAISE", {
    	raised: true,
    	userId: meeting.self.userId,
    	sentAt: new Date(),
    });
    
    participants.on(
    "broadcastedMessage",
    ({ type, payload, timestamp }) => {
    if (type === "HAND_RAISE") {
    // payload.raised, payload.userId, payload.sentAt
    }
    },
    );
    
    
    await meeting.participants.broadcastMessage("HAND_RAISE", {
    	raised: true,
    	userId: meeting.self.userId,
    	sentAt: new Date(),
    });
    
    meeting.participants.on(
    "broadcastedMessage",
    ({ type, payload, timestamp }) => {
    if (type === "HAND_RAISE") {
    // payload.raised, payload.userId, payload.sentAt
    }
    },
    );
    
    
    await meeting.participants.broadcastMessage("HAND_RAISE", {
    	raised: true,
    	userId: meeting.self.userId,
    	sentAt: new Date(),
    });
    
    meeting.participants.on(
    "broadcastedMessage",
    ({ type, payload, timestamp }) => {
    if (type === "HAND_RAISE") {
    // payload.raised, payload.userId, payload.sentAt
    }
    },
    );

#### Broadcast to a specific set of participants.

Only the participants with those participantIds receive the message.
    
    
    const participants = useRealtimeKitSelector((m) => m.participants);
    await participants.broadcastMessage(
    	"PRIVATE_NOTE",
    	{ message: "You are on stage in 30 seconds" },
    	{
    		participantIds: ["peer-id-1", "peer-id-2"],
    	},
    );
    
    
    await meeting.participants.broadcastMessage(
    	"PRIVATE_NOTE",
    	{ message: "You are on stage in 30 seconds" },
    	{
    		participantIds: ["peer-id-1", "peer-id-2"],
    	},
    );
    
    
    await meeting.participants.broadcastMessage(
    	"PRIVATE_NOTE",
    	{ message: "You are on stage in 30 seconds" },
    	{
    		participantIds: ["peer-id-1", "peer-id-2"],
    	},
    );

#### Broadcast to a preset

All participants whose preset name is `speaker` receive the message.
    
    
    const participants = useRealtimeKitSelector((m) => m.participants);
    await participants.broadcastMessage(
    	"STAGE_INSTRUCTION",
    	{ text: "Prepare for Q&A" },
    	{
    		presetNames: ["speaker"],
    	},
    );
    
    
    await meeting.participants.broadcastMessage(
    	"STAGE_INSTRUCTION",
    	{ text: "Prepare for Q&A" },
    	{
    		presetNames: ["speaker"],
    	},
    );
    
    
    await meeting.participants.broadcastMessage(
    	"STAGE_INSTRUCTION",
    	{ text: "Prepare for Q&A" },
    	{
    		presetNames: ["speaker"],
    	},
    );

#### Broadcast across multiple meetings

All participants in the specified meetings receive the message.
    
    
    const participants = useRealtimeKitSelector((m) => m.participants);
    await participants.broadcastMessage(
    	"GLOBAL_ANNOUNCEMENT",
    	{ text: "The event will end in 5 minutes." },
    	{
    		meetingIds: ["meeting-1", "meeting-2"],
    	},
    );
    
    
    await meeting.participants.broadcastMessage(
    	"GLOBAL_ANNOUNCEMENT",
    	{ text: "The event will end in 5 minutes." },
    	{
    		meetingIds: ["meeting-1", "meeting-2"],
    	},
    );
    
    
    await meeting.participants.broadcastMessage(
    	"GLOBAL_ANNOUNCEMENT",
    	{ text: "The event will end in 5 minutes." },
    	{
    		meetingIds: ["meeting-1", "meeting-2"],
    	},
    );

[PreviousCollaborative Stores](https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/)[NextOverview](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/collaborative-stores/broadcast.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
