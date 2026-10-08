---
url: https://developers.cloudflare.com/bots/plans/biz-and-ent/
title: Plans \u2014 Business and Enterprise \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:33.770730+00:00
---

# Plans — Business and Enterprise · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/plans/biz-and-ent/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /[Plans](https://developers.cloudflare.com/bots/plans/)
  4. /Biz And Ent



# Business

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/plans/biz-and-ent/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBot settings versus custom rulesHow do I get started?

To learn more about features and functionality, select a plan.

[Free](https://developers.cloudflare.com/bots/plans/free/) [Pro](https://developers.cloudflare.com/bots/plans/pro/) [Business](https://developers.cloudflare.com/bots/plans/biz-and-ent/) [Bot Management for Enterprise](https://developers.cloudflare.com/bots/plans/bm-subscription/) |   
---|---  
**Plan name**|  Super Bot Fight Mode  
**Availability**|  All Business customers and Enterprise customers without Bot Management1  
**Type of bots detected**|  Simple bots, headless browsers, and many sophisticated bots  
**Actions**|  Customer chooses whether to allow, block, or challenge  
**Analytics**|  Dedicated Bot Analytics tool, available in **Security Analytics**  
**Control**|  Applied to all traffic across a domain  
**Additional features**| [Block AI bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/),   
[AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/),   
[Instruct AI bot traffic with `robots.txt`](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/),   
[Definitely and Likely automated bots](https://developers.cloudflare.com/bots/concepts/bot-score/#bot-groupings),   
[Verified bots](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/),   
[Static resource protection](https://developers.cloudflare.com/bots/additional-configurations/static-resources/),   
[Optimize for WordPress](https://developers.cloudflare.com/bots/troubleshooting/wordpress-loopback-issue/),   
[JavaScript Detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/)  
  
## Bot settings versus custom rules

The following features are handled automatically in **Security Settings** and do not require custom rules:

Feature | Handled by bot settings | Requires custom rules  
---|---|---  
Block or challenge definitely automated traffic | Yes | Only for path-specific or threshold-tuned rules  
Block or challenge likely automated traffic | Not available on Pro | Yes, with [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/)  
Allow or block verified bots | Yes | No  
Block AI crawlers | Yes | Only to target individual AI crawlers  
Protect static resources | Yes | No  
Optimize for WordPress | Yes | No  
  
For more details on when custom rules are needed, refer to [custom rules](https://developers.cloudflare.com/bots/additional-configurations/custom-rules/).

## How do I get started?

To get started, review our [setup guides](https://developers.cloudflare.com/bots/get-started/). If you have any questions, visit the [community ↗︎](https://community.cloudflare.com/) to engage with other Cloudflare users.

## Footnotes

  1. When users purchase Bot Management for Enterprise, Cloudflare automatically replaces and disables other bot products to prevent overlap. ↩




Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/plans/biz-and-ent.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
