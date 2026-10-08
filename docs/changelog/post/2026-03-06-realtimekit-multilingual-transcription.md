---
url: https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/
title: Real-time transcription in RealtimeKit now supports 10 languages with regional variants \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:40.093318+00:00
---

# Real-time transcription in RealtimeKit now supports 10 languages with regional variants · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 6, 2026

## Real-time transcription in RealtimeKit now supports 10 languages with regional variants

[Workers AI](https://developers.cloudflare.com/workers-ai/)[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-06-realtimekit-multilingual-transcription/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Real-time transcription](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/) in RealtimeKit now supports 10 languages with regional variants, powered by [Deepgram Nova-3](https://developers.cloudflare.com/workers-ai/models/nova-3/) running on [Workers AI](https://developers.cloudflare.com/workers-ai/).

During a meeting, participant audio is routed through [AI Gateway](https://developers.cloudflare.com/ai-gateway/) to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.

Set the language when [creating a meeting](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/) via `ai_config.transcription.language`:
    
    
    {
    	"ai_config": {
    		"transcription": {
    			"language": "fr"
    		}
    	}
    }

Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like `en-AU`, `en-GB`, `en-IN`, `en-NZ`, `es-419`, `fr-CA`, `de-CH`, `pt-BR`, and `pt-PT`. Use `multi` for automatic multilingual detection.

If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.

  * [Transcription docs](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/)
  * [Nova-3 model page](https://developers.cloudflare.com/workers-ai/models/nova-3/)
  * [Workers AI](https://developers.cloudflare.com/workers-ai/)
  * [AI Gateway](https://developers.cloudflare.com/ai-gateway/)


