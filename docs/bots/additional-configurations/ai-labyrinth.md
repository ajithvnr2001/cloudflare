---
url: https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/
title: AI Labyrinth \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:32.125792+00:00
---

# AI Labyrinth · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Additional configurations
  4. /AI Labyrinth



# AI Labyrinth

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAI Labyrinth in Security Analytics After you turn off AI LabyrinthEnable AI Labyrinth

The AI Labyrinth adds invisible links on your webpage with specific `Nofollow` tags to block AI crawlers that do not adhere to the recommended guidelines and crawl without permission. AI crawlers that scrape your website content without permission will be stuck in a maze of never-ending links, and their details are recorded and used by all Cloudflare customers who choose to block [AI bots](https://developers.cloudflare.com/bots/concepts/bot/#ai-bots).

These links do not impact your search engine optimization (SEO) or your website's appearance, and are only seen by bots. AI bots that respect no-crawl instructions will safely ignore this honeypot.

## AI Labyrinth in Security Analytics

When AI Labyrinth is enabled, Cloudflare logs security events for AI Labyrinth under the **AI Labyrinth** service. The following actions describe what happened to the request:

Action | Description  
---|---  
**AI Labyrinth Served** | Cloudflare injected AI Labyrinth honeypot links into the HTML response.  
**AI Labyrinth Crawls** | A crawler followed one of the injected honeypot links and entered the maze.  
  
AI Labyrinth actions are not mitigations. Cloudflare does not block or challenge the request.

A high volume of **AI Labyrinth Crawls** relative to **AI Labyrinth Served** indicates that non-compliant AI crawlers are actively following the injected links.

You can view these events in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) and [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/).

### After you turn off AI Labyrinth

When you turn off AI Labyrinth, Cloudflare immediately stops injecting new honeypot links into your pages. However, links generated while the feature was on remain valid for a limited time. Cloudflare still serves labyrinth content for these links, so you may continue to see AI Labyrinth actions in Security Analytics and Security Events until the links expire. This is expected behavior and does not mean the feature is still on.

## Enable AI Labyrinth

  1. In the Cloudflare dashboard, go to the **Security Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **Bot traffic**.

  3. Go to **AI Labyrinth**.

  4. Turn **AI Labyrinth** on.




[PreviousSequence rules](https://developers.cloudflare.com/bots/additional-configurations/sequence-rules/)[NextBlock AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/additional-configurations/ai-labyrinth.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
