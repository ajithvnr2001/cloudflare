---
url: https://developers.cloudflare.com/time-services/roughtime/usage/
title: Get the Roughtime from Cloudflare \u00b7 Cloudflare Time Services docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:02.599797+00:00
---

# Get the Roughtime from Cloudflare · Cloudflare Time Services docs

> Source: https://developers.cloudflare.com/time-services/roughtime/usage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Time Services](https://developers.cloudflare.com/time-services/)
  3. /[Roughtime](https://developers.cloudflare.com/time-services/roughtime/)
  4. /Get the Roughtime



# Get the Roughtime

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/time-services/roughtime/usage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBeta noticeNext steps

The "Hello, world!" of Roughtime is very simple: the client sends a request over UDP to the server and the server responds with a signed timestamp.

You just need the server's address and public key to run the protocol:

  * **Server address** : `roughtime.cloudflare.com:2003` (resolves to an IP address in our [anycast IP range ↗︎](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)). You can use either IPv4 or IPv6.
  * **Public key** : `0GD7c3yP8xEc4Zl2zeuN2SlLvDVVocjsPSL8/Rl/7zg=`



To get started, download and run Cloudflare's [Go client ↗︎](https://github.com/cloudflare/roughtime):
    
    
    go install github.com/cloudflare/roughtime/cmd/getroughtime@latest
    getroughtime -ping roughtime.cloudflare.com:2003 -pubkey 0GD7c3yP8xEc4Zl2zeuN2SlLvDVVocjsPSL8/Rl/7zg=

## Beta notice

Cloudflare Roughtime is currently in beta. As such, our root public key may change in the future. We will keep this page up-to-date with the most current public key.

You can also obtain it programmatically using DNS. For example:
    
    
    dig TXT roughtime.cloudflare.com | grep -oP 'TXT\s"\K.*?(?=")'

## Next steps

Beyond just getting the Roughtime from Cloudflare, you may want to use it to [keep your clock in sync](https://developers.cloudflare.com/time-services/roughtime/recipes/).

[PreviousOverview](https://developers.cloudflare.com/time-services/roughtime/)[NextUse Roughtime](https://developers.cloudflare.com/time-services/roughtime/recipes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/time-services/roughtime/usage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
