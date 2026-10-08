---
url: https://developers.cloudflare.com/realtime/realtimekit/core/polls/
title: Polls \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:01.608818+00:00
---

# Polls · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/polls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)
  5. /Polls



# Polls

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/polls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntroduction Poll TypeCreating a PollVoting on a PollOther Poll Functions View Poll Results Get Notified When a Poll is Created or Updated

This guide explains how to create, vote on, and interact with polls in a meeting using Cloudflare RealtimeKit.

WebMobile

ReactWeb ComponentsAngular

## Introduction

The meetings polls object can be accessed using `meeting.polls`. It provides methods to create polls, vote, and more.
    
    
    console.log("Polls object:", meeting.polls);

The `meeting.polls.items` property returns an array of all polls created in a meeting, where each element is an object of type `Poll`.
    
    
    console.log("All polls:", meeting.polls.items);

The meetings polls object can be accessed using `meeting.polls`. It provides methods to create polls, vote, and more.
    
    
    console.log("Polls object:", meeting.polls);

The `meeting.polls.items` property returns an array of all polls created in a meeting, where each element is an object of type `Poll`.
    
    
    console.log("All polls:", meeting.polls.items);

You can access the polls functionality in a meeting using the `meeting.polls` object. This object provides methods to create polls, vote, and perform other poll-related actions.

To retrieve all polls created during a meeting, use `meeting.polls.items`. This returns an array where each element is an object of type `com.cloudflare.realtimekit.polls.Poll`.

The meetings polls object can be accessed using `meeting.polls`. It provides methods to create polls, vote, and more.

`meeting.polls.items` returns an array of all polls created in a meeting, where each element is an object of type `Poll`.

The meetings polls object can be accessed using `meeting.polls`. It provides methods to create polls, vote, and more.

`meeting.polls.items` returns an array of all polls created in a meeting, where each element is an object of type `Poll`.

### Poll Type

The `Poll` type is defined as follows:
    
    
    interface Poll {
    	id: string;
    	question: string;
    	options: PollOption[];
    	anonymous: boolean;
    	hideVotes: boolean;
    	createdBy: string;
    	createdByUserId: string;
    	voted: string[]; // stores participant ID
    }
    
    interface PollOption {
    	text: string;
    	votes: {
    		id: string; // stores participant ID
    		name: string;
    	}[];
    	count: number;
    }

The `Poll` type is defined as follows:
    
    
    interface Poll {
    	id: string;
    	question: string;
    	options: PollOption[];
    	anonymous: boolean;
    	hideVotes: boolean;
    	createdBy: string;
    	createdByUserId: string;
    	voted: string[]; // stores participant ID
    }
    
    interface PollOption {
    	text: string;
    	votes: {
    		id: string; // stores participant ID
    		name: string;
    	}[];
    	count: number;
    }

The `Poll` type represents a poll within a meeting:
    
    
    class Poll(
      val id: String,
      val question: String,
      val anonymous: Boolean,
      val hideVotes: Boolean,
      val createdBy: String,
      val options: List<PollOption>,
      val voted: List<String>,
    )

Each poll contains a list of `PollOption` objects, representing the available options for that poll.

Every `PollOption` includes a list of `PollVote` objects, where each vote contains the voter's `id` and `name`.
    
    
    class PollOption(
      val text: String,
      val votes: List<PollVote>,
      val count: Int
    )
    
    
    class PollVote(
      val id: String,
      val name: String
    )

The `Poll` type is defined as follows:
    
    
    class Poll {
      let id: String
      let question: String
      let anonymous: Bool
      let hideVotes: Bool
      let createdBy: String
      let options: [PollOption]
      let voted: [String]
    }

The type `Poll` is the main class for any poll in RealtimeKit. It also contains list of `PollOption` which are options for a given poll. And every `PollOption` has list of votes inside of it. Votes are objects of class `PollVote` which internally has id and name of the vote.
    
    
    class PollOption {
      let text: String
      let votes: [PollVote]
      let count: Int
    }
    
    class PollVote {
      let id: String
      let name: String
    }

The `Poll` type is defined as follows:
    
    
    interface Poll {
    	id: string;
    	question: string;
    	options: PollOption[];
    	anonymous: boolean;
    	hideVotes: boolean;
    	createdBy: string;
    	createdByUserId: string;
    	voted: string[]; // stores participant ID
    }
    
    interface PollOption {
    	text: string;
    	votes: {
    		id: string; // stores participant ID
    		name: string;
    	}[];
    	count: number;
    }

## Creating a Poll

A new poll can be created using the `create` method from the `meeting.polls` object. The `meeting.polls.create()` method accepts the following parameters:

  * `question` (string) - The poll question
  * `options` (string[]) - Array of poll options
  * `anonymous` (boolean) - Whether votes are anonymous
  * `hideVotes` (boolean, optional) - Whether to hide vote counts



The following snippet creates a poll where votes are anonymous:
    
    
    await meeting.polls.create(
    	"Are you an early bird or a night owl?",
    	["Early bird", "Night owl"],
    	true,
    );

A new poll can be created using the `create` method from the `meeting.polls` object. The `meeting.polls.create()` method accepts the following parameters:

  * `question` (string) - The poll question
  * `options` (string[]) - Array of poll options
  * `anonymous` (boolean) - Whether votes are anonymous
  * `hideVotes` (boolean, optional) - Whether to hide vote counts



The following snippet creates a poll where votes are anonymous:
    
    
    await meeting.polls.create(
    	"Are you an early bird or a night owl?",
    	["Early bird", "Night owl"],
    	true,
    );

To create a new poll, use the `create` method available on the `meeting.polls` object. The `meeting.polls.create()` function requires the following parameters:

Param | Type | Required | Description  
---|---|---|---  
question | `String` | yes | The question that is to be voted for.  
options | `List<String>` | yes | The options of the poll.  
anonymous | `Boolean` | yes | If true, the poll votes are anonymous.  
hideVotes | `Boolean` | yes | If true, the votes on the poll are hidden.  
  
The following snippet creates a poll where votes are anonymous.
    
    
    val pollsCreateError: PollsError? = meeting.polls.create(
      question = "Are you an early bird or a night owl?",
      options = listOf("Early bird", "Night owl"),
      anonymous = true,
      hideVotes = false
    )

A new poll can be created using the `create` method from the `meeting.polls` object. The `meeting.polls.createPoll()` method accepts the following parameters:

Param | Type | Default Value | Required | Description  
---|---|---|---|---  
question | `string` | - | yes | The question that is to be voted for.  
options | `string[]` | - | yes | The options of the poll.  
anonymous | `boolean` | - | no | If true, the poll votes are anonymous.  
hideVotes | `boolean` | - | no | If true, the votes on the poll are hidden.  
  
The following snippet creates a poll where votes are anonymous.
    
    
    let pollsCreateError: PollsError? = meeting.polls.createPoll(
        question: "Are you an early bird or a night owl?",
        options: ["Early bird", "Night owl"],
        anonymous: true,
        hideVotes: false
    )

A new poll can be created using the `create` method from the `meeting.polls` object. The `meeting.polls.create()` method accepts the following parameters:

Param | Type | Default Value | Required | Description  
---|---|---|---|---  
question | `string` | - | yes | The question that is to be voted for.  
options | `string[]` | - | yes | The options of the poll.  
anonymous | `boolean` | false | no | If true, the poll votes are anonymous.  
hideVotes | `boolean` | false | no | If true, the votes on the poll are hidden.  
  
The following snippet creates a poll where votes are anonymous.
    
    
    await meeting.poll.create(
    	"Are you an early bird or a night owl?",
    	["Early bird", "Night owl"],
    	true,
    );

## Voting on a Poll

The `meeting.polls.vote()` method can be used to register a vote on a poll. It accepts the following parameters:

  * `pollId` (string) - The ID of the poll
  * `optionIndex` (number) - The index of the selected option



The following snippet votes for the first option on the first poll created in the meeting:
    
    
    const poll = meeting.polls.items[0];
    await meeting.polls.vote(poll.id, 0);

The `meeting.polls.vote()` method can be used to register a vote on a poll. It accepts the following parameters:

  * `pollId` (string) - The ID of the poll
  * `optionIndex` (number) - The index of the selected option



The following snippet votes for the first option on the first poll created in the meeting:
    
    
    const poll = meeting.polls.items[0];
    await meeting.polls.vote(poll.id, 0);

To register a vote on a poll, use the `meeting.polls.vote()` method. This method requires the following parameters:

Param | Type | Default Value | Required | Description  
---|---|---|---|---  
pollMessage | `Poll` | - | yes | The poll message to vote on.  
pollOption | `PollOption` | - | yes | The option to vote for.  
  
The following snippet votes for the first option on the first poll created in the meeting.
    
    
    val poll: Poll = meeting.polls.items.first()
    val selectedPollOption: PollOption = poll.options.first()
    
    val pollsError: PollsError? = meeting.polls.vote(poll.id, selectedPollOption)

The `meeting.polls.vote()` method can be used to register a vote on a poll. It accepts the following parameters:

Param | Type | Default Value | Required | Description  
---|---|---|---|---  
pollMessage | `Poll` | - | yes | The poll message to vote on.  
pollOption | `PollOption` | - | yes | The option to vote for.  
  
The following snippet votes for the first option on the first poll created in the meeting.
    
    
    let poll: Poll = meeting.polls.items[0]
    let selectedPollOption: PollOption = poll.options[0]
    
    meeting.poll.vote(poll, selectedPollOption)

The `meeting.polls.vote()` method can be used to register a vote on a poll. It accepts the following parameters:

Param | Type | Default Value | Required | Description  
---|---|---|---|---  
id | `string` | - | yes | The ID of the poll that is to be voted on.  
index | `number` | - | yes | The index of the option.  
  
The following snippet votes for the first option on the first poll created in the meeting.
    
    
    const poll = meeting.polls.items[0];
    await meeting.poll.vote(poll.id, 0);

## Other Poll Functions

### View Poll Results

The total votes on a poll can be accessed in the following manner:
    
    
    const poll = meeting.polls.items[0];
    const votes = poll.voted;

`votes` is an array of participant IDs (`meeting.participant.id`).

The total votes on a poll option can be accessed in the following manner:
    
    
    const poll = meeting.polls.items[0];
    const options = poll.options;

`options` returns an array of objects, where each object is of type `PollOption`.

The total votes on a poll can be accessed in the following manner:
    
    
    const poll = meeting.polls.items[0];
    const votes = poll.voted;

`votes` is an array of participant IDs (`meeting.participant.id`).

The total votes on a poll option can be accessed in the following manner:
    
    
    const poll = meeting.polls.items[0];
    const options = poll.options;

`options` returns an array of objects, where each object is of type `PollOption`.

The total votes on a poll can be accessed in the following manner:
    
    
    val poll = meeting.polls.items[0]
    val votes = poll.voted

`votes` is an array of participant IDs (`meeting.participant.id`).

The total votes on a poll option can be accessed in the following manner:
    
    
    val poll = meeting.polls.items[0]
    val options = poll.options

`options` returns an array of objects, where each object is of type `PollOption`.

The total votes on a poll can be accessed in the following manner:
    
    
    let poll = meeting.polls.items[0]
    let votes = poll.voted

`votes` is an array of participant IDs (`meeting.participant.id`).

The total votes on a poll option can be accessed in the following manner:
    
    
    let poll = meeting.polls.items[0]
    let options = poll.options

`options` returns an array of objects, where each object is of type `PollOption`.

The total votes on a poll can be accessed in the following manner:
    
    
    const poll = meeting.polls.items[0];
    const votes = poll.voted;

`votes` is an array of participant IDs (`meeting.participant.id`).

The total votes on a poll option can be accessed in the following manner:
    
    
    const poll = meeting.polls.items[0];
    const options = poll.options;

`options` returns an array of objects, where each object is of type `PollOption`.

### Get Notified When a Poll is Created or Updated

An event is fired each time `meeting.polls.items` is updated or created. You can listen for this to get the updated list of polls. The response object contains the following properties:

  * `polls` \- List of all polls
  * `newPoll` \- A boolean variable which is `true` when a new poll has been created


    
    
    meeting.polls.on("pollsUpdate", ({ polls, newPoll }) => {
    	console.log("Polls updated:", polls);
    	console.log("Is new poll:", newPoll);
    });

An event is fired each time `meeting.polls.items` is updated or created. You can listen for this to get the updated list of polls. The response object contains the following properties:

  * `polls` \- List of all polls
  * `newPoll` \- A boolean variable which is `true` when a new poll has been created


    
    
    meeting.polls.on("pollsUpdate", ({ polls, newPoll }) => {
    	console.log("Polls updated:", polls);
    	console.log("Is new poll:", newPoll);
    });

Alternatively, you can use React hooks to listen for poll updates:
    
    
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react";
    
    // useRealtimeKitSelector hook only works when `RealtimeKitProvider` is used.
    const polls = useRealtimeKitSelector((m) => m.polls.items);

An event is fired each time `meeting.polls.items` is updated or created. You can listen for this to get the updated list of polls. The response object contains the following properties:

  * `polls` \- List of all polls
  * `newPoll` \- A boolean variable which is `true` when a new poll has been created


    
    
    meeting.polls.on("pollsUpdate", ({ polls, newPoll }) => {
    	console.log(polls, newPoll);
    });

To receive updates about new polls or poll changes during a meeting, implement the `RtkPollsEventListener` interface. Register your listener using `meeting.addPollsEventListener(rtkPollsEventListener)`.

The `onNewPoll()` method is called whenever a new poll is created in the meeting.

The `onPollUpdate()` method is invoked when a specific poll is updated, such as when participants vote or poll details change. The `onPollUpdates()` method is called when there are updates to the list of polls, including new polls being created or multiple polls being updated at once. Use these callbacks to keep your poll UI in sync with the latest poll data.
    
    
    meeting.addPollsEventListener(object : RtkPollsEventListener {
        override fun onNewPoll(poll: Poll) {
        }
    
        override fun onPollUpdate(poll: Poll) {
        }
    
        override fun onPollUpdates(pollItems: List<Poll>) {
        }
      }
    )

To be able to receive new poll messages you need to implement a method `onPollUpdates()` method from callback `RtkPollsEventListener`. You can subscribe to this events by calling `meeting.addPollsEventListener(meetingViewModel)`
    
    
    extension MeetingViewModel: RtkPollsEventListener {
      func onNewPoll(poll: Poll) {
        // code to handle new poll
      }
    
      func onPollUpdates(pollItems: [Poll]) {
        // code to handle polls and their vote updates.
      }
    
      func onPollUpdate(poll: Poll) {}
    }

[PreviousChat](https://developers.cloudflare.com/realtime/realtimekit/core/chat/)[NextVideo Effects](https://developers.cloudflare.com/realtime/realtimekit/core/video-effects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/polls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
