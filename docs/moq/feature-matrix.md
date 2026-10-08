---
url: https://developers.cloudflare.com/moq/feature-matrix/
title: MoQ Feature Matrix \u00b7 Cloudflare MoQ docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:22.045191+00:00
---

# MoQ Feature Matrix · Cloudflare MoQ docs

> Source: https://developers.cloudflare.com/moq/feature-matrix/

  1. [Home](https://developers.cloudflare.com/)
  2. /[MoQ](https://developers.cloudflare.com/moq/)
  3. /MoQ Feature Matrix



# MoQ Feature Matrix

Last updated Jul 31, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/moq/feature-matrix/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDraft-16 messages Supported Partial UnsupportedDraft-14 messages Supported Unsupported

## Draft-16 messages

### Supported

Message | Support | Relevant specification  
---|---|---  
SUBSCRIBE | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
UNSUBSCRIBE | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
PUBLISH | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
PUBLISH_OK | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
SUBSCRIBE_NAMESPACE | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
SUBSCRIBE_NAMESPACE_OK | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
SUBSCRIBE_NAMESPACE_ERROR | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
UNSUBSCRIBE_NAMESPACE | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
SUBSCRIBE_OK | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
SUBSCRIBE_ERROR | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
TRACK_STATUS | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
TRACK_STATUS_OK | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
SETUP_MESSAGES (client and server) | ✅ | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
  
### Partial

Message | Support | Notes | Relevant specification  
---|---|---|---  
MAX_REQUEST_ID | Partial | Initial limit negotiated in SETUP and mid-session raises are applied. REQUESTS_BLOCKED does not trigger an automatic limit increase. | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
REQUESTS_BLOCKED | Partial | Received and logged. It does not trigger an automatic MAX_REQUEST_ID response. | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
  
### Unsupported

Message | Support | Relevant specification  
---|---|---  
GOAWAY | No | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
SUBSCRIBE_UPDATE | No | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
PUBLISH_ERROR | No | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
FETCH | No | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
FETCH_OK | No | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
FETCH_ERROR | No | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
FETCH_CANCEL | No | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
TRACK_STATUS_ERROR | No | [draft-ietf-moq-transport-16 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-16)  
  
## Draft-14 messages

### Supported

Message | Support | Relevant specification  
---|---|---  
SUBSCRIBE | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
UNSUBSCRIBE | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
TRACK_STATUS | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
PUBLISH_NAMESPACE_CANCEL | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
PUBLISH_NAMESPACE_OK | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
PUBLISH_NAMESPACE_ERROR | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
PUBLISH_OK | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
PUBLISH_NAMESPACE | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
PUBLISH_NAMESPACE_DONE | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
PUBLISH_DONE | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
SUBSCRIBE_OK | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
SUBSCRIBE_ERROR | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
TRACK_STATUS_OK | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
SETUP_MESSAGES (client and server) | ✅ | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
  
### Unsupported

Message | Support | Relevant specification  
---|---|---  
GOAWAY | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
MAX_REQUEST_ID | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
REQUESTS_BLOCKED | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
SUBSCRIBE_UPDATE | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
PUBLISH_ERROR | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
FETCH | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
FETCH_OK | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
FETCH_ERROR | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
FETCH_CANCEL | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
TRACK_STATUS_ERROR | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
SUBSCRIBE_NAMESPACE | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
SUBSCRIBE_NAMESPACE_OK | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
SUBSCRIBE_NAMESPACE_ERROR | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
UNSUBSCRIBE_NAMESPACE | No | [draft-ietf-moq-transport-14 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14)  
  
[PreviousDemo streams](https://developers.cloudflare.com/moq/demo-streams/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/moq/feature-matrix.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
