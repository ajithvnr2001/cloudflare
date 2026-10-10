---
url: https://developers.cloudflare.com/ai/models/xai/grok-voice/
title: Grok Voice (xAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:04.729648+00:00
---

# Grok Voice (xAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/xai/grok-voice/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![xAI logo](https://developers.cloudflare.com/_astro/xai.2Y8IhZGx.svg)

# Grok Voice

websocket • xAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`xai/grok-voice`

  * Third-party
  * Zero data retention



xAI's real-time voice conversation model with low-latency audio input and output streaming.

Model Info|   
---|---  
Terms and License| [link ↗](https://x.ai/legal/terms-of-service)  
More information| [link ↗](https://docs.x.ai/developers/rest-api-reference/inference/voice)  
Zero data retention| Yes  
Pricing| 

  * total audio minutes$0.05
  * input text messages$0.004

  
  
## Usage
    
    
    // Establish WebSocket connection
    const response = await fetch(
      `https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run?model=xai/grok-voice`,
      {
        method: 'GET',
        headers: {
          'Authorization': `Bearer $CLOUDFLARE_API_TOKEN`,
          'Upgrade': 'websocket'
        }
      }
    )
    
    const ws = response.webSocket
    ws.accept()
    
    // Send audio chunks
    ws.send(JSON.stringify({
      type: 'input_audio_buffer.append',
      audio: audioBase64
    }))
    
    // Receive transcriptions and audio responses
    ws.addEventListener('message', (event) => {
      const data = JSON.parse(event.data)
      console.log(data)
    })
    
    
    # Note: WebSocket connections require a WebSocket client
    # curl does not support WebSocket upgrade
    # Use wscat, websocat, or a programming language WebSocket library
    
    wscat -c 'wss://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run?model=xai/grok-voice' \
      -H 'Authorization: Bearer $CLOUDFLARE_API_TOKEN'
    
    
    {
      "websocket": {
        "url": "wss://api.x.ai/v1/realtime?model=grok-voice-latest",
        "headers": {
          "Authorization": "Bearer [ephemeral_token]"
        }
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

websocket

`boolean`Enable real-time WebSocket connection for voice conversations. When true, establishes a bidirectional WebSocket for speech-to-speech interaction with Grok voice models.

url

`string`WebSocket URL for the realtime connection (e.g., wss://...)

▶headers{}

`object`Optional headers to include when establishing the WebSocket connection (e.g., Authorization)

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/xai/grok-voice/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-voice/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/xai/grok-voice/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-voice/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
