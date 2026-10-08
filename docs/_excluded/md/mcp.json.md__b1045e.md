---
url: https://community.cloudflare.com/.well-known/mcp.json
title: https://community.cloudflare.com/.well-known/mcp.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:21:34.455032+00:00
---

# https://community.cloudflare.com/.well-known/mcp.json

> Source: https://community.cloudflare.com/.well-known/mcp.json

{ "name": "Cloudflare Community (Discourse MCP)", "serverInfo": { "name": "Cloudflare Community (Discourse MCP)", "version": "1.0.0" }, "description": "MCP server for the Cloudflare Community forum at community.cloudflare.com. Provides search, topic reading, filtering, user lookup, and more.", "url": "https://community.cloudflare.com", "transport": { "type": "stdio", "command": [ "npx", "-y", "@discourse/mcp@latest" ], "args": [] }, "capabilities": { "tools": true, "resources": false, "prompts": false }, "tools": [ { "name": "discourse_select_site", "description": "Connect to community.cloudflare.com" }, { "name": "discourse_search", "description": "Full-text search across all topics" }, { "name": "discourse_filter_topics", "description": "Filter topics by category, tags, status, dates" }, { "name": "discourse_read_topic", "description": "Read a topic's posts and metadata" }, { "name": "discourse_read_post", "description": "Read a specific post" }, { "name": "discourse_get_user", "description": "Get user profile information" }, { "name": "discourse_list_user_posts", "description": "List posts by a user" } ], "authentication": { "type": "none", "description": "No authentication needed for public data. API key required for write operations." } }
