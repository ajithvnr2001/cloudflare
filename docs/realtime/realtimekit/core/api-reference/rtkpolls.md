---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/
title: RTKPolls \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:56.644341+00:00
---

# RTKPolls · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKPolls



# RTKPolls

Last updated Jul 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpolls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.polls.items meeting.polls.create(question, options, anonymous, hideVotes) meeting.polls.vote(pollId, index)

The RTKPolls module consists of the polls that have been created in the meeting.

  * RTKPolls
    * .items
    * .create(question, options, anonymous, hideVotes)
    * .vote(pollId, index)



### meeting.polls.items

An array of poll items.

**Kind** : instance property of `RTKPolls`  


### meeting.polls.create(question, options, anonymous, hideVotes)

Creates a poll in the meeting.

**Kind** : instance method of `RTKPolls`

Param | Default | Description  
---|---|---  
question |  | The question that is to be voted for.  
options |  | The options of the poll.  
anonymous | `false` | If true, the poll votes are anonymous.  
hideVotes | `false` | If true, the votes on the poll are hidden.  
  
### meeting.polls.vote(pollId, index)

Casts a vote on an existing poll.

**Kind** : instance method of `RTKPolls`

Param | Description  
---|---  
pollId | The ID of the poll that is to be voted on.  
index | The index of the option.  
  
[PreviousRTKPlugins](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/)[NextRTKRecording](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkrecording/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKPolls.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
