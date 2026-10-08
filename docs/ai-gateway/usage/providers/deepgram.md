---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/
title: Deepgram \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.384308+00:00
---

# Deepgram · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Deepgram



# Deepgram

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL StructurePrerequisitesExample SDK

[Deepgram ↗︎](https://developers.deepgram.com/home) provides Voice AI APIs for speech-to-text, text-to-speech, and voice agents.

Note

Deepgram is also available through Workers AI, see [Deepgram Workers AI](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/#deepgram-workers-ai).

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram

## URL Structure

When making requests to Deepgram, replace `https://api.deepgram.com/` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/`.

## Prerequisites

When making requests to Deepgram, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Deepgram API token.



## Example

### SDK

TSts
    
    
    import { createClient, LiveTranscriptionEvents } from "@deepgram/sdk";
    
    
    const deepgram = createClient("{deepgram_api_key}", {
        global: {
          websocket: {
            options: {
              url: "wss://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/",
              _nodeOnlyHeaders: {
                "cf-aig-authorization": "Bearer {CF_AIG_TOKEN}"
              }
            }
          }
        }
    });
    
    
    const connection = deepgram.listen.live({
        model: "nova-3",
        language: "en-US",
        smart_format: true,
    });
    
    connection.send(...);

[PreviousCohere](https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/)[NextDeepSeek](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/deepgram.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
