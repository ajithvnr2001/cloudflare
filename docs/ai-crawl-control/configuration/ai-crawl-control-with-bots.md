---
url: https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/
title: AI Crawl Control with Cloudflare Bots \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:25.595416+00:00
---

# AI Crawl Control with Cloudflare Bots · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /Configuration
  4. /AI Crawl Control with Cloudflare Bots



# AI Crawl Control with Cloudflare Bots

Last updated Jul 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOrder of precedenceExamples Bot rule which blocks all AI bots vs pay per crawl

AI Crawl Control works alongside other Cloudflare products, such as Cloudflare [bot solutions](https://developers.cloudflare.com/bots/). Bot solutions identifies traffic matching patterns of known bots, and can challenge or block the bots as you wish.

## Order of precedence

  * AI Crawl Control's AI crawler blocking uses [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/), which take place before Cloudflare bot solutions.
  * AI Crawl Control's pay per crawl takes place after Cloudflare bot solutions.


    
    
    graph LR
    A[Traffic] --> B[WAF custom rules<br>AI Crawl Control: Crawler blocks]
    B --> C[Cloudflare<br>Bot Solutions]
    C --> D[AI Crawl Control:<br>Pay Per Crawl]
    classDef highlight fill:#F6821F,color:white
    

For more information on how Cloudflare classifies bot traffic, refer to [AI bots](https://developers.cloudflare.com/bots/concepts/bot/#ai-bots).

## Examples

Consider the following examples.

### Bot rule which blocks all AI bots vs pay per crawl

You may have both of the following enabled:

  * A selection of AI crawlers to be charged through AI Crawl Control's pay per crawl
  * Bot configuration option to [Block AI Bots](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/#block-ai-bots).



Since pay per crawl happens after bot solutions, you need to first turn off **Block AI Bots** to ensure pay per crawl works as intended.

[PreviousAI Crawl Control with Cloudflare WAF](https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-waf/)[NextAI Crawl Control with Transform Rules](https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-transform-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/configuration/ai-crawl-control-with-bots.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
