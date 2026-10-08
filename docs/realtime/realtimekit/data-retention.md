---
url: https://developers.cloudflare.com/realtime/realtimekit/data-retention/
title: Data retention \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:03.879983+00:00
---

# Data retention · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/data-retention/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /Data retention



# Data retention

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/data-retention/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

RealtimeKit retains data for the following periods:

Data type | Retention period  
---|---  
Meeting and participant records | Indefinitely  
Meeting chat with [`persist_chat`](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/#\(resource\)%20realtime_kit.meetings%20%3E%20\(method\)%20create%20%3E%20\(params\)%200%20%3E%20\(param\)%20persist_chat%20%3E%20\(schema\)) | Indefinitely  
Meeting chat without [`persist_chat`](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/#\(resource\)%20realtime_kit.meetings%20%3E%20\(method\)%20create%20%3E%20\(params\)%200%20%3E%20\(param\)%20persist_chat%20%3E%20\(schema\)) | 7 days  
Composite recordings | 7 days  
Track recordings | 7 days  
Transcripts | 7 days  
Call analytics | 6 months  
Webhook logs | 1 month  
  
[PreviousPricing](https://developers.cloudflare.com/realtime/realtimekit/pricing/)[NextLimits](https://developers.cloudflare.com/realtime/realtimekit/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/data-retention.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
