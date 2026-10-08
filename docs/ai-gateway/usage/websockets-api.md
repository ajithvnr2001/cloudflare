---
url: https://developers.cloudflare.com/ai-gateway/usage/websockets-api/
title: WebSockets API \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:36.159045+00:00
---

# WebSockets API · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/websockets-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Using AI Gateway
  4. /WebSockets API



# WebSockets API

Last updated Jun 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use WebSocketsKey benefitsKey differences

The AI Gateway WebSockets API provides a persistent connection for AI interactions, eliminating repeated handshakes and reducing latency. This API is divided into two categories:

  * **Realtime APIs** \- Designed for AI providers that offer low-latency, multimodal interactions over WebSockets.
  * **Non-Realtime APIs** \- Supports standard WebSocket communication for AI providers, including those that do not natively support WebSockets.



## When to use WebSockets

WebSockets are long-lived TCP connections that enable bi-directional, real-time and non realtime communication between client and server. Unlike HTTP connections, which require repeated handshakes for each request, WebSockets maintain the connection, supporting continuous data exchange with reduced overhead. WebSockets are ideal for applications needing low-latency, real-time data, such as voice assistants.

## Key benefits

  * **Reduced overhead** : Avoid overhead of repeated handshakes and TLS negotiations by maintaining a single, persistent connection.
  * **Provider compatibility** : Works with all AI providers in AI Gateway. Even if your chosen provider does not support WebSockets, Cloudflare handles it for you, managing the requests to your preferred AI provider.



## Key differences

Feature | Realtime APIs | Non-Realtime APIs  
---|---|---  
**Purpose** | Enables real-time, multimodal AI interactions for providers that offer dedicated WebSocket endpoints. | Supports WebSocket-based AI interactions with providers that do not natively support WebSockets.  
**Use Case** | Streaming responses for voice, video, and live interactions. | Text-based queries and responses, such as LLM requests.  
**AI Provider Support** | [Limited to providers offering real-time WebSocket APIs.](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/#supported-providers) | [All AI providers in AI Gateway.](https://developers.cloudflare.com/ai-gateway/usage/providers/)  
**Streaming Support** | Providers natively support real-time data streaming. | AI Gateway handles streaming via WebSockets.  
  
For details on implementation, refer to the next sections:

  * [Realtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/)
  * [Non-Realtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/non-realtime-api/)



[PreviousWeb Search](https://developers.cloudflare.com/ai-gateway/usage/web-search/)[NextRealtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/websockets-api/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
