---
url: https://developers.cloudflare.com/agents/model-context-protocol/guides/test-remote-mcp-server/
title: Test a Remote MCP Server \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:15.984965+00:00
---

# Test a Remote MCP Server · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/model-context-protocol/guides/test-remote-mcp-server/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Model Context Protocol (MCP)](https://developers.cloudflare.com/agents/model-context-protocol/)

  4. /Guides
  5. /Test a Remote MCP Server



# Test a Remote MCP Server

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/model-context-protocol/guides/test-remote-mcp-server/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewThe Model Context Protocol (MCP) inspectorConnect your remote MCP server to Cloudflare Workers AI PlaygroundConnect your remote MCP server to Claude Desktop via a local proxyConnect your remote MCP server to CursorConnect your remote MCP server to Windsurf

Remote, authorized connections are an evolving part of the [Model Context Protocol (MCP) specification ↗︎](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization). Not all MCP clients support remote connections yet.

This guide will show you options for how to start using your remote MCP server with MCP clients that support remote connections. If you haven't yet created and deployed a remote MCP server, you should follow the [Build a Remote MCP Server](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/) guide first.

## The Model Context Protocol (MCP) inspector

The [`@modelcontextprotocol/inspector` package ↗︎](https://github.com/modelcontextprotocol/inspector) is a visual testing tool for MCP servers.

  1. Open a terminal and run the following command:
         
         npx @modelcontextprotocol/inspector
         
         🚀 MCP Inspector is up and running at:
         	http://localhost:5173/?MCP_PROXY_AUTH_TOKEN=46ab..cd3
         
         🌐 Opening browser...

The MCP Inspector will launch in your web browser. You can also launch it manually by opening a browser and going to `http://localhost:<PORT>`. Check the command output for the local port where MCP Inspector is running. In this example, MCP Inspector is served on port `5173`.

  2. In the MCP inspector, enter the URL of your MCP server (for example, `http://localhost:8788/mcp`). Select **Connect**.

You can connect to an MCP server running on your local machine or a remote MCP server running on Cloudflare.

  3. If your server requires authentication, the connection will fail. To authenticate:

     1. In MCP Inspector, select **Open Auth settings**.
     2. Select **Quick OAuth Flow**.
     3. Once you have authenticated with the OAuth provider, you will be redirected back to MCP Inspector. Select **Connect**.



You should see the **List tools** button, which will list the tools that your MCP server exposes.

## Connect your remote MCP server to Cloudflare Workers AI Playground

Visit the [Workers AI Playground ↗︎](https://playground.ai.cloudflare.com/), enter your MCP server URL, and click "Connect". Once authenticated (if required), you should see your tools listed and they will be available to the AI model in the chat.

## Connect your remote MCP server to Claude Desktop via a local proxy

You can use the [`mcp-remote` local proxy ↗︎](https://www.npmjs.com/package/mcp-remote) to connect Claude Desktop to your remote MCP server. This lets you test what an interaction with your remote MCP server will be like with a real-world MCP client.

  1. Open Claude Desktop and navigate to Settings -> Developer -> Edit Config. This opens the configuration file that controls which MCP servers Claude can access.
  2. Replace the content with a configuration like this:


    
    
    {
    	"mcpServers": {
    		"my-server": {
    			"command": "npx",
    			"args": ["mcp-remote", "http://my-mcp-server.my-account.workers.dev/mcp"]
    		}
    	}
    }

  3. Save the file and restart Claude Desktop (command/ctrl + R). When Claude restarts, a browser window will open showing your OAuth login page. Complete the authorization flow to grant Claude access to your MCP server.



Once authenticated, you'll be able to see your tools by clicking the tools icon in the bottom right corner of Claude's interface.

## Connect your remote MCP server to Cursor

Connect [Cursor ↗︎](https://cursor.com/docs/context/mcp) to your remote MCP server by editing the project's `.cursor/mcp.json` file or a global `~/.cursor/mcp.json` file and adding the following configuration:
    
    
    {
    	"mcpServers": {
    		"my-server": {
    			"url": "http://my-mcp-server.my-account.workers.dev/mcp"
    		}
    	}
    }

## Connect your remote MCP server to Windsurf

You can connect your remote MCP server to [Windsurf ↗︎](https://docs.windsurf.com) by editing the [`mcp_config.json` file ↗︎](https://docs.windsurf.com/windsurf/cascade/mcp), and adding the following configuration:
    
    
    {
    	"mcpServers": {
    		"my-server": {
    			"serverUrl": "http://my-mcp-server.my-account.workers.dev/mcp"
    		}
    	}
    }

[PreviousBuild a Remote MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/)[NextSecuring MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/guides/securing-mcp-server/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/model-context-protocol/guides/test-remote-mcp-server.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
