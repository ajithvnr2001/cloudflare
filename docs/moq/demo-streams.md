---
url: https://developers.cloudflare.com/moq/demo-streams/
title: Demo streams \u00b7 Cloudflare MoQ docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:21.963290+00:00
---

# Demo streams · Cloudflare MoQ docs

> Source: https://developers.cloudflare.com/moq/demo-streams/

  1. [Home](https://developers.cloudflare.com/)
  2. /[MoQ](https://developers.cloudflare.com/moq/)
  3. /Demo streams



# Demo streams

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/moq/demo-streams/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable namespacesSubscribe with moq-sub

Cloudflare publishes long-running streams on the public [MoQ](https://developers.cloudflare.com/moq/) relays. Use these streams to test client implementations without setting up your own publisher.

## Available namespaces

The relays host the following namespaces. A check mark indicates that a namespace is available for that draft.

Namespace | Draft-14 | Draft-16  
---|---|---  
`/bbb` | ✅ | ✅  
`/demo-tos-360p` | ✅ | —  
`/demo-tos-720p` | ✅ | —  
`/demo-tos-1080p` | ✅ | —  
`/demo-tos-4k` | ✅ | —  
  
## Subscribe with moq-sub

`moq-sub` from the [moq-rs ↗︎](https://github.com/cloudflare/moq-rs) project writes the media as fragmented MP4 to standard output. Select a draft to view the matching command.

Draft-14 supports every namespace in the table. This example subscribes to `/bbb`:
    
    
    moq-sub https://draft-14.cloudflare.mediaoverquic.com --name bbb

Draft-16 supports only `/bbb`. Its relay URL includes the provided JSON Web Token (JWT):
    
    
    moq-sub https://draft-16.cloudflare.mediaoverquic.com/eyJhbGciOiJFZERTQSIsImtpZCI6Im1vcS12MSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJtb3EuY2xvdWRmbGFyZS5jb20iLCJleHAiOjE4MTY0NDA0NTcsImlhdCI6MTc4NDkwNDQ1OCwiaXNzIjoiY2xvdWRmbGFyZSIsImp0aSI6IjgxMTc4MjIyZmIzNTVjMDQ3YmM0MDNkODQ2NWI0YWIzIiwib3BlcmF0aW9ucyI6WyJzdWJzY3JpYmUiXSwic3ViIjoiZWJkMWZlZDdhZjMzNzYzMjc3MDc0ODQ0NThmYWIxZmEifQ.VlTscBfWmjSybWx1NpmF0f1g5Gtfxg5H4rkUQQa2JHATtjGwO5iwl71DAS5kJ98-3ukPvmGe9RE7peYs_dqgCg --name bbb

The provided JWT lets you subscribe without provisioning a relay or creating a token.

To play the stream with `ffplay`, append `| ffplay -` to either command.

[PreviousBackground](https://developers.cloudflare.com/moq/about/)[NextMoQ Feature Matrix](https://developers.cloudflare.com/moq/feature-matrix/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/moq/demo-streams/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
