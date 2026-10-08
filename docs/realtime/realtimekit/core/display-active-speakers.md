---
url: https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/
title: Display active speakers \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:58.465346+00:00
---

# Display active speakers · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)
  5. /Display active speakers



# Display active speakers

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDisplay a single active speakerDisplay multiple active speakersVisualize audio activityRelated resources

WebMobile

ReactWeb ComponentsAngular

RealtimeKit automatically detects and tracks participants who are actively speaking in a meeting. You can display either a single active speaker or multiple active speakers in your application UI, depending on your design requirements.

An active speaker in RealtimeKit is a remote participant with prominent audio activity at any given moment. The SDK maintains two types of data to help you build your UI:

  * **Active speaker** — A single remote participant who is currently speaking most prominently.
  * **Active participants** — A set of remote participants with the most prominent audio activity.



The SDK automatically updates these properties and subscribes to participant media as speaking activity changes. It prioritizes prominent audio activity, so a participant not currently visible in your UI can replace a visible participant if their audio becomes more active.

Note

The SDK tracks active speakers only when the local participant is viewing or rendering participants in ACTIVE mode (page 0). Refer to the [Remote participants](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#participant-view-modes) page to learn about participant view modes.

Active speaker properties contain only remote participants. The local participant is available separately.

The maximum number of participants in the `active` map is one less than the grid size configured in the local participant's [Preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/). This reserves space for the local participant in your UI. For example, if the grid size is 6, the `active` map contains a maximum of 5 remote participants.

## Display a single active speaker

Use `lastActiveSpeaker` to show the most recently active participant in your UI. Access the current active speaker with the `useRealtimeKitSelector` hook:
    
    
    const activeSpeaker = useRealtimeKitSelector((meeting) => {
    	const activeSpeakerId = meeting.participants.lastActiveSpeaker;
    	return meeting.participants.joined.get(activeSpeakerId);
    });
    
    if (activeSpeaker) {
    	// Render the active speaker video
    }

The `useRealtimeKitSelector` hook automatically updates your component when the active speaker changes.

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK also emits an `activeSpeaker` event on `meeting.participants` when a different participant becomes the active speaker. For imperative updates or side effects, listen to this event:
    
    
    meeting.participants.on("activeSpeaker", ({ peerId, volume }) => {
    	const activeSpeaker = meeting.participants.joined.get(peerId);
    	// Update your UI or trigger side effects
    });

Use `lastActiveSpeaker` to show the most recently active participant in your UI.

Access the `lastActiveSpeaker` property to get the participant ID, then retrieve the participant object from the joined participants map:
    
    
    const activeSpeakerId = meeting.participants.lastActiveSpeaker;
    const activeSpeaker = meeting.participants.joined.get(activeSpeakerId);
    
    if (activeSpeaker) {
    	// Render the active speaker video
    }

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK emits an `activeSpeaker` event on `meeting.participants` when a different participant becomes the active speaker:
    
    
    meeting.participants.on("activeSpeaker", ({ peerId, volume }) => {
    	const activeSpeaker = meeting.participants.joined.get(peerId);
    	// Update your UI to display the new active speaker
    });

Use `lastActiveSpeaker` to show the most recently active participant in your UI.

Access the `lastActiveSpeaker` property to get the participant ID, then retrieve the participant object from the joined participants map:
    
    
    const activeSpeakerId = meeting.participants.lastActiveSpeaker;
    const activeSpeaker = meeting.participants.joined.get(activeSpeakerId);
    
    if (activeSpeaker) {
    	// Render the active speaker video
    }

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK emits an `activeSpeaker` event on `meeting.participants` when a different participant becomes the active speaker:
    
    
    meeting.participants.on("activeSpeaker", ({ peerId, volume }) => {
    	const activeSpeaker = meeting.participants.joined.get(peerId);
    	// Update your UI to display the new active speaker
    });

Use `activeSpeaker` to show the most recently active participant in your UI.

Access the `activeSpeaker` property to get the current active speaker:
    
    
    val activeSpeaker = meeting.participants.activeSpeaker
    
    if (activeSpeaker != null) {
    	// Render the active speaker video
    }

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK emits an event when a different participant becomes the active speaker. Listen to this event using `RtkParticipantsEventListener`:
    
    
    meeting.addParticipantsEventListener(object : RtkParticipantsEventListener {
    	override fun onActiveSpeakerChanged(participant: RtkRemoteParticipant?) {
    		// Update your UI to display the new active speaker
    	}
    })

Use `activeSpeaker` to show the most recently active participant in your UI.

Access the `activeSpeaker` property to get the current active speaker:
    
    
    let activeSpeaker = meeting.participants.activeSpeaker
    
    if let activeSpeaker = activeSpeaker {
    	// Render the active speaker video
    }

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK emits an event when a different participant becomes the active speaker. Listen to this event by implementing `RtkParticipantsEventListener`:
    
    
    extension MeetingViewModel: RtkParticipantsEventListener {
    	func onActiveSpeakerChanged(participant: RtkRemoteParticipant?) {
    		// Update your UI to display the new active speaker
    	}
    }
    
    meeting.addParticipantsEventListener(self)

Use `lastActiveSpeaker` to show the most recently active participant in your UI. Access the current active speaker with the `useRealtimeKitSelector` hook:
    
    
    const activeSpeaker = useRealtimeKitSelector((meeting) => {
    	const activeSpeakerId = meeting.participants.lastActiveSpeaker;
    	return meeting.participants.joined.get(activeSpeakerId);
    });
    
    if (activeSpeaker) {
    	// Render the active speaker video
    }

The `useRealtimeKitSelector` hook automatically updates your component when the active speaker changes.

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK also emits an `activeSpeaker` event on `meeting.participants` when a different participant becomes the active speaker. For imperative updates or side effects, listen to this event:
    
    
    meeting.participants.on("activeSpeaker", (participant) => {
    	// Update your UI or trigger side effects
    });

## Display multiple active speakers

Use the `active` map to show multiple participants with prominent audio activity, typically in a grid layout. Access the current active participants with the `useRealtimeKitSelector` hook:
    
    
    const activeMap = useRealtimeKitSelector(
    	(meeting) => meeting.participants.active,
    );
    
    const activeParticipants = activeMap.toArray();
    
    // Render active participants in your grid
    activeParticipants.forEach((participant) => {
    	// Render participant video tile
    });

The `useRealtimeKitSelector` hook automatically updates your component when the set of active speakers changes.

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK also emits a `participantsUpdate` event on the `active` map when the set of active speakers changes. For imperative updates or side effects when the `active` map changes, listen to this event:
    
    
    meeting.participants.active.on("participantsUpdate", () => {
    	const activeParticipants = meeting.participants.active.toArray();
    	// Perform side effects
    });

(Optional) If your application needs to respond when a specific participant is added to or removed from the active map, listen for `participantJoined` and `participantLeft` on `meeting.participants.active` map.
    
    
    meeting.participants.active.on("participantJoined", (participant) => {
    	console.log("Participant added to active map:", participant.id);
    });
    
    meeting.participants.active.on("participantLeft", (participant) => {
    	console.log("Participant removed from active map:", participant.id);
    });

Use the `active` map to show multiple participants with prominent audio activity, typically in a grid layout.
    
    
    const activeParticipants = meeting.participants.active.toArray();
    
    // Render active participants in your grid
    activeParticipants.forEach((participant) => {
    	// Render participant video tile
    });

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK emits a `participantsUpdate` event on the `active` map when the set of active speakers changes. Listen to this event, retrieve the updated array, and re-render your grid:
    
    
    meeting.participants.active.on("participantsUpdate", () => {
    	const activeParticipants = meeting.participants.active.toArray();
    	// Update your grid UI with the new active participants
    });

(Optional) If your application needs to respond when a specific participant is added to or removed from the active map, listen for `participantJoined` and `participantLeft` on `meeting.participants.active` map.
    
    
    meeting.participants.active.on("participantJoined", (participant) => {
    	console.log("Participant added to active map:", participant.id);
    });
    
    meeting.participants.active.on("participantLeft", (participant) => {
    	console.log("Participant removed from active map:", participant.id);
    });

Use the `active` map to show multiple participants with prominent audio activity, typically in a grid layout.
    
    
    const activeParticipants = meeting.participants.active.toArray();
    
    // Render active participants in your grid
    activeParticipants.forEach((participant) => {
    	// Render participant video tile
    });

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK emits a `participantsUpdate` event on the `active` map when the set of active speakers changes. Listen to this event, retrieve the updated array, and re-render your grid:
    
    
    meeting.participants.active.on("participantsUpdate", () => {
    	const activeParticipants = meeting.participants.active.toArray();
    	// Update your grid UI with the new active participants
    });

(Optional) If your application needs to respond when a specific participant is added to or removed from the active map, listen for `participantJoined` and `participantLeft` on `meeting.participants.active` map.
    
    
    meeting.participants.active.on("participantJoined", (participant) => {
    	console.log("Participant added to active map:", participant.id);
    });
    
    meeting.participants.active.on("participantLeft", (participant) => {
    	console.log("Participant removed from active map:", participant.id);
    });

Use the `active` list to show multiple participants with prominent audio activity, in a grid layout:
    
    
    val activeParticipants = meeting.participants.active
    
    // Render active participants in your grid
    activeParticipants.forEach { participant ->
    	// Render participant video tile
    }

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK emits an event when the set of active speakers changes. Listen to this event using `RtkParticipantsEventListener`:
    
    
    meeting.addParticipantsEventListener(object : RtkParticipantsEventListener {
    	override fun onActiveParticipantsChanged(active: List<RtkRemoteParticipant>) {
    		// Update your grid UI with the new active participants
    	}
    })

Use the `active` list to show multiple participants with prominent audio activity, typically in a grid layout:
    
    
    let activeParticipants = meeting.participants.active
    
    // Render active participants in your grid
    for participant in activeParticipants {
    	// Render participant video tile
    }

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK emits an event when the set of active speakers changes. Listen to this event by implementing `RtkParticipantsEventListener`:
    
    
    extension MeetingViewModel: RtkParticipantsEventListener {
    	func onActiveParticipantsChanged(active: [RtkRemoteParticipant]) {
    		// Update your grid UI with the new active participants
    	}
    }
    
    meeting.addParticipantsEventListener(self)

Use the `active` map to show multiple participants with prominent audio activity, typically in a grid layout. Access the current active participants with the `useRealtimeKitSelector` hook:
    
    
    const activeMap = useRealtimeKitSelector(
    	(meeting) => meeting.participants.active,
    );
    
    const activeParticipants = activeMap.toArray();
    
    // Render active participants in your grid
    activeParticipants.forEach((participant) => {
    	// Render participant video tile
    });

The `useRealtimeKitSelector` hook automatically updates your component when the set of active speakers changes.

Refer to [Display participant videos](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#display-participant-videos) to learn how to render the participant video in your UI.

The SDK also emits a `participantsUpdate` event on the `active` map when the set of active speakers changes. For imperative updates or side effects when the `active` map changes, listen to this event:
    
    
    meeting.participants.active.on("participantsUpdate", () => {
    	const activeParticipants = meeting.participants.active.toArray();
    	// Perform side effects
    });

(Optional) If your application needs to respond when a specific participant is added to or removed from the active map, listen for `participantJoined` and `participantLeft` on `meeting.participants.active` map:
    
    
    meeting.participants.active.on("participantJoined", (participant) => {
    	console.log("Participant added to active map:", participant.id);
    });
    
    meeting.participants.active.on("participantLeft", (participant) => {
    	console.log("Participant removed from active map:", participant.id);
    });

## Visualize audio activity

You can create custom audio visualizations using audio data from a participant's audio track. Extract volume information from the audio track to calculate amplitude series. Use this data to render waveforms, speech indicators, or audio level meters in your UI.

You can create custom audio visualizations using audio data from a participant's audio track. Extract volume information from the audio track to calculate amplitude series. Use this data to render waveforms, speech indicators, or audio level meters in your UI.

You can create custom audio visualizations using audio data from a participant's audio track. Extract volume information from the audio track to calculate amplitude series. Use this data to render waveforms, speech indicators, or audio level meters in your UI.

Audio activity visualization is not supported on Android.

Audio activity visualization is not supported on iOS.

Audio activity visualization is not supported on React Native.

## Related resources

  * [Meeting object explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/) \- Understand the meeting object structure and available properties.
  * [Remote participant](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/) \- Learn more about remote participants in a session and how to display their video.



[PreviousPicture in Picture](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/pip/)[NextManage Participants in a Session](https://developers.cloudflare.com/realtime/realtimekit/core/manage-participants-in-a-session/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/display-active-speakers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
