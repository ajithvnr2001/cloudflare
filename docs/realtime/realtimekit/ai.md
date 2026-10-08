---
url: https://developers.cloudflare.com/realtime/realtimekit/ai/
title: AI \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:52.115868+00:00
---

# AI · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ai/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /AI



# AI

Last updated Sep 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable featuresQuick startStorage and retention

RealtimeKit provides AI-powered features using Cloudflare's AI infrastructure to enhance your meetings with transcription and summarization capabilities.

  * [Transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)
  * [Summary](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/)



## Available features

Feature | Description  
---|---  
[Transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) | Real-time and post-meeting speech-to-text  
[Summary](https://developers.cloudflare.com/realtime/realtimekit/ai/summary/) | AI-generated meeting summaries  
  
## Quick start

Turn on post-meeting transcription and automatic summaries when creating a meeting:
    
    
    {
    	"title": "Team Standup",
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
    }

Use `transcribe_on_end` for post-meeting transcripts. Use `summarize_on_end` for AI-generated summaries. For real-time transcription, make sure participants have `transcription_enabled: true` in their [preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).

## Storage and retention

  * Transcripts and summaries are stored for **7 days** after the meeting ends
  * Files are stored in R2 with presigned URLs for secure access
  * Delivered via [webhooks](https://developers.cloudflare.com/realtime/realtimekit/webhooks/) or REST API



[PreviousAudio Only Calls](https://developers.cloudflare.com/realtime/realtimekit/audio-calls/)[NextTranscription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ai/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
