---
url: https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-video-caption/
title: Automatic captioning for video uploads \u00b7 Cloudflare Reference Architecture docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:40.697574+00:00
---

# Automatic captioning for video uploads · Cloudflare Reference Architecture docs

> Source: https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-video-caption/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Reference Architecture](https://developers.cloudflare.com/reference-architecture/)
  3. /…

Reference Architecture Diagrams

  4. /Artificial Intelligence (AI)
  5. /Automatic captioning for video uploads



# Automatic captioning for video uploads

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-video-caption/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntroductionAutomatic captioning on uploadRelated resources

## Introduction

Automatic Speech Recognition (ASR) models have revolutionized the accessibility of video content by enabling the generation of subtitles and translations. These models utilize advanced algorithms to transcribe spoken words into text with high accuracy. By integrating ASR technology into video platforms, content creators, publishers, and distributors can reach a broader audience, including individuals with hearing impairments or those who prefer to consume content in different languages.

The process begins with capturing the audio from the video source, which is then fed into the ASR model. This model analyzes the audio waveform and converts it into a textual representation, capturing the spoken content in the form of subtitles. Furthermore, you can also use ASR models for language translation, enabling the creation of multilingual subtitles. Once the subtitles are generated, they can be displayed alongside the video, providing a synchronized text representation of the spoken content.

## Automatic captioning on upload

![Figure 1: Automatic captioning on upload](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=600,format=svg/_astro/ai-auto-caption-architecture-diagram.CyBpgQKS.svg)Figure 1: Automatic captioning on upload

  1. **Client upload** : Send POST request with both video and audio to API endpoint.
  2. **Audio transcription** : Generate timestamped transcriptions by calling [Workers AI](https://developers.cloudflare.com/workers-ai/) [automatic speech recognition (ARS) model](https://developers.cloudflare.com/workers-ai/models/) with audio as input. Use [Workers](https://developers.cloudflare.com/workers/) to convert the output to a supported subtitled format.
  3. **Store subtitles** : Store the subtitle file(s) on [R2](https://developers.cloudflare.com/r2/).
  4. **Store video** : Store the video files on [R2](https://developers.cloudflare.com/r2/).
  5. **Client request** : Send GET requests for video and subtitle(s) to origin. Use global [Cache](https://developers.cloudflare.com/cache/) to increase performance.
  6. **Origin request** : Fetch file(s) from [R2](https://developers.cloudflare.com/r2/) on cache `MISS` by using [Public Buckets](https://developers.cloudflare.com/r2/buckets/public-buckets/).



## Related resources

  * [Community project: automatic captioning demo ↗︎](https://auto-caption.pages.dev/)
  * [Workers AI: Automatic speech recognition (ARS) model](https://developers.cloudflare.com/workers-ai/models/)
  * [R2: Object storage for all your data](https://developers.cloudflare.com/r2/)



[PreviousAI Vibe Coding Platform](https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-vibe-coding-platform/)[NextComposable AI architecture](https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-composable/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/reference-architecture/diagrams/ai/ai-video-caption.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
