---
url: https://developers.cloudflare.com/ai/models/pruna/p-video-avatar/
title: P-Video-Avatar (Pruna AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:05.459765+00:00
---

# P-Video-Avatar (Pruna AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/pruna/p-video-avatar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Video-Avatar

Image-to-Video • Pruna AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/pruna/p-video-avatar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-video-avatar`

  * Third-party



Pruna's P-Video-Avatar generates talking-head videos from a single portrait image driven by a text script or audio file, with multiple voices, languages, and output resolutions.

Model Info|   
---|---  
More information| [link ↗](https://docs.api.pruna.ai/guides/quickstart)  
Pricing| 

  * Default (per second)$0.025
  * @720p (per second)$0.025
  * @1080p (per second)$0.045

  
  
## Usage
    
    
    const response = await env.AI.run(
      'pruna/p-video-avatar',
      {
        image: 'https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg',
        voice_script: 'Hello, welcome to our product demo!',
        voice: 'Zephyr (Female)',
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-video-avatar",
      "input": {
        "image": "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg",
        "voice_script": "Hello, welcome to our product demo!",
        "voice": "Zephyr (Female)",
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/pruna/p-video-avatar/product-demo-greeting.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

image

`string`requiredInput portrait image (first frame). HTTP(S) URL or data URI. Supports jpg, jpeg, png, webp.

audio

`string`URL of uploaded audio to drive speech. HTTP(S) URL or data URI. If both audio and voice_script are provided, audio takes priority.

voice

`string`requireddefault: Zephyr (Female)enum: Zephyr (Female), Puck (Male), Charon (Male), Kore (Female), Fenrir (Male), Leda (Female), Orus (Male), Aoede (Female), Callirrhoe (Female), Autonoe (Female), Enceladus (Male), Iapetus (Male), Umbriel (Male), Algenib (Male), Despina (Female), Erinome (Female), Laomedeia (Female), Achernar (Female), Algieba (Male), Schedar (Male), Gacrux (Female), Pulcherrima (Female), Achird (Male), Zubenelgenubi (Male), Vindemiatrix (Female), Sadachbia (Male), Sadaltager (Male), Sulafat (Female), Alnilam (Male), Rasalgethi (Male)Voice for generated speech.

voice_script

`string`requireddefault: Script for the person to say when no audio is uploaded.

voice_language

`string`requireddefault: English (US)enum: English (US), English (UK), Spanish, French, German, Italian, Portuguese (Brazil), Japanese, Korean, HindiOutput language.

resolution

`string`requireddefault: 720penum: 720p, 1080pResolution of the video.

video_prompt

`string`requireddefault: The person is talking.Optional prompt for the video.

voice_prompt

`string`requireddefault: Say the following.Optional speaking style, tone, pacing or emotion instructions.

negative_prompt

`string`requireddefault: Mention what you do NOT want in the video. Disabled if empty.

strength_negative_prompt

`number`requireddefault: 0.5minimum: 0maximum: 4Strength of the negative prompt (0-4).

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation.

disable_safety_filter

`boolean`requireddefault: trueDisable safety filter for prompts and input image.

disable_prompt_upsampling

`boolean`requireddefault: falseWhen true, skip the prompt upsampler and pass the raw user prompt.

video

`string`format: uriPresigned URL for the generated avatar video.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/pruna/p-video-avatar/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-video-avatar/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/pruna/p-video-avatar/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-video-avatar/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
