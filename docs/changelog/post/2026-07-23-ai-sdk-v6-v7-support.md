---
url: https://developers.cloudflare.com/changelog/post/2026-07-23-ai-sdk-v6-v7-support/
title: Agents SDK packages support AI SDK v6 and v7 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:04.501819+00:00
---

# Agents SDK packages support AI SDK v6 and v7 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-23-ai-sdk-v6-v7-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 23, 2026

## Agents SDK packages support AI SDK v6 and v7

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-23-ai-sdk-v6-v7-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `agents`, `@cloudflare/ai-chat`, `@cloudflare/codemode`, and `@cloudflare/think` packages now support AI SDK v6 and v7. Existing applications can remain on v6 when updating these packages. Applications can also adopt v7 without changing the Cloudflare Agents APIs they use.

The supported peer ranges are `ai@^6 || ^7` and `@ai-sdk/react@^3 || ^4`. Use matching major versions: pair AI SDK v6 with `@ai-sdk/react` v3, or pair AI SDK v7 with `@ai-sdk/react` v4.

To install the latest packages with AI SDK v7:

npmyarnpnpmbun
    
    
    npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4
    
    
    yarn add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4
    
    
    pnpm add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4
    
    
    bun add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4

Think normalizes streaming, tool completion events, and telemetry across both AI SDK versions. Existing v6 applications do not need to migrate these integrations before updating Think.

For setup and usage details, refer to the [Think documentation](https://developers.cloudflare.com/agents/harnesses/think/).
