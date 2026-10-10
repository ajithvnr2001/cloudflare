---
url: https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/
title: Clef-omni adds audio and video input, Clef-flash is now cheaper, and Clef is faster \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T07:57:29.174548+00:00
---

# Clef-omni adds audio and video input, Clef-flash is now cheaper, and Clef is faster · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 9, 2026

## Clef-omni adds audio and video input, Clef-flash is now cheaper, and Clef is faster

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/cloudflare/clef-omni`](https://developers.cloudflare.com/workers-ai/models/clef-omni/) is now available on Workers AI. Clef-omni is a decision model that takes audio (WAV or MP3) and video (MP4 or WebM) input alongside text and images. It joins [Clef](https://developers.cloudflare.com/workers-ai/models/clef/) and [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/) in the Clef family of open-weight decision models. We also cut the price of Clef-flash, so it now costs less than Jev, and made Clef faster.

#### Clef-omni: one decision model for every modality

Previously, making a decision about a voice recording or a video meant chaining models together: transcribe the speech, split the audio and visual tracks, then pass the results to a text decision model. Clef-omni reads every modality directly in one request. A video's soundtrack is aligned with its frames, so the model can reason over what is seen and heard at the same time.

Clef-omni is built on a 30B-parameter mixture-of-experts (MoE) backbone with 3B active parameters. Like the rest of the Clef family, it does not generate text. It scores every allowed answer in a single pass, so decisions return quickly:

  * Text requests: about 20 ms
  * Image or audio inputs: under 100 ms
  * A 21-second video clip with sound: about 300 ms



Pass media as base64 data URLs in the `images`, `audio`, and `videos` fields:
    
    
    const response = await env.AI.run("@cf/cloudflare/clef-omni", {
    	model: "clef-omni",
    	state:
    		"Review the installation: a photo of the unit, an audio recording of it running, and a video of the fan.",
    	images: ["data:image/png;base64,<base64-png>"],
    	audio: ["data:audio/mpeg;base64,<base64-mp3>"],
    	videos: ["data:video/mp4;base64,<base64-mp4>"],
    	questions: {
    		label_visible: {
    			type: "noul",
    			instructions:
    				"Is the model and serial number label visible in the photo?",
    		},
    		sounds_normal: {
    			type: "noul",
    			instructions:
    				"Does the unit sound like it is running smoothly, without rattling or grinding?",
    		},
    		fan_running: {
    			type: "noul",
    			instructions: "Is the fan running in the video?",
    		},
    	},
    });
    
    
    const response = await env.AI.run("@cf/cloudflare/clef-omni", {
    	model: "clef-omni",
    	state:
    		"Review the installation: a photo of the unit, an audio recording of it running, and a video of the fan.",
    	images: ["data:image/png;base64,<base64-png>"],
    	audio: ["data:audio/mpeg;base64,<base64-mp3>"],
    	videos: ["data:video/mp4;base64,<base64-mp4>"],
    	questions: {
    		label_visible: {
    			type: "noul",
    			instructions:
    				"Is the model and serial number label visible in the photo?",
    		},
    		sounds_normal: {
    			type: "noul",
    			instructions:
    				"Does the unit sound like it is running smoothly, without rattling or grinding?",
    		},
    		fan_running: {
    			type: "noul",
    			instructions: "Is the fan running in the video?",
    		},
    	},
    });

Clef-omni scores highest of the Clef family on BANKING77, CLINC150+OOS, and Amazon ESCI:

Benchmark | Clef-omni | Clef | Clef-flash | Jev  
---|---|---|---|---  
BFCL (case exact) | 98.2 | 98.47 | **98.76** | 95.75  
BANKING77 (macro-F1) | **94.8** | 94.20 | 90.93 | 79.74  
CLINC150+OOS (macro-F1) | **97.7** | 97.43 | 66.77 | 89.27  
Amazon ESCI (macro-F1) | **57.8** | 57.48 | 57.39 | 55.21  
PhishNChips (accuracy) | 73.2 | **79.60** | 75.05 | 62.55  
  
#### Clef-flash is now cheaper

Clef-flash now costs **$0.038 per million input tokens** , down from $0.090, which makes it cheaper than Jev. To offer this price, the hosted Clef-flash context window is now 24K tokens, down from 64K. Based on usage data, only 0.24% of requests exceed 24K input tokens. If you need a larger context window, use Clef, which keeps its 64K context window.

The Clef-flash weights on Hugging Face are unchanged and support up to a 256K context window if you self-host.

Model | Price | Context window  
---|---|---  
[`@cf/cloudflare/clef-flash`](https://developers.cloudflare.com/workers-ai/models/clef-flash/) | $0.038 per M input tokens | 24K tokens  
[`@cf/cloudflare/clef`](https://developers.cloudflare.com/workers-ai/models/clef/) | $0.240 per M input tokens | 64K tokens  
[`@cf/cloudflare/clef-omni`](https://developers.cloudflare.com/workers-ai/models/clef-omni/) | $0.150 per M input tokens | 64K tokens  
  
All Clef models convert image inputs to input tokens, and Clef-omni does the same for audio and video. For details on how each input type is tokenized, refer to the [Clef](https://developers.cloudflare.com/workers-ai/models/clef/), [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/), and [Clef-omni](https://developers.cloudflare.com/workers-ai/models/clef-omni/) model pages.

#### Clef is now faster

We optimized how Clef is served on Workers AI, so it now returns decisions up to 2x faster. The model weights are unchanged.

Input size | Before: median / p95 (ms) | Now: median / p95 (ms) | Median speedup  
---|---|---|---  
~800 tokens | 262 / 438 | 152 / 351 | 1.7x  
~3,400 tokens | 616 / 777 | 305 / 531 | 2.0x  
~16,000 tokens | 2,721 / 3,250 | 1,635 / 1,805 | 1.7x  
  
Part of this speedup comes from moving Clef to [SGLang ↗︎](https://github.com/sgl-project/sglang). Clef support is coming to SGLang in version 0.5.22 ([PR #42721 ↗︎](https://github.com/sgl-project/sglang/pull/42721)). If you self-host Clef, launch commands are available in the [Clef collection on Hugging Face ↗︎](https://huggingface.co/collections/Cloudflare/clef).

#### Get started

Clef-omni follows the same System One API as Clef and Clef-flash, and works with [AI Gateway](https://developers.cloudflare.com/ai-gateway/). To try it, change the model ID to `@cf/cloudflare/clef-omni` and set the `model` selector to `clef-omni`.

For more information, refer to the [Clef-omni model page](https://developers.cloudflare.com/workers-ai/models/clef-omni/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).
