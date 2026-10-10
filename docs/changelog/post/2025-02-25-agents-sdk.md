---
url: https://developers.cloudflare.com/changelog/post/2025-02-25-agents-sdk/
title: Introducing the Agents SDK \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.588297+00:00
---

# Introducing the Agents SDK · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-25-agents-sdk/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 25, 2025

## Introducing the Agents SDK

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've released the [Agents SDK ↗︎](http://blog.cloudflare.com/build-ai-agents-on-cloudflare/), a package and set of tools that help you build and ship AI Agents.

You can get up and running with a [chat-based AI Agent ↗︎](https://github.com/cloudflare/agents-starter) (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:
    
    
    npm create cloudflare@latest agents-starter -- --template="cloudflare/agents-starter"
    # open up README.md and follow the instructions

You can also add an Agent to any existing Workers application by installing the `agents` package directly
    
    
    npm i agents

... and then define your first Agent:
    
    
    import { Agent } from "agents";
    
    export class YourAgent extends Agent<Env> {
    	// Build it out
    	// Access state on this.state or query the Agent's database via this.sql
    	// Handle WebSocket events with onConnect and onMessage
    	// Run tasks on a schedule with this.schedule
    	// Call AI models
    	// ... and/or call other Agents.
    }

Head over to the [Agents documentation](https://developers.cloudflare.com/agents/) to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.
