---
url: https://developers.cloudflare.com/realtime/realtimekit/ai/summary/
title: Summary \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:52.673985+00:00
---

# Summary · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ai/summary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[AI](https://developers.cloudflare.com/realtime/realtimekit/ai/)
  5. /Summary



# Summary

Last updated Jun 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTurn on summarizationConfiguration Summary typesConsume summaries Webhook REST APIExample outputRetention

RealtimeKit generates AI-powered meeting summaries from transcript data.

Note

Summarization requires a transcript. To generate summaries automatically when a meeting ends, turn on [real-time transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#real-time-transcription) or [post-meeting transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#post-meeting-transcription), and set `summarize_on_end: true`. With post-meeting transcription, RealtimeKit generates the summary after the transcript is available.

## Turn on summarization

Set `summarize_on_end: true` when [creating a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/). For post-meeting summaries, also set `transcribe_on_end: true` so RealtimeKit generates the summary automatically after the transcript is available:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "title": "Product Review",
        "transcribe_on_end": true,
        "summarize_on_end": true,
        "ai_config": {
          "transcription": {
            "language": "en-US"
          },
          "summarization": {
            "word_limit": 500,
            "text_format": "markdown",
            "summary_type": "team_meeting"
          }
        }
      }'

## Configuration

Option | Type | Default | Description  
---|---|---|---  
`word_limit` | number | 500 | Summary length (150-1000 words)  
`text_format` | string | `markdown` | Output format: `plain_text` or `markdown`  
`summary_type` | string | `general` | Meeting context for tailored summaries  
  
### Summary types

Choose a type that matches your meeting for better results:

Type | Best for  
---|---  
`general` | Any meeting (default)  
`team_meeting` | Regular team syncs  
`daily_standup` | Agile standups  
`one_on_one_meeting` | 1:1 meetings  
`sales_call` | Customer sales conversations  
`client_check_in` | Client status updates  
`interview` | Job interviews  
`lecture` | Educational content  
`code_review` | Technical code reviews  
  
## Consume summaries

### Webhook

Configure the `meeting.summary` event in [RealtimeKit webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/#meetingsummary) to receive the summary download URL when it is ready:
    
    
    {
    	"event": "meeting.summary",
    	"meeting": {
    		"id": "bbb8940e-1b97-402a-97d6-2708b7feca41",
    		"sessionId": "05e57591-d89e-45c9-ae44-08dc1eaad0e0",
    		"organizedBy": {
    			"id": "c94c437b-592a-4a39-b9e2-47ef1451e43b",
    			"name": "Example organization"
    		}
    	},
    	"summaryDownloadUrl": "https://example.com/summary.txt",
    	"summaryDownloadUrlExpiry": "2026-06-10T10:30:00.000Z"
    }

### REST API

#### Fetch summary

Refer to [Fetch summary of transcripts for a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/).
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

#### Trigger manually

Use the [Generate summary of transcripts for the session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/) API if `summarize_on_end` was not set and you want to generate a summary manually after the transcript is available.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Example output

With `text_format: "markdown"` and `summary_type: "team_meeting"`:
    
    
    ## Meeting Summary
    
    ### Key Discussion Points
    
    - Reviewed Q4 roadmap priorities
    - Discussed deployment timeline for v2.0
    - Identified blockers for the auth migration
    
    ### Action Items
    
    - @alice: Update design specs by Friday
    - @bob: Schedule security review
    - @charlie: Create migration runbook
    
    ### Decisions Made
    
    - Approved moving forward with Kubernetes migration
    - Delayed analytics dashboard to next sprint

## Retention

Summaries are stored for **7 days** after the meeting ends.

[PreviousTranscription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)[NextWebhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ai/summary.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
