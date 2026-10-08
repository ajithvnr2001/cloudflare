---
url: https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/
title: Block AI Bots \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:32.365389+00:00
---

# Block AI Bots · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Additional configurations
  4. /Block AI Bots



# Block AI Bots

Last updated Jul 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure AI bot policies New defaults on September 15, 2026Block AI bots [Deprecating on September 15, 2026]

## Configure AI bot policies

### New defaults on September 15, 2026

On September 15, 2026, Cloudflare will set updated defaults for new domains: bots classified as Training or as Agent will be blocked on pages that display ads, and Search will remain allowed. Mixed-purpose crawlers that combine Search and Training will also be blocked by all configurations to block AI training, including the legacy "Block AI bots" option. Before September 15, all customers can [opt out of these new defaults ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/settings).

All Cloudflare customers can choose to block AI bots and agents based on their behavior. Cloudflare offers presets for the most common AI behaviors to give customers the option to treat different AI use cases distinctly:

  * **Search** : crawlers that collect or index your content to answer questions about it later.
  * **Agent** : automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents.
  * **Training** : crawlers taking your content to train or fine-tune a model, including mixed-purpose crawlers that are used both for Training and for Search.



Each blocking option will block Verified bots classified with that behavior, plus additional unverified bots that fall under these classifications.

Each setting includes three mitigation options:

  * **Block (on all pages)** \- Issues the block across the entire zone.
  * **Block on pages with ads** \- Uses Cloudflare automated detection for pages that display ads on your zone to block only on those pages.
  * **Allow (do not block)** \- Does not add any blocking.



To configure these policies, customers can go to **Security Settings** > **Configure AI bot policies**.

## Block AI bots [Deprecating on September 15, 2026]

This setting blocks verified bots that are classified as crawling for the purpose of AI training, as well as a number of unverified bots that behave similarly.

Note

This option excludes mixed-purpose bots that are used both for Training and for Search.

To configure this setting and set their preference for blocking mixed-purpose bots, customers can go to **Security Settings** > **Block AI bots**.

[PreviousAI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/)[NextCustom rules](https://developers.cloudflare.com/bots/additional-configurations/custom-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/additional-configurations/block-ai-bots.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
