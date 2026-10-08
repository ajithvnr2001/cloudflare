---
url: https://developers.cloudflare.com/workers/reference/protocols/
title: Protocols \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:41.344211+00:00
---

# Protocols · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/reference/protocols/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Reference
  4. /Protocols



# Protocols

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/reference/protocols/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Workers support the following protocols and interfaces:

Protocol | Inbound | Outbound  
---|---|---  
**HTTP / HTTPS** | Handle incoming HTTP requests using the [`fetch()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/) | Make HTTP subrequests using the [`fetch()` API](https://developers.cloudflare.com/workers/runtime-apis/fetch/)  
**Direct TCP sockets** | Support for handling inbound TCP connections is [coming soon ↗︎](https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/) | Create outbound TCP connections using the [`connect()` API](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/)  
**WebSockets** | Accept incoming WebSocket connections using the [`WebSocket` API](https://developers.cloudflare.com/workers/runtime-apis/websockets/) |   
**HTTP/3 (QUIC)** | Accept inbound requests over [HTTP/3 ↗︎](https://www.cloudflare.com/learning/performance/what-is-http3/) by enabling it on your [zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) in **Speed** > **Settings** > **Protocol Optimization** area of the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/). |   
**SMTP** | Use [Email Workers](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) to process and forward email, without having to manage TCP connections to SMTP email servers | [Email Workers](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/)  
  
[PreviousMigrate from Service Workers to ES Modules](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/)[NextSecurity model](https://developers.cloudflare.com/workers/reference/security-model/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/reference/protocols.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
