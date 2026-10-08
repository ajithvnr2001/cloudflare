---
url: https://developers.cloudflare.com/changelog/post/2025-03-20-websockets/
title: AI Gateway launches Realtime WebSockets API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:06.926089+00:00
---

# AI Gateway launches Realtime WebSockets API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-20-websockets/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 21, 2025

## AI Gateway launches Realtime WebSockets API

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-20-websockets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are excited to announce that [AI Gateway](https://developers.cloudflare.com/ai-gateway/) now supports real-time AI interactions with the new [Realtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/).

This new capability allows developers to establish persistent, low-latency connections between their applications and AI models, enabling natural, real-time conversational AI experiences, including speech-to-speech interactions.

The Realtime WebSockets API works with the [OpenAI Realtime API ↗︎](https://platform.openai.com/docs/guides/realtime#connect-with-websockets), [Google Gemini Live API ↗︎](https://ai.google.dev/gemini-api/docs/multimodal-live), and supports real-time text and speech interactions with models from [Cartesia ↗︎](https://docs.cartesia.ai/api-reference/tts/tts), and [ElevenLabs ↗︎](https://elevenlabs.io/docs/conversational-ai/api-reference/conversational-ai/websocket).

Here's how you can connect AI Gateway to [OpenAI's Realtime API ↗︎](https://platform.openai.com/docs/guides/realtime#connect-with-websockets) using WebSockets:

OpenAI Realtime API examplejavascript
    
    
    import WebSocket from "ws";
    
    const url =
    	"wss://gateway.ai.cloudflare.com/v1/<account_id>/<gateway>/openai?model=gpt-4o-realtime-preview-2024-12-17";
    const ws = new WebSocket(url, {
    	headers: {
    		"cf-aig-authorization": process.env.CLOUDFLARE_API_KEY,
    		Authorization: "Bearer " + process.env.OPENAI_API_KEY,
    		"OpenAI-Beta": "realtime=v1",
    	},
    });
    
    ws.on("open", () => console.log("Connected to server."));
    ws.on("message", (message) => console.log(JSON.parse(message.toString())));
    
    ws.send(
    	JSON.stringify({
    		type: "response.create",
    		response: { modalities: ["text"], instructions: "Tell me a joke" },
    	}),
    );

Get started by checking out the [Realtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/) documentation.
