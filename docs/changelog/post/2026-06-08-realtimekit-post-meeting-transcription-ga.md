---
url: https://developers.cloudflare.com/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/
title: Post-meeting transcriptions are now Generally Available in RealtimeKit \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:56.927013+00:00
---

# Post-meeting transcriptions are now Generally Available in RealtimeKit · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 8, 2026

## Post-meeting transcriptions are now Generally Available in RealtimeKit

[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/) lets you build products where people meet over live audio and video — such as HealthTech, EdTech, proctoring, and other real-time platforms — on Cloudflare's [global WebRTC infrastructure](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/).

[Post-meeting transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#post-meeting-transcription) is now Generally Available, so completed RealtimeKit meetings can automatically produce full transcript files after they end. Those transcripts can also power [AI-generated summaries](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/) for meeting notes, review workflows, and follow-up tasks after the transcript is available.

Post-meeting transcription is a managed service powered by [Workers AI](https://developers.cloudflare.com/workers-ai/) using [Whisper Large v3 Turbo](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/). RealtimeKit handles transcription processing and can return transcript and summary files through [webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/) or the REST API, so you do not need to run your own transcription infrastructure.

#### Generate transcripts and summaries

To generate a transcript after a meeting ends, set `transcribe_on_end: true` when [creating a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/). To also generate an AI summary automatically after the transcript is available, set `summarize_on_end: true`:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "title": "Weekly product review",
        "transcribe_on_end": true,
        "summarize_on_end": true,
        "ai_config": {
          "transcription": {
            "language": "en"
          },
          "summarization": {
            "word_limit": 500,
            "text_format": "markdown",
            "summary_type": "team_meeting"
          }
        }
      }'

#### Consume results

When RealtimeKit finishes processing a meeting, it creates download URLs for the transcript and, if `summarize_on_end` is set, the summary. You can receive those URLs automatically with [webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/), or fetch them later for a specific session with the [REST API](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/#rest-api).

To receive results as soon as they are ready, configure the `meeting.transcript` and `meeting.summary` webhook events:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "AI results webhook",
        "url": "https://example.com/webhook",
        "events": ["meeting.transcript", "meeting.summary"],
        "enabled": true
      }'

To fetch results later, call the [transcript](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/) or [summary](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/) endpoint for the session:
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Use the [Generate summary of transcripts for the session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/) API only if `summarize_on_end` was not set and you want to generate a summary manually after the transcript is available:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Post-meeting transcription supports [CSV, JSON, SRT, and VTT transcript outputs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#output-formats), [automatic language detection and Whisper language codes](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#post-meeting-supported-languages). RealtimeKit also supports [real-time transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#real-time-transcription) with [Deepgram Nova-3](https://developers.cloudflare.com/workers-ai/models/nova-3/) for live captions, in-meeting accessibility, and real-time note-taking.

Learn more in the [RealtimeKit transcription docs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) and [summary docs](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/).
