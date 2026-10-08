---
url: https://developers.cloudflare.com/agents/model-context-protocol/
title: Model Context Protocol (MCP) \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:13.650708+00:00
---

# Model Context Protocol (MCP) · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/model-context-protocol/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Model Context Protocol (MCP)



# Model Context Protocol (MCP)

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/model-context-protocol/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is the Model Context Protocol (MCP)? MCP Terminology Remote vs. local MCP connections Best Practices Get Started

You can build and deploy [Model Context Protocol (MCP) ↗︎](https://modelcontextprotocol.io/) servers on Cloudflare.

## What is the Model Context Protocol (MCP)?

[Model Context Protocol (MCP) ↗︎](https://modelcontextprotocol.io) is an open standard that connects AI systems with external applications. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various accessories, MCP provides a standardized way to connect AI agents to different services.

### MCP Terminology

  * **MCP Hosts** : AI assistants (like [Claude ↗︎](https://claude.ai) or [Cursor ↗︎](https://cursor.com)), AI agents, or applications that need to access external capabilities.
  * **MCP Clients** : Clients embedded within the MCP hosts that connect to MCP servers and invoke tools. Each MCP client instance has a single connection to an MCP server.
  * **MCP Servers** : Applications that expose [tools](https://developers.cloudflare.com/agents/model-context-protocol/protocol/tools/), [prompts ↗︎](https://modelcontextprotocol.io/docs/concepts/prompts), and [resources ↗︎](https://modelcontextprotocol.io/docs/concepts/resources) that MCP clients can use.



### Remote vs. local MCP connections

The MCP standard supports two modes of operation:

  * **Remote MCP connections** : MCP clients connect to MCP servers over the Internet, establishing a connection using [Streamable HTTP](https://developers.cloudflare.com/agents/model-context-protocol/protocol/transport/), and authorizing the MCP client access to resources on the user's account using [OAuth](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/).
  * **Local MCP connections** : MCP clients connect to MCP servers on the same machine, using [stdio ↗︎](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#stdio) as a local transport method.



### Best Practices

  * **Tool design** : Do not treat your MCP server as a wrapper around your full API schema. Instead, build tools that are optimized for specific user goals and reliable outcomes. Fewer, well-designed tools often outperform many granular ones, especially for agents with small context windows or tight latency budgets.
  * **Scoped permissions** : Deploying several focused MCP servers, each with narrowly scoped permissions, reduces the risk of over-privileged access and makes it easier to manage and audit what each server is allowed to do.
  * **Tool descriptions** : Detailed parameter descriptions help agents understand how to use your tools correctly — including what values are expected, how they affect behavior, and any important constraints. This reduces errors and improves reliability.
  * **Evaluation tests** : Use evaluation tests ('evals') to measure the agent’s ability to use your tools correctly. Run these after any updates to your server or tool descriptions to catch regressions early and track improvements over time.



### Get Started

Go to the [Getting Started](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/) guide to learn how to build and deploy your first remote MCP server to Cloudflare.

[PreviousEmail agent](https://developers.cloudflare.com/agents/examples/email-agent/)[NextMCP handler APIs](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/model-context-protocol/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
