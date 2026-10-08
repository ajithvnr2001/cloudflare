---
url: https://developers.cloudflare.com/bots/concepts/bot-tags/
title: Bot tags \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:33.384303+00:00
---

# Bot tags · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/concepts/bot-tags/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Concepts
  4. /Bot tags



# Bot tags

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/concepts/bot-tags/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPotential valuesUse bot tags

Bot tags provide more detail about _why_ Cloudflare assigned a [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/) to a request.

Use these tags to learn more about your bot traffic and better inform security settings.

Note

Bot tags are only available to Enterprise customers who have purchased Bot Management.

## Potential values

Once you enable bot tags, you can see more information about bot requests, such as whether a request came from a verified bot (like Bing) or a category of verified bot (like SearchEngine).

The following values are **examples** of what may be present in the `BotTags` log field, but not an exhaustive list:

  * api
  * google
  * bing
  * googleAds
  * googleMedia
  * googleImageProxy
  * pinterest
  * newRelic
  * baidu
  * apple
  * yandex



When matching the Ruleset Engine field, use uppercase tag values such as `API`, `GOOGLE`, or `BING`.

## Use bot tags

To include bot tags in logs, add the `BotTags` field when using [Logpush](https://developers.cloudflare.com/logs/logpush/).

To match bot tags in Ruleset Engine expressions, use the [`cf.bot_management.tags`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.tags/) field. For example:
    
    
    any(cf.bot_management.tags[*] eq "API")

[PreviousBot scores](https://developers.cloudflare.com/bots/concepts/bot-score/)[NextBot Feedback Loop](https://developers.cloudflare.com/bots/concepts/feedback-loop/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/concepts/bot-tags.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
