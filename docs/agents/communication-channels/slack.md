---
url: https://developers.cloudflare.com/agents/communication-channels/slack/
title: Slack \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:07.541921+00:00
---

# Slack · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/communication-channels/slack/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Communication channels
  4. /Slack



# Slack

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/communication-channels/slack/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksBuild a Slack agentRelated resources

Slack is a communication channel for agents that need to participate in team conversations. A Slack-connected agent can receive events from Slack, route each message to the right agent instance, and respond back to direct messages or channel mentions.

Use Slack when you want an agent to:

  * Respond to direct messages from Slack users.
  * Reply when mentioned in public channels.
  * Maintain context inside Slack threads.
  * Serve multiple Slack workspaces from one deployment.



## How it works

Slack sends events to your Worker through the [Slack Events API ↗︎](https://api.slack.com/apis/events-api). Your Worker verifies each request, identifies the installed workspace, and routes the event to an agent instance.

Common Slack events include:

Event | Use case  
---|---  
`message.im` | Direct messages to the bot  
`app_mention` | Mentions in channels  
  
For multi-workspace Slack apps, store each workspace installation separately and route events by team or enterprise ID. Each workspace can map to an isolated agent instance with its own Durable Object-backed state.

## Build a Slack agent

For a complete walkthrough, including Slack app setup, OAuth, event subscriptions, and deployment, use the Slack agent example.

### [Slack agent](https://developers.cloudflare.com/agents/examples/slack-agent/)

Build and deploy an AI-powered Slack bot on Cloudflare Workers using the Agents SDK.

## Related resources

### [Slack Events API](https://api.slack.com/apis/events-api)

Receive events when users message, mention, or interact with a Slack app.

### [Slack app authentication](https://api.slack.com/authentication)

Configure OAuth, bot tokens, signing secrets, and request verification for Slack apps.

[PreviousEmail](https://developers.cloudflare.com/agents/communication-channels/email/)[NextOverview](https://developers.cloudflare.com/agents/communication-channels/webhooks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/communication-channels/slack.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
