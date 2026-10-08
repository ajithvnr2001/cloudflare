---
url: https://developers.cloudflare.com/learning-paths/holistic-ai-security/concepts/mcp/
title: What is Model Context Protocol (MCP)? \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:49.041916+00:00
---

# What is Model Context Protocol (MCP)? · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/holistic-ai-security/concepts/mcp/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Holistic Ai Security

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/holistic-ai-security/concepts/)
  5. /What is Model Context Protocol (MCP)?



# What is Model Context Protocol (MCP)?

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/holistic-ai-security/concepts/mcp/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow does MCP work?What are the security concerns with MCP?

[Model Context Protocol (MCP) ↗︎](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) is a standardized way for AI agents to get the information and tools they need to operate. Similar to how an API works, it is a protocol that allows AI programs to connect to external sources of information and take actions in the real world, going beyond the limits of their original training data.

## How does MCP work?

MCP uses a client-server architecture where an AI agent acts as the client and sends requests to a server. This allows the AI agent to connect to multiple servers at once to get the information it needs. An MCP server is a program that exposes capabilities to AI agents, giving them access to new datasets or tools — like an email service to send messages on behalf of a user.

## What are the security concerns with MCP?

MCP doesn't have native authentication, authorization, or encryption. Because it functions similarly to an API, many of the same security considerations apply. If developers do not proactively implement security measures like Transport Layer Security (TLS) and rate limiting, MCP servers can be vulnerable to attacks, data leaks, and unauthorized access. Organizations must ensure that they validate inputs and protect confidential data to secure their MCP implementations.

[PreviousWhat is Shadow AI?](https://developers.cloudflare.com/learning-paths/holistic-ai-security/concepts/shadow-ai/)[NextOverview](https://developers.cloudflare.com/learning-paths/holistic-ai-security/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/holistic-ai-security/concepts/mcp.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
