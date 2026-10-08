---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/
title: ElevenLabs \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.270414+00:00
---

# ElevenLabs · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /ElevenLabs



# ElevenLabs

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointPrerequisitesExample cURL

[ElevenLabs ↗︎](https://elevenlabs.io/) offers advanced text-to-speech services, enabling high-quality voice synthesis in multiple languages.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs

## Prerequisites

When making requests to ElevenLabs, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active ElevenLabs API token.
  * The model ID of the ElevenLabs voice model you want to use.



## Example

### cURL

Requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128 \
      --header 'Content-Type: application/json' \
      --header 'xi-api-key: {elevenlabs_api_token}' \
      --data '{
        "text": "Welcome to Cloudflare - AI Gateway!",
        "model_id": "eleven_multilingual_v2"
    }'

[PreviousDeepSeek](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/)[NextFal AI](https://developers.cloudflare.com/ai-gateway/usage/providers/fal/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/elevenlabs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
