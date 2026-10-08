---
url: https://developers.cloudflare.com/realtime/realtimekit/core/stage-management/
title: Stage Management \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:02.645613+00:00
---

# Stage Management · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/stage-management/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)
  5. /Stage Management



# Stage Management

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/stage-management/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccess the Stage APIsProperties StatusHost Controls Join Stage Leave Stage Grant Access Deny Access Kick UsersParticipant Controls Request Access Cancel Access RequestEvents Stage Access Requests Updated Stage Access Request Accepted Stage Status Updated New Stage Request Stage Request Approved Stage Request Rejected

This guide explains how to use stage management APIs for Webinar (WebRTC) use cases in Cloudflare RealtimeKit.

WebMobile

ReactWeb ComponentsAngular

Instead of a traditional publish-subscribe model, where a user can publish their media and others can choose to subscribe, RealtimeKit comes with an optional managed configuration. In this managed configuration, a less privileged user can be configured with a default behavior to not publish media. The user can then request permission to be allowed to publish their media, where a privileged user can choose to grant or deny access.

Using RealtimeKit's stage management APIs, a user can perform actions such as:

  * Leave and join stage
  * Manage stage requests and permissions
  * Kick participants



## Access the Stage APIs

The stage module can be accessed under the `meeting.stage` namespace.
    
    
    console.log("Stage object:", meeting.stage);
    
    
    console.log("Stage object:", meeting.stage);
    
    
    console.log("Stage object:", meeting.stage);
    
    
    Log.d("Stage", "Stage object: ${meeting.stage}")
    
    
    print("Stage object: \(meeting.stage)")
    
    
    console.log("Stage object:", meeting.stage);

## Properties

### Status

The `meeting.stage.status` property returns the current stage status of the local user.
    
    
    console.log("Stage status:", meeting.stage.status);
    
    
    console.log("Stage status:", meeting.stage.status);
    
    
    console.log("Stage status:", meeting.stage.status);
    
    
    Log.d("Stage", "Stage status: ${meeting.stage.stageStatus}")
    
    
    print("Stage status: \(meeting.stage.stageStatus)")
    
    
    console.log("Stage status:", meeting.stage.status);

**Possible status values:**

  * **`ON_STAGE`** \- The user is currently on the stage and sharing audio and video.
  * **`OFF_STAGE`** \- The user is viewing the session but is not on the stage and is not sharing audio or video.
  * **`REQUESTED_TO_JOIN_STAGE`** \- The user has a pending request to join the stage and share audio and video. This status remains until the host accepts or rejects the request.
  * **`ACCEPTED_TO_JOIN_STAGE`** \- The host has accepted the user's request to join the stage.



Note

A user with permission to join stage directly can only assume `ON_STAGE` and `ACCEPTED_TO_JOIN_STAGE` status values.

## Host Controls

RealtimeKit's stage management APIs allow hosts to receive and manage stage requests as well as leave and join the stage.

### Join Stage

This method connects the user to the media room, enabling them to interact with other peers in the meeting.
    
    
    await meeting.stage.join();
    
    
    await meeting.stage.join();
    
    
    await meeting.stage.join();
    
    
    meeting.stage.join()
    
    
    meeting.stage.join()
    
    
    await meeting.stage.join();

### Leave Stage

By employing this method, the user will be disconnected from the media room and subsequently unable to communicate with their peers. Additionally, their audio and video will no longer be visible to others in the room.
    
    
    await meeting.stage.leave();
    
    
    await meeting.stage.leave();
    
    
    await meeting.stage.leave();
    
    
    meeting.stage.leave()
    
    
    meeting.stage.leave()
    
    
    await meeting.stage.leave();

### Grant Access

A privileged user can grant access to stage for a set of users with the `grantAccess` method.
    
    
    await meeting.stage.grantAccess(userIds);
    
    
    await meeting.stage.grantAccess(userIds);
    
    
    await meeting.stage.grantAccess(userIds);
    
    
    meeting.stage.grantAccess(userIds)
    
    
    meeting.stage.grantAccess(userIds: userIds)
    
    
    await meeting.stage.grantAccess(userIds);

**Parameters:**

  * `userIds` (`string[]`) - Array of user IDs to grant stage access. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`string[]`) - Array of user IDs to grant stage access. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`string[]`) - Array of user IDs to grant stage access. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`List<String>`) - List of user IDs to grant stage access. You can retrieve user IDs using `meeting.participants.map { it.userId }`



  * `userIds` (`[String]`) - Array of user IDs to grant stage access. You can retrieve user IDs using `meeting.participants.map { $0.userId }`



  * `userIds` (`string[]`) - Array of user IDs to grant stage access. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



### Deny Access

A privileged user can deny access to stage for a set of users with the `denyAccess` method.
    
    
    await meeting.stage.denyAccess(userIds);
    
    
    await meeting.stage.denyAccess(userIds);
    
    
    await meeting.stage.denyAccess(userIds);
    
    
    meeting.stage.denyAccess(userIds)
    
    
    meeting.stage.denyAccess(userIds: userIds)
    
    
    await meeting.stage.denyAccess(userIds);

**Parameters:**

  * `userIds` (`string[]`) - Array of user IDs to deny stage access. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`string[]`) - Array of user IDs to deny stage access. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`string[]`) - Array of user IDs to deny stage access. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`List<String>`) - List of user IDs to deny stage access. You can retrieve user IDs using `meeting.participants.map { it.userId }`



  * `userIds` (`[String]`) - Array of user IDs to deny stage access. You can retrieve user IDs using `meeting.participants.map { $0.userId }`



  * `userIds` (`string[]`) - Array of user IDs to deny stage access. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



### Kick Users

A privileged user can remove a set of users from stage using the `kick` method.
    
    
    await meeting.stage.kick(userIds);
    
    
    await meeting.stage.kick(userIds);
    
    
    await meeting.stage.kick(userIds);
    
    
    meeting.stage.kick(userIds)
    
    
    meeting.stage.kick(userIds: userIds)
    
    
    await meeting.stage.kick(userIds);

**Parameters:**

  * `userIds` (`string[]`) - Array of user IDs to remove from stage. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`string[]`) - Array of user IDs to remove from stage. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`string[]`) - Array of user IDs to remove from stage. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



  * `userIds` (`List<String>`) - List of user IDs to remove from stage. You can retrieve user IDs using `meeting.participants.map { it.userId }`



  * `userIds` (`[String]`) - Array of user IDs to remove from stage. You can retrieve user IDs using `meeting.participants.map { $0.userId }`



  * `userIds` (`string[]`) - Array of user IDs to remove from stage. You can retrieve user IDs using `meeting.participants.toArray().map(p => p.userId)`



## Participant Controls

RealtimeKit's stage management APIs allow participants to request and manage stage access.

### Request Access

This method is used to create a new stage request which can be approved by the host. Each user (viewer or host) must call this method in order to join the stage.

When the host calls this method, their status will be updated to `ACCEPTED_TO_JOIN_STAGE`.
    
    
    await meeting.stage.requestAccess();
    
    
    await meeting.stage.requestAccess();
    
    
    await meeting.stage.requestAccess();
    
    
    meeting.stage.requestAccess()
    
    
    meeting.stage.requestAccess()
    
    
    await meeting.stage.requestAccess();

### Cancel Access Request

You can call this method to cancel your stage request.
    
    
    await meeting.stage.cancelRequestAccess();
    
    
    await meeting.stage.cancelRequestAccess();
    
    
    await meeting.stage.cancelRequestAccess();
    
    
    meeting.stage.cancelRequestAccess()
    
    
    meeting.stage.cancelRequestAccess()
    
    
    await meeting.stage.cancelRequestAccess();

## Events

The `meeting.stage` module emits the following events:

### Stage Access Requests Updated

Emitted when there is an update to stage access requests.
    
    
    meeting.stage.on("stageAccessRequestUpdate", (data) => {
    	console.log("Stage access request updated:", data);
    });

Alternatively, you can use React hooks to listen for stage updates:
    
    
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react";
    
    // useRealtimeKitSelector hook only works when `RealtimeKitProvider` is used.
    const stageStatus = useRealtimeKitSelector((m) => m.stage.status);
    
    
    meeting.stage.on("stageAccessRequestUpdate", (data) => {
    	console.log("Stage access request updated:", data);
    });
    
    
    meeting.stage.on("stageAccessRequestUpdate", (data) => {
    	console.log("Stage access request updated:", data);
    });
    
    
    meeting.addStageEventListener(object : RtkStageEventListener {
    	override fun onStageAccessRequestsUpdated(accessRequests: List<RtkRemoteParticipant>) {
    		// Stage access requests list updated
    		Log.d("Stage", "Access requests updated: ${accessRequests.size}")
    	}
    })
    
    
    extension WebinarViewModel: RtkStageEventListener {
    	func onStageAccessRequestsUpdated(accessRequests: [RtkRemoteParticipant]) {
    		// Stage access requests list updated
    		print("Access requests updated: \(accessRequests.count)")
    	}
    }
    
    
    meeting.stage.on("stageAccessRequestUpdate", (data) => {
    	console.log("Stage access request updated:", data);
    });

Alternatively, you can use React hooks to listen for stage updates:
    
    
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react-native";
    
    // useRealtimeKitSelector hook only works when `RealtimeKitProvider` is used.
    const stageStatus = useRealtimeKitSelector((m) => m.stage.status);

### Stage Access Request Accepted

Emitted when the host accepts the join stage request or invites a user directly to stage.
    
    
    meeting.stage.on("acceptPresentRequests", (data) => {
    	console.log("Present requests accepted:", data);
    });
    
    
    meeting.stage.on("acceptPresentRequests", (data) => {
    	console.log("Present requests accepted:", data);
    });
    
    
    meeting.stage.on("acceptPresentRequests", (data) => {
    	console.log("Present requests accepted:", data);
    });
    
    
    meeting.addStageEventListener(object : RtkStageEventListener {
    	override fun onStageAccessRequestAccepted() {
    		// Host accepted the join stage request or invited user directly to stage
    		Log.d("Stage", "Access request accepted")
    	}
    })
    
    
    extension WebinarViewModel: RtkStageEventListener {
    	func onStageAccessRequestAccepted() {
    		// Host accepted the join stage request or invited user directly to stage
    		print("Access request accepted")
    	}
    }
    
    
    meeting.stage.on("acceptPresentRequests", (data) => {
    	console.log("Present requests accepted:", data);
    });

### Stage Status Updated

Emitted when the local user's stage status changes.
    
    
    meeting.stage.on("stageStatusUpdate", (status) => {
    	console.log("Stage status updated:", status);
    });
    
    
    meeting.stage.on("stageStatusUpdate", (status) => {
    	console.log("Stage status updated:", status);
    });
    
    
    meeting.stage.on("stageStatusUpdate", (status) => {
    	console.log("Stage status updated:", status);
    });
    
    
    meeting.addStageEventListener(object : RtkStageEventListener {
    	override fun onStageStatusUpdated(oldStatus: StageStatus, newStatus: StageStatus) {
    		// Local user's stage status changed
    		Log.d("Stage", "Status updated from $oldStatus to $newStatus")
    	}
    })
    
    
    extension WebinarViewModel: RtkStageEventListener {
    	func onStageStatusUpdated(oldStatus: StageStatus, newStatus: StageStatus) {
    		// Local user's stage status changed
    		print("Status updated from \(oldStatus) to \(newStatus)")
    	}
    }
    
    
    meeting.stage.on("stageStatusUpdate", (status) => {
    	console.log("Stage status updated:", status);
    });

### New Stage Request

Emitted when a new participant requests to join the stage.
    
    
    meeting.stage.on("newStageRequest", (request) => {
    	console.log("New stage request:", request);
    });
    
    
    meeting.stage.on("newStageRequest", (request) => {
    	console.log("New stage request:", request);
    });
    
    
    meeting.stage.on("newStageRequest", (request) => {
    	console.log("New stage request:", request);
    });
    
    
    meeting.addStageEventListener(object : RtkStageEventListener {
    	override fun onNewStageAccessRequest(participant: RtkRemoteParticipant) {
    		// New participant requested to join the stage
    		Log.d("Stage", "New stage request from: ${participant.name}")
    	}
    })
    
    
    extension WebinarViewModel: RtkStageEventListener {
    	func onNewStageAccessRequest(participant: RtkRemoteParticipant) {
    		// New participant requested to join the stage
    		print("New stage request from: \(participant.name)")
    	}
    }
    
    
    meeting.stage.on("newStageRequest", (request) => {
    	console.log("New stage request:", request);
    });

### Stage Request Approved

Emitted when a stage request is approved by the host.
    
    
    meeting.stage.on("stageRequestApproved", (data) => {
    	console.log("Stage request approved:", data);
    });
    
    
    meeting.stage.on("stageRequestApproved", (data) => {
    	console.log("Stage request approved:", data);
    });
    
    
    meeting.stage.on("stageRequestApproved", (data) => {
    	console.log("Stage request approved:", data);
    });
    
    
    meeting.addStageEventListener(object : RtkStageEventListener {
    	override fun onStageAccessRequestAccepted() {
    		// Host accepted the join stage request or invited user directly to stage
    		Log.d("Stage", "Stage request approved")
    	}
    })
    
    
    extension WebinarViewModel: RtkStageEventListener {
    	func onStageAccessRequestAccepted() {
    		// Host accepted the join stage request or invited user directly to stage
    		print("Stage request approved")
    	}
    }
    
    
    meeting.stage.on("stageRequestApproved", (data) => {
    	console.log("Stage request approved:", data);
    });

### Stage Request Rejected

Emitted when the host rejects a stage request.
    
    
    meeting.stage.on("stageRequestRejected", (data) => {
    	console.log("Stage request rejected:", data);
    });
    
    
    meeting.stage.on("stageRequestRejected", (data) => {
    	console.log("Stage request rejected:", data);
    });
    
    
    meeting.stage.on("stageRequestRejected", (data) => {
    	console.log("Stage request rejected:", data);
    });
    
    
    meeting.addStageEventListener(object : RtkStageEventListener {
    	override fun onStageAccessRequestRejected() {
    		// Host rejected the join stage request
    		Log.d("Stage", "Stage request rejected")
    	}
    })
    
    
    extension WebinarViewModel: RtkStageEventListener {
    	func onStageAccessRequestRejected() {
    		// Host rejected the join stage request
    		print("Stage request rejected")
    	}
    }
    
    
    meeting.stage.on("stageRequestRejected", (data) => {
    	console.log("Stage request rejected:", data);
    });

[PreviousWaiting Room](https://developers.cloudflare.com/realtime/realtimekit/core/waiting-room/)[NextPlugins](https://developers.cloudflare.com/realtime/realtimekit/core/plugins/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/stage-management.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
