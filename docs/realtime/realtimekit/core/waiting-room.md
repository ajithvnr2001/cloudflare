---
url: https://developers.cloudflare.com/realtime/realtimekit/core/waiting-room/
title: Waiting Room \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:03.179368+00:00
---

# Waiting Room · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/waiting-room/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)
  5. /Waiting Room



# Waiting Room

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/waiting-room/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow the Waiting Room WorksWaiting Room States State FlowListening to State Changes Joined Event Waitlisted Event Rejected Event Monitor State with roomStateHost Actions Example: Host Accepting ParticipantsBest Practices

Prerequisites

This page assumes you've already initialized the SDK and understand the meeting object structure. Refer to [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/) if needed.

The waiting room feature allows hosts to control who can join a meeting. When enabled, participants must wait for approval before entering the meeting.

WebMobile

ReactWeb ComponentsAngular

## How the Waiting Room Works

After you call `meeting.join()`, one of two events will occur:

  * **`roomJoined`** \- You are allowed to join the meeting immediately
  * **`waitlisted`** \- You are placed in the waiting room and must wait for host approval



Use `meeting.self.roomState` to track the user's state in the meeting.

Note

The diagram below represents only waiting room-related states. The `roomState` property also transitions through other states like `'disconnected'`, `'left'`, `'kicked'`, and `'ended'`.

## Waiting Room States

### State Flow
    
    
            join()
              ↓
        [waitlisted]  ←------ (host rejects)
              ↓                     ↓
       (host accepts)           [rejected]
              ↓
          [joined]

## Listening to State Changes

### Joined Event

Triggered when the local user successfully joins the meeting.

Monitor when the local user joins the meeting:
    
    
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react";
    import { useEffect } from "react";
    
    function MeetingStatus() {
    	const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    	const joined = roomState === "joined";
    
    	useEffect(() => {
    		if (joined) {
    			console.log("Successfully joined the meeting");
    		}
    	}, [joined]);
    
    	return joined ? <div>You are in the meeting</div> : null;
    }

Alternatively, use event listeners:
    
    
    import { useRealtimeKitClient } from "@cloudflare/realtimekit-react";
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleRoomJoined = () => {
    		console.log("Successfully joined the meeting");
    	};
    
    	meeting.self.on("roomJoined", handleRoomJoined);
    
    	return () => {
    		meeting.self.off("roomJoined", handleRoomJoined);
    	};
    }, [meeting]);
    
    
    meeting.self.on("roomJoined", () => {
    	// Local user is in the meeting
    	console.log("Successfully joined the meeting");
    });
    
    
    meeting.addMeetingRoomEventListener(object : RtkMeetingRoomEventListener {
    	override fun onMeetingRoomJoinCompleted(meeting: RealtimeKitClient) {
    		// Local user is in the meeting
    	}
    })
    
    
    extension MeetingViewModel: RtkMeetingRoomEventListener {
    	func onMeetingRoomJoinCompleted(meeting: RealtimeKitClient) {
    		// Local user is in the meeting
    	}
    }

Monitor when the local user joins the meeting:
    
    
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react-native";
    import { useEffect } from "react";
    
    function MeetingStatus() {
    	const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    	const joined = roomState === "joined";
    
    	useEffect(() => {
    		if (joined) {
    			console.log("Successfully joined the meeting");
    		}
    	}, [joined]);
    
    	return joined ? <Text>You are in the meeting</Text> : null;
    }

Alternatively, use event listeners:
    
    
    import { useRealtimeKitClient } from "@cloudflare/realtimekit-react-native";
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleRoomJoined = () => {
    		console.log("Successfully joined the meeting");
    	};
    
    	meeting.self.on("roomJoined", handleRoomJoined);
    
    	return () => {
    		meeting.self.off("roomJoined", handleRoomJoined);
    	};
    }, [meeting]);

### Waitlisted Event

Triggered when the local user is placed in the waiting room.

Monitor when the local user is in the waiting room:
    
    
    function WaitingRoomStatus() {
    	const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    	const isWaitlisted = roomState === "waitlisted";
    
    	useEffect(() => {
    		if (isWaitlisted) {
    			console.log("You are in the waiting room");
    		}
    	}, [isWaitlisted]);
    
    	return isWaitlisted ? <div>Waiting for host approval...</div> : null;
    }

Alternatively, use event listeners:
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleWaitlisted = () => {
    		console.log("You are in the waiting room");
    	};
    
    	meeting.self.on("waitlisted", handleWaitlisted);
    
    	return () => {
    		meeting.self.off("waitlisted", handleWaitlisted);
    	};
    }, [meeting]);
    
    
    meeting.self.on("waitlisted", () => {
    	// Local user is waitlisted
    	console.log("You are in the waiting room. Waiting for host approval...");
    });
    
    
    meeting.addSelfEventListener(object : RtkSelfEventListener {
    	override fun onWaitListStatusUpdate(waitListStatus: WaitListStatus) {
    		when (waitListStatus) {
    			WAITING -> {
    				// Local user is in the waiting room
    			}
    			REJECTED -> {
    				// Local user's join room request was rejected by the host
    			}
    			NONE, ACCEPTED -> {
    				// Local user is not in the wait list or was already accepted
    			}
    		}
    	}
    })
    
    
    extension MeetingViewModel: RtkSelfEventListener {
    	func onWaitListStatusUpdate(waitListStatus: WaitListStatus) {
    		switch waitListStatus {
    		case .accepted:
    			// Local user's join room request was accepted by the host
    		case .waiting:
    			// Local user is in the waiting room
    		case .rejected:
    			// Local user's join room request was rejected by the host
    		default:
    			return .none
    		}
    	}
    }

Monitor when the local user is in the waiting room:
    
    
    function WaitingRoomStatus() {
    	const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    	const isWaitlisted = roomState === "waitlisted";
    
    	useEffect(() => {
    		if (isWaitlisted) {
    			console.log("You are in the waiting room");
    		}
    	}, [isWaitlisted]);
    
    	return isWaitlisted ? <Text>Waiting for host approval...</Text> : null;
    }

Alternatively, use event listeners:
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleWaitlisted = () => {
    		console.log("You are in the waiting room");
    	};
    
    	meeting.self.on("waitlisted", handleWaitlisted);
    
    	return () => {
    		meeting.self.off("waitlisted", handleWaitlisted);
    	};
    }, [meeting]);

### Rejected Event

Triggered when the host rejects the entry request.

Monitor when the host rejects the entry request:
    
    
    function RejectionStatus() {
    	const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    	const rejected = roomState === "rejected";
    
    	useEffect(() => {
    		if (rejected) {
    			console.log("Your entry request was rejected");
    		}
    	}, [rejected]);
    
    	return rejected ? <div>Your entry was rejected by the host</div> : null;
    }

Alternatively, use event listeners:
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleRoomLeft = ({ state }) => {
    		if (state === "rejected") {
    			console.log("Your entry request was rejected");
    		}
    	};
    
    	meeting.self.on("roomLeft", handleRoomLeft);
    
    	return () => {
    		meeting.self.off("roomLeft", handleRoomLeft);
    	};
    }, [meeting]);
    
    
    meeting.self.on("roomLeft", ({ state }) => {
    	if (state === "rejected") {
    		// Host rejected the entry
    		console.log("Your entry request was rejected");
    	}
    });

When the host rejects the entry request, the `onWaitListStatusUpdate` callback is triggered with `WaitListStatus.REJECTED`:
    
    
    meeting.addSelfEventListener(object : RtkSelfEventListener {
    	override fun onWaitListStatusUpdate(waitListStatus: WaitListStatus) {
    		when (waitListStatus) {
    			WaitListStatus.REJECTED -> {
    				// Local user's join room request was rejected by the host
    				Log.d("WaitingRoom", "Your entry request was rejected")
    			}
    			WaitListStatus.WAITING -> {
    				// Local user is in the waiting room
    			}
    			WaitListStatus.ACCEPTED, WaitListStatus.NONE -> {
    				// Local user was accepted or not in waitlist
    			}
    		}
    	}
    })

When the host rejects the entry request, the `onWaitListStatusUpdate` callback is triggered with `WaitListStatus.rejected`:
    
    
    extension MeetingViewModel: RtkSelfEventListener {
    	func onWaitListStatusUpdate(waitListStatus: WaitListStatus) {
    		switch waitListStatus {
    		case .rejected:
    			// Local user's join room request was rejected by the host
    			print("Your entry request was rejected")
    		case .waiting:
    			// Local user is in the waiting room
    			break
    		case .accepted:
    			// Local user's join room request was accepted by the host
    			break
    		default:
    			break
    		}
    	}
    }

Monitor when the host rejects the entry request:
    
    
    function RejectionStatus() {
    	const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    	const rejected = roomState === "rejected";
    
    	useEffect(() => {
    		if (rejected) {
    			console.log("Your entry request was rejected");
    		}
    	}, [rejected]);
    
    	return rejected ? <Text>Your entry was rejected by the host</Text> : null;
    }

Alternatively, use event listeners:
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleRoomLeft = ({ state }) => {
    		if (state === "rejected") {
    			console.log("Your entry request was rejected");
    		}
    	};
    
    	meeting.self.on("roomLeft", handleRoomLeft);
    
    	return () => {
    		meeting.self.off("roomLeft", handleRoomLeft);
    	};
    }, [meeting]);

### Monitor State with roomState

You can also directly check the current room state.

Handle all waiting room states in one component:
    
    
    function WaitingRoomManager() {
    	const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    
    	switch (roomState) {
    		case "init":
    			return <div>Connecting...</div>;
    		case "waitlisted":
    			return <div>Waiting for host approval...</div>;
    		case "joined":
    			return <div>You are in the meeting</div>;
    		case "rejected":
    			return <div>Your entry was rejected</div>;
    		case "left":
    			return <div>You left the meeting</div>;
    		case "kicked":
    			return <div>You were removed from the meeting</div>;
    		case "ended":
    			return <div>The meeting has ended</div>;
    		case "disconnected":
    			return <div>Connection lost</div>;
    		default:
    			return null;
    	}
    }
    
    
    const currentState = meeting.self.roomState;
    
    if (currentState === "waitlisted") {
    	console.log("Waiting for approval");
    } else if (currentState === "joined") {
    	console.log("In the meeting");
    } else if (currentState === "rejected") {
    	console.log("Entry was rejected");
    }

Use the event listeners shown above to monitor state changes.

Use the event listeners shown above to monitor state changes.

Handle all waiting room states in one component:
    
    
    function WaitingRoomManager() {
    	const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    
    	switch (roomState) {
    		case "init":
    			return <Text>Connecting...</Text>;
    		case "waitlisted":
    			return <Text>Waiting for host approval...</Text>;
    		case "joined":
    			return <Text>You are in the meeting</Text>;
    		case "rejected":
    			return <Text>Your entry was rejected</Text>;
    		case "left":
    			return <Text>You left the meeting</Text>;
    		case "kicked":
    			return <Text>You were removed from the meeting</Text>;
    		case "ended":
    			return <Text>The meeting has ended</Text>;
    		case "disconnected":
    			return <Text>Connection lost</Text>;
    		default:
    			return null;
    	}
    }

## Host Actions

Hosts can manage waiting room requests using participant management methods. See [Remote Participants](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/) for details on:

  * **`acceptWaitingRoomRequest(participantId)`** \- Accept a participant from the waiting room
  * **`rejectWaitingRoomRequest(participantId)`** \- Reject a participant's entry request



### Example: Host Accepting Participants
    
    
    import {
    	useRealtimeKitClient,
    	useRealtimeKitSelector,
    } from "@cloudflare/realtimekit-react";
    
    function WaitingRoomHost() {
    	const [meeting] = useRealtimeKitClient();
    	const waitlistedParticipants = useRealtimeKitSelector((m) =>
    		m.participants.waitlisted.toArray(),
    	);
    
    	const acceptParticipant = async (participantId) => {
    		await meeting.participants.acceptWaitingRoomRequest(participantId);
    	};
    
    	const rejectParticipant = async (participantId) => {
    		await meeting.participants.rejectWaitingRoomRequest(participantId);
    	};
    
    	return (
    		<div>
    			<h3>Waiting Room ({waitlistedParticipants.length})</h3>
    			{waitlistedParticipants.map((participant) => (
    				<div key={participant.id}>
    					<span>{participant.name}</span>
    					<button onClick={() => acceptParticipant(participant.id)}>
    						Accept
    					</button>
    					<button onClick={() => rejectParticipant(participant.id)}>
    						Reject
    					</button>
    				</div>
    			))}
    		</div>
    	);
    }
    
    
    // Get waitlisted participants
    const waitlistedParticipants = meeting.participants.waitlisted.toArray();
    
    // Accept the first waitlisted participant
    if (waitlistedParticipants.length > 0) {
    	const participantId = waitlistedParticipants[0].id;
    	await meeting.participants.acceptWaitingRoomRequest(participantId);
    }
    
    
    // Get waitlisted participants
    val waitlistedParticipants = meeting.participants.waitlisted
    
    // Accept a participant from the waiting room
    if (waitlistedParticipants.isNotEmpty()) {
    	val participant = waitlistedParticipants[0]
    	meeting.participants.acceptWaitingRoomRequest(participant.id)
    }
    
    // Reject a participant's entry request
    if (waitlistedParticipants.isNotEmpty()) {
    	val participant = waitlistedParticipants[0]
    	meeting.participants.rejectWaitingRoomRequest(participant.id)
    }
    
    // Listen for waiting room events
    meeting.addWaitlistEventListener(object : RtkWaitlistEventListener {
    	override fun onWaitListParticipantJoined(participant: RtkRemoteParticipant) {
    		// Called when a new participant joins the waiting room
    	}
    
    	override fun onWaitListParticipantAccepted(participant: RtkRemoteParticipant) {
    		// Called when a waitlisted participant is accepted into the meeting
    	}
    
    	override fun onWaitListParticipantRejected(participant: RtkRemoteParticipant) {
    		// Called when a waitlisted participant is denied entry
    	}
    
    	override fun onWaitListParticipantClosed(participant: RtkRemoteParticipant) {
    		// Called when a waitlisted participant leaves the waiting room
    	}
    })
    
    
    // Get waitlisted participants
    let waitlistedParticipants = meeting.participants.waitlisted
    
    // Accept a participant from the waiting room
    if let participant = waitlistedParticipants.first {
    	meeting.participants.acceptWaitingRoomRequest(id: participant.id)
    }
    
    // Reject a participant's entry request
    if let participant = waitlistedParticipants.first {
    	meeting.participants.rejectWaitingRoomRequest(participant.id)
    }
    
    // Listen for waiting room events
    extension MeetingViewModel: RtkWaitlistEventListener {
    	func onWaitListParticipantJoined(participant: RtkRemoteParticipant) {
    		// Called when a new participant joins the waiting room
    	}
    
    	func onWaitListParticipantAccepted(participant: RtkRemoteParticipant) {
    		// Called when a waitlisted participant is accepted into the meeting
    	}
    
    	func onWaitListParticipantRejected(participant: RtkRemoteParticipant) {
    		// Called when a waitlisted participant is denied entry
    	}
    
    	func onWaitListParticipantClosed(participant: RtkRemoteParticipant) {
    		// Called when a waitlisted participant leaves the waiting room
    	}
    }
    
    
    import {
    	useRealtimeKitClient,
    	useRealtimeKitSelector,
    } from "@cloudflare/realtimekit-react-native";
    import { View, Text, Button } from "react-native";
    
    function WaitingRoomHost() {
    	const [meeting] = useRealtimeKitClient();
    	const waitlistedParticipants = useRealtimeKitSelector((m) =>
    		m.participants.waitlisted.toArray(),
    	);
    
    	const acceptParticipant = async (participantId) => {
    		await meeting.participants.acceptWaitingRoomRequest(participantId);
    	};
    
    	const rejectParticipant = async (participantId) => {
    		await meeting.participants.rejectWaitingRoomRequest(participantId);
    	};
    
    	return (
    		<View>
    			<Text>Waiting Room ({waitlistedParticipants.length})</Text>
    			{waitlistedParticipants.map((participant) => (
    				<View key={participant.id}>
    					<Text>{participant.name}</Text>
    					<Button
    						title="Accept"
    						onPress={() => acceptParticipant(participant.id)}
    					/>
    					<Button
    						title="Reject"
    						onPress={() => rejectParticipant(participant.id)}
    					/>
    				</View>
    			))}
    		</View>
    	);
    }

## Best Practices

  * **Provide Clear Feedback** \- Show users when they're in the waiting room and that they're waiting for approval
  * **Set Expectations** \- Let users know their request is being reviewed
  * **Handle Rejection Gracefully** \- Provide a friendly message if entry is rejected
  * **Monitor State Changes** \- Subscribe to room state changes to update your UI accordingly
  * **Check Permissions** \- Ensure your app has appropriate permissions configured in the preset to use waiting room features



[PreviousEnd a session](https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/)[NextStage Management](https://developers.cloudflare.com/realtime/realtimekit/core/stage-management/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/waiting-room.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
