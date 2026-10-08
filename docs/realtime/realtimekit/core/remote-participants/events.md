---
url: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/events/
title: Events \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:02.097824+00:00
---

# Events · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /[Remote Participants](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/)
  5. /Events



# Events

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGrid events View mode change Page change Active speakerParticipant map events Participant joined Participant left Active participants changed Participant unpinnedParticipant events Video update Audio update Screen share update Network quality scoreListen to participant events

This page provides an overview of the events emitted by `meeting.participants` and related participant maps, which you can use to keep your UI in sync with changes such as participants joining or leaving, pinning updates, active speaker changes, and grid view mode or page changes.

Prerequisites

This page assumes you have already initialized the SDK and understand the meeting object structure. Refer to [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/) if needed.

WebMobile

ReactWeb ComponentsAngular

## Grid events

These events allow you to monitor changes to the grid.

### View mode change

Triggered when the view mode changes between `ACTIVE_GRID` and `PAGINATED`.
    
    
    meeting.participants.on(
    	"viewModeChanged",
    	({ viewMode, currentPage, pageCount }) => {
    		console.log("view mode changed", viewMode);
    	},
    );

Triggered when the view mode changes between `ACTIVE_GRID` and `PAGINATED`.
    
    
    const viewMode = useRealtimeKitSelector((m) => m.participants.viewMode);

Or use event listener:
    
    
    meeting.participants.on(
    	"viewModeChanged",
    	({ viewMode, currentPage, pageCount }) => {
    		console.log("view mode changed", viewMode);
    	},
    );

This event is not available on this platform.

Triggered when the view mode changes between `ACTIVE_GRID` and `PAGINATED`.
    
    
    const viewMode = useRealtimeKitSelector((m) => m.participants.viewMode);

Or use event listener:
    
    
    meeting.participants.on(
    	"viewModeChanged",
    	({ viewMode, currentPage, pageCount }) => {
    		console.log("view mode changed", viewMode);
    	},
    );

### Page change

Triggered when the page changes in paginated mode.
    
    
    meeting.participants.on(
    	"pageChanged",
    	({ viewMode, currentPage, pageCount }) => {
    		console.log("page changed", currentPage);
    	},
    );

Triggered when the page changes in paginated mode.
    
    
    const currentPage = useRealtimeKitSelector((m) => m.participants.currentPage);
    const pageCount = useRealtimeKitSelector((m) => m.participants.pageCount);

This event is not available on this platform.

Triggered when the page changes in paginated mode.
    
    
    const currentPage = useRealtimeKitSelector((m) => m.participants.currentPage);
    const pageCount = useRealtimeKitSelector((m) => m.participants.pageCount);

### Active speaker

Triggered when a participant starts speaking.
    
    
    meeting.participants.on("activeSpeaker", (participant) => {
    	console.log(`${participant.id} is currently speaking`);
    });
    
    
    const activeSpeaker = useRealtimeKitSelector(
    	(m) => m.participants.lastActiveSpeaker,
    );

Or use event listener:
    
    
    meeting.participants.on("activeSpeaker", (participant) => {
    	console.log(`${participant.id} is currently speaking`);
    });
    
    
    meeting.addParticipantsEventListener(object : RtkParticipantsEventListener {
    	override fun onActiveSpeakerChanged(participant: RtkRemoteParticipant?) {
    		participant?.let {
    			println("${it.id} is currently speaking")
    		}
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantsEventListener {
    	func onActiveSpeakerChanged(participant: RtkRemoteParticipant?) {
    		if let participant = participant {
    			print("\(participant.id) is currently speaking")
    		}
    	}
    }
    
    meeting.addParticipantsEventListener(self)
    
    
    const activeSpeaker = useRealtimeKitSelector(
    	(m) => m.participants.lastActiveSpeaker,
    );

Or use event listener:
    
    
    meeting.participants.on("activeSpeaker", (participant) => {
    	console.log(`${participant.id} is currently speaking`);
    });

## Participant map events

These events allow you to monitor changes to remote participant maps. Use them to get notified when a participant joins or leaves the meeting, is pinned, or moves out of the grid.

### Participant joined

Triggered when any participant joins the meeting.
    
    
    meeting.participants.joined.on("participantJoined", (participant) => {
    	console.log(`A participant with id "${participant.id}" has joined`);
    });
    
    
    const joinedParticipants = useRealtimeKitSelector((m) => m.participants.joined);

Or use event listener:
    
    
    meeting.participants.joined.on("participantJoined", (participant) => {
    	console.log(`A participant with id "${participant.id}" has joined`);
    });
    
    
    meeting.addParticipantsEventListener(object : RtkParticipantsEventListener {
    	override fun onParticipantJoin(participant: RtkRemoteParticipant) {
    		println("A participant with id ${participant.id} has joined")
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantsEventListener {
    	func onParticipantJoin(participant: RtkRemoteParticipant) {
    		print("A participant with id \(participant.id) has joined")
    	}
    }
    
    meeting.addParticipantsEventListener(self)
    
    
    const joinedParticipants = useRealtimeKitSelector((m) => m.participants.joined);

Or use event listener:
    
    
    meeting.participants.joined.on("participantJoined", (participant) => {
    	console.log(`A participant with id "${participant.id}" has joined`);
    });

### Participant left

Triggered when any participant leaves the meeting.
    
    
    meeting.participants.joined.on("participantLeft", (participant) => {
    	console.log(`A participant with id "${participant.id}" has left the meeting`);
    });
    
    
    const joinedParticipants = useRealtimeKitSelector((m) => m.participants.joined);

Or use event listener:
    
    
    meeting.participants.joined.on("participantLeft", (participant) => {
    	console.log(`A participant with id "${participant.id}" has left the meeting`);
    });
    
    
    meeting.addParticipantsEventListener(object : RtkParticipantsEventListener {
    	override fun onParticipantLeave(participant: RtkRemoteParticipant) {
    		println("A participant with id ${participant.id} has left the meeting")
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantsEventListener {
    	func onParticipantLeave(participant: RtkRemoteParticipant) {
    		print("A participant with id \(participant.id) has left the meeting")
    	}
    }
    
    meeting.addParticipantsEventListener(self)
    
    
    const joinedParticipants = useRealtimeKitSelector((m) => m.participants.joined);

Or use event listener:
    
    
    meeting.participants.joined.on("participantLeft", (participant) => {
    	console.log(`A participant with id "${participant.id}" has left the meeting`);
    });

### Active participants changed

Each participant map emits `participantJoined` and `participantLeft` events:
    
    
    // Listen for when a participant gets pinned
    meeting.participants.pinned.on("participantJoined", (participant) => {
    	console.log(`Participant ${participant.name} got pinned`);
    });
    
    // Listen for when a participant gets unpinned
    meeting.participants.pinned.on("participantLeft", (participant) => {
    	console.log(`Participant ${participant.name} got unpinned`);
    });
    
    
    meeting.addParticipantsEventListener(object : RtkParticipantsEventListener {
    	override fun onActiveParticipantsChanged(active: List<RtkRemoteParticipant>) {
    		// Called when active participants change
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantsEventListener {
    	func onActiveParticipantsChanged(active: [RtkRemoteParticipant]) {
    		// Called when active participants change
    	}
    }
    
    meeting.addParticipantsEventListener(self)

### Participant pinned

Triggered when a participant is pinned.
    
    
    meeting.participants.joined.on("pinned", (participant) => {
    	console.log(`Participant with id "${participant.id}" was pinned`);
    });
    
    
    const pinnedParticipants = useRealtimeKitSelector((m) => m.participants.pinned);

Or use event listener:
    
    
    meeting.participants.joined.on("pinned", (participant) => {
    	console.log(`Participant with id "${participant.id}" was pinned`);
    });
    
    
    meeting.addParticipantsEventListener(object : RtkParticipantsEventListener {
    	override fun onParticipantPinned(participant: RtkRemoteParticipant) {
    		println("Participant with id ${participant.id} was pinned")
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantsEventListener {
    	func onParticipantPinned(participant: RtkRemoteParticipant) {
    		print("Participant with id \(participant.id) was pinned")
    	}
    }
    
    meeting.addParticipantsEventListener(self)
    
    
    const pinnedParticipants = useRealtimeKitSelector((m) => m.participants.pinned);

Or use event listener:
    
    
    meeting.participants.joined.on("pinned", (participant) => {
    	console.log(`Participant with id "${participant.id}" was pinned`);
    });

### Participant unpinned

Triggered when a participant is unpinned.
    
    
    meeting.participants.joined.on("unpinned", (participant) => {
    	console.log(`Participant with id "${participant.id}" was unpinned`);
    });
    
    
    const pinnedParticipants = useRealtimeKitSelector((m) => m.participants.pinned);

Or use event listener:
    
    
    meeting.participants.joined.on("unpinned", (participant) => {
    	console.log(`Participant with id "${participant.id}" was unpinned`);
    });
    
    
    meeting.addParticipantsEventListener(object : RtkParticipantsEventListener {
    	override fun onParticipantUnpinned(participant: RtkRemoteParticipant) {
    		println("Participant with id ${participant.id} was unpinned")
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantsEventListener {
    	func onParticipantUnpinned(participant: RtkRemoteParticipant) {
    		print("Participant with id \(participant.id) was unpinned")
    	}
    }
    
    meeting.addParticipantsEventListener(self)
    
    
    const pinnedParticipants = useRealtimeKitSelector((m) => m.participants.pinned);

Or use event listener:
    
    
    meeting.participants.joined.on("unpinned", (participant) => {
    	console.log(`Participant with id "${participant.id}" was unpinned`);
    });

## Participant events

You can monitor changes to a specific participant using the following events.

### Video update

Triggered when any participant starts or stops video.
    
    
    meeting.participants.joined.on("videoUpdate", (participant) => {
    	console.log(
    		`A participant with id "${participant.id}" updated their video track`,
    	);
    
    	if (participant.videoEnabled) {
    		// Use participant.videoTrack
    	} else {
    		// Handle stop video
    	}
    });
    
    
    // Check for one participant
    const videoEnabled = useRealtimeKitSelector(
    	(m) => m.participants.joined.get(participantId)?.videoEnabled,
    );
    
    // All video enabled participants
    const videoEnabledParticipants = useRealtimeKitSelector((m) =>
    	m.participants.joined.toArray().filter((p) => p.videoEnabled),
    );
    
    
    meeting.addParticipantEventListener(object : RtkParticipantEventListener {
    	override fun onVideoUpdate(participant: RtkRemoteParticipant, isEnabled: Boolean) {
    		println("Participant ${participant.id} video is now ${if (isEnabled) "enabled" else "disabled"}")
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantEventListener {
    	func onVideoUpdate(participant: RtkRemoteParticipant, isEnabled: Bool) {
    		print("Participant \(participant.id) video is now \(isEnabled ? "enabled" : "disabled")")
    	}
    }
    
    meeting.addParticipantEventListener(self)
    
    
    // Check for one participant
    const videoEnabled = useRealtimeKitSelector(
    	(m) => m.participants.joined.get(participantId)?.videoEnabled,
    );
    
    // All video enabled participants
    const videoEnabledParticipants = useRealtimeKitSelector((m) =>
    	m.participants.joined.toArray().filter((p) => p.videoEnabled),
    );

### Audio update

Triggered when any participant starts or stops audio.
    
    
    meeting.participants.joined.on("audioUpdate", (participant) => {
    	console.log(
    		`A participant with id "${participant.id}" updated their audio track`,
    	);
    
    	if (participant.audioEnabled) {
    		// Use participant.audioTrack
    	} else {
    		// Handle stop audio
    	}
    });
    
    
    // Check for one participant
    const audioEnabled = useRealtimeKitSelector(
    	(m) => m.participants.joined.get(participantId)?.audioEnabled,
    );
    
    // All audio enabled participants
    const audioEnabledParticipants = useRealtimeKitSelector((m) =>
    	m.participants.joined.toArray().filter((p) => p.audioEnabled),
    );
    
    
    meeting.addParticipantEventListener(object : RtkParticipantEventListener {
    	override fun onAudioUpdate(participant: RtkRemoteParticipant, isEnabled: Boolean) {
    		println("Participant ${participant.id} audio is now ${if (isEnabled) "enabled" else "disabled"}")
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantEventListener {
    	func onAudioUpdate(participant: RtkRemoteParticipant, isEnabled: Bool) {
    		print("Participant \(participant.id) audio is now \(isEnabled ? "enabled" : "disabled")")
    	}
    }
    
    meeting.addParticipantEventListener(self)
    
    
    // Check for one participant
    const audioEnabled = useRealtimeKitSelector(
    	(m) => m.participants.joined.get(participantId)?.audioEnabled,
    );
    
    // All audio enabled participants
    const audioEnabledParticipants = useRealtimeKitSelector((m) =>
    	m.participants.joined.toArray().filter((p) => p.audioEnabled),
    );

### Screen share update

Triggered when any participant starts or stops screen share.
    
    
    meeting.participants.joined.on("screenShareUpdate", (participant) => {
    	console.log(
    		`A participant with id "${participant.id}" updated their screen share`,
    	);
    
    	if (participant.screenShareEnabled) {
    		// Use participant.screenShareTracks
    	} else {
    		// Handle stop screen share
    	}
    });
    
    
    // Check for one participant
    const screensharingParticipant = useRealtimeKitSelector((m) =>
    	m.participants.joined.toArray().find((p) => p.screenShareEnabled),
    );
    
    // All screen sharing participants
    const screenSharingParticipants = useRealtimeKitSelector((m) =>
    	m.participants.joined.toArray().filter((p) => p.screenShareEnabled),
    );
    
    
    meeting.addParticipantEventListener(object : RtkParticipantEventListener {
    	override fun onScreenShareUpdate(participant: RtkRemoteParticipant, isEnabled: Boolean) {
    		println("Participant ${participant.id} screen share is now ${if (isEnabled) "enabled" else "disabled"}")
    	}
    })
    
    
    extension MeetingViewModel: RtkParticipantEventListener {
    	func onScreenShareUpdate(participant: RtkRemoteParticipant, isEnabled: Bool) {
    		print("Participant \(participant.id) screen share is now \(isEnabled ? "enabled" : "disabled")")
    	}
    }
    
    meeting.addParticipantEventListener(self)
    
    
    // Check for one participant
    const screensharingParticipant = useRealtimeKitSelector((m) =>
    	m.participants.joined.toArray().find((p) => p.screenShareEnabled),
    );
    
    // All screen sharing participants
    const screenSharingParticipants = useRealtimeKitSelector((m) =>
    	m.participants.joined.toArray().filter((p) => p.screenShareEnabled),
    );

### Network quality score

Monitor participant network quality using the `mediaScoreUpdate` event.
    
    
    meeting.participants.joined.on(
    	"mediaScoreUpdate",
    	({ participantId, kind, isScreenshare, score, scoreStats }) => {
    		if (kind === "video") {
    			console.log(
    				`Participant ${participantId}'s ${isScreenshare ? "screenshare" : "video"} quality score is`,
    				score,
    			);
    		}
    
    		if (kind === "audio") {
    			console.log(
    				`Participant ${participantId}'s audio quality score is`,
    				score,
    			);
    		}
    
    		if (score < 5) {
    			console.log(`Participant ${participantId}'s media quality is poor`);
    		}
    	},
    );

Monitor participant network quality using the `mediaScoreUpdate` event.
    
    
    import { useEffect } from "react";
    
    // Use event listener for media score updates
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleMediaScoreUpdate = ({
    		participantId,
    		kind,
    		isScreenshare,
    		score,
    		scoreStats,
    	}) => {
    		if (kind === "video") {
    			console.log(
    				`Participant ${participantId}'s ${isScreenshare ? "screenshare" : "video"} quality score is`,
    				score,
    			);
    		}
    
    		if (score < 5) {
    			console.log(`Participant ${participantId}'s media quality is poor`);
    		}
    	};
    
    	meeting.participants.joined.on("mediaScoreUpdate", handleMediaScoreUpdate);
    
    	return () => {
    		meeting.participants.joined.off("mediaScoreUpdate", handleMediaScoreUpdate);
    	};
    }, [meeting]);

This event is not available on this platform.

Monitor participant network quality using the `mediaScoreUpdate` event.
    
    
    import { useEffect } from "react";
    
    // Use event listener for media score updates
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleMediaScoreUpdate = ({
    		participantId,
    		kind,
    		isScreenshare,
    		score,
    		scoreStats,
    	}) => {
    		if (kind === "video") {
    			console.log(
    				`Participant ${participantId}'s ${isScreenshare ? "screenshare" : "video"} quality score is`,
    				score,
    			);
    		}
    
    		if (score < 5) {
    			console.log(`Participant ${participantId}'s media quality is poor`);
    		}
    	};
    
    	meeting.participants.joined.on("mediaScoreUpdate", handleMediaScoreUpdate);
    
    	return () => {
    		meeting.participants.joined.off("mediaScoreUpdate", handleMediaScoreUpdate);
    	};
    }, [meeting]);

## Listen to participant events

Each participant object is an event emitter:
    
    
    meeting.participants.joined
    	.get(participantId)
    	.on("audioUpdate", ({ audioEnabled, audioTrack }) => {
    		console.log(
    			"The participant with id",
    			participantId,
    			"has toggled their mic to",
    			audioEnabled,
    		);
    	});

Alternatively, listen on the participant map for all participants:
    
    
    meeting.participants.joined.on(
    	"audioUpdate",
    	(participant, { audioEnabled, audioTrack }) => {
    		console.log(
    			"The participant with id",
    			participant.id,
    			"has toggled their mic to",
    			audioEnabled,
    		);
    	},
    );
    
    
    import { useRealtimeKitClient } from "@cloudflare/realtimekit-react";
    import { useEffect } from "react";
    
    function ParticipantAudioListener({ participantId }) {
    	const [meeting] = useRealtimeKitClient();
    
    	useEffect(() => {
    		if (!meeting) return;
    
    		const handleAudioUpdate = ({ audioEnabled, audioTrack }) => {
    			console.log(
    				"The participant with id",
    				participantId,
    				"has toggled their mic to",
    				audioEnabled,
    			);
    		};
    
    		const participant = meeting.participants.joined.get(participantId);
    		participant.on("audioUpdate", handleAudioUpdate);
    
    		return () => {
    			participant.off("audioUpdate", handleAudioUpdate);
    		};
    	}, [meeting, participantId]);
    }

Or use the selector for specific properties:
    
    
    const audioEnabled = useRealtimeKitSelector(
    	(m) => m.participants.joined.get(participantId)?.audioEnabled,
    );

Implement the `RtkParticipantEventListener` interface to receive participant event updates:
    
    
    meeting.addParticipantEventListener(object : RtkParticipantEventListener {
    	override fun onVideoUpdate(participant: RtkRemoteParticipant, isEnabled: Boolean) {
    		// Called when participant's video state changes
    	}
    
    	override fun onAudioUpdate(participant: RtkRemoteParticipant, isEnabled: Boolean) {
    		// Called when participant's audio state changes
    	}
    
    	override fun onScreenShareUpdate(participant: RtkRemoteParticipant, isEnabled: Boolean) {
    		// Called when participant's screen share state changes
    	}
    })

Implement the `RtkParticipantEventListener` protocol to receive participant event updates:
    
    
    extension MeetingViewModel: RtkParticipantEventListener {
    	func onVideoUpdate(participant: RtkRemoteParticipant, isEnabled: Bool) {
    		// Called when participant's video state changes
    	}
    
    	func onAudioUpdate(participant: RtkRemoteParticipant, isEnabled: Bool) {
    		// Called when participant's audio state changes
    	}
    
    	func onScreenShareUpdate(participant: RtkRemoteParticipant, isEnabled: Bool) {
    		// Called when participant's screen share state changes
    	}
    }
    
    meeting.addParticipantEventListener(self)
    
    
    import { useRealtimeKitClient } from "@cloudflare/realtimekit-react-native";
    import { useEffect } from "react";
    
    function ParticipantAudioListener({ participantId }) {
    	const [meeting] = useRealtimeKitClient();
    
    	useEffect(() => {
    		if (!meeting) return;
    
    		const handleAudioUpdate = ({ audioEnabled, audioTrack }) => {
    			console.log(
    				"The participant with id",
    				participantId,
    				"has toggled their mic to",
    				audioEnabled,
    			);
    		};
    
    		const participant = meeting.participants.joined.get(participantId);
    		participant.on("audioUpdate", handleAudioUpdate);
    
    		return () => {
    			participant.off("audioUpdate", handleAudioUpdate);
    		};
    	}, [meeting, participantId]);
    }

Or use the selector for specific properties:
    
    
    const audioEnabled = useRealtimeKitSelector(
    	(m) => m.participants.joined.get(participantId)?.audioEnabled,
    );

[PreviousOverview](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/)[NextPicture in Picture](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/pip/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/remote-participants/events.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
