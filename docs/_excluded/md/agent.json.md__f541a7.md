---
url: https://community.cloudflare.com/.well-known/agent.json
title: https://community.cloudflare.com/.well-known/agent.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:21:36.833115+00:00
---

# https://community.cloudflare.com/.well-known/agent.json

> Source: https://community.cloudflare.com/.well-known/agent.json

{ "name": "Cloudflare Community Agent", "description": "AI agent interface for the Cloudflare Community forum. Supports searching topics, reading posts, triaging support issues, and managing deflection workflows.", "url": "https://community.cloudflare.com", "version": "1.0.0", "provider": { "organization": "Cloudflare", "url": "https://www.cloudflare.com" }, "capabilities": { "streaming": false, "pushNotifications": false, "stateTransitionHistory": false }, "supportedInterfaces": [ { "type": "https://a2a.dev/interfaces/text", "url": "https://community.cloudflare.com/api/a2a", "versions": [ "1.0" ], "defaultInputModes": [ "text/plain" ], "defaultOutputModes": [ "text/plain", "application/json" ] } ], "defaultInputModes": [ "text/plain" ], "defaultOutputModes": [ "text/plain", "application/json" ], "skills": [ { "id": "search", "name": "Search Topics", "description": "Search the Cloudflare Community forum for topics matching a query", "inputModes": [ "text/plain" ], "outputModes": [ "application/json" ] }, { "id": "read-topic", "name": "Read Topic", "description": "Read the full content of a forum topic by ID", "inputModes": [ "text/plain" ], "outputModes": [ "application/json" ] }, { "id": "triage", "name": "Triage Forum", "description": "Scan for unanswered topics and recommend actions", "inputModes": [ "text/plain" ], "outputModes": [ "application/json" ] } ] }
