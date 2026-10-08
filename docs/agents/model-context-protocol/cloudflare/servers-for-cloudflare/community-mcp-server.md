---
url: https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/
title: Cloudflare Community MCP Server \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:14.997875+00:00
---

# Cloudflare Community MCP Server · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Model Context Protocol (MCP)](https://developers.cloudflare.com/agents/model-context-protocol/)Cloudflare

  4. /[Cloudflare's own MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/)
  5. /Cloudflare Community MCP Server



# Cloudflare Community MCP Server

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallConfigure OpenCode Claude Desktop CursorConnect to the Cloudflare CommunityAvailable toolsExample usageMachine-readable discoveryRelated resources

The MCP server for the [Cloudflare Community forum ↗︎](https://community.cloudflare.com) lets AI agents search topics, read posts, look up users, and filter content.

The server is powered by [`@discourse/mcp` ↗︎](https://www.npmjs.com/package/@discourse/mcp), the official Discourse MCP server.

## Install
    
    
    npx @discourse/mcp@latest

## Configure

### OpenCode

Add to `~/.config/opencode/opencode.jsonc` inside the `"mcp"` block:
    
    
    "discourse": {
      "type": "local",
      "command": ["npx", "-y", "@discourse/mcp@latest"],
      "enabled": true
    }

### Claude Desktop

Add to `claude_desktop_config.json`:
    
    
    {
      "mcpServers": {
        "discourse": {
          "command": "npx",
          "args": ["-y", "@discourse/mcp@latest"]
        }
      }
    }

### Cursor

Add to `.cursor/mcp.json` in your project root:
    
    
    {
      "mcpServers": {
        "discourse": {
          "command": "npx",
          "args": ["-y", "@discourse/mcp@latest"]
        }
      }
    }

## Connect to the Cloudflare Community

After configuring your client, use the `discourse_select_site` tool with:
    
    
    https://community.cloudflare.com

No API key is needed for reading public data. An API key is only required for write operations (posting, moderation).

## Available tools

Tool | Description  
---|---  
`discourse_select_site` | Connect to community.cloudflare.com  
`discourse_search` | Full-text search across topics and posts  
`discourse_filter_topics` | Filter by category, tags, status, dates  
`discourse_read_topic` | Read a topic's posts and metadata  
`discourse_read_post` | Read a specific post  
`discourse_get_user` | Look up a user's profile  
`discourse_list_user_posts` | List posts by a user  
  
## Example usage

Once connected, you can ask your AI assistant things like:

  * "Search the Cloudflare community for topics about Error 522"
  * "Find unanswered topics in the SSL category from the last 3 days"
  * "Read topic 42325 and summarize the issue"
  * "Show me recent replies from user sandro"



## Machine-readable discovery

AI agents can automatically discover the MCP server through these endpoints on community.cloudflare.com:

  * [`/.well-known/mcp.json` ↗︎](https://community.cloudflare.com/.well-known/mcp.json) — MCP Server Card
  * [`/llms.txt` ↗︎](https://community.cloudflare.com/llms.txt) — LLMs.txt with server info and install instructions
  * [`/.well-known/agent.json` ↗︎](https://community.cloudflare.com/.well-known/agent.json) — A2A Agent Card



## Related resources

  * [Setup guide with detailed configuration instructions ↗︎](https://community.cloudflare.com/mcp)
  * [The official `npm: @discourse/mcp` package ↗︎](https://www.npmjs.com/package/@discourse/mcp)
  * [Model Context Protocol specification ↗︎](https://modelcontextprotocol.io)
  * [Building AI agents on Cloudflare](https://developers.cloudflare.com/agents/)
  * [Cloudflare Community forum ↗︎](https://community.cloudflare.com)



[PreviousOverview](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/)[NextCode Mode MCP server patterns](https://developers.cloudflare.com/agents/model-context-protocol/codemode/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
