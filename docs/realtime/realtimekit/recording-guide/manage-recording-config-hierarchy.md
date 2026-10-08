---
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/
title: Manage Recording Config Precedence Order \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:07.035927+00:00
---

# Manage Recording Config Precedence Order · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Recording](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/)
  5. /Manage Recording Config Precedence Order



# Manage Recording Config Precedence Order

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUnderstand Recording Configuration PrecedenceExample Scenario

This document provides an overview of the precedence structure for managing recording configurations within our system. It explains how various configuration levels interact and prioritize settings. The recording configuration can be defined at three different levels:

  * [Start recording a meeting API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/)
  * [Create a meeting API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/)
  * Specified via [Cloudflare RealtimeKit Dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/realtime/kit)



## Understand Recording Configuration Precedence

To comprehend the precedence of recording configurations, it is important to delve into the following details. This understanding becomes crucial when dealing with multiple configurations set through APIs and the developer portal.

Precedence | Config | Description  
---|---|---  
1 | [Start recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/) configs | Highest priority in the system. Any settings defined here will take precedence over other configurations.  
2 | [Create a meeting API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/) configs | Second level of priority in the system. Settings here will supersede Org level config but not Start recording a meeting API configs.  
3 | Specified via Dashboard | Lowest priority in the system. Settings defined here will be overridden by both Start recording a meeting API config and Create a meeting API config.  
  
## Example Scenario

To illustrate the precedence order in action, consider the following scenario for the same meeting:

  1. Org Level Config specifies that recordings to be stored in the Cloudflare R2 bucket.

  2. Create a Meeting API sets recordings to be stored in the AWS S3 storage bucket using the H264 codec.

  3. Start recording a meeting API is configured to store recordings in the GCS bucket using the VP8 codec.




In this scenario, the Start recording a meeting API takes precedence over the Create a Meeting API Config and Org Level Config. As a result, the meeting's recording will be stored in the GCS bucket using VP8 codec, regardless of the defaults set at other levels.

Manage Recording Config Precedence Order Guide

[PreviousInteractive Recordings with Timed Metadata](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/interactive-recording/)[NextUpload Recording to Your Cloud](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/recording-guide/manage-recording-config-hierarchy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
