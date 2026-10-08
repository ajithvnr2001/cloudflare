---
url: https://developers.cloudflare.com/bots/plans/bm-subscription/
title: Plans \u2014 Bot Management for Enterprise \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:34.086432+00:00
---

# Plans — Bot Management for Enterprise · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/plans/bm-subscription/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /[Plans](https://developers.cloudflare.com/bots/plans/)
  4. /Bm Subscription



# Enterprise Bot Management

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/plans/bm-subscription/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBot settings vs. custom rulesHow do I get started?

To learn more about features and functionality, select a plan.

[Free](https://developers.cloudflare.com/bots/plans/free/) [Pro](https://developers.cloudflare.com/bots/plans/pro/) [Business](https://developers.cloudflare.com/bots/plans/biz-and-ent/) [Bot Management for Enterprise](https://developers.cloudflare.com/bots/plans/bm-subscription/) |   
---|---  
**Plan name**|  Bot Management for Enterprise  
**Availability**|  Added to Enterprise plans by your account team  
**Enablement**|  Quick onboarding with help from our Solutions Engineering team  
**Type of bots detected**|  Simple and sophisticated bots, headless browsers, and domain-specific anomalies  
**Actions**|  Customer chooses from several options, including block and various challenges  
**Analytics**|  Dedicated Bot Analytics tool, available in **Security Analytics**  
**Control**|  Ability to restrict by path, IP address, and more.   
  
Access to [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/), [JA3/JA4 fingerprint](https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/), [bot tags](https://developers.cloudflare.com/bots/concepts/bot-tags/) fields, and [detection IDs](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/).  
**Additional features**| [Block AI bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/),   
[AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/),   
[Instruct AI bot traffic with `robots.txt`](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/),   
[Definitely and Likely automated bots](https://developers.cloudflare.com/bots/concepts/bot-score/#bot-groupings),   
[Verified bots](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/),   
[Static resource protection](https://developers.cloudflare.com/bots/additional-configurations/static-resources/),   
[Optimize for WordPress](https://developers.cloudflare.com/bots/troubleshooting/wordpress-loopback-issue/),   
[JavaScript Detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/)  
  
Note

Zones that have [Enterprise Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/) enabled will not see Bot Fight Mode or Super Bot Fight Mode under **Security** > **Bots**.

## Bot settings vs. custom rules

Bot Management customers have both bot settings (configured in **Security Settings**) and the ability to create custom rules using bot score fields. Start with the bot settings for baseline protection, then add custom rules only when you need additional control.

Feature | Handled by bot settings | When to use custom rules instead  
---|---|---  
Block or challenge definitely automated traffic | No | Path-specific rules, custom thresholds, or combining with other fields  
Block or challenge likely automated traffic | No | Path-specific rules, custom thresholds, or combining with other fields  
Allow or block verified bots | No | Granular control by verified bot category  
Block AI crawlers | Yes | Target individual AI crawlers using detection IDs  
Protect static resources | No | Exclude static resources from specific rules  
Optimize for WordPress | No | No  
Forward bot data to origin | No | Use [Transform Rules](https://developers.cloudflare.com/rules/transform/) or [Snippets](https://developers.cloudflare.com/rules/snippets/)  
Detection ID targeting | No | Use `cf.bot_management.detection_ids` in [custom rules](https://developers.cloudflare.com/waf/custom-rules/)  
JA3/JA4 fingerprint rules | No | Use `cf.bot_management.ja3_hash` or `cf.bot_management.ja4` in [custom rules](https://developers.cloudflare.com/waf/custom-rules/)  
  
For more details on when custom rules are needed, refer to [custom rules](https://developers.cloudflare.com/bots/additional-configurations/custom-rules/).

## How do I get started?

To get started, review our [setup guides](https://developers.cloudflare.com/bots/get-started/). If you have any questions, visit the [community ↗︎](https://community.cloudflare.com/) to engage with other Cloudflare users.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/plans/bm-subscription.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
