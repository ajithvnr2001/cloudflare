---
url: https://developers.cloudflare.com/changelog/post/2026-04-15-agentlee-writeops-genui/
title: Agent Lee adds Write Operations and Generative UI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.488122+00:00
---

# Agent Lee adds Write Operations and Generative UI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-15-agentlee-writeops-genui/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 15, 2026

## Agent Lee adds Write Operations and Generative UI

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Agent Lee adds Write Operations and Generative UI

We are excited to announce two major capability upgrades for **Agent Lee** , the AI co-pilot built directly into the Cloudflare dashboard. Agent Lee is designed to understand your specific account configuration, and with this release, it moves from a passive advisor to an active assistant that can help you manage your infrastructure and visualize your data through natural language.

#### Take action with Write Operations

Agent Lee can now perform changes on your behalf across your Cloudflare account. Whether you need to update DNS records, modify SSL/TLS settings, or configure Workers routes, you can simply ask.

To ensure security and accuracy, every write operation requires **explicit user approval**. Before any change is committed, Agent Lee will present a summary of the proposed action in plain language. No action is taken until you select **Confirm** , and this approval requirement is enforced at the infrastructure level to prevent unauthorized changes.

**Example requests:**

  * _"Add an A record for blog.example.com pointing to 192.0.2.10."_
  * _"Enable Always Use HTTPS on my zone."_
  * _"Set the SSL mode for example.com to Full (strict)."_



#### Visualize data with Generative UI

Understanding your traffic and security trends is now as easy as asking a question. Agent Lee now features **Generative UI** , allowing it to render inline charts and structured data visualizations directly within the chat interface using your actual account telemetry.

**Example requests:**

  * _"Show me a chart of my traffic over the last 7 days."_
  * _"What does my error rate look like for the past 24 hours?"_
  * _"Graph my cache hit rate for example.com this week."_



* * *

#### Availability

These features are currently available in **Beta** for all users on the **Free plan**. To get started, log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) and select **Ask AI** in the upper right corner.

To learn more about how to interact with your account using AI, refer to the [Agent Lee documentation](https://developers.cloudflare.com/agent-lee/).
